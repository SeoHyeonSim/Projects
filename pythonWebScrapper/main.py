from bs4 import BeautifulSoup

from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

# jobs = extract_wwr_jobs("python")
# print(jobs)

base_url = 'https://kr.indeed.com/jobs?q=python&limit=50'
search_term = 'python'

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
    print('cannot request page')
    print(response.status_code)
    print(response.text)
else:
    soup = BeautifulSoup(response.text, "html.parser")
    job_list = soup.find('ul', class_="jobsearch-ResultsList")
    jobs = job_list.find_all('li')
    for job in jobs:
        print(job)
