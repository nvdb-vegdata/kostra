from api.download_nvdb_data import RoadNetworkDownloader
from arb_kostrarapportering_2025.main import vegnettsfilter, tell_vegnett_lengde_per_fylke, rapportgenerator
import pandas as pd

def main():
    f = vegnettsfilter()
    f['vegsystemreferanse'] = 'Fv'
    f['typeveg'] = 'kanalisertVeg,enkelBilveg,rampe,rundkjøring,gangOgSykkelveg,sykkelveg,gangveg,gatetun'
    f['trafikantgruppe'] = 'G'

    r = RoadNetworkDownloader("prod", **f)
    r.download()
    r_df = r.road_segments

    r_df.to_excel("src/arb_kostrarapportering_2025/test_rapport21.xlsx")
    lengde = tell_vegnett_lengde_per_fylke(r_df)

    lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde [m]'])
    lengde_df.index.name = 'Fylke'
    lengde_df = lengde_df.reset_index()

    rapportgenerator(lengde_df, f, "Kostra 21 - Fylkesveg gang- og sykkelveg", "Fv gang- og sykkelvel")

if __name__ == "__main__":
    main()