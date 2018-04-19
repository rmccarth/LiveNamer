import os
import pandas as pd
import re
import xlsxwriter
import numpy as np



def main():
    filePath = 'C:\\Users\\rmccarth\\AppData\\Local\\Continuum\\anaconda3\\repositoryPythonForDevs\\livenamer\\LiveNamer\\reform_test.xlsx'
    df = pd.read_excel(filePath)
    print('read in file..')
    # print(df)
    # df.replace('[^a-zA-Z0-9_]', [''])
    # print(df)
    df = pd.DataFrame(df, columns=['Title', 'Viewer_Count'])
    df['Title'].replace(r'[^\x00-\x7F]', '', regex=True, inplace=True)
    #df['Title'].replace(r'[^\w+( +\w+)*$]', '', regex=True, inplace=True)
    df['Title'] =df['Title'].str.strip()
    df['Title'].replace('', np.nan, inplace=True)

    df.dropna(inplace=True)

    writer = pd.ExcelWriter('out.xlsx', engine='xlsxwriter')
    df.to_excel(writer)
    writer.save()
    
    # mystring = "hi, my name is *&@*!&(!#$"
    # mystring = re.sub('[^a-zA-Z0-9_]', '', mystring)
    # print(mystring)

main()

#def reformed():
    #with open("test3.txt", 'a', encoding='utf-8') as dirtyfile:                         # fix with
            
            
            
            
            # for item in parsed_json['data']:
                
            #     if 'title' and 'viewer_count' in item:

            #         title = item['title'].replace('\t', "")
            #         if title not in storage:
                    
            #             storage.append(title)
                  
            #             dirtyfile.write(title)                   
            #             storage.append(item['viewer_count'])
            #             dirtyfile.write('\t')
            #             dirtyfile.write(str(item['viewer_count']))
            #             dirtyfile.write('\n')