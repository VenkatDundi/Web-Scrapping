import requests
from bs4 import BeautifulSoup

''' Demonstrates extraction of Table of Contents & Urls from Wikipedia Article about 'Wikipedia' '''

# Input Wiki URL to extract content        

try:

    url = input('Enter the URL : ')                 # https://en.wikipedia.org/wiki/Wikipedia

    req = requests.get(url)                 # request the url

    status, res = req.status_code, req.content      # Status - OK, if we receive success response for the request 

    if status == 200:

        soup = BeautifulSoup(res, 'lxml')                  # lxml is one of available parsers to parse the content

        link1 = soup.find('div', {'class': 'toc'}).find('ul')       # Inspecting 'Div' tag for Table of contents 
        link2 = link1.find_all('span', {'class': 'tocnumber'})      # Capturing S.No & Description
        link3 = link1.find_all('span', {'class': 'toctext'})

        for i,j in zip(link2, link3):                               # displaying extracted content
            print('{}  {}'.format(i.text,j.text))
        
    # lists = [(i,j) for i,j in zip(link2, link3)]                  # list of tuple with (S.No & Description)

        anchors = link1.find_all('a')
        anchors_list = [url+i['href'] for i in anchors]

        print('\n')
        print(anchors_list)                                   # Lists  urls for contents within the Table of contents
    
    else:

        print('Unable to receive successful response from the URL - status : {}'.format(status))


except Exception as e:
    print(e)




