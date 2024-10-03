import soup_fetch 
import form


f_rentals_address_list = soup_fetch.soup_fetch()[0]
f_rentals_price_list = soup_fetch.soup_fetch()[1]
f_rentals_properties_list = soup_fetch.soup_fetch()[2]
f_rentals_link_list = soup_fetch.soup_fetch()[3]

# print(len(f_rentals_address_list))
# print(len(f_rentals_price_list))
# print(len(f_rentals_properties_list))
# print(len(f_rentals_link_list))

form.initialize_driver()

f_rentals_dict = {}
for index in range(len(f_rentals_address_list)):
    form.form_interaction(
    f_rentals_address_list[index],
    f_rentals_price_list[index],
    f_rentals_properties_list[index],
    f_rentals_link_list[index]
    )

form.form_quit()
