from api.download_nvdb_data import RoadNetworkDownloader
from arb_kostrarapportering_2025.main import vegnettsfilter, tell_vegnett_lengde_per_fylke, rapportgenerator
import pandas as pd

def main():
    f = vegnettsfilter()
    f['vegsystemreferanse'] = 'Fv'
    del f['sideanlegg']

    r = RoadNetworkDownloader("prod", **f)
    r.download()
    r_df = r.road_segments

    r_df = r_df[r_df['feltoversikt'].apply(lambda x: any('K' in i for i in x))]
    r_df['antall_kollektivfelt'] = r_df['feltoversikt'].apply(lambda x: sum(1 for felt in x if 'K' in felt))
    r_df['total_kollektivlengde'] = r_df.apply(lambda row: row['lengde']*row['antall_kollektivfelt'], axis=1)
    r_df['geometri.lengde'] = r_df['total_kollektivlengde']

    r_df.to_excel("src/arb_kostrarapportering_2025/test_rapport25.xlsx")
    lengde = tell_vegnett_lengde_per_fylke(r_df)

    lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde [m]'])
    lengde_df.index.name = 'Fylke'
    lengde_df = lengde_df.reset_index()

    rapportgenerator(lengde_df, f, "Kostra 25 - Fylkesveg med kollektivfelt", "Fv med kollektivfelt")

if __name__ == "__main__":
    main()