import pandas as pd

class ListEachValue:
    # {variableX} (unique) and {variableY} (with separetor) in rows 
    def __init__(self,df,variableX:str, variableY:str, sep:str):
        self.df = df
        self.variableX = variableX
        self.variableY = variableY
        self.sep = sep
        self.created = self.createNewDf(df)
    
    #Create new dataframe for list all cods of {variableX} (unique) and {variableY} (with separetor) in rows 
    def createNewDf(self,df):
        i = 0
        key = 0
        edges = pd.DataFrame()
        for index, row in df.iterrows():    
            if(self.sep in row[self.variableY]):    
                for x in row[self.variableY].split(self.sep):
                    edges = edges.append(pd.DataFrame({self.variableY: x, 'title': 1, 'title': row[self.variableX]}, index=[0]), ignore_index=True, sort=False)            
            else:
                edges= edges.append(pd.DataFrame({self.variableY: row[self.variableY], 'title': 1, 'title': row[self.variableX]}, index=[0]), ignore_index=True, sort=False)                
            i = i + 1
        return edges
    
    def group(self, column):
        a = self.created.groupby(self.created.columns[0]).count().reset_index()
        return a.sort_values(column, ascending=False)

class cleaningDatabase:
    #Init executing function and replace columsn
    def __init__(self, df, col):
        self.col = col
        self.df = df.rename(columns=self.renameColuns)

    #function for replace key by value
    def renameColuns(self,x):
        col = self.col
        #if the change has already been made 
        if(x in col['Value'].values):
            return x.replace('\r\n', '')
        if(x in col['Key'].values):
            return col[col['Key'] == x]['Value'].iloc[0].replace('\r\n', '')
        else:
            return x
    
    #replace strings for lowercase and remove spaces        
    def lowerSpaceValues(self, column):
        if(type(column) == list):
            for y in column:
                self.df[y] = self.df[y].apply(lambda x: x.strip().lower() if type(x) != float else x)
        else:
            self.df[column] = self.df[column].apply(lambda x: x.strip().lower() if type(x) != float else x)
    
    #Get all values in columns that are empty or null
    def getNullValues(self):
        df = self.df
        valoresNulos = [(((len(df) - df.count())  / len(df)) * 100), len(df) - df.count()]
        dfnulos = pd.DataFrame([valoresNulos[0].apply(lambda x: ("{0:.2f} %".format(x))).values,valoresNulos[1].values], columns=df.columns, index=['Relativo','Absoluto']).transpose()
        return(dfnulos)

class VerifyAuthors():
    """docstring for VerifyAuthors"""
    def __init__(self, df):
        self.df = df
        return df['Authors'].apply(lambda x: x.lower().strip())
        
