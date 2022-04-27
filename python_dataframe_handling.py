import pandas as pd
df1=pd.read_csv('01 - astra_stream_data.csv',header=0)

df2['HSL']=df2.apply(lambda x: int(x['Overall_Customer Happiness Score'].split(":")[0]),axis=1)
df2['HSU']=df2.apply(lambda x: int(x['Overall_Customer Happiness Score'].split(":")[1]),axis=1)

df2['LCDL']=df2.apply(lambda x: int(x['Last_Contacted_Days_Elapsed'].split(":")[0]),axis=1)
df2['LCDU']=df2.apply(lambda x: int(x['Last_Contacted_Days_Elapsed'].split(":")[1]),axis=1)

df4=df3.loc[np.where(df3['User_ID']==custid)]

for n in range(50):
    custid=df1['custid'][n]
    if df3.loc[np.where(df3['User_ID']==custid)].any()[0]:
        
        for i in range(len(df2)):
            df4=pd.DataFrame()
            df4=df3.loc[np.where(df3['User_ID']==custid)]
            if df4.iloc[0][1] >= df2['HSL'][i] and df4.iloc[0][1] <= df2['HSU'][i]:
                if df4.iloc[0][3] >= df2['LCDL'][i] and df4.iloc[0][3] <= df2['LCDU'][i]:
                    if df2['Customer Segment'][i] == df4.iloc[0][2] and df2['Last Campaign_Outcome'][i] == df4.iloc[0][4] and df2.iloc[0][4]== df4.iloc[0][5]:
                        print(df2['Rule_ID'][i])
                        data = {'AstraID':[custid], 'RuleID':[df2['Rule_ID'][i]],'CampaignID':[df2['Campaign_Id'][i]]} 
                        df = pd.DataFrame(data)
                        x=df.to_csv(index=False,header=True) 
            
                        print(x)
                        
 for n in range(50):
    custid=df1['custid'][n]
    if df3.loc[np.where(df3['User_ID']==custid)].any()[0]:
        df4=df3.loc[np.where(df3['User_ID']==custid)].reset_index()
        for i in range(len(df2)):
            if df4['Overall_Customer_Happiness_Score'][0] >= df2['HSL'][i] and df4['Overall_Customer_Happiness_Score'][0] <= df2['HSU'][i]:
                if df4['Last_Contacted_Days_Elapsed'][0] >= df2['LCDL'][i] and df4['Last_Contacted_Days_Elapsed'][0] <= df2['LCDU'][i]:
                    if df2['Customer Segment'][i] == df4['Customer_Segment'][0] and df2['Last Campaign_Outcome'][i] == df4['Last_Campaign_Outcome'][0] and df2['Preferred_Channel'][i]==df4['Preferred_Channel'][0]:
                        #print(df2['Rule_ID'][i])
                        data = {'AstraID':[custid], 'RuleID':[df2['Rule_ID'][i]],'CampaignID':[df2['Campaign_Id'][i]]} 
                        df = pd.DataFrame(data)
                        x=df.to_csv(index=False,header=True) 
                        print(x)
                        
                        
