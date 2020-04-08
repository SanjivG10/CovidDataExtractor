from scrapper import getDataCountryWise,countDict
import re
import pandas as pd 


def changeToInt(val):
    val = val.strip()
    val = val.replace(',','')
    val = val.replace('+','')
    if val:
        return int(val)
    else:
        return 0

def get_dict_again(sort_by_val):
    countryData = getDataCountryWise()
    df = pd.DataFrame(countryData)
    df = df.iloc[1:len(df)]
    df_total_cases= df[sort_by_val].apply(changeToInt)
    df[sort_by_val]  = df_total_cases
    df = df.sort_values(by=sort_by_val,ascending=False)
    return df.to_dict('index').values()