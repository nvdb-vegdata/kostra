from api.download_nvdb_data import FeatureTypeDownloader
from arb_kostrarapportering_2025.main import fagdatafilter, tell_lengde_per_fylke, rapportgenerator
import pandas as pd

def main():
    f = fagdatafilter()
    f['vegsystemreferanse'] = 'Fv'
    f['overlapp'] = '616(12628=21827 OR 12628=21823 OR 12628=21923 OR 12628=21926 OR 12628=21824 OR 12628=21922)'
    f['egenskap'] = 'egenskap(1248)=11788 OR egenskap(1248)=11789'
    f['inkluder'] = 'lokasjon,egenskaper'
    f['sideanlegg'] = 'false'
    f['adskiltelop'] = 'med,nei'
    del f['trafikantgruppe']

    obj = FeatureTypeDownloader(5, "prod", **f)
    obj.download()
    obj.populate_columns(True, False, False, True, False)
    obj_df = obj.objects

    obj_df.to_excel("src/arb_kostrarapportering_2025/test_rapport20.xlsx")
    lengde = tell_lengde_per_fylke(obj_df)

    lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde [m]'])
    lengde_df.index.name = 'Fylke'
    lengde_df = lengde_df.reset_index()

    rapportgenerator(lengde_df, f, "Kostra 20 - Fylkesveg to- og trefelt midtrekkverk", "Fv 2-3 felt midtrekkverk")

    #lengde, antall = tell_brulengde_og_antall_per_fylke(obj_df)
    return
    lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde [m]'])
    lengde_df.index.name = 'Fylke'
    lengde_df = lengde_df.reset_index()

    antall_df = pd.DataFrame.from_dict(antall, orient='index', columns=['Antall [stk]'])
    antall_df.index.name = 'Fylke'
    antall_df = antall_df.reset_index()

    resultat_df = pd.merge(lengde_df, antall_df, how="outer", on='Fylke')
    rapportgenerator(resultat_df, f, "Kostra 19 - Bruer høydebegrensning under 4m", "Bru høyde under 4m")

if __name__ == "__main__":
    main()