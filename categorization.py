import pandas as pd
import requests
from bs4 import BeautifulSoup

# scrape wikipedia restaurants page
page=requests.get("https://en.wikipedia.org/wiki/List_of_restaurant_chains")
soup = BeautifulSoup(page.content, "lxml")
foodTable = soup.find("table", {'class':"wikitable"})

# convert table to dataframe
food = pd.read_html(str(foodTable))
food= pd.DataFrame(food[0])

# take Name column of dataframe, cast to list
food = list(food.Name)
# join list to string in format for contains method
food = "|".join(food).upper()

# scrape wikipedia grocery chains page
page=requests.get("https://en.wikipedia.org/wiki/List_of_supermarket_chains_in_Canada")
soup = BeautifulSoup(page.content, 'lxml')

# list of words to exclude, not grocery stores
exclude = "None List Americas Territory territory Category Discussion Edit edit Wikipedia link mandatory page Article Wikidata policy Wikimedia files article".split()
grocery = ""

# every title of links
for title in soup.find_all('a'):
    store = title.get('title')
    # if not nonetype or including an excluded substring, add to grocery string
    if not (store is None or store.isspace() or store == "" or any(substring in store for substring in exclude)):
        grocery = grocery + "|" + store.upper()

# take off extra | at start
grocery = grocery[1:len(grocery)]

# transit string
transit = "Uber|Lyft|Bus|Train|Plane|Travel|Taxi".upper()

# rent string
rent = "Rent|Lease".upper()

# entertainment string
entertainment = "Theater|Museum|Gallery|Movie|Cineplex|Game".upper()



