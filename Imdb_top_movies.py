import requests
from bs4 import BeautifulSoup

''' Demonstrates extraction of 250 Top Rated Movies from IMDB to a text file '''

# Input Wiki URL to extract content        

try:

    url = input('Enter the URL : ')                 # https://www.imdb.com/chart/top/

    req = requests.get(url)                 # request the url

    status, res = req.status_code, req.content      # Status - OK, if we receive success response for the request 

    if status == 200:

        soup = BeautifulSoup(res, 'lxml')                  # lxml is one of available parsers to parse the content

        chart = soup.find('tbody', {'class' : 'lister-list'})   # Inspect list of movies

        rows = chart.find_all('tr')                                 

      
        with open('top_250_movies.txt', 'a') as file:                 # opening file in append mode 
            
            for i in rows:
                movie_name = i.find('td', {'class' : 'titleColumn'}).find('a').text
                stars = i.find('td', {'class' : 'titleColumn'}).find('a')['title']
                year = i.find('td', {'class' : 'titleColumn'}).find('span').text[1:-1]
                users = i.find('td', {'class' : 'ratingColumn imdbRating'}).find('strong')['title']
                users = users[users.index('on')+3 : users.index(' user')]
                rating = i.find('td', {'class' : 'ratingColumn imdbRating'}).find('strong').text

                file.writelines('{}\t --- {}\t --- {}\t --- {}\t --- {}\n'.format(movie_name,stars,year,users,rating))    # writing data to text file 

                # Use case - provide Rating as Input and retrieve movies with rating >= input
    
    else:
        print('Unable to receive successful response from the URL - status : {}'.format(status))


except Exception as e:
    print(e)        

        
