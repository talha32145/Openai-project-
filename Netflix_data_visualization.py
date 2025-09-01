import pandas as pd
import matplotlib.pyplot as plt 

df=pd.read_csv("netflix_titles.csv")

cleaning_data=df.dropna(inplace=True)

counts_values=df["type"].value_counts()

plt.figure(figsize=(6,4))
plt.bar(counts_values.index,counts_values.values,color=["Green","Black"],width=0.4)
plt.xlabel("Types of Tv")
plt.ylabel("Counts")
plt.title("Comparision between Tv vs Movies watch")
plt.savefig("bar.png",dpi=300,bbox_inches="tight")

rating=df["rating"].value_counts()
plt.pie(rating,labels=rating.index,autopct="%1.1f%%")
plt.legend(title="Rating of movies",bbox_to_anchor=((1,0,0.5,1)))
plt.title("Presenting the Rating of Netflix movies")
plt.savefig("pie_chart.png",dpi=300,bbox_inches="tight")

movie_duration=df[df["type"]=="Movie"].copy()
movie_duration["duration_int"]=movie_duration["duration"].str.replace("min"," ").astype(int)
plt.hist(movie_duration["duration_int"],bins=30,color="black",edgecolor="yellow")
plt.xlabel("Movies Minutes")
plt.ylabel("Number of Movies")
plt.title("Number of minutes of Movies")
plt.savefig("histogram.png",dpi=300,bbox_inches="tight")

count_release_year=df["release_year"].value_counts().sort_index()
plt.scatter(count_release_year.index,count_release_year.values,color="yellow",marker="^")
plt.xlabel("Year of Movies")
plt.ylabel("Number of Movies per year")
plt.title("Representing how many movies release in specific year")
plt.savefig("Scatter plot.png",dpi=300,bbox_inches="tight")

country_count=df["country"].value_counts().head(10)
plt.bar(country_count.index,country_count.values,color=["Green","Red","yellow","black","grey","white","blue","lightgreen","Green","blue"],label=country_count.values)
plt.xlabel("Name of countries")
plt.ylabel("Number of movies")
plt.legend(title="countries list")
plt.savefig("bar_1.png",dpi=300,bbox_inches="tight")
