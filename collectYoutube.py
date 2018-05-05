import requests
import json

# text analytics api

def main():
    #start from findnig category in youtube live videos
    get_category()


#https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&regionCode=US&key=AIzaSyCJED6t5YBwxkVS5_mENZBFfPKq5ErlC7U

#get category_id for all categories in youtube
#Since we found that youtube sometimes cannot response enough data as it shouws, so we decide to use category to get as many data back as possible
#category is how different live videos is organized in topics
def get_category():
    URL = 'https://www.googleapis.com/youtube/v3/videoCategories'
    headers = {}
    params = {"part": "snippet","regionCode":"US","key": "AIzaSyCJED6t5YBwxkVS5_mENZBFfPKq5ErlC7U"}
    response = requests.get(URL, headers=headers, params=params)  # Standard requests-module request for the API.
    parsed_json = json.loads(response.text)
    for item in parsed_json['items']:
        categoryid = item['id']
        nextpage = 'null'
        #get videoid
        get_videoid(nextpage,categoryid)


#get a specific live video id in a page in a catergory

def get_videoid(nextpage,categoryid):
    URL = 'https://www.googleapis.com/youtube/v3/search'
    headers = {}
    if nextpage=='null':

        params = {"part": "snippet", "type": "video", "videoCategoryId":categoryid,"eventType": "live", "maxResults": "50", "relevanceLanguage": "en","key": "AIzaSyCJED6t5YBwxkVS5_mENZBFfPKq5ErlC7U"}

    else:
        params = {"part": "snippet","pageToken": nextpage,"videoCategoryId":categoryid,"type": "video", "eventType": "live", "maxResults": "50", "relevanceLanguage": "en","key": "AIzaSyCJED6t5YBwxkVS5_mENZBFfPKq5ErlC7U"}

    response = requests.get(URL, headers=headers, params=params)  # Standard requests-module request for the API.
    parsed_json = json.loads(response.text)

    for item in parsed_json['items']:
            id = item['id']['videoId']
            #use get youtube method to get title and count viewers for every video
            get_youtube(id)

    #keep find nextpage to see if there are more video id, if there is, recall get video id again
    if 'nextPageToken' in parsed_json:
        npage = parsed_json['nextPageToken']
        get_videoid(npage,categoryid)




#get title and concurrent viewers by video id that get from get_videoid
def get_youtube(videoid):
    URL = 'https://www.googleapis.com/youtube/v3/videos'
    headers = {}
    params = {"part": "snippet,liveStreamingDetails","id": videoid,"key": "AIzaSyDaBJzazt-uzvgnAszYJ7XDJd18cVqbthY"}
    response = requests.get(URL, headers=headers, params=params)  # Standard requests-module request for the API.

    parsed_json = json.loads(response.text)  # Stores the response in JSON dictionary format.
    #write dirty data into file which directly store json string
    with open("yrawdata.txt", 'a', encoding='utf-8') as dirtyfile:
         dirtyfile.write('\t')
         dirtyfile.write(response.text)
         dirtyfile.write('\n')

    # get title and viewcounts back based on json structure
    if 'items' in parsed_json:
        item = parsed_json['items']
        # make sure there is data in items
        if item != []:
           if 'snippet' in item[0]:
               title = item[0]['snippet']['title']
           else:
               title = 'null'
           if 'concurrentViewers' in item[0]['liveStreamingDetails']:
               count = item[0]['liveStreamingDetails']['concurrentViewers']
               #use for debug
               #print(videoid, title, count)
           else:
               count = 'null'
        #write title and viewcounts into cleanfile
           with open("ycleandata.txt", 'a', encoding='utf-8') as cleanfile:
              cleanfile.write('\t')
              cleanfile.write(str(title))
              cleanfile.write('\t')
              cleanfile.write(str(count))
              cleanfile.write('\n')





main()




# https://www.googleapis.com/youtube/v3/search?key=AIzaSyCJED6t5YBwxkVS5_mENZBFfPKq5ErlC7U&part=snippet
#AIzaSyDaBJzazt-uzvgnAszYJ7XDJd18cVqbthY
