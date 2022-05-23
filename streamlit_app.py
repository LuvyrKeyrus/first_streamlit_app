import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")

st.title('Application de repas')
st.header('Liste des repas')

my_meal_list = pd.read_csv("Repas.csv", sep=';')
my_meal_list = my_meal_list.set_index('plats')
liste_achats = pd.read_csv("Achats.csv", sep=';')


meals_selected = []
meals_to_show = pd.DataFrame()
col_lun, col_mar, col_mer, col_jeu, col_ven, col_sam, col_dim = st.columns(7)

col_lun.header("Lundi")
col_lun.multiselect("midi :",list(my_meal_list.index),key = "lun_midi")
col_lun.multiselect("soir :",list(my_meal_list.index),key = "lun_soir")
meals_selected = meals_selected + st.session_state['lun_midi']
meals_selected = meals_selected + st.session_state['lun_soir']

col_mar.header("Mardi")
col_mar.multiselect("midi :",list(my_meal_list.index),key = "mar_midi")
col_mar.multiselect("soir :",list(my_meal_list.index),key = "mar_soir")
meals_selected = meals_selected + st.session_state['mar_midi']
meals_selected = meals_selected + st.session_state['mar_soir']

col_mer.header("Mercredi")
col_mer.multiselect("midi :",list(my_meal_list.index),key = "mer_midi")
col_mer.multiselect("soir :",list(my_meal_list.index),key = "mer_soir")
meals_selected = meals_selected + st.session_state['mer_midi']
meals_selected = meals_selected + st.session_state['mer_soir']

col_jeu.header("jeudi")
col_jeu.multiselect("midi :",list(my_meal_list.index),key = "jeu_midi")
col_jeu.multiselect("soir :",list(my_meal_list.index),key = "jeu_soir")
meals_selected = meals_selected + st.session_state['jeu_midi']
meals_selected = meals_selected + st.session_state['jeu_soir']

col_ven.header("vendredi")
col_ven.multiselect("midi :",list(my_meal_list.index),key = "ven_midi")
col_ven.multiselect("soir :",list(my_meal_list.index),key = "ven_soir")
meals_selected = meals_selected + st.session_state['ven_midi']
meals_selected = meals_selected + st.session_state['ven_soir']

col_sam.header("Samedi")
col_sam.multiselect("midi :",list(my_meal_list.index),key = "sam_midi")
col_sam.multiselect("soir :",list(my_meal_list.index),key = "sam_soir")
meals_selected = meals_selected + st.session_state['sam_midi']
meals_selected = meals_selected + st.session_state['sam_soir']

col_dim.header("dimanche")
col_dim.multiselect("midi :",list(my_meal_list.index),key = "dim_midi")
col_dim.multiselect("soir :",list(my_meal_list.index),key = "dim_soir")
meals_selected = meals_selected + st.session_state['dim_midi']
meals_selected = meals_selected + st.session_state['dim_soir']

liste_select_achats = st.multiselect("produits complémentaires :",list(liste_achats.achat),key = "produits_comp")
df_produits =  liste_achats.isin(liste_select_achats)

st.dataframe(df_produits)
for taille in range(len(meals_selected)):
    if meals_selected[taille] not in meals_to_show.index :
        st.text('dans le if')
        meals_to_show=meals_to_show.append(my_meal_list.loc[meals_selected[taille]])
    else:
        st.text('dans le else')
        meals_to_show ['quantite'][meals_selected[taille]] = meals_to_show ['quantite'][meals_selected[taille]] + 1




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

col2.download_button(
     label="Télécharger la liste de courses",
     data=csv,
     file_name='liste_courses.csv',
     mime='text/csv',
 )