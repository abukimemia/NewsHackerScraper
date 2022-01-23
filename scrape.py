import requests

# use BeautifulSoup module to scrape data from websites
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
news = BeautifulSoup(res.text, 'html.parser')
links = news.select('.titlelink')
subtext = news.select('.subtext')

# Funtion to sort the news stories
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse= True)

def create_custom_news(links, subtext):
    hackerNews = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hackerNews.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hackerNews)

pprint.pprint(create_custom_news(links, subtext))