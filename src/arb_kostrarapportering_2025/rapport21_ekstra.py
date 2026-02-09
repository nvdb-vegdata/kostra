from api.download_nvdb_data import RoadNetworkDownloader
from arb_kostrarapportering_2025.main import vegnettsfilter, tell_vegnett_lengde_per_fylke, rapportgenerator
import pandas as pd

def main():
    f = vegnettsfilter()
    f['vegsystemreferanse'] = 'Ev,Rv,Fv,Kv,Pv,Sv'
    f['typeveg'] = 'kanalisertVeg,enkelBilveg,rampe,rundkjøring,gangOgSykkelveg,sykkelveg,gangveg,gatetun'
    f['trafikantgruppe'] = 'G'

    r = RoadNetworkDownloader("prod", **f)
    r.download()
    r_df = r.road_segments

    r_df = r_df[['geometri.lengde', 'fylke', 'vegsystemreferanse.vegsystem.vegkategori']]
    r_df = r_df.rename(columns={'geometri.lengde':'lengde', 'vegsystemreferanse.vegsystem.vegkategori':'vegkategori'})
    lengde_df = r_df.groupby(['vegkategori', 'fylke']).agg({'lengde' : 'sum'}).reset_index()

    writer = pd.ExcelWriter(f'src/arb_kostrarapportering_2025/rapporter/Kostra 21 - EKSTRA alle gang- og sykkelveg.xlsx', engine='openpyxl')
    lengde_df.to_excel(writer, sheet_name="Gang- og sykkelvel", index=False)

    filter_df = pd.DataFrame.from_dict(f, orient='index', columns=[''])
    filter_df.index.name = 'Filter'
    filter_df = filter_df.reset_index()

    filter_df.to_excel(writer, sheet_name='Metadata', index=False)
    writer.close()
    #r_df.to_excel("src/arb_kostrarapportering_2025/test_rapport21.xlsx")
    #lengde = tell_vegnett_lengde_per_fylke(r_df)

    #lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde [m]'])
    #lengde_df.index.name = 'Fylke'
    #lengde_df = lengde_df.reset_index()

    #rapportgenerator(lengde_df, f, "Kostra 21 - EKSTRA alle gang- og sykkelveg", "Gang- og sykkelvel")

if __name__ == "__main__":
    main()