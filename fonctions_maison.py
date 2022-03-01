import pandas as pd 
def extraire_la_premiere_lettre(serie):
    #recupere une serie en ragument
    #retourne un dataframe (comptabilite col transformer)    
    return pd.DataFrame(serie.str[0])