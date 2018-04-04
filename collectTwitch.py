import requests  
import json
import bs4


def main():
    key_value = get_twitch()                                # Take the value given by the "cursor" field in the JSON response and store it in key_value. 
    """while key_value != None:                                # Trying to iterate here in order to pull down all pages based on the cursor field number.
        get_next_page(key_value)"""                            # When the cursor field is not longer populated, we don't have to query the API anymore (we willl have all data)

    print('out of loop')                

    
    
#def create_json_library():

def get_twitch():
    
    URL = 'https://api.twitch.tv/helix/streams'                         
    headers = {"Client-ID": "t8ag4decgvfrpm3foi7mxb3rgqgleg"}
    response = requests.get(URL, headers=headers)                   # Standard requests-module request for the API. 

    parsed_json = json.loads(response.text)                         # Stores the response in JSON dictionary format. 
    page_number = parsed_json['pagination']['cursor']               # Storing the cursor value here (JSON dictionary lookup)
    
    storage = []
    for item in parsed_json['data']:
        if 'title' and 'viewer_count' in item:
            #print(item['title'] + ' ' + str(item['viewer_count']))
            storage.append(item['title'])
            storage.append(item['viewer_count'])
            with open("workfile.txt",'a',encoding = 'utf-8') as dirtyfile:
                dirtyfile.write(item['title'] + ' ' + str(item['viewer_count']))
   
    


    return page_number


def get_next_page(page_number):                                     # Pretty much the same stuff here but passing the cursor number in the paramaters
                                                                    # In order to make sure we are querying the next page. 
    URL = 'https://api.twitch.tv/helix/streams'
    headers = {"Client-ID": "t8ag4decgvfrpm3foi7mxb3rgqgleg"}
    params = {"after": page_number}
    response = requests.get(URL, headers=headers, params=params)    
    print(response.status_code)

    parsed_json = json.loads(response.text)
    iterative_page = parsed_json['pagination']['cursor']
    return iterative_page

main()

# twitch client ID: t8ag4decgvfrpm3foi7mxb3rgqgleg
# twitch client secret: pgbt0f4li1d0giof91z5ug68klhstn


