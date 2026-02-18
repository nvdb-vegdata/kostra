from api.download_nvdb_data import FeatureTypeDownloader
from arb_kostrarapportering_2025.main import fagdatafilter, tell_lengde_per_fylke, rapportgenerator
import pandas as pd

def main():
    f = fagdatafilter()
    f['vegsystemreferanse'] = 'Fv'
    f['overlapp'] = '616(12628=21827 OR 12628=21823 OR 12628=21923 OR 12628=21926 OR 12628=21824 OR 12628=21922)'
    f['egenskap'] = 'egenskap(1248)=11788 OR egenskap(1248)=11789'
    f['inkluder'] = 'lokasjon,egenskaper'
    f['sideanlegg'] = 'false'
    f['adskiltelop'] = 'med,nei'
    del f['trafikantgruppe']

    obj = FeatureTypeDownloader(5, "prod", **f)
    obj.download()
    obj.populate_columns(True, False, False, True, False)
    obj_df = obj.objects

    #Rekkverk-objekter som er feilklassifiserte i NVDB og filtreres bort fra rapporten:
    obj_df = obj_df[
            ~obj_df['nvdbId'].isin([
                101889419, 336893739, 484480611, 625421619, 671258127, 671258176, 674335610,
                748765592, 760955847, 852957266, 919422071, 1004755045, 1004755046,
                1008888652, 1008888660, 1013448224, 1013448227, 1013448234, 1013448247,
                1013448371, 1013448372, 1013516169, 1013516170, 1013516172, 1014164449,
                1014171127, 1016390477, 1016390479, 1017564058, 1017564062, 1018727703,
                1019431483, 1019431503, 1019484033, 1019787341, 1019787435, 1019787440,
                1019787463, 1019791671, 1021382394, 1021382400, 1021382401, 1022263982,
                1022263985, 1022263986, 1022274406, 1022441085, 1022441086, 1022441087,
                1022441090, 1025170830, 1025285771, 1025927336
                ])]

    obj_df.to_excel("src/arb_kostrarapportering_2025/test_rapport20.xlsx")
    lengde = tell_lengde_per_fylke(obj_df)

    lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde [m]'])
    lengde_df.index.name = 'Fylke'
    lengde_df = lengde_df.reset_index()

    rapportgenerator(lengde_df, f, "Kostra 20 - Fylkesveg to- og trefelt midtrekkverk", "Fv 2-3 felt midtrekkverk")

if __name__ == "__main__":
    main()