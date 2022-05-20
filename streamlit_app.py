import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")

st.title('Application de repas')
st.header('Liste des repas')
my_meal_list = pd.read_csv("Repas.csv", sep=';')
my_meal_list = my_meal_list.set_index('plats')
meals_selected = []


#todo faire par jours pour sortir le tableau des repas de la semaine ensuite
st.header("Lundi")
if pd.isna(st.multiselect("midi :",list(my_meal_list.index),key = "lun_midi")) :
    pass
else:
    meals_selected.append(st.multiselect("midi :",list(my_meal_list.index),key = "lun_midi"))
if pd.isna(st.multiselect("midi :",list(my_meal_list.index),key = "lun_soir")) :
    pass
else:
    meals_selected.append(st.multiselect("soir :",list(my_meal_list.index),key = "lun_soir"))  
#meals_selected.append(st.session_state['lun_midi'])
#meals_selected.append(st.session_state['lun_soir'])

st.header("Mardi")
meals_selected=st.multiselect("midi :",list(my_meal_list.index),key = "mar_midi")
meals_selected=st.multiselect("soir :",list(my_meal_list.index),key = "mar_soir")

st.header("Mercredi")
meals_selected=st.multiselect("midi :",list(my_meal_list.index),key = "mer_midi")
meals_selected=st.multiselect("soir :",list(my_meal_list.index),key = "mer_soir")

st.header("jeudi")
meals_selected=st.multiselect("midi :",list(my_meal_list.index),key = "jeu_midi")
meals_selected=st.multiselect("soir :",list(my_meal_list.index),key = "jeu_soir")

st.header("vendredi")
meals_selected=st.multiselect("midi :",list(my_meal_list.index),key = "ven_midi")
meals_selected=st.multiselect("soir :",list(my_meal_list.index),key = "ven_soir")

st.header("Samedi")
meals_selected=st.multiselect("midi :",list(my_meal_list.index),key = "sam_midi")
meals_selected=st.multiselect("soir :",list(my_meal_list.index),key = "sam_soir")

st.header("dimanche")
meals_selected=st.multiselect("midi :",list(my_meal_list.index),key = "dim_midi")
meals_selected=st.multiselect("soir :",list(my_meal_list.index),key = "dim_soir")

#meals_selected = st.multiselect("selection plat :",list(my_meal_list.index))
st.text(meals_selected)
st.dataframe(my_meal_list)

meals_to_show=my_meal_list.loc[meals_selected]
coltitre1, coltitre2 = st.columns(2)
col1, col2 = st.columns([2,2])
coltitre1.header('Repas choisis')


liste_courses=pd.DataFrame(columns=['Ingredient','Quantite','Unite'])
coltitre2.header('Ingredients choisis')

liste_index = meals_to_show.index

def aff_col_repas(index_select):
    if index_select not in st.session_state:
        st.session_state[index_select] = meals_to_show.loc[index_select,'quantite']
    col1.number_input(index_select,min_value=0, max_value=10,value = int(meals_to_show.loc[index_select,['quantite']]),step=1,key = index_select)
    meals_to_show['quantite'][index_select] = st.session_state[index_select]

for i in range(len(liste_index)):
    aff_col_repas(liste_index[i])
    
    for y in range (1,11):
        ingredient_col = 'ingrédient_'+ str(y)
        quantite_col = 'quantite_ingredient_'+ str(y)
        unite_col = 'unité_mesure_ingredient_'+ str(y)

        ingredient_val = meals_to_show.loc[liste_index[i],ingredient_col]
        quantite_val = meals_to_show.loc[liste_index[i],quantite_col]
        unite_val = meals_to_show.loc[liste_index[i],unite_col]

        if pd.isna(meals_to_show.loc[liste_index[i],ingredient_col]) :
            continue
        else:
            if ingredient_val in liste_courses['Ingredient'].values :
                temp_index = liste_courses.index[(liste_courses['Ingredient'] == ingredient_val)]
                liste_courses['Quantite'][temp_index] = liste_courses.loc[temp_index,['Quantite']] + quantite_val * meals_to_show.loc[liste_index[i],'quantite']
            else :
                liste_courses = liste_courses.append({'Ingredient':ingredient_val,'Quantite':quantite_val * meals_to_show.loc[liste_index[i],'quantite'] ,'Unite':unite_val}, ignore_index=True)

indexNames = liste_courses[ liste_courses['Quantite'] == 0 ].index
# Delete these row indexes from dataFrame
liste_courses.drop(indexNames , inplace=True)
col2.dataframe(liste_courses)

csv = liste_courses.to_csv().encode('utf-8')

st.download_button(
     label="Télécharger la liste de courses",
     data=csv,
     file_name='liste_courses.csv',
     mime='text/csv',
 )