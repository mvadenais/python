"""
Class: CS230--Section HB4
Author: Madison Vadenais
Date Created: 4/15/2021
Description: Final Project- Tallest Skyscrapers in the World
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

print("Final Project: Tallest Skyscrapers in the World")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import statistics

def read_data(fileName):
    df = pd.read_csv(fileName)
    lst = []

    columns = ["Name", "Feet", "Country", "City", "Lat", "Lon"]

# to iterate through rows with pandas
    for index, row in df.iterrows():
        sub = []
        for col in columns:
            index_no = df.columns.get_loc(col)
            sub.append(row[index_no])
        lst.append(sub)
    return df

data = read_data("skyscrapers.csv")

st.title("The Skyscrapers Across the World!")

# Part 1

# display dataframe of skyscrapers with heights over 1500 feet
df = pd.DataFrame(data, columns=["Name", "Feet", "Country", "City", "Lat", "Lon"])
st.dataframe(df)

# functions to find mean, median, max, and min from the heights of all the skyscrapers
def mean(data):
    average = statistics.mean(data)
    return average

mean = mean(df["Feet"])
st.write(f"The mean height of all 77 Skyscrapers in the world is {mean:0.2f} feet")

def median(data):
    median = statistics.median(data)
    return median

med = median(df["Feet"])
st.write(f"The median height is {med:0.2f} feet")

def max_min(data):
    maxNum = max(data)
    minNum = min(data)
    return maxNum, minNum

maxNum, minNum = max_min(df["Feet"])
st.write(f"The minumum height of the skyscrapers is {minNum}")
st.write(f"The maximum height of the skyscrapers is {maxNum}")

# display dataframe of the country selected
countries = []
for i in data["Country"]:
    if i not in countries:
        countries.append(i)
country_df = pd.DataFrame(data, columns=["Name", "Feet", "Country"])
country = st.sidebar.selectbox("Which country do you want to select for the Data Frame?", countries)
st.header(f"The Skyscraper's located in {country}")
st.dataframe(country_df.loc[(country_df["Country"] == country)])

# dataframe with skyscraper's over 1500 feet
st.header("The Skyscraper's with heights greater than 1,500 feet!")
st.dataframe(country_df.loc[(country_df["Feet"] > 1500)])

# slider for the height of the skyscrapers
feet = st.slider("Choose the minimum height for the skyscrapers: ", min_value=1148, max_value=2721, value=1500, step=1)
st.write("You selected: ", feet)
st.dataframe(df.loc[(df["Feet"] > feet)])

# Part 2
# line chart comparing all the skyscrapers in the United States
# include a colored legend to show the US

def line_chart(data):
    data = pd.read_csv("skyscrapers.csv")
    us_df = data[(data.Country == " United States")]
    x = us_df["Name"]
    y = us_df["Feet"]
    plt.plot(x, y, marker="o", color="magenta")
    plt.xlabel("Skyscraper's in the United States")
    plt.ylabel("Height in Feet")
    plt.legend(loc="upper right")
    plt.xticks(rotation=90)
    plt.title("The Heights of Skyscrapers in the United States")

st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(line_chart(df))

# display a dataframe that shows each country and the name of their tallest skyscraper,
# along with the height and city

st.header("The Tallest Skyscraper in each Country")
df1 = df.groupby(["Country"]).max()
st.dataframe(df1)

# create a bar chart that shows the top five tallest skyscrapers in the world and their
# corresponding height and country

def bar_plot(df):
    df0 = pd.DataFrame(df, columns=["Name", "Country", "City", "Feet"])

    df1 = df0.groupby(["Country"]).max()
    df1.sort_values(["Feet"], ascending=False, inplace=True)
    topfive = df1.iloc[0:5,]
    xAxis = topfive.index.values.tolist()
    yAxis = list(topfive["Feet"])
    plt.bar(xAxis,yAxis)
    plt.title("Top Five Tallest Skyscrapers")
    plt.xlabel("Country")
    plt.xticks(rotation=45)
    plt.ylabel("Feet")

st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(bar_plot(data))

# create a map with the given latitudes and longitudes of the tallest skyscrapers in each country to see where
# they are across the world

def display_map():
    data = read_data("skyscrapers.csv")
    country1 = st.sidebar.selectbox("Select a country to display on the map: ", countries)
    map_df = pd.DataFrame(data)
    map_df["lat"] = map_df["Lat"]
    map_df["lon"] = map_df["Lon"]
    map_df1 = map_df[map_df["Country"] == country1]
    st.dataframe(map_df1)
    st.map(map_df1)

display_map()
