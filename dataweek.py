"""
    
    
  Altra fonte dati:

    https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv

    https://raw.githubusercontent.com/boolean-data-analytics/data/main/benzina_gestori_2022.csv
    https://raw.githubusercontent.com/boolean-data-analytics/data/main/benzina_prezzi_2022.csv

    
"""

from icecream import ic
import pandas as pd
import os
from pathlib import Path


if __name__ == "__main__":
    """_summary_
    """
    ic.enable()

    # Get Flussi
    programname = os.path.abspath(__file__)
    programpath = os.getcwd()
    # Get CSV via file
    #programparentpath = (Path(programpath).parent.absolute())
    #fileprezzocsv = os.path.join(programparentpath, "Flussi\\prezzo_alle_8.csv")
    #ic(fileprezzocsv)
    #fprezzo = open(fileprezzocsv, "r")
    #lines_prezzo= fprezzo.readlines()
    #ic(lines_prezzo)
    # Get CSV via http
    df_prezzo = pd.read_csv("https://raw.githubusercontent.com/boolean-data-analytics/data/main/benzina_prezzi_2022.csv")
    ic(df_prezzo)
    df_prezzo.to_csv("./flussi/prezzo.csv", encoding='utf-8',index=False)
    df_anagrafe = pd.read_csv("https://raw.githubusercontent.com/boolean-data-analytics/data/main/benzina_gestori_2022.csv")
    ic(df_anagrafe)
    df_anagrafe.to_csv("./flussi/anagrafe.csv", encoding='utf-8', index=False)
    # Merge
    df_anagrafe_verona = df_anagrafe[df_anagrafe['Comune']=='VERONA']
    df_merge = df_anagrafe_verona.merge(df_prezzo, how='left', on='idImpianto')
    #df_merge = df_anagrafe.merge(df_prezzo, how='left', on='idImpianto')
    df_merge.to_csv(".\\flussi\\merge.csv", encoding="utf-8", index=False)
    ic(df_merge)
    ic.disable()