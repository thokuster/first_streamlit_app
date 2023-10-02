import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title("My Parents healthy new diner")
streamlit.header("🥣 🥗 🐔 🥑🍞Breakfast")
streamlit.text("eggs and bacon")
streamlit.header("lunch")
streamlit.text("Schnitzel and Pommes Frites")
streamlit.header("supper")
streamlit.text("🍞 Abendbrot :D")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.

streamlit.dataframe(my_fruit_list)
