import os
import pandas as pd
import re
import xlsxwriter
import numpy as np



def main():
    filePath = 'C:\\Users\\rmccarth\\AppData\\Local\\Continuum\\anaconda3\\repositoryPythonForDevs\\livenamer\\LiveNamer\\YouTube_Day1_Clean.xlsx'
    df = pd.read_excel(filePath)
    print('read in file..')
    
    df = pd.DataFrame(df, columns=['Title', 'Viewer_Count'])
    df['Title'].replace(r'[^\x00-\x7F]', '', regex=True, inplace=True)
    df['Title'] =df['Title'].str.strip()
    df['Title'].replace('', np.nan, inplace=True)

    df.dropna(inplace=True)

    writer = pd.ExcelWriter('out_youTube.xlsx', engine='xlsxwriter')
    df.to_excel(writer)
    writer.save()
    

main()