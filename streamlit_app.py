import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


streamlit.title("My Parents healthy new diner")
streamlit.header("🥣 🥗 🐔 🥑🍞Breakfast")
streamlit.text("eggs and bacon")
streamlit.header("lunch")
streamlit.text("Schnitzel and Pommes Frites")
streamlit.header("supper")
streamlit.text("🍞 Abendbrot :D")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

streamlit.dataframe(my_fruit_list)
