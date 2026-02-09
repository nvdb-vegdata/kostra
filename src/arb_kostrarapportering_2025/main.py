from api.download_nvdb_data import RoadNetworkDownloader
import pandas as pd
import requests
import time

def v3_hent_objekter(vtid, **kwargs) -> pd.DataFrame:
    base_url = f'https://nvdbapiles-v3.atlas.vegvesen.no/vegobjekter/{vtid}?{"&".join([f"{key}={value}" for key, value in kwargs.items()])}'
    df_list = []
    total_fetched = 0
    print(base_url)
    while True:
        r = requests.get(base_url, headers={"X-Client": "Andryg python"})
        if r.status_code != 200:
            print(r.text)
            break
        data = r.json()
        df_list.append(pd.json_normalize(data.get('objekter', [])))
        total_fetched += data.get('metadata', {}).get('returnert', 0)
        print(f"Total fetched: {total_fetched}")
        
        next_url : str = data.get('metadata', {}).get('neste', {}).get('href', "")
        antall = data.get('metadata', {}).get('antall', 0)
        sidestørrelse = data.get('metadata', {}).get('sidestørrelse', 0)
        if antall < sidestørrelse:
            break
        
        base_url: str = next_url
        
    if df_list:
        objects = pd.concat(df_list, ignore_index=True)
        return objects
    else:
        return pd.DataFrame()

def vegnettsfilter():
    return {'trafikantgruppe':'K', 'adskiltelop':'med,nei', 'veglenketype':'hoved', 'sideanlegg':'false', 'vegsystemreferanse':'Ev,Rv', 'detaljniva':'VT,VTKB', 'typeveg':'kanalisertVeg,enkelBilveg,rampe,rundkjøring,gatetun', 'tidspunkt':'2025-12-31'}

def fagdatafilter():
    return {'trafikantgruppe':'K', 'tidspunkt':'2025-12-31'}

def tell_lengde_per_vegsystem(df):
    lengder = {}
    df = df.rename(columns={'lokasjon.vegsystemreferanser':'vref'})
    for row in df.itertuples():
        for vref in row.vref:
            vegsystem = vref['vegsystem']['vegkategori']+vref['vegsystem']['fase']+str(vref['vegsystem']['nummer'])
            if 'kryssystem' in vref:
                lengde = vref['kryssystem']['til_meter'] - vref['kryssystem']['fra_meter']
            else:
                lengde = vref['strekning']['til_meter'] - vref['strekning']['fra_meter']
            if vegsystem not in lengder:
                lengder[vegsystem] = lengde
            else:
                lengder[vegsystem] += lengde
    lengder = {key:round(value) for key, value in lengder.items()}
    return lengder

def tell_lengde_per_fylke(df):
    lengder = {}
    df = df.rename(columns={'lokasjon.fylker':'Fylker', 'lokasjon.lengde':'lengde', 'Stedfestingslengde':'lengde'})
    for row in df.itertuples():
        fylker = row.Fylker
        lengde = row.lengde / len(fylker)
        for fylke in fylker:
            if fylke not in lengder:
                lengder[fylke] = lengde
            else:
                lengder[fylke] += lengde
    lengder = {key:round(value) for key, value in lengder.items()}
    return lengder

def tell_brulengde_og_antall_per_fylke(df):
    lengder = {}
    antall = {}
    df = df.rename(columns={'ET_1313.Lengde':'ET_lengde'})
    for row in df.itertuples():
        fylker = row.Fylker
        lengde = row.ET_lengde / len(fylker) if pd.notna(row.ET_lengde) else row.Stedfestingslengde / len(fylker)
        for fylke in fylker:
            if fylke not in lengder:
                lengder[fylke] = lengde
                antall[fylke] = 1
            else:
                lengder[fylke] += lengde
                antall[fylke] += 1
    lengder = {key:round(value) for key, value in lengder.items()}
    return lengder, antall

def tell_antall_per_fylke(df):
    antall = {}
    df = df.rename(columns={'lokasjon.fylker':'Fylker'})
    for row in df.itertuples():
        fylker = row.Fylker
        for fylke in fylker:
            if fylke not in antall:
                antall[fylke] = 1
            else:
                antall[fylke] += 1
    return antall

def tell_antall_og_lengde_per_fylke(df):
    lengder = {}
    antall = {}
    df = df.rename(columns={'lokasjon.fylker':'Fylker', 'lokasjon.lengde':'lengde'})
    for row in df.itertuples():
        fylker = row.Fylker
        lengde = row.lengde / len(fylker)
        for fylke in fylker:
            if fylke not in antall:
                lengder[fylke] = lengde
                antall[fylke] = 1
            else:
                lengder[fylke] += lengde
                antall[fylke] += 1
    lengder = {key:round(value) for key, value in lengder.items()}
    return lengder, antall

def tell_vegnett_lengde_per_fylke(df):
    lengder = {}
    df = df.rename(columns={'geometri.lengde':'geometrilengde'})
    for row in df.itertuples():
        fylke = row.fylke
        lengde = row.geometrilengde
        if fylke not in lengder:
            lengder[fylke] = lengde
        else:
            lengder[fylke] += lengde
    lengder = {key:round(value) for key, value in lengder.items()}
    return lengder

def rapportgenerator(df, filter, rapportnavn, arknavn):
    df = df.sort_values(by=['Fylke'])
    #df.to_excel(f'src/arb_kostrarapportering_2025/rapporter/{rapportnavn}.xlsx')
    writer = pd.ExcelWriter(f'src/arb_kostrarapportering_2025/rapporter/{rapportnavn}.xlsx', engine='openpyxl')
    df.to_excel(writer, sheet_name=arknavn, index=False)

    filter_df = pd.DataFrame.from_dict(filter, orient='index', columns=[''])
    filter_df.index.name = 'Filter'
    filter_df = filter_df.reset_index()

    filter_df.to_excel(writer, sheet_name='Metadata', index=False)
    writer.close()

def rapportgenerator_24(df, df2, filter1, filter2, rapportnavn, arknavn, arknavn2, metadata1, metadata2):
    df = df.sort_values(by=['Fylke'])
    df2 = df2.sort_values(by=['Fylke'])
    #df.to_excel(f'src/arb_kostrarapportering_2025/rapporter/{rapportnavn}.xlsx')
    writer = pd.ExcelWriter(f'src/arb_kostrarapportering_2025/rapporter/{rapportnavn}.xlsx', engine='openpyxl')
    df.to_excel(writer, sheet_name=arknavn, index=False)
    df2.to_excel(writer, sheet_name=arknavn2, index=False)

    filter1_df = pd.DataFrame.from_dict(filter1, orient='index', columns=[''])
    filter1_df.index.name = 'Filter'
    filter1_df = filter1_df.reset_index()

    filter1_df.to_excel(writer, sheet_name=metadata1, index=False)

    filter2_df = pd.DataFrame.from_dict(filter2, orient='index', columns=[''])
    filter2_df.index.name = 'Filter'
    filter2_df = filter2_df.reset_index()

    filter2_df.to_excel(writer, sheet_name=metadata2, index=False)
    writer.close()

def main(kostranr, **kwargs):
    pass

if __name__ == "__main__":
    f = vegnettsfilter()
    r = RoadNetworkDownloader("prod", **f)
    r.download()
    r.export(file_name=f'src/arb_kostrarapportering_2025/Road_network_ER', file_type='excel')