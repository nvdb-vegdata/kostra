from api.download_nvdb_data import RoadNetworkDownloader, FeatureTypeDownloader
from arb_kostrarapportering_2025.main import vegnettsfilter, tell_vegnett_lengde_per_fylke, rapportgenerator, fagdatafilter, tell_lengde_per_fylke
import pandas as pd

def main():
    f = fagdatafilter()
    f['vegsystemreferanse'] = 'Fv'
    f['egenskap'] = '(egenskap(12628)=21825 OR egenskap(12628)=21826) AND (egenskap(12633)=21829 OR egenskap(12633)=21830)'
    f['inkluder'] = 'lokasjon'

    obj = FeatureTypeDownloader(616, "prod", **f)
    obj.download()
    obj_df = obj.objects

    obj_df.to_excel("src/arb_kostrarapportering_2025/test_rapport4.xlsx")
    lengde = tell_lengde_per_fylke(obj_df)

    lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde [m]'])
    lengde_df.index.name = 'Fylke'
    lengde_df = lengde_df.reset_index()

    rapportgenerator(lengde_df, f, "Kostra 04 - Fylkesveg med 4 felt", "Fv med 4 felt")

"""def main():
    f = vegnettsfilter()
    f['vegsystemreferanse'] = 'Fv'
    del f['sideanlegg']

    r = RoadNetworkDownloader("prod", **f)
    r.download()
    r_df = r.road_segments

    excluded_letters = {'S', 'O', 'B', 'H', 'V'}  # Add more letters as needed
    r_df['tellende_feltoversikt'] = r_df['feltoversikt'].apply(lambda x: [i for i in x if not any(letter in i for letter in excluded_letters)])
    r_df = r_df[r_df['tellende_feltoversikt'].apply(lambda x: len(x) >= 4)]

    r_df.to_excel("src/arb_kostrarapportering_2025/test_rapport4.xlsx")
    lengde = tell_vegnett_lengde_per_fylke(r_df)

    lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde [m]'])
    lengde_df.index.name = 'Fylke'
    lengde_df = lengde_df.reset_index()

    rapportgenerator(lengde_df, f, "Kostra 04 - Fylkesveg med 4 felt", "Fv med 4 felt")"""

if __name__ == "__main__":
    main()