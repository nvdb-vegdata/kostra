from api.download_nvdb_data import FeatureTypeDownloader
from arb_kostrarapportering_2025.main import fagdatafilter, tell_brulengde_og_antall_per_fylke, rapportgenerator
import pandas as pd

def main():
    f = fagdatafilter()
    f['vegsystemreferanse'] = 'Fv'
    f['egenskap'] = 'egenskap(1263)=7304 OR egenskap(1263)=7305'
    f['inkluder'] = 'lokasjon,egenskaper'
    del f['trafikantgruppe']

    obj = FeatureTypeDownloader(60, "prod", **f)
    obj.download()
    obj.populate_columns(True, False, False, True, False)
    obj_df = obj.objects

    obj_df.to_excel("src/arb_kostrarapportering_2025/test_rapport17.xlsx")
    lengde, antall = tell_brulengde_og_antall_per_fylke(obj_df)

    lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde [m]'])
    lengde_df.index.name = 'Fylke'
    lengde_df = lengde_df.reset_index()

    antall_df = pd.DataFrame.from_dict(antall, orient='index', columns=['Antall [stk]'])
    antall_df.index.name = 'Fylke'
    antall_df = antall_df.reset_index()

    resultat_df = pd.merge(lengde_df, antall_df, how="outer", on='Fylke')
    rapportgenerator(resultat_df, f, "Kostra 17 - Bruer fylkesveg", "Bruer fylkesveg")

if __name__ == "__main__":
    main()