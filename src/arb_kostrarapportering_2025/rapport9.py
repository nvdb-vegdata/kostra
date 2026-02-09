from api.download_nvdb_data import FeatureTypeDownloader
from arb_kostrarapportering_2025.main import fagdatafilter, tell_antall_per_fylke, rapportgenerator
import pandas as pd

def main():
    f = fagdatafilter()
    f['vegsystemreferanse'] = 'Fv'
    f['egenskap'] = 'egenskap(5277)<4 AND egenskap(5270)=8151'
    f['inkluder'] = 'lokasjon'

    obj = FeatureTypeDownloader(591, "prod", **f)
    obj.download()
    obj_df = obj.objects

    obj_df.to_excel("src/arb_kostrarapportering_2025/test_rapport9.xlsx")
    antall = tell_antall_per_fylke(obj_df)

    antall_df = pd.DataFrame.from_dict(antall, orient='index', columns=['Antall [stk]'])
    antall_df.index.name = 'Fylke'
    antall_df = antall_df.reset_index()

    rapportgenerator(antall_df, f, "Kostra 09 - Undergang lavere enn 4m", "Undergang lavere enn 4m")

if __name__ == "__main__":
    main()