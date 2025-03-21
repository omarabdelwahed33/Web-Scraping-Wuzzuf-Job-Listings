from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import csv

url = "https://wuzzuf.net/search/jobs/?q=illustrator&a=navbg"
client = urlopen(url)
html = client.read()
client.close()
soup = bs(html, "html.parser")
containers = soup.find_all("div", {'class': "css-1gatmva e1v1l3u10"})


jtitle = containers[0].find_all("h2",{"class": "css-m604qf"})


cname = containers[0].find_all("a", {"class": "css-17s97q8"})

jtype = containers[0].find_all("span", {"class": "css-o1vzmt eoyjyou0"})



f = open("C:/Users/DELL/Documents/web scrapinggg/wuzzuf.csv","w" ,encoding="utf-8")
header = "job_title, company_name, jop_type\n"
f.write(header)

for container in containers :
    jtitle = container.find_all("h2",{"class": "css-m604qf"})
    job_title = jtitle[0].text.strip()

    cname = container.find_all("a", {"class": "css-17s97q8"})
    company_name = cname[0].text.strip()
    
    jtype = container.find_all("span", {"class": "css-o1vzmt eoyjyou0"})
    jop_type = jtype[0].text.strip()
    
    f.write(job_title + "," + company_name + "," + jop_type +  "\n")

f.close()



