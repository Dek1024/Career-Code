import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv(r"C:\Users\sgdee\OneDrive\Documents\Finlatics - Data Science Experience Program\Assignments\DsResearch\Media and Technology\Media and Technology\Global YouTube Statistics.csv",encoding="latin-1")
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
print(df.columns)

print(df.shape)
print(df.isnull().sum())

print(df["category"].value_counts())
#Since approximately 5% of the data is missing and adding 55 numbers to highest category does not change the mode
df["category"] = df["category"].fillna(df["category"].mode()[0])
print(df.isnull().sum())

#Since country information is missing in all the columns,
#It will be removed in individual analysis as imputing will give inaccurate results as it makes up 10% of the data
print(df["channel_type"].value_counts())
print(df["category"].value_counts())

#What is the distribution of channels across different category ?
print(df.groupby(["category","channel_type"])["Youtuber"].count())

#There are entries with nan values in all the date columns
date_missing_check = df[df["created_year"].isna()]
print(date_missing_check[["created_year","created_month","created_date"]])

#Removing missings entries in created_month, created_date and created_year columns
df.dropna(subset=["created_date","created_month","created_year"],inplace = True)
print(df.isnull().sum())

#Droping rows containing Nan subscriber values
df.dropna(subset=["subscribers"],inplace = True)
print(df.isnull().sum())

#Chechking if Youtuber column and Title column are the same
print(df["Youtuber"].value_counts())
print(df["Title"].value_counts())
print(df["Youtuber"].equals(df["Title"]))
print((df["Youtuber"]==df["Title"]).sum())

check = df[df["Youtuber"]!=df["Title"]]
print(check[["Youtuber","Title"]].head(20))
print(df.isnull().sum())

print(df["Country"].equals(df["Country of origin"]))
print((df["Country"]==df["Country of origin"]).sum())
check = df[df["Country"]!=df["Country of origin"]]
print(check[["Country","Country of origin"]])
df.drop(columns = ["Country of origin"], inplace = True)
print(df.isnull().sum())

#Replacing long column names
df.rename(columns  = {'video_views_for_the_last_30_days':'30_days_views','Gross tertiary education enrollment (%)':'Gtee','subscribers_for_last_30_days':'30_days_subscribers'},inplace = True)
print(df.columns)

#The 30_days_subscribers column Nan values are filledwith median since the boxplot shows outliers
sns.boxplot(y = '30_days_subscribers' ,data = df)
df['30_days_subscribers'].fillna(df["30_days_subscribers"].median(),inplace = True)
print(df.isnull().sum())

#The 30_days_views column Nan values are filledwith median since the boxplot shows outliers
sns.boxplot(y = '30_days_views' ,data = df)
df['30_days_views'].fillna(df["30_days_views"].median(),inplace = True)
print(df.isnull().sum())

print(df['Country'].value_counts())
#Since USA is has the largest number of YouTube channels at 310 and adding the 124 channels to any of the other categories does not change mode therefore, the missing columns is being imputed with USA country
print(df.groupby(['Country',"Latitude","Longitude"])["Country"].count().sort_values(ascending = False))
print(df.groupby(['Country',"Latitude","Longitude"])["Country"].count().sort_values(ascending = False))
df["Country"] = df["Country"].fillna(df["Country"].mode()[0])

#After filling the missing country entries with the mode, the other dependent columns are filled with the mode country data
us_data = df.loc[df["Country"] == "United States",["Abbreviation","Gtee","Population","Unemployment rate","Urban_population","Latitude","Longitude"]].head(1)
print(us_data.index)
us_dict = us_data.iloc[0].to_dict()
print(us_dict)
for key0,value0 in us_dict.items():
    df[key0].fillna(value0, inplace = True)
print(df.isnull().sum())

#Refiling the Nan channel_type rows 
df1 = pd.DataFrame(df.groupby(["category","channel_type"])["Youtuber"].count())
print(df1.columns)

d1 = {"Autos & Vehicles":"Autos","Comedy":"Comedy",\
      "Education":"Education","Entertainment":"Entertainment",\
          "Film & Animation":"Film","Gaming":"Games"\
              ,"Howto & Style":"Howto","Movies":"Film",\
                  "Music":"Music","News & Politics":"News",\
                      "Nonprofits & Activism":"Nonprofit",\
                          "People & Blogs":"People","Pets & Animals":"Animals",\
                              "Science & Technology":"Tech","Shows":"Entertainment",\
                                  "Sports":"Sports","Trailers":"Music","Travel & Events":"Entertainment"}

nan_entries = df[df["channel_type"].isna()]
print(nan_entries.shape)
for key, value in d1.items():
    filtered_data = nan_entries[nan_entries["category"] == key]
    filtered_data["channel_type"] = value
    nan_entries.update(filtered_data)
df.update(nan_entries)
print(df.isnull().sum())

#Fillinf the country_rank for united states as per the number of scribers 
temp_df = df[df["Country"] == "United States"]
sorted_temp_df = temp_df.sort_values(by = "subscribers", ascending = True)
sorted_temp_df["country_rank"] = range(1,len(sorted_temp_df)+1)
df.update(sorted_temp_df)
print(df.isnull().sum())

#Dropping the remaining rows where channel_type_rank is NaN
df.dropna(subset = ["channel_type_rank"],inplace = True)
print(df.isnull().sum())

df.to_csv(r"C:\Users\sgdee\OneDrive\Documents\Finlatics - Data Science Experience Program\Assignments\DsResearch\Media and Technology\Media and Technology\Cleaned_YouTube_Statistics.csv",index = False)
