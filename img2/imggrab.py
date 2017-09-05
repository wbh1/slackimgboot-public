from imgurpython import ImgurClient
import random
from img2 import creds
from py_ms_cognitive import PyMsCognitiveImageSearch

def risky(criteria):
    bing_image = PyMsCognitiveImageSearch(creds.ms, criteria)
    first_few_results = bing_image.search(limit=10, format='json') #1-10
    numResults = len(first_few_results)  # too lazy to update variable name
    if numResults != 0:
        if numResults != 1:
            numb = random.randrange(1, numResults, 1)
            item = first_few_results[numb]
            result = item.content_url
            return result
        else:
            item = first_few_results[1]
            result = item.content_url
            return result
    else:
        failed = {'text': 'No Results.'}
        return failed

def find(criteria):
    client = ImgurClient(creds.client_id, creds.client_secret)

    q = criteria.replace("'", "")
    search = client.gallery_search(q, advanced=None, sort='top', window='all')
    numresults = len(search)
    if numresults != 0:
        if numresults != 1:
            numb = random.randrange(1, numresults, 1)
            item = search[numb]
            imgID = item.id
            result = client.get_image(imgID)
            result = result.link
            return result
        else:
            item = search[0]
            imgID = item.id
            result = client.get_image(imgID)
            result = result.link
            return result
    else:
        # use bing if no imgur results
        return risky(q)
