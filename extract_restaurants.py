import pandas as pd
import json

# Load the restaurant data from the JSON file
with open('restaurant_data.json', 'r') as f:
    restaurant_data = json.load(f)

# Load the country code data from the Excel file
country_codes = pd.read_excel('Country-Code.xlsx')

# Extract the required fields
restaurants_list = []
for entry in restaurant_data:
    restaurant = entry.get('restaurant')
    if restaurant:
        restaurant_id = restaurant.get('id')
        restaurant_name = restaurant.get('name')
        country_id = restaurant['location'].get('country_id')
        city = restaurant['location'].get('city')
        user_rating_votes = restaurant['user_rating'].get('votes')
        user_aggregate_rating = float(restaurant['user_rating'].get('aggregate_rating'))
        cuisines = restaurant.get('cuisines')

        # Find the corresponding country name using country_id
        country_name = country_codes.loc[country_codes['Country Code'] == country_id, 'Country'].values[0]

        # Append the restaurant details to the list
        restaurants_list.append([restaurant_id, restaurant_name, country_name, city, user_rating_votes, user_aggregate_rating, cuisines])

# Create a DataFrame from the list
restaurants_df = pd.DataFrame(restaurants_list, columns=['Restaurant Id', 'Restaurant Name', 'Country', 'City', 'User Rating Votes', 'User Aggregate Rating', 'Cuisines'])

# Save the DataFrame to a CSV file
restaurants_df.to_csv('restaurants.csv', index=False)

print("Data has been successfully extracted and saved to restaurants.csv")
