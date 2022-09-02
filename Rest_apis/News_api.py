import requests

#r = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=6a6f262c2c3e4052b15651a3ca99038c')
#
#content = r.json()
#
#articles=content['articles']
#
#for article in articles: 
#    print(f"TITLE: {article['title']}\nAUTHOR: {article['author']}")
    
    
def get_news(topic, from_date, to_date, language='en',
             api_key='6a6f262c2c3e4052b15651a3ca99038c'):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&language={language}&apiKey={api_key}'
    r = requests.get(url)
    content=r.json()
    articles=content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE:\n{article['title']}\nAUTHOR:{article['author']}")
    return results

print(get_news(topic='japan', from_date='2022-7-27', to_date='2022-8-26'))