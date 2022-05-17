import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("Repas.csv", sep='; ', delimiter=None,index_col='plats')
#my_fruit_list = my_fruit_list.set_index('plats')

#fruits_selected = streamlit.multiselect("Pick some fruits :")#,list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
  

#fruits_to_show=my_fruit_list.loc[fruits_selected]
#streamlit.header('🍌🥭 Selected fruits 🥝🍇')
#streamlit.dataframe(fruits_to_show)
#csv = fruits_to_show.to_csv().encode('utf-8')
#
#streamlit.download_button(
#     label="Download data as CSV",
#     data=csv,
#     file_name='fruits_to_show.csv',
#     mime='text/csv',
# )