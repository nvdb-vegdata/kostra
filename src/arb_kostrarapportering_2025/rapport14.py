from api.download_nvdb_data import FeatureTypeDownloader
from arb_kostrarapportering_2025.main import fagdatafilter, tell_antall_per_fylke, rapportgenerator
import pandas as pd
from shapely import wkt

def main():
    f = fagdatafilter()
    f['vegsystemreferanse'] = 'Fv'
    f['inkluder'] = 'lokasjon,egenskaper,relasjoner'

    obj = FeatureTypeDownloader(581, "prod", **f)
    obj.download()
    obj.populate_columns(True, False, True, True, False)
    obj_df = obj.objects

    obj_df.to_excel("src/arb_kostrarapportering_2025/test_rapport14.xlsx")
    antall = tell_antall_per_fylke(obj_df)

    antall_df = pd.DataFrame.from_dict(antall, orient='index', columns=['Lengde [m]'])
    antall_df.index.name = 'Fylke'
    antall_df = antall_df.reset_index()

    rapportgenerator(antall_df, f, "Kostra 14 - Fylkesveg antall tunnel", "Fv antall tunnel")

if __name__ == "__main__":
    main()