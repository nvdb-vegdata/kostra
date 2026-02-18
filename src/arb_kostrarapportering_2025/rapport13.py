from api.download_nvdb_data import FeatureTypeDownloader
from arb_kostrarapportering_2025.main import fagdatafilter, tell_lengde_per_fylke, rapportgenerator
import pandas as pd
from shapely import wkt

def main():
    f = fagdatafilter()
    f['vegsystemreferanse'] = 'Fv'
    f['inkluder'] = 'lokasjon,egenskaper,relasjoner'
    del f['trafikantgruppe']

    obj = FeatureTypeDownloader(581, "prod", **f)
    obj.download()
    obj.populate_columns(True, False, True, True, False)
    obj_df = obj.objects
    print(obj_df.columns)
    obj_df['lengde'] = obj_df['ET_8945.Lengde, offisiell']

    mangler_lengde_df = obj_df[pd.isna(obj_df['lengde'])]
    har_lengde_df = obj_df[pd.notna(obj_df['lengde'])]

    løp_ider = mangler_lengde_df['Barn_67.Tunnelløp'].values.tolist()
    løp_ider = [item for sublist in løp_ider for item in sublist]
    f['inkluder'] = 'egenskaper,geometri,lokasjon'
    f['ider'] = ','.join([str(i) for i in løp_ider])
    løp_obj = FeatureTypeDownloader(67, "prod", **f)
    løp_obj.download()
    løp_obj.populate_columns(True, False, False, True, True)
    løp_df = løp_obj.objects
    løp_df['Geometri'] = løp_df['Geometri'].apply(wkt.loads) # type: ignore
    løp_df['lengde'] = løp_df.apply(lambda row: row['ET_1317.Lengde'] if pd.notna(row['ET_1317.Lengde']) else row['Geometri'].length, axis=1)    
    #løp_df['lengde'] = løp_df['Geometri'].apply(lambda x: x.length)
    løp_df = løp_df[['nvdbId', 'lengde']]

    length_map = løp_df.set_index('nvdbId')['lengde']
    totals = (
        mangler_lengde_df.explode('Barn_67.Tunnelløp', ignore_index=False)['Barn_67.Tunnelløp']
            .map(length_map)
            .fillna(0)
            .groupby(level=0).sum()
    )
    mangler_lengde_df['lengde'] = totals
    har_lengde_df = har_lengde_df[['nvdbId', 'Fylker', 'lengde']]
    mangler_lengde_df = mangler_lengde_df[['nvdbId', 'Fylker', 'lengde']]

    tunnel_df = pd.concat([har_lengde_df, mangler_lengde_df], ignore_index=True)

    tunnel_df.to_excel("src/arb_kostrarapportering_2025/test_rapport13.xlsx")
    lengde = tell_lengde_per_fylke(tunnel_df)

    lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde [m]'])
    lengde_df.index.name = 'Fylke'
    lengde_df = lengde_df.reset_index()

    del f['ider']
    rapportgenerator(lengde_df, f, "Kostra 13 - Fylkesveg lengde tunnel", "Fv lengde tunnel")

if __name__ == "__main__":
    main()