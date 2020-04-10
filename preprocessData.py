from scrapper import getDataCountryWise,countDict
import re
import pandas as pd 



def changeToInt(val):
    val = str(val).strip()
    if len(val)==0:
        return 0
    val = val.replace(',','')
    val = val.replace('+','')
    return int(val)

def changeEveryStringToInt(df):

    column_names = df.columns.values.tolist()
    for eachColumn in column_names:
        if not eachColumn=='country':
            df_val = df[eachColumn].apply(changeToInt)
            df[eachColumn]  = df_val
    return df

def get_processed_dict(data=None,sort_by_val='total cases',dontProcessNicely=False):
    if not data:
        data = getDataCountryWise()
    df = pd.DataFrame(data)
    df = df.iloc[1:len(df)]
    df = df.fillna(0)
    
    df = changeEveryStringToInt(df)
    if dontProcessNicely:
        return df
    if sort_by_val:
        df = df.sort_values(by=sort_by_val,ascending=False)
    return df.to_dict('records')


def getExploredDataCountryWise(cursor,country,columnName):
    dfs = []
    timeEvents = []
    for eachTimeData in cursor:
        for key,val in eachTimeData.items():
            if not key=='_id':
                recordsINeed = val[1:]
                timeEvents.append(key)
        df = pd.DataFrame().from_records(recordsINeed)
        df = changeEveryStringToInt(df)
        dfs.append(df)
    
    valueToSend= []
    for df in dfs:
        indexOfThatCountryInPresentDF = df.index[df["country"] == country].tolist()[0]
        val = df.iloc[indexOfThatCountryInPresentDF][columnName]
        valueToSend.append(str(val))
    return timeEvents,valueToSend


        
            # if index>0:
            #     print(myNewDFS[indexSecond])
            #     print(newDF)
            #     myNewDFS[indexSecond]=pd.merge(myNewDFS[indexSecond],newDF)
            #     continue
            # myNewDFS.append(newDF)
        
    # USA: {total cases: [day1:'', day2: '', day3: ''...], total deaths [day1: '',day2: '', day3: '']}
    
        #column names from eachDFCOLUMNS

    # for eachDF in dfs:
    #     #Let me get eachData country wise! This shit is dangerous! 
    #     for index in  range(len(allCountries)):
    #         eachCountryRowOfAllData = eachDF.iloc[index]
    #         eachCountryRowDataCollection.append(eachCountryRowOfAllData)
    #         break
    #     break
    # print(eachCountryRowDataCollection)
        # There are about 7 columns of eachColNames.
            # eachCountryTimeWiseData[eachCountry]
        
