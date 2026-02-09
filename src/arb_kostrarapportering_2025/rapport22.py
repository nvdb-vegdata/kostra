from api.download_nvdb_data import RoadNetworkDownloader
from arb_kostrarapportering_2025.main import vegnettsfilter, tell_vegnett_lengde_per_fylke, rapportgenerator
import pandas as pd
from shapely import wkt
import geopandas as gpd

def main():
    f = vegnettsfilter()
    f['vegsystemreferanse'] = 'Fv'
    f['typeveg'] = 'kanalisertVeg,enkelBilveg,rampe,rundkjøring,gangOgSykkelveg,sykkelveg,gangveg,gatetun'
    f['trafikantgruppe'] = 'G'

    r = RoadNetworkDownloader("prod", **f)
    r.download()
    r_df = r.road_segments

    r_df.to_excel("src/arb_kostrarapportering_2025/test_rapport22.xlsx")
    
    r_df['geometri.wkt'] = r_df['geometri.wkt'].apply(wkt.loads) # type: ignore
    r_gdf = gpd.GeoDataFrame(r_df, geometry='geometri.wkt', crs=5973)
    r_gdf.to_file("src/arb_kostrarapportering_2025/rapporter/Kostra 22 - Fylkesveg gang- og sykkelveg.geojson", driver='GeoJSON')

    #rapportgenerator(lengde_df, f, "Kostra 22 - Fylkesveg gang- og sykkelveg", "Fv gang- og sykkelvel")

if __name__ == "__main__":
    main()