import requests
import json

def main():
    results = 'y'
    while results == 'y':
        user_string = input('Enter a Title: ')
        user_platform = input('Enter Your Platform, youtube/twitch: ')
        print('Checking the sentiment of your title now...')
        dictionary = create_dicitonary(user_string)
        sentiment = get_sentiment(dictionary)

        if user_platform == 'twitch':
            
            if sentiment >= .9:
                print('Great Title! Your sentiment score is: ' + str(sentiment))
            if sentiment > .6 and sentiment < .9:
                print('Your strings sentiment value is: ' + str(sentiment) + 'Our research shows that a higher sentiment score is correlated with more viewers! Go for a more positive rating!')
            if sentiment <= .5:
                print('Your strings sentiment is neutral (.5) or less than .5. Our research on this is inconclusive. Consider going for a sentiment higher than .6! Sentiment score: ' + str(sentiment))
        
        if user_platform =='youtube':
            
            if sentiment <.5:
                print('Your sentiment value is: ' +str(sentiment) + 'If possible, enter a title that gives a sentiment value closer to .5 for potentially increased viewers')
            if sentiment >=.5: 
                print('Our study has shown no correlation for sentiment values greater than .5; you may try streaming with this title for mixed results. Sentiment score: ' +str(sentiment))
        results = input('Keep testing titles? y/n :')

    print('Exiting')    
def create_dicitonary(userString):
    item_list=[]
    dictionary = {'documents':item_list}
    item_list.append({'id':1,'text':userString,'language':'en'})
    dictionary = json.dumps(dictionary)
    return dictionary

def get_sentiment(dictionary):

    URL = 'https://eastus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'                         
    headers = {'Ocp-Apim-Subscription-Key': '4820ff11f82e4ecb9dbe9812897ece38','Host':'eastus.api.cognitive.microsoft.com','Content-Type':'application/json', 'Accept':'application/json'}
    response = requests.post(URL, headers=headers, data=dictionary)
    final = json.loads(response.text)
    
    return final['documents'][0]['score']


main()