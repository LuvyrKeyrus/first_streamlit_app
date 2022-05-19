import streamlit as st
import pandas as pd
import numpy as np

st.title('Application de repas')
st.header('Liste des repas')
my_meal_list = pd.read_csv("Repas.csv", sep=';')
my_meal_list = my_meal_list.set_index('plats')

meals_selected = st.multiselect("Pick some meals :",list(my_meal_list.index))

st.dataframe(my_meal_list)
st.text(st.session_state)

meals_to_show=my_meal_list.loc[meals_selected]
coltitre1, coltitre2 = st.columns(2)
col1, col2, col3 = st.columns([2,2,4])
coltitre1.header('Repas choisis')


liste_courses=pd.DataFrame(columns=['Ingredient','Quantite','Unite'])
coltitre2.header('Ingredients choisis')

liste_index = meals_to_show.index
def increment_repas(repas):
    st.text(repas)
    st.text(meals_to_show.loc[repas,'quantite'])
    meals_to_show['quantite'][repas] = meals_to_show.loc[repas,'quantite'] + 1
def decrement_repas(repas):
    meals_to_show['quantite'][repas] = meals_to_show.loc[repas,'quantite'] - 1

def aff_col_repas(index_select):
    if index_select not in st.session_state:
        st.session_state[index_select] = meals_to_show.loc[index_select,'quantite']
    col1.text(index_select)
    col2.number_input('',min_value=0, max_value=10,value = int(meals_to_show.loc[index_select,['quantite']]),step=1,key = index_select)
    
    meals_to_show['quantite'][index_select] = st.write(st.session_state[index_select])

for i in range(len(liste_index)):
    aff_col_repas(liste_index[i])
    
    for y in range (1,11):
        ingredient_col = 'ingrédient_'+ str(y)
        quantite_col = 'quantite_ingredient_'+ str(y)
        unite_col = 'unité_mesure_ingredient_'+ str(y)

        ingredient_val = meals_to_show.loc[liste_index[i],ingredient_col]
        quantite_val = meals_to_show.loc[liste_index[i],quantite_col]
        unite_val = meals_to_show.loc[liste_index[i],unite_col]

        #todo check de null avants intégrations au df de la liste de course
        if pd.isna(meals_to_show.loc[liste_index[i],ingredient_col]) :
            continue
        else:
            if ingredient_val in liste_courses['Ingredient'].values :
                temp_index = liste_courses.index[(liste_courses['Ingredient'] == ingredient_val)]
                liste_courses['Quantite'][temp_index] = liste_courses.loc[temp_index,['Quantite']] + quantite_val
            else :
                liste_courses = liste_courses.append({'Ingredient':ingredient_val,'Quantite':quantite_val,'Unite':unite_val}, ignore_index=True)

col3.dataframe(liste_courses)
st.dataframe(meals_to_show)

csv = liste_courses.to_csv(sep=';').encode('utf-8')

st.download_button(
     label="Download data as CSV",
     data=csv,
     file_name='liste_courses.csv',
     mime='text/csv',
 )