import requests
from bs4 import BeautifulSoup  # bs4 to import beautiful soup 4
import pprint # pprint = pretty print is a built-in module to print in a nicer way (more spaces, etc)
                            

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k : k['votes'], reverse=True) # sort the hn list by the votes key,
                                                                    # and reverse so it's > to <


hn = []


def hn_data(page_number):
    res = requests.get('https://news.ycombinator.com/news?p=' + str(page_number))
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.titlelink')
    subtext = soup.select('.subtext') # grab the subtext (the scores are inside the subtext) bc all articles
                            # have a subtext, but not all have votes. then we'll grab the scores from there

    def create_custom_hn(links, subtext):
        for index, item in enumerate(links):
            title = links[index].getText() # getText so that we get the text and not the html
            href = links[index].get('href', None) # get href=... it's the link. None is the default value
            vote = subtext[index].select('.score') # grab the score from the subtext and returns it in a
                                                   # one-item list. that's why later we have to use 
                                                   # vote[0], bc we need the text, not the list.

            if len(vote): # if it has any votes (!= 0)
                points = int(vote[0].getText().replace(' points', '')) # replace points with an empty string
                if points >= 100: # so that we get relevant articles
                    hn.append({'title': title, 'link': href, 'votes': points}) # appends dicts into the list
        return hn 
    return create_custom_hn(links, subtext)



for x in range(1, 3):
    hn_data(x) # runs the function twice so now hn contains info from page 1 and 2


pprint.pprint(sort_stories_by_votes(hn)) # sorts the new hn list while using pretty print
