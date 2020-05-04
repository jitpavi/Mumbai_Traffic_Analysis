"""
Code Name: HeatMap of Mumbai Traffic (Last 7 days)
Code Author: Jitin Pavithran
Code Version: 1.0
Code Description: The aim of this Python code is to generate a visualisation HeatMap chart for the viewers to understand the traffic intensity in Mumbai city last 7 days for each respective hours of the day
in the present Covid-19 crisis.
"""

# Import all the required modules for this code
import calendar
import time
import pandas as pd
import json
import requests
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns

# Compute the total execution time for this code hence evaluate the starttime
start_time=time.time()

# Perform the Data Import from the URL and create a JSON object out of the imported data
url = r"https://api.midway.tomtom.com/ranking/live/IND_mumbai"
mum_req = requests.request("GET",url)
mum_json = mum_req.json()

# Check the availability of the website
code = mum_req.status_code

while code != 200:
    print(f"Unable to reach the URL and returned with the status code: {mum_req.status_code}")
    print("Trying again to reach the URL")
    code = mum_req.status_code

list_id = list(mum_json)

val = mum_json[list_id[0]]

len_val = len(val)

# Import the values under  each of the keys in the form of the lists
TrafficIndexLive = [mum_json[list_id[0]][i]['TrafficIndexLive'] for i in range(len_val)]
UpdateTime = [mum_json[list_id[0]][i]['UpdateTime'] for i in range(len_val)]
JamsDelay = [mum_json[list_id[0]][i]['JamsDelay'] for i in range(len_val)]
JamsLength = [mum_json[list_id[0]][i]['JamsLength'] for i in range(len_val)]
JamsCount = [mum_json[list_id[0]][i]['JamsCount'] for i in range(len_val)]

# Create a Panda Dataframe and import the data into this frame
tom_df = pd.DataFrame({'TrafficIndexLive': TrafficIndexLive,'UpdateTime':UpdateTime,'JamsDelay': JamsDelay,'JamsLength': JamsLength,'JamsCount': JamsCount})

# convert the traffic index into percentage
tom_df['TrafficIndexLive'].apply(lambda x: x*100/(tom_df['TrafficIndexLive'].sum()))

# Convert the values into the Date time format
tom_df['UpdateTime'] = pd.to_datetime(tom_df['UpdateTime'], unit='ms')

# Derive the hours and dayname against each
tom_df['Hour'] = tom_df['UpdateTime'].dt.hour
tom_df['WeekDay'] = tom_df['UpdateTime'].dt.day_name()

# Create a sorter list for each day name
sorter = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
sorterindex = dict(zip(sorter,range(len(sorter))))

# Sort the DayNames according to the value in the list
tom_df['DayID'] = tom_df['WeekDay'].map(sorterindex)

# Compute the total traffic by adding the values of JamsDelay, JamsCount and TrafficIndexLive
tom_df['TotalTraffic'] = tom_df['JamsDelay'] + tom_df['JamsLength'] + tom_df['JamsCount'] + tom_df['TrafficIndexLive']

tom_df.sort_values(by='DayID',inplace=True)

# Drop the index as it is not required in the final Heatmap
tom_df.reset_index(drop=True,inplace=True)
tom_df['WeekDay'] = pd.Categorical(tom_df['WeekDay'],categories=sorter)

# Perform a groupby in the dataframe and unstack it to give a feel of Pivot table
btom_df = tom_df.groupby(['WeekDay','Hour'])['TotalTraffic'].sum().unstack()

# Save the Dataframe into the CSV file
tom_df.to_csv(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\Mumbai Live Traffic Analysis\mum_traffic.csv",index=False)

# Save the groupby values into the CSV file
btom_df.to_csv(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\Mumbai Live Traffic Analysis\mum_trafficgrp.csv",index=False)

# Create a subplot including figure and axis
fig,ax = plt.subplots(figsize=(14,7))

# Create heatmap object using the seaborn module
ax = sns.heatmap(btom_df,fmt="",cmap="YlGnBu",linewidths=1.0,vmin=-10,vmax=147)

#Total execution time
end_time = time.time()
print(end_time-start_time)

fig.tight_layout()

#Save the HeatMap figure in the given location of drive
plt.savefig(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\Mumbai Live Traffic Analysis\Traffic_HeatMap.jpg")

#display the Heatmap figure on the screen
plt.show()