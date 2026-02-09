from api.download_nvdb_data import FeatureTypeDownloader
from arb_kostrarapportering_2025.main import fagdatafilter, tell_antall_og_lengde_per_fylke, rapportgenerator_24
import pandas as pd

def hent_voll():
    f = fagdatafilter()
    f['vegsystemreferanse'] = 'Fv'
    f['egenskap'] = 'egenskap(1286)=1996'
    f['inkluder'] = 'lokasjon'

    obj = FeatureTypeDownloader(234, "prod", **f)
    obj.download()
    obj_df = obj.objects
    return obj_df, f

def hent_skjerm():
    f = fagdatafilter()
    f['vegsystemreferanse'] = 'Fv'
    f['egenskap'] = 'egenskap(1247)=1994'
    f['inkluder'] = 'lokasjon'

    obj = FeatureTypeDownloader(3, "prod", **f)
    obj.download()
    obj_df = obj.objects
    return obj_df, f

def main():
    skjerm_df, f_skjerm = hent_skjerm()
    voll_df, f_voll = hent_voll()

    skjerm_df.to_excel("src/arb_kostrarapportering_2025/test_rapport24_1.xlsx")
    voll_df.to_excel("src/arb_kostrarapportering_2025/test_rapport24_2.xlsx")
    lengde, antall = tell_antall_og_lengde_per_fylke(skjerm_df)

    lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde [m]'])
    lengde_df.index.name = 'Fylke'
    lengde_df = lengde_df.reset_index()

    antall_df = pd.DataFrame.from_dict(antall, orient='index', columns=['Antall [stk]'])
    antall_df.index.name = 'Fylke'
    antall_df = antall_df.reset_index()

    resultat1_df = pd.merge(lengde_df, antall_df, how="outer", on='Fylke')

    lengde, antall = tell_antall_og_lengde_per_fylke(voll_df)

    lengde_df = pd.DataFrame.from_dict(lengde, orient='index', columns=['Lengde [m]'])
    lengde_df.index.name = 'Fylke'
    lengde_df = lengde_df.reset_index()

    antall_df = pd.DataFrame.from_dict(antall, orient='index', columns=['Antall [stk]'])
    antall_df.index.name = 'Fylke'
    antall_df = antall_df.reset_index()

    resultat2_df = pd.merge(lengde_df, antall_df, how="outer", on='Fylke')

    rapportgenerator_24(resultat1_df, resultat2_df, f_skjerm, f_voll, "Kostra 24 - Fylkesveg med støyskjerm og voll", "Fv med støyskjerm", "Fv med voll", "Metadata Skjerm", "Metadata Voll")

if __name__ == "__main__":
    main()