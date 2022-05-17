import streamlit as st
import pandas as pd

st.title('application de repas')
st.header('liste des repas')
my_meal_list = pandas.read_csv("Repas.csv", sep=';')
my_meal_list = my_meal_list.set_index('plats')

meals_selected = st.multiselect("Pick some meals :",list(my_meal_list.index))

st.dataframe(my_meal_list)
  

meals_to_show=my_meal_list.loc[meals_selected]
st.header('repas choisis')
st.dataframe(meals_to_show)

liste_courses=pd.DataFrame({"Date","Quantité","Unité"})
st.header('ingredients choisis')
for i in range(len(meals_selected)):
    st.dataframe(liste_courses)




csv = meals_to_show.to_csv().encode('utf-8')

st.download_button(
     label="Download data as CSV",
     data=csv,
     file_name='meals_to_show.csv',
     mime='text/csv',
 )