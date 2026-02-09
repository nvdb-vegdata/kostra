from api.download_nvdb_data import FeatureTypeDownloader
from arb_kostrarapportering_2025.main import fagdatafilter, tell_brulengde_og_antall_per_fylke, rapportgenerator
import pandas as pd

def main():
    f = fagdatafilter()
    f['vegsystemreferanse'] = 'Fv'
    f['egenskap'] = 'egenskap(1263)=7304'
    f['overlapp'] = '591(5277<4 AND (5270=8168 OR 5270=8149))'
    f['inkluder'] = 'lokasjon,egenskaper'

    obj = FeatureTypeDownloader(60, "prod", **f)
    obj.download()
    obj.populate_columns(True, False, False, True, False)
    obj_df = obj.objects

    obj_df.to_excel("src/arb_kostrarapportering_2025/test_rapport19.xlsx")
    lengde, antall = tell_brulengde_og_antall_per_fylke(obj_df)

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