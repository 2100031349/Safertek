import pandas as pd

# Create the locations and countries dataframes
locations_data = {
    'location_id': [1000, 1200, 1300, 1400, 1500, 1600, 1700],
    'street_address': ['1297 Via Cola di Rie', '2017 Shinjuku-ku Kamiya-cho', '9450', '2014 Jabberwocky Rd Interiors Blvd', '2011', '2007 2004 Zagora St Charade Ad', '147 Spadina Ave'],
    'city': ['Roma', 'Tokyo Hiroshima', '6623', 'Southlake Texas', '99236', 'South Brun New Jersey U5', 'Toronto'],
    'state_province': ['1100', 'Tokyo Prefectu 3P', '1689', '26192', 'South San California', '50090 98199', 'MSV 267'],
    'country_id': ['93091', 'ΣΤ', '1200', '2014', '147', '2007', 'CA']
}

countries_data = {
    'country_id': ['AR', 'AU', 'BE', 'BR', 'CA', 'CH', 'CN', 'DE'],
    'country_name': ['Argentina', 'Australia', 'Belgium', 'Brazil', 'Canada', 'Switzerland', 'China', 'Germany'],
    'region_id': [2, 2, 1, 2, 2, 1, 3, 1]
}

locations_df = pd.DataFrame(locations_data)
countries_df = pd.DataFrame(countries_data)

# Filter the locations dataframe to include only Canada
canada_locations_df = locations_df[locations_df['country_id'] == 'CA']

# Merge the filtered locations dataframe with the countries dataframe
result = pd.merge(canada_locations_df, countries_df, left_on='country_id', right_on='country_id')

# Display the result
print(result[['location_id', 'street_address', 'city', 'state_province', 'country_name']])
