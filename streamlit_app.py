import streamlit
import pandas
streamlit.title("My first Streamlit")
streamlit.header(" 🥣 Application")
streamlit.text("🐔 Text1")
streamlit.text("🐔 Text2")
streamlit.text("🐔 Text3")
streamlit.header("🍞 Second header")
my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
