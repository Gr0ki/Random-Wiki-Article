# https://en.wikipedia.org/wiki/Special:Random
import requests
import bs4

def creating_site_object():
    try:
        return requests.get('https://en.wikipedia.org/wiki/Special:Random')
    except:
        print('Ops! There is a problem with internet connection.')
        exit()

def taking_article_title(site_object):
    return site_object.url[30:].replace('_', ' ')

def suggest_article_to_user(article_title):
    return input('Do you wanna read about "' + article_title + '"? (press "Y" for yes, "N" for no): ')

def take_content(site_object):
    html = bs4.BeautifulSoup(site_object.text, 'html.parser')
    html = html.find_all(id='mw-content-text')
    html = html[0].find_all(['ul', 'p', 'h1', 'h2', 'h3', 'table'])
    for text in html:
        yield text.get_text()

def output_content(content):
    print()
    for i in content:
        print(i)
    print('\n\n')


while True:
    site_object = creating_site_object()
    article_title = taking_article_title(site_object)
    feedback = suggest_article_to_user(article_title)

    if feedback == 'y' or feedback == 'Y':
        content = take_content(site_object)
        output_content(content)
    elif feedback == 'n' or feedback == 'N':
        break
    else:
        print('Something goes wrong...\n')
