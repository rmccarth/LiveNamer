import openpyxl
import json
import requests
import time

def main():
    wb = openpyxl.load_workbook('out_youTube.xlsx')             #Load workbook + sheet. 
    sheet = wb['test']                                  
    
    item_list = []                                                      #Initialize variables and set values. Create empty list. 
    i = 1
    n = 81758
    while i <= n:
        cell = sheet['a'+str(i)]
        
        dictionary = {'documents':item_list}
        item_list.append({'id':i,'text':cell.value,'language':'en'})

        if i % 30 == 0:                                                 #POSTs to API for every 30 ID's. 
            time.sleep(1)
            serialized_json = json.dumps(dictionary)
            do_POST_request(serialized_json)
            item_list = []                                              #Resets the 
        i = i+1
    if (i-1) % 30 != 0:                                                 #If there are IDs left over, sends those over as well. 
        serialized_json = json.dumps(dictionary)
        do_POST_request(serialized_json)
        

def do_POST_request(input):
    URL = 'https://eastus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'                         
    headers = {'Ocp-Apim-Subscription-Key': '4820ff11f82e4ecb9dbe9812897ece38','Host':'eastus.api.cognitive.microsoft.com','Content-Type':'application/json', 'Accept':'application/json'}
    response = requests.post(URL, headers=headers, data=input)
    print(response.status_code)
    final = json.loads(response.text)
    
    writeToNotepad(final)

def writeToNotepad(file):
    
    with open("AzureYouTube.txt", 'a', encoding='utf-8') as dirtyfile:
        for item in file['documents']:
            if 'score' and 'id' in item:
                
                score = str(item['score'])
                id = str(item['id'])

                dirtyfile.write(id)
                dirtyfile.write('\t')
                dirtyfile.write(score)
                dirtyfile.write('\n')



main()