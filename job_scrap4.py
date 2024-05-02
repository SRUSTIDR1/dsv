
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

# Access Parent Elements
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# Extract link (href) to apply jobs

#print (python_job_elements)


for job_element in python_job_elements:
    links = job_element.find_all("a")
    for link in links:    	
    	if link.text == "Apply":
    		print(link)
    		link_url = link["href"]
    		#print(f"Apply here: {link_url}\n")
     
