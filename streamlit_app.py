from cmath import nan
import streamlit as st
import pandas as pd
import numpy as np

st.title('Application de repas')
st.header('Liste des repas')
my_meal_list = pd.read_csv("Repas.csv", sep=';')
my_meal_list = my_meal_list.set_index('plats')

meals_selected = st.multiselect("Pick some meals :",list(my_meal_list.index))

st.dataframe(my_meal_list)


meals_to_show=my_meal_list.loc[meals_selected]
coltitre1, coltitre2 = st.columns(2)
col1, col2, col3, col4 = st.columns([1,1,1,3])
coltitre1.header('Repas choisis')
#col1.dataframe(meals_to_show)

liste_courses=pd.DataFrame(columns=['Ingredient','Quantite','Unite'])
coltitre2.header('Ingredients choisis')

liste_index = meals_to_show.index
def increment_repas(repas):
    meals_to_show['quantite'][repas] = meals_to_show.loc[repas,'quantite'] + 1
def decrement_repas(repas):
    meals_to_show['quantite'][repas] = meals_to_show.loc[repas,'quantite'] - 1

def aff_col_repas(index_select):

    col1.text(index_select)
    col2.button('+1', on_click=increment_repas, args=(index_select,))
    col3.button('-1', on_click=decrement_repas, args=(index_select,))

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

col4.dataframe(liste_courses)


csv = liste_courses.to_csv(sep=';').encode('utf-8')

st.download_button(
     label="Download data as CSV",
     data=csv,
     file_name='liste_courses.csv',
     mime='text/csv',
 )