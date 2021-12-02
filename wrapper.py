import requests
import urllib



def search_wiki(title: str):
    '''Summarizes requested Wikipedia page'''


    title = urllib.parse.quote(title.lower())

    r = requests.get(f'http://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro&explaintext&format=json&titles={title}')
    
    response = r.json()

    pagenum = next(iter(response['query']['pages']))


    try:
        sum = response['query']['pages'][pagenum]['extract']
        if sum == '': print('This article has no summary. It must be terribly complex.')
        print(sum)
    except KeyError:
        print('Wiki page not found')
    except:
        print("Don't fuck with the program like that")

