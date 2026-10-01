from api.download_nvdb_data import FeatureTypeDownloader
from arb_kostrarapportering_2026.main import fagdatafilter, tell_lengde_per_fylke, rapportgenerator
import pandas as pd
from shapely import wkt

def main():
    f = fagdatafilter()
    f['vegsystemreferanse'] = 'Fv'
    f['egenskap'] = 'egenskap(12057)=20911'
    f['inkluder'] = 'lokasjon'
    f['sideanlegg'] = 'false'
    f['adskiltelop'] = 'med,nei'

    obj = FeatureTypeDownloader(900, "prod", **f)
    obj.download()
    obj.populate_columns(False, False, False, True, False)
    obj_df = obj.objects

    obj_df['Lokasjonsgeometri'] = obj_df['Lokasjonsgeometri'].apply(wkt.loads) # type: ignore
    obj_df['Stedfestingslengde'] = obj_df.apply(lambda row: row['Stedfestingslengde'] if pd.notna(row['Stedfestingslengde']) else row['Lokasjonsgeometri'].length, axis=1)

    #obj_df.to_excel("test_rapport26.xlsx")
    lengde = tell_lengde_per_fylke(obj_df)

    lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde [km]'])
    lengde_df['Lengde [km]'] = lengde_df['Lengde [km]'].apply(lambda x: round(x/1000))
    lengde_df.index.name = 'Fylke'
    lengde_df = lengde_df.reset_index()

    rapportgenerator(lengde_df, f, "Kostra 26 - Fylkesveg tillatt kjøretøylengde 25,25m", "Fv lengde 25,25m")

if __name__ == "__main__":
    main()