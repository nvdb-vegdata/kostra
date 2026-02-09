from arb_kostrarapportering_2025.main import vegnettsfilter
from api.download_nvdb_data import RoadNetworkDownloader
import pandas as pd

def transponerFylkePerVegkategori( df ): 
    if 'fylke' in df.columns and 'vegkategori' in df.columns and 'lengde' in df.columns: 
        data = []
        for junk, row in df.iterrows(): 
            data.append( {'fylke' : row['fylke'], row['vegkategori'] : round( row['lengde'] ), }   )

        df = pd.DataFrame( data )
        df = df.groupby( ['fylke']).sum().reset_index()

    else: 
        print( 'Kan ikke transponere denne dataframen per vegkategori. Kolonner=', df.columns) 

    return df 


def transponerKommunePerVegkategori( df ): 
    if 'fylke' in df.columns and 'kommune' in df.columns and 'vegkategori' in df.columns and 'lengde' in df.columns: 
        data  = []
        for junk, row in df.iterrows(): 
            data.append( {'fylke' : row['fylke'], 'kommune' : row['kommune'],  row['vegkategori'] : round( row['lengde'] ), }   )
            
        df = pd.DataFrame( data )
        df = df.groupby( ['fylke', 'kommune']).sum().reset_index()

    else: 
        print( 'Kan ikke transponere denne dataframen per kommune og vegkategori. Kolonner=', df.columns) 

    return df 

def fylkesnr2fylkesnavn( df, fylkesnrkolonne='fylke'):
    fylkesnavn = {  11: 'Rogaland',
                    54: 'Troms og Finnmark',
                    18: 'Nordland',
                    15: 'Møre og Romsdal',
                    34: 'Innlandet',
                    42: 'Agder',
                    38: 'Vestfold og Telemark',
                    46: 'Vestland',
                    30: 'Viken',
                    3: 'Oslo',
                    50: 'Trøndelag', 
                    31 : 'Østfold', 
                    32 : 'Akershus', 
                    33 : 'Buskerud', 
                    39 : 'Vestfold', 
                    40 : 'Telemark',
                    55 : 'Troms',
                    56 : 'Finnmark'
                    }

    df = df.copy()
    df[fylkesnrkolonne] = df[fylkesnrkolonne].apply( lambda x : fylkesnavn[x])
    return df 

def main():
    f = vegnettsfilter()
    f['vegsystemreferanse'] = 'Ev,Rv,Fv,Kv,Sv,Pv'
    r = RoadNetworkDownloader("prod", **f)
    r.download()
    r_df = r.road_segments

    r_df = r_df[['fylke', 'kommune', 'vegsystemreferanse.kryssystem.kryssystem', 'vegsystemreferanse.vegsystem.vegkategori', 'lengde']]
    r_df.rename(columns={'vegsystemreferanse.kryssystem.kryssystem' : 'kryssystem', 'vegsystemreferanse.vegsystem.vegkategori' : 'vegkategori'}, inplace=True)
    r_df['lengde'] = r_df['lengde'] / 1000

    r_df_kryss = r_df[pd.notna(r_df['kryssystem'])]
    
    t2 = r_df.groupby(['fylke', 'vegkategori']).agg({'lengde' : 'sum'}).reset_index()
    t2x = r_df_kryss.groupby(['fylke', 'vegkategori']).agg({'lengde' : 'sum'}).reset_index()
    t3 = r_df.groupby(['fylke', 'kommune']).agg({'lengde' : 'sum'}).reset_index()
    t4 = r_df.groupby(['fylke', 'kommune', 'vegkategori']).agg({'lengde' : 'sum'}).reset_index()

    t2 = fylkesnr2fylkesnavn(t2)
    t2_trans = transponerFylkePerVegkategori(t2)
    t2_trans['Riksveg (E+R)'] = t2_trans['E'] + t2_trans['R']
    t2_trans = t2_trans[['fylke', 'Riksveg (E+R)', 'E', 'R', 'F', 'K', 'P', 'S']]

    t2x = fylkesnr2fylkesnavn(t2x)
    t2x_trans = transponerFylkePerVegkategori(t2x)
    t2x_trans['Riksveg (E+R)'] = t2x_trans['E'] + t2x_trans['R']
    t2x_trans = t2x_trans[['fylke', 'Riksveg (E+R)', 'E', 'R', 'F', 'K', 'P']]

    t4_trans = transponerKommunePerVegkategori(t4)

    writer = pd.ExcelWriter(f'src/arb_kostrarapportering_2025/rapporter/Kostra 01 - Vegnett hele landet.xlsx', engine='openpyxl')
    t2_trans.to_excel(writer, sheet_name="Tabell fylker", index=False)
    t2x_trans.to_excel(writer, sheet_name="Lengde kryssystem", index=False)
    t4_trans.to_excel(writer, sheet_name="Tabell kommuner", index=False)
    t2.to_excel(writer, sheet_name="Radvis per fylke og vegkat", index=False)
    t3.to_excel(writer, sheet_name="Radvis per kommune", index=False)
    t4.to_excel(writer, sheet_name="Radvis per kommune og vegkat", index=False)

    filter_df = pd.DataFrame.from_dict(f, orient='index', columns=[''])
    filter_df.index.name = 'Filter'
    filter_df = filter_df.reset_index()

    filter_df.to_excel(writer, sheet_name='Metadata', index=False)
    writer.close()

if __name__ == "__main__":
    main()