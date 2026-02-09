from api.download_nvdb_data import FeatureTypeDownloader
from arb_kostrarapportering_2025.main import fagdatafilter, tell_antall_og_lengde_per_fylke, rapportgenerator
import pandas as pd

def main():
    f = fagdatafilter()
    f['vegsystemreferanse'] = 'Fv'
    f['egenskap'] = 'egenskap(9500)=13384'
    f['inkluder'] = 'lokasjon'

    obj = FeatureTypeDownloader(836, "prod", **f)
    obj.download()
    obj_df = obj.objects

    obj_df.to_excel("src/arb_kostrarapportering_2025/test_rapport23.xlsx")
    lengde, antall = tell_antall_og_lengde_per_fylke(obj_df)

    lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde [m]'])
    lengde_df.index.name = 'Fylke'
    lengde_df = lengde_df.reset_index()

    antall_df = pd.DataFrame.from_dict(antall, orient='index', columns=['Antall [stk]'])
    antall_df.index.name = 'Fylke'
    antall_df = antall_df.reset_index()

    resultat_df = pd.merge(lengde_df, antall_df, how="outer", on='Fylke')
    rapportgenerator(resultat_df, f, "Kostra 23 - Fylkesveg med forsterket midtoppmerking", "Fv med FMO")

if __name__ == "__main__":
    main()