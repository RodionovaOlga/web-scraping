import requests
import bs4
import fake_headers

start_url = ('https://hh.ru/search/vacancy?text=Python+django+flask&salary=&ored_clusters=true&area=2&'
             'area=1&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line')


def gen_headers():
    headers_gen = fake_headers.Headers(os="win", browser="chrome")
    return headers_gen.generate()


response = requests.get(start_url, headers=gen_headers())
main_page = bs4.BeautifulSoup(response.text, "lxml")

vacancies_page_tag = main_page.find("main", class_="vacancy-serp-content")

job_vacancy_list = vacancies_page_tag.find_all("div", class_='serp-item serp-item_link')

for idx, job in enumerate(job_vacancy_list):
    job.find('a', class_='bloko-link')
    link = job.find('a', class_='bloko-link')['href']
    name = job.find('span', class_='serp-itemtitle serp-itemtitle-link').text
    if job.find('span', class_="bloko-header-section-2") is not None:
        salary = job.find('span', class_="bloko-header-section-2")
    print(name, idx)