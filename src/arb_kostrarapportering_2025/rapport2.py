#Motorveg på fylkesveg
from api.download_nvdb_data import FeatureTypeDownloader
from arb_kostrarapportering_2025.main import fagdatafilter, tell_lengde_per_vegsystem, rapportgenerator
import pandas as pd

def main():
    f = fagdatafilter()
    f['vegsystemreferanse'] = 'Fv'
    f['inkluder'] = 'lokasjon'
    obj = FeatureTypeDownloader(595, "prod", **f)
    obj.download()
    obj_df = obj.objects

    obj_df.to_excel("src/arb_kostrarapportering_2025/test_rapport2.xlsx")
    lengde = tell_lengde_per_vegsystem(obj_df)

    lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde [m]'])
    lengde_df.index.name = 'Fylke'
    lengde_df = lengde_df.reset_index()

    rapportgenerator(lengde_df, f, "Kostra 02 - Fylkesveg med motor- og motortrafikkveg", "Fv motor- og motortrafikkveg")

if __name__ == "__main__":
    main()