import requests
from bs4 import BeautifulSoup as bs

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=Python&limit={LIMIT}&radius=25"

def extract_last_page():
    # indeed_result = requests.get("https://kr.indeed.com/jobs?q=Python&limit=50&radius=25&start=850")
    result = requests.get(URL)

    soup = bs(result.text, 'html.parser')

    pagination = soup.find('div', {'class': 'pagination'})
    links = pagination.find_all('a')
    pages = []

    for link in links[:-1]:
        # pages.append(link.find("span").string)
        # 아래와 같다. anchor 안에 텍스트라고는 숫자밖에 없으니까..
        pages.append(int(link.string))
        # find('span') 태그에 해당하는 줄을 가져온다.
        # string 태그가 아닌 정말 문자열만 가져온다.

    return pages[-1]

def extrtact_indeed_jobs(last_page):
    jobs = []

    #for page in range(last_page):
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = bs(result.text, 'html.parser')

    #회사 정보의 전체가 담긴 html을 추출
    job_results = soup.find_all('div', {'class':'jobsearch-SerpJobCard unifiedRow row result'})

    # job title 추출
    for job_result in job_results:
        # 마지막에 key 값으로 문자열을 넣어주면 그것에 해당하는 정보만 추출할 수 있음.
        job_title = job_result.find('h2', {'class':'title'}).find('a', {'target': '_blank'})['title']

        # 회사명 추출
        company = job_result.find('div', {'class': 'sjcl'})
        if company.find('span', {'class':'company'}).find('a') is not None:
            company = company.find('span', {'class':'company'}).find('a', {'target': '_blank'}).string
        else:
            company =company.find('span', {'class': 'company'}).string
        company = company.strip() ## 공백을 제거하는 메소드, string 매개변수를 주면 그 글자를 다지움

        print(company)
    return jobs