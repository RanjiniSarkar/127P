from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = (
    "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
)
page= requests.get(START_URL)
soup = BeautifulSoup(page.text, "html.parser")
temp_list = []
for tr in soup.find("table").find_all("tr"):
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

mass = []
name = []
distance = []
radius = []



for i in range(1, len(temp_list)):
     mass.append(temp_list[i][5])
     name.append(temp_list[i][1])
     distance.append(temp_list[i][3])
     radius.append(temp_list[i][6])

df = pd.DataFrame(
    list(zip(name, distance, mass, radius)),
    columns=[ "Mass","Star_name", "Distance", "Radius"],
)
df.to_csv("final.csv")