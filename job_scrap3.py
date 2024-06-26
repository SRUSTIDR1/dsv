import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

 
# Find Elements by Class Name and Text Content

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
#print()
#print (python_jobs)



# Access Parent Elements
'''
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
'''
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

#print(python_job_elements)


for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()


