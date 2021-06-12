import requests
from bs4 import BeautifulSoup

''' Demonstrates extraction of National News Article from THE HINDU Web site '''

# Input Wiki URL to extract content        

try:

    url = input('Enter the URL : ')     # https://www.thehindu.com/news/national/data-breaches-expose-data-of-several-govt-officials-to-hackers/article34798982.ece

    req = requests.get(url)                 # request the url

    status, res = req.status_code, req.content      # Status - OK, if we receive success response for the request 

    if status == 200:

        soup = BeautifulSoup(res, 'lxml')               
        article = soup.find('div', {'class' : 'articlepage story'})         # Inspecting complete article
        article_id = article['data-artid']
        heading = article.find('h1').text.strip()                           # Capturing Id, Heading & Intro
        intro = article.find('h2').text.strip()
        
        identifier = "content-body-14269002-"+article_id                       # Id to capture main content from division tag
        paragraphs = article.find('div', {'id' : identifier}).find_all('p')

        article_main_content = '\n{}\n{}\n'.format(heading, intro)

        for i in paragraphs:                                                              # Main content
            article_main_content += '\n{}\n'.format(i.text.strip())

        auth_details = article.find('div', {'class' : 'author-container hidden-xs'})          # Authors Details
        authors = auth_details.find_all('a', {'class' : 'auth-nm lnk'})
        authors_link = auth_details.find_all('a', {'class' : 'auth-nm lnk'})

        for i,j in zip(authors, authors_link):
            article_main_content += '\n{} \t\t {}\n'.format(i.text.strip(), j['href'])
        
        print(article_main_content)

        '''
            with open('National_article.txt', 'a') as file:             # snip to save content to a text file
                file.write(heading+'\n')
                file.write(intro+'\n')
                file.write(article_main_content)
        '''
    else:
        print('Unable to receive successful response from the URL - status : {}'.format(status))

except Exception as e:
    print(e)
