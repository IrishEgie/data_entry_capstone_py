from bs4 import BeautifulSoup
import os
import requests as rq

response = rq.get(os.getenv("ZILLOW_SCRAPE_LINK"))

soup = BeautifulSoup(response.text, "html.parser")

# Find all rental tiles
rentals_soup = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

rentals_list = [title.getText().split("\n") for title in rentals_soup]

print(rentals_list)