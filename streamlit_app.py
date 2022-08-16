import streamlit
import pandas
streamlit.title("My first Streamlit")
streamlit.header(" 🥣 Application")
streamlit.text("🐔 Text1")
streamlit.text("🐔 Text2")
streamlit.text("🐔 Text3")
streamlit.header("🍞 Second header")
my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Banana'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
