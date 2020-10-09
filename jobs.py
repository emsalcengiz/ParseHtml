import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/jobs"
rqst = requests.get(url)
print(rqst.status_code)
print(rqst.content)

soup = BeautifulSoup(rqst.content,"lxml")
pages = len(soup.find_all("ul",attrs={"class":"pagination"})[0].find_all("li")) -2

totaljobs = 0
for page in range(1,pages+1):
    pageRequest = requests.get("https://www.python.org/jobs/?page=" + str(page))
    pageSource = BeautifulSoup(pageRequest.content,"lxml")
    jobs = pageSource.find("div",attrs={"class":"row"}).ol.find_all("li")

    for job in jobs:
        name = job.h2.find("a").text
        company = job.find("span", attrs={"class": "listing-company-name"}).br.next.strip()
        publish_time = job.find("time").text
        totaljobs += 1
        print(name, company, publish_time, sep="\n")


print("Total {} jobs found.".format(totaljobs))




