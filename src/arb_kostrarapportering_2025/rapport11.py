from api.download_nvdb_data import FeatureTypeDownloader
from arb_kostrarapportering_2025.main import fagdatafilter, tell_lengde_per_fylke, rapportgenerator, v3_hent_objekter
import pandas as pd

def main():
    f = fagdatafilter()
    f['vegsystemreferanse'] = 'Fv'
    f['egenskap'] = '1216=3615'
    f['overlapp'] = '540(4623>=5000)'
    f['inkluder'] = 'lokasjon'

    obj_df = v3_hent_objekter(241, **f)
    obj_df = obj_df.rename(columns={'lokasjon.lengde' : 'lengde', 'lokasjon.fylker' : 'Fylker'})
    print(obj_df)

    obj_df.to_excel("src/arb_kostrarapportering_2025/test_rapport11.xlsx")
    lengde = tell_lengde_per_fylke(obj_df)

    lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde [m]'])
    lengde_df.index.name = 'Fylke'
    lengde_df = lengde_df.reset_index()

    rapportgenerator(lengde_df, f, "Kostra 11 - Fylkesveg uten fast dekke ÅDT over 5000", "Fv grus over 5000 ÅDT")

if __name__ == "__main__":
    main()