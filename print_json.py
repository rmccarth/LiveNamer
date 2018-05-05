import requests  
import json
import time

#text analytics api

def main():
    
    page_number = None
    page_number = get_twitch(page_number)
    if page_number == 'done':
        print('...All data printed')
        return
    else:                                    # Take the value given by the "cursor" field in the JSON response and store it in key_value. 
        while page_number != None:
            time.sleep(3)                                # Trying to iterate here in order to pull down all pages based on the cursor field number.
            page_number = get_twitch(page_number)                            # When the cursor field is not longer populated, we don't have to query the API anymore (we will have all data)
            if page_number == 'done':
                print('...All data printed')
                return

def get_twitch(after_value):
    
    URL = 'https://api.twitch.tv/helix/streams'                         
    headers = {"Client-ID": "t8ag4decgvfrpm3foi7mxb3rgqgleg"}
    if after_value is None:
        params = {"language": "en"}
    else:
        params = {"after": after_value, "language": "en"}
    response = requests.get(URL, headers=headers, params=params)                   # Standard requests-module request for the API. 
    parsed_json = json.loads(response.text)                      # Stores the response in JSON dictionary format. 
    after_value = parsed_json['pagination']['cursor']               # Storing the cursor value here (JSON dictionary lookup)
    
    if response.status_code != '429':  
        with open("json.txt", 'a', encoding='utf-8') as dirtyfile:                         # fix with
            for item in parsed_json['data']:
                
                        dirtyfile.write(str(item))
                        dirtyfile.write('\n')

    if response.status_code == '429':
        return 'done'
    else:
        return after_value

main()

# twitch client ID: t8ag4decgvfrpm3foi7mxb3rgqgleg
# twitch client secret: pgbt0f4li1d0giof91z5ug68klhstn


