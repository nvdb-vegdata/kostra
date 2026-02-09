from api.download_nvdb_data import FeatureTypeDownloader
from arb_kostrarapportering_2025.main import fagdatafilter, tell_lengde_per_fylke, rapportgenerator_24
import pandas as pd

def main():
    f = fagdatafilter()
    f['vegsystemreferanse'] = 'Fv'
    f['egenskap'] = '1216=3615'
    f['inkluder'] = 'lokasjon'

    obj = FeatureTypeDownloader(241, "prod", **f)
    obj.download()
    obj_df = obj.objects

    obj_df.to_excel("src/arb_kostrarapportering_2025/test_rapport3_1.xlsx")
    lengde = tell_lengde_per_fylke(obj_df)

    lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde kjøreveg [m]'])
    lengde_df.index.name = 'Fylke'
    lengde_df1 = lengde_df.reset_index()

    f2 = f.copy()
    f2['trafikantgruppe'] = 'G'

    obj = FeatureTypeDownloader(241, "prod", **f2)
    obj.download()
    obj_df = obj.objects

    obj_df.to_excel("src/arb_kostrarapportering_2025/test_rapport3_2.xlsx")
    lengde = tell_lengde_per_fylke(obj_df)

    lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde gang/sykkelveg [m]'])
    lengde_df.index.name = 'Fylke'
    lengde_df2 = lengde_df.reset_index()

    rapportgenerator_24(lengde_df1, lengde_df2, f, f2, "Kostra 03 - Fylkesveg uten fast dekke", "Fv grus K", "Fv grun GS", "Metadata K", "Metadata GS")

if __name__ == "__main__":
    main()