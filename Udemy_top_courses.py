import requests
from bs4 import BeautifulSoup
#from pandas import DataFrame as df

''' Demonstrates extraction of Top Rated Python course details from Udemy to a csv file '''      

# Spinner Alert !! - Unable to extract due to Bootstrap Load Spinner and JS code

def extraction(url,course,desc,instructor,rating_cost_details):
    ''' Function to traverse through a single page to collect data '''

    req = requests.get(url)

    status, res = req.status_code, req.content

    if status == 200:

        soup = BeautifulSoup(res, 'lxml')
        
        course_container = soup.find('div', {'class' : 'main-content-wrapper'}).find('div', {'class' : 'main-content'}).find('div', {'class' : 'udlite-container udlite-page-wrapper'}).find_all('div', {'class' : 'component-margin'})

        print(course_container) 
        
        ''' Spinner Alert !! - Unable to extract due to Bootstrap Load Spinner and JS code  '''

        #course_container = course_container.find('div', {'class' : 'course-directory--container--5ZPhr'}).find('div', {'class' : 'filter-panel--filtered-course-list--SD4_5'}).find('div', {'class' : 'course-list--container--3zXPS'}).find_all('div', {'class' : 'popper--popper--19faV popper--popper-hover--4YJ5J'})

        #with open('abc.text', 'w') as f:
        #    f.write(str(course_container))

        '''
        for i in data:
            course.append(i.find('div',{'class' : 'udlite-focus-visible-target udlite-heading-md course-card--course-title--2f7tE'}).text)
            desc.append(i.find('p', {'class' : 'udlite-text-sm course-card--course-headline--yIrRk'}).text)
            instructor.append(i.find('div', {'class' : 'udlite-text-xs course-card--instructor-list--lIA4f'}).text)
            rating_cost_details.append("{}  ||  {}  ||  {}  ||  {}  || {}".format
            (i.find('span', {'class' : 'udlite-heading-sm star-rating--rating-number--3lVe8'}).text,
            i.find('span', {'class' : 'udlite-text-xs course-card--reviews-text--12UpL'}).text,
            i.find_all('span', {'class' : 'course-card--row--1OMjg'})[0].text,
            i.find_all('span', {'class' : 'course-card--row--1OMjg'})[1].text,
            i.find('div', {'class' : 'price-text--price-part--Tu6MH course-card--discount-price--3TaBk udlite-heading-md'}).find('span')[1]).text)
        '''
    return (course, desc, instructor, rating_cost_details)


url = input('Enter the URL : ')                 # https://www.udemy.com/topic/python

pages_list = [url+"/?p="+str(i) for i in range(1, 2)]             #https://www.udemy.com/topic/python/?p=1

content_dictionary = {}
course,desc,instructor,rating_cost_details = [], [], [], []
for i in pages_list:
    content_dictionary['Course'], content_dictionary['Course Description'], content_dictionary['Instructor'], content_dictionary['More Details'] = extraction(i,course,desc,instructor,rating_cost_details)

print(content_dictionary)
