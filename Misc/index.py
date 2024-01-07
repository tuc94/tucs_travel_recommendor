from pytrends.request import TrendReq
import pandas as pd
from datetime import datetime, timedelta

def get_country_interest(pytrends, country):
    # Customize the search terms and timeframe as needed
    countryList = [country]

    # Set the timeframe to within the week of the query
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=6)
    timeframe = f'{start_date} {end_date}'

    pytrends.build_payload(countryList, cat=203, timeframe=timeframe)
   
    # Get interest over time
    interest_over_time_df = pytrends.interest_over_time()

    # Add a column for the country
    interest_over_time_df['Country'] = country

    return interest_over_time_df

# List of countries you want to check
countries = ["Iceland", "United States", "Germany", "Japan"]

# Create an empty dataframe to store the results
all_data = pd.DataFrame()

# Initialize pytrends object
pytrends = TrendReq(hl='en-US', tz=360)

# Iterate through each country and store the data in the dataframe
for country in countries:
    country_data = get_country_interest(pytrends, country)
    all_data = pd.concat([all_data, country_data])

# Print or process the results as needed
print("Interest in multiple countries:")
print(all_data)
