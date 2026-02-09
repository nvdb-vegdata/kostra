from api.download_nvdb_data import FeatureTypeDownloader
from arb_kostrarapportering_2025.main import fagdatafilter, tell_brulengde_og_antall_per_fylke, rapportgenerator, v3_hent_objekter
import pandas as pd

def main():
    f = fagdatafilter()
    f['vegsystemreferanse'] = 'Fv'
    f['egenskap'] = 'egenskap(1263)=7304'
    f['overlapp'] = '904(10901=18186 OR 10901=18187 OR 10901=18188 OR 10901=18189 OR 10901=18190)'
    #f['overlapp'] = '60(1263=7304)'
    #f['egenskap'] = 'egenskap(10901)=18186'
    f['inkluder'] = 'lokasjon,egenskaper'
    #f['fylke'] = '56'
    del f['trafikantgruppe']

    df_list = []
    for vgid in [18186, 18187, 18188, 18189, 18190]:
        f['overlapp'] = f'904(10901={vgid})'
        obj_df = v3_hent_objekter(60, **f)
        obj_df = obj_df.rename(columns={'lokasjon.lengde' : 'lengde', 'lokasjon.fylker' : 'Fylker'})
        df_list.append(obj_df)
    obj_df = pd.concat(df_list, ignore_index=True)
    obj_df['ET_lengde'] = obj_df['egenskaper'].apply(lambda x: next((i.get('verdi') for i in x if i.get('id') == 1313), None))
    obj_df.rename(columns={'lengde': 'Stedfestingslengde'}, inplace=True)

    obj_df.to_excel("src/arb_kostrarapportering_2025/test_rapport18.xlsx")
    lengde, antall = tell_brulengde_og_antall_per_fylke(obj_df)

    lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde [m]'])
    lengde_df.index.name = 'Fylke'
    lengde_df = lengde_df.reset_index()

    antall_df = pd.DataFrame.from_dict(antall, orient='index', columns=['Antall [stk]'])
    antall_df.index.name = 'Fylke'
    antall_df = antall_df.reset_index()

    resultat_df = pd.merge(lengde_df, antall_df, how="outer", on='Fylke')
    f['overlapp'] = '904(10901=18186 OR 10901=18187 OR 10901=18188 OR 10901=18189 OR 10901=18190)'
    rapportgenerator(resultat_df, f, "Kostra 18 - Bruer under 10t", "Bruer under 10t")

if __name__ == "__main__":
    main()