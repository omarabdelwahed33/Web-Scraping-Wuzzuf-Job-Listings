from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import csv
import time


with open("C:/Users/DELL/Documents/web scrapinggg/wuzzuf.csv", "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["job_title", "company_name", "job_type"])

    
    for page in range(0, 50, 10):  
        url = f"https://wuzzuf.net/search/jobs/?q=illustrator&a=navbg&start={page}"
        client = urlopen(url)
        html = client.read()
        client.close()

        soup = bs(html, "html.parser")
        containers = soup.find_all("div", {'class': "css-1gatmva e1v1l3u10"})

        for container in containers:
            try:
                job_title = container.find("h2", {"class": "css-m604qf"}).text.strip()
                company_name = container.find("a", {"class": "css-17s97q8"}).text.strip()
                job_type = container.find("span", {"class": "css-o1vzmt eoyjyou0"}).text.strip()
                writer.writerow([job_title, company_name, job_type])
            except AttributeError:
                continue  
        
        time.sleep(1)




