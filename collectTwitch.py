import requests  
import json

def main():
    key_value = get_twitch()
    print(key_value)
    get_next_page(key_value)
      
#def create_json_library():

def get_twitch():
    
    URL = 'https://api.twitch.tv/helix/streams'
    headers = {"Client-ID": "t8ag4decgvfrpm3foi7mxb3rgqgleg"}
    response = requests.get(URL, headers=headers)

    print(response.status_code)
    parsed_json = json.loads(response.text)
    key_value = parsed_json['pagination']['cursor']
    print('passing key... ' + key_value)

    return key_value

def get_next_page(page_number):
    
    URL = 'https://api.twitch.tv/helix/streams'
    headers = {"Client-ID": "t8ag4decgvfrpm3foi7mxb3rgqgleg"}
    params = {"after": page_number}
    print(params)
    response = requests.get(URL, headers=headers, params=params)    
    print(response.status_code)

    parsed_json = json.loads(response.text)
    print(parsed_json)

main()

# twitch client ID: t8ag4decgvfrpm3foi7mxb3rgqgleg
# twitch client secret: pgbt0f4li1d0giof91z5ug68klhstn


