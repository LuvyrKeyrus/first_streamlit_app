import streamlit
import pandas

streamlit.title('application de repas')
streamlit.header('liste des repas')
my_meal_list = pandas.read_csv("Repas.csv", sep=';')
my_meal_list = my_meal_list.set_index('plats')

meals_selected = streamlit.multiselect("Pick some meals :",list(my_meal_list.index))

streamlit.dataframe(my_meal_list)
  

meals_to_show=my_meal_list.loc[meals_selected]
streamlit.header('repas choisis')
streamlit.dataframe(meals_to_show)
csv = meals_to_show.to_csv().encode('utf-8')

streamlit.download_button(
     label="Download data as CSV",
     data=csv,
     file_name='meals_to_show.csv',
     mime='text/csv',
 )