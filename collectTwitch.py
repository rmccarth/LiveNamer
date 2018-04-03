import requests  
import json

def main():
    key_value = get_twitch()
    while key_value != None:
        get_next_page(key_value)
    print('out of loop')

    
    
#def create_json_library():

def get_twitch():
    
    URL = 'https://api.twitch.tv/helix/streams'
    headers = {"Client-ID": "t8ag4decgvfrpm3foi7mxb3rgqgleg"}
    response = requests.get(URL, headers=headers)

    parsed_json = json.loads(response.text)
    page_number = parsed_json['pagination']['cursor']
    print('starting to write')
    
    with open("data.text", 'w') as outfile:
        json.dump(parsed_json, outfile)

    return page_number


def get_next_page(page_number):
    
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


