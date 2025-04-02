# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df = pd.read_csv(r"C:\Users\sgdee\OneDrive\Documents\Finlatics - Data Science Experience Program\Assignments\DsResearch\Media and Technology\Media and Technology\Cleaned_YouTube_Statistics.csv", encoding = 'latin-1')
print(df.head())

#1.	What are the top 10 YouTube channels based on the number of subscribers?
df_sorted = df.sort_values(by=['subscribers'], ascending=False)
top_channels = df_sorted[['Youtuber','subscribers']].head(10)
print(top_channels)
sns.barplot(data = top_channels, x = 'Youtuber', y= 'subscribers')
plt.xticks(rotation = 90) 

#2. Average of the subscribers grouped by category and order by descending to diplay the highest
category_subscribers = pd.DataFrame(df.groupby('category')['subscribers'].mean().sort_values(ascending=False)).reset_index()
sns.barplot(data = category_subscribers, x = 'category', y= 'subscribers')
plt.ylabel("Average subsctibers")
plt.xticks(rotation = 90) 

#3.	How many videos, on average, are uploaded by YouTube channels in each category?
upload_category = pd.DataFrame(df.groupby("category")['uploads'].mean().sort_values(ascending = False)).reset_index()
sns.barplot(data = upload_category, x = 'category', y= 'uploads')
plt.xticks(rotation = 90)
plt.ylabel("Average uploads")
print(upload_category)

#4.	What are the top 5 countries with the highest number of YouTube channels?
channels_country = pd.DataFrame(df.groupby('Country')['Title'].count().sort_values(ascending  = False)).reset_index()
print(channels_country)
sns.barplot(data = channels_country.head(5), x = 'Country', y= 'Title')
plt.ylabel("No. of Youtube channels")
plt.xticks(rotation = 90)

#5.	What is the distribution of channel types across different categories?
hist_data = pd.DataFrame(df.groupby('category')['Title'].count()).reset_index()
sns.barplot(data = hist_data, x = 'category', y= 'Title')
plt.xticks(rotation = 90)
plt.ylabel("No. of Channels")

#6.	Is there a correlation between the number of subscribers and total video views for YouTube channels ?
corr_data = df[['subscribers','video views']]
print(corr_data.corr())
sns.scatterplot(corr_data, x = 'subscribers', y = 'video views')

#7.	How do the monthly earnings vary throughout different categories?
plt.figure()
hist_high_earnings = df.groupby('category')['highest_monthly_earnings'].sum().sort_values()
sns.barplot(data = hist_high_earnings, orient = 'h')
plt.figure()
hist_high_earnings = df.groupby('category')['lowest_monthly_earnings'].sum().sort_values()
sns.barplot(data = hist_high_earnings, orient = 'h')

#8.	What is the overall trend in subscribers gained in the last 30 days across all channels?
sub_data = df.groupby('category')['30_days_subscribers'].mean().sort_values()
sns.barplot(data = sub_data, orient = 'h')

#9.	Are there any outliers in terms of yearly earnings from YouTube channels?
width = 20
height = 8
sns.set(rc = {'figure.figsize':(width, height)})
sns.boxplot(data = df['highest_monthly_earnings'], orient = 'h')

#10.	What is the distribution of channel creation dates? Is there any trend over time?
sns.displot(df['created_date'])
plt.close()
time_trend = pd.DataFrame(df.groupby('created_year')['Title'].count().sort_values()).reset_index()
sns.barplot(data = time_trend, orient = 'h')

#11.	Is there a relationship between gross tertiary education enrollment and the number of YouTube channels in a country?
youtuber_data = df.groupby('Country')['Youtuber'].count()
employment_data = df.groupby('Country')['Gtee'].max()
youtuber_data = pd.DataFrame(youtuber_data)
employment_channel_data = youtuber_data.merge(employment_data, on = 'Country')
employment_channel_data.corr()
sns.scatterplot(data = employment_channel_data, x = 'Gtee', y = 'Youtuber')

#12.	How does the unemployment rate vary among the top 10 countries with the highest number of YouTube channels?
um_employ_data = pd.DataFrame(df.groupby('Country')['Unemployment rate'].max().sort_values())
youtuber_data = pd.DataFrame(df.groupby('Country')['Youtuber'].count().sort_values()).reset_index()
merge_data = um_employ_data.merge(youtuber_data, on = 'Country')
plot_data = merge_data.sort_values(by = 'Youtuber', ascending = False).head(10)
sns.barplot(x = 'Country', y = 'Unemployment rate', data = plot_data)
plt.xticks(rotation = 60)

#13.	What is the average urban population percentage in countries with YouTube channels?
pop_data = df.groupby('Country').apply(lambda x: x['Urban_population'] * 100 / x['Population']).reset_index(level = 0,name = 'Urban population %')
pop_data = pop_data.groupby('Country').max().reset_index()
pop_data.drop(pop_data.index[[1]], inplace = True)
pop_data['Urban population %'].mean()

#14.	Are there any patterns in the distribution of YouTube channels based on latitude and longitude coordinates?
lat_long_data = pd.DataFrame(df[['Youtuber','Latitude','Longitude']])
sns.scatterplot(x = "Latitude", y = "Longitude",data = lat_long_data)

new_data = df.groupby(['Latitude','Longitude'])['Youtuber'].count()
print(new_data)

#15.	What is the correlation between the number of subscribers and the population of a country?
pop_sub_dat = df.groupby(['Country','Population'])['subscribers'].mean().reset_index(name = 'Average subscribers')
pop_sub_dat[['Population','Average subscribers']].corr()

#16.	How do the top 10 countries with the highest number of YouTube channels compare in terms of their total population?
pop_dat = pd.DataFrame(df.groupby(['Country','Population'])['Youtuber'].count().sort_values(ascending = False)).reset_index()
plot_dat = pop_dat.head(10)
sns.barplot(x = 'Country', y = 'Population', data = plot_dat)
plt.xticks(rotation = 60)

#17.	Is there a correlation between the number of subscribers gained in the last 30 days and the unemployment rate in a country?
unemp_dat = df.groupby(['Country','Unemployment rate'])['30_days_subscribers'].mean().reset_index(name = 'Average_subscribers_last_30_days')
unemp_dat[['Unemployment rate','Average_subscribers_last_30_days']].corr()

#18.	How does the distribution of video views for the last 30 days vary across different channel types?
views_dat = df.groupby('channel_type')['30_days_views'].sum().reset_index(name = 'Average_video_views_for_the_last_30_days')
sns.barplot(x = 'channel_type', y = 'Average_video_views_for_the_last_30_days' , data = views_dat )
plt.xticks(rotation = 90)

#19.	Are there any seasonal trends in the number of videos uploaded by YouTube channels?
print(df.columns)
monthly_trends = pd.DataFrame(df.groupby('created_month')['uploads'].mean().sort_values(ascending = False)).reset_index()
sns.barplot(x = 'created_month', y = 'uploads', data = monthly_trends)
plt.xticks(rotation = 90)

#20.	What is the average number of subscribers gained per month since the creation of YouTube channels till now?
current_year = df['created_year'].max()
df["months"] = (current_year - df['created_year'] ) * 12
df["subscribers_month"] = df['subscribers'] / df['months']
df['subscribers_month'] = df['subscribers_month'].astype(float)
df['subscribers_month'].replace([np.inf,-np.inf],0,inplace = True)
answer = df['subscribers_month'].mean()
print(answer)