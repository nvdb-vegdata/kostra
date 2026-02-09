#Motorveg på fylkesveg
from api.download_nvdb_data import FeatureTypeDownloader
from arb_kostrarapportering_2025.main import fagdatafilter, tell_lengde_per_vegsystem, rapportgenerator
import pandas as pd

def main():
    f = fagdatafilter()
    f['vegsystemreferanse'] = 'Ev,Rv,Fv,Kv,Pv,Sv'
    f['inkluder'] = 'lokasjon'
    obj = FeatureTypeDownloader(595, "prod", **f)
    obj.download()
    obj.populate_columns(False,False,False,True,False)
    obj_df = obj.objects

    print(obj_df.columns)
    obj_df = obj_df[['Stedfestingslengde', 'Fylker', 'Vegkategorier']]
    obj_df.rename(columns={'Stedfestingslengde':'lengde'}, inplace=True)
    obj_df['Fylker'] = obj_df['Fylker'].apply(lambda x: x[0])
    obj_df['Vegkategorier'] = obj_df['Vegkategorier'].apply(lambda x: x[0])
    lengde_df = obj_df.groupby(['Vegkategorier', 'Fylker']).agg({'lengde' : 'sum'}).reset_index()

    writer = pd.ExcelWriter(f'src/arb_kostrarapportering_2025/rapporter/Kostra 02 - EKSTRA alle motor- og motortrafikkveger.xlsx', engine='openpyxl')
    lengde_df.to_excel(writer, sheet_name="Motor- og motortrafikkveg", index=False)

    filter_df = pd.DataFrame.from_dict(f, orient='index', columns=[''])
    filter_df.index.name = 'Filter'
    filter_df = filter_df.reset_index()

    filter_df.to_excel(writer, sheet_name='Metadata', index=False)
    writer.close()
    #obj_df.to_excel("src/arb_kostrarapportering_2025/test_rapport2.xlsx")
    #lengde = tell_lengde_per_vegsystem(obj_df)

    #lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde [m]'])
    #lengde_df.index.name = 'Fylke'
    #lengde_df = lengde_df.reset_index()

    #rapportgenerator(lengde_df, f, "Kostra 02 - Fylkesveg med motor- og motortrafikkveg", "Fv motor- og motortrafikkveg")

if __name__ == "__main__":
    main()