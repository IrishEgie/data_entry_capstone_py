from bs4 import BeautifulSoup
import os
import requests as rq
import re  # For regex operations

response = rq.get(os.getenv("ZILLOW_SCRAPE_LINK"))

soup = BeautifulSoup(response.text, "html.parser")


# ----------------------------- Address ---------------------------- #
# Find all rental tiles
rentals_address_soup = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
rentals_properties_list = [details.getText().split() for details in rentals_address_soup]

# Format the rentals addresses
f_rentals_address_list = []
for rental in rentals_properties_list:
    formatted = " ".join(rental)
    f_rentals_address_list.append(formatted)
# print(f_rentals_address_list) # For Debugging


# ----------------------------- Price ---------------------------- #
rentals_price_soup = soup.find_all(name="span", class_= "PropertyCardWrapper__StyledPriceLine")
rentals_price_list = [price.getText() for price in rentals_price_soup]

f_rentals_price_list = []
for price_tag in rentals_price_list:
    str_price = re.sub('[^0-9]','', price_tag)
    if len(str_price) > 4:  # Ensure price is not more than 4 digits
        str_price = str_price[:4]  # Take only the first 4 digits
    f_price = int(str_price)
    f_rentals_price_list.append(f_price)
# print(f_rentals_price_list) # For Debugging


# ----------------------------- Properties ---------------------------- #
rentals_properties_soup = soup.find_all(name="ul", class_="StyledPropertyCardHomeDetailsList")
rentals_properties_list = [prop.getText().split() for prop in rentals_properties_soup]

f_rentals_properties_list = []
for prop in rentals_properties_list:
    # Filter out empty strings
    if prop:  # Checks if the list 'prop' is not empty
        formatted = " ".join(prop)
        f_rentals_properties_list.append(formatted)
f_rentals_properties_list = [entry for entry in f_rentals_properties_list if entry.strip()] # Filter out any empty strings from the final list (just in case)
# print(f_rentals_properties_list)


# ----------------------------- Links ---------------------------- #
rentals_link_soup = soup.find_all(name="a", href=True, class_= "StyledPropertyCardDataArea-anchor")

f_rentals_link_list = []
for link in rentals_link_soup:
    f_rentals_link_list.append(link['href'])
print(f_rentals_link_list)


