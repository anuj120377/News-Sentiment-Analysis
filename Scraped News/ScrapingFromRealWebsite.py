from bs4 import BeautifulSoup
import requests

#html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=Python&txtLocation=')
#print(html_text)
## <Response [200]>  -->> 200 is convention no. in web that request is done successfully

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=Python&txtLocation=').text
#print(html_text)

soup = BeautifulSoup(html_text, 'lxml')

job = soup.find('li',class_="clearfix job-bx wht-shd-bx")
## company_name = job.find('h3',class_="joblist-comp-name").text
## print(company_name)

company_name = job.find('h3',class_="joblist-comp-name").text.replace(' ','')  #To avoid unnecessary spaces
skills = job.find('span',class_="srp-skills").text.replace(' ','')
#print(company_name)
#print(skills)

#print(f'''
#Company Name: {company_name}
#Skills: {skills}'''
#)

## Now adding one functionality where it only looks into jobs posted few days ago

published_date = job.find('span',class_="sim-posted").span.text
print(published_date)


jobs = soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
"""
for job in jobs:
    published_date = job.find('span', class_="sim-posted").span.text

    if 'few' in published_date:
        company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ', '')  # To avoid unnecessary spaces
        skills = job.find('span', class_="srp-skills").text.replace(' ', '')

        print(f'''
        Company Name: {company_name}
        Skills: {skills}'''
        )

        print('')
"""

## Adding more features to the Project, Prettifying Paragraph


print('Put Some Skill You are not familiar with')
unfamiliar_skill = input('>')
print(f"Filtering Out {unfamiliar_skill}")

"""
for job in jobs:
    published_date = job.find('span', class_="sim-posted").span.text

    if 'few' in published_date:
        company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ', '')  # To avoid unnecessary spaces
        skills = job.find('span', class_="srp-skills").text.replace(' ', '')
        more_info = job.header.h2.a['href']
        if unfamiliar_skill not in skills:
            print(f"Company Name: {company_name.strip()}")
            print(f"Skills: {skills.strip()}")
            print(f"More Info: {more_info}")
            print('')
            
            
"""

## Setting Up Project So that it scrape every 10 minutes

import time

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
    for index,job in enumerate(jobs):
        published_date = job.find('span', class_="sim-posted").span.text

        if 'few' in published_date:
            company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ', '')  # To avoid unnecessary spaces
            skills = job.find('span', class_="srp-skills").text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info} \n")
                print(f"File Saved : {index}")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes.....')
        time.sleep(time_wait * 60)  # 600 seconds
