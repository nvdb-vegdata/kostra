from api.download_nvdb_data import FeatureTypeDownloader
from arb_kostrarapportering_2026.main import fagdatafilter, tell_lengde_per_fylke, rapportgenerator
import pandas as pd

def main():
    f = fagdatafilter()
    f['vegsystemreferanse'] = 'Fv'
    f['egenskap'] = 'egenskap(4623)>=4000'
    f['inkluder'] = 'lokasjon'

    obj = FeatureTypeDownloader(540, "prod", **f)
    obj.download()
    obj_df = obj.objects

    #obj_df.to_excel("src/arb_kostrarapportering_2026/test_rapport12.xlsx")
    lengde = tell_lengde_per_fylke(obj_df)

    lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde [km]'])
    lengde_df['Lengde [km]'] = lengde_df['Lengde [km]'].apply(lambda x: round(x/1000))
    lengde_df.index.name = 'Fylke'
    lengde_df = lengde_df.reset_index()

    rapportgenerator(lengde_df, f, "Kostra 12 - Fylkesveg ÅDT over 4000", "Fv ÅDT over 4000")

    print(obj_df.shape)
    print(obj_df.head())

if __name__ == "__main__":
    main()