from api.download_nvdb_data import FeatureTypeDownloader
from arb_kostrarapportering_2025.main import fagdatafilter, tell_lengde_per_fylke, rapportgenerator
import pandas as pd

def main():
    f = fagdatafilter()
    f['vegsystemreferanse'] = 'Fv'
    f['egenskap'] = 'egenskap(2021)=2726 OR egenskap(2021)=2728 OR egenskap(2021)=11576 OR egenskap(2021)=2730 OR egenskap(2021)=19885'
    f['inkluder'] = 'lokasjon'
    f['sideanlegg'] = 'false'
    f['adskiltelop'] = 'med,nei'

    obj = FeatureTypeDownloader(105, "prod", **f)
    obj.download()
    obj_df = obj.objects

    obj_df.to_excel("src/arb_kostrarapportering_2025/test_rapport7.xlsx")
    lengde = tell_lengde_per_fylke(obj_df)

    lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde [m]'])
    lengde_df.index.name = 'Fylke'
    lengde_df = lengde_df.reset_index()

    rapportgenerator(lengde_df, f, "Kostra 07 - Fylkesveg fartsgrense maks 50kmt", "Fv maks 50kmt")

if __name__ == "__main__":
    main()