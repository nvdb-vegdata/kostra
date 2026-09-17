from api.download_nvdb_data import FeatureTypeDownloader
from arb_kostrarapportering_2026.main import fagdatafilter, tell_antall_per_fylke, rapportgenerator
import pandas as pd
from shapely import wkt

def main():
    f = fagdatafilter()
    f['vegsystemreferanse'] = 'Fv'
    f['egenskap'] = 'egenskap(9229)=12865 AND ((egenskap(7560)=9829) OR (egenskap(7560)=null AND (egenskap(7559)=9825 OR egenskap(7559)=null)))'
    f['inkluder'] = 'lokasjon,egenskaper,relasjoner'
    del f['trafikantgruppe']

    obj = FeatureTypeDownloader(64, "prod", **f)
    obj.download()
    obj.populate_columns(True, False, True, True, False)
    obj_df = obj.objects

    obj_df.to_excel("test_rapport27.xlsx")
    antall = tell_antall_per_fylke(obj_df)

    antall_df = pd.DataFrame.from_dict(antall, orient='index', columns=['Antall [stk]'])
    antall_df.index.name = 'Fylke'
    antall_df = antall_df.reset_index()

    rapportgenerator(antall_df, f, "Kostra 27 - Fylkesveg antall ferjekai", "Fv antall ferjekai")

if __name__ == "__main__":
    main()