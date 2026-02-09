from api.download_nvdb_data import FeatureTypeDownloader
from arb_kostrarapportering_2025.main import fagdatafilter, tell_lengde_per_fylke, rapportgenerator
import pandas as pd
from shapely import wkt

def main():
    f = fagdatafilter()
    f['vegsystemreferanse'] = 'Fv'
    f['egenskap'] = 'egenskap(10913)=18254 OR egenskap(10913)=18255 OR egenskap(10913)=18256'
    f['inkluder'] = 'lokasjon'
    f['sideanlegg'] = 'false'
    f['adskiltelop'] = 'med,nei'

    obj = FeatureTypeDownloader(904, "prod", **f)
    obj.download()
    obj.populate_columns(False, False, False, True, False)
    obj_df = obj.objects

    obj_df['Lokasjonsgeometri'] = obj_df['Lokasjonsgeometri'].apply(wkt.loads) # type: ignore
    obj_df['Stedfestingslengde'] = obj_df.apply(lambda row: row['Stedfestingslengde'] if pd.notna(row['Stedfestingslengde']) else row['Lokasjonsgeometri'].length, axis=1)

    obj_df.to_excel("src/arb_kostrarapportering_2025/test_rapport8.xlsx")
    lengde = tell_lengde_per_fylke(obj_df)

    lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde [m]'])
    lengde_df.index.name = 'Fylke'
    lengde_df = lengde_df.reset_index()

    rapportgenerator(lengde_df, f, "Kostra 08 - Fylkesveg maks vogntoglengde under 19.5m,", "Fv lengde u 19,5m")

if __name__ == "__main__":
    main()