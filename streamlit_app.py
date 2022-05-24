import streamlit as st
import pandas as pd

def suppr_carac(string):
    characters = "'[]"
    for x in range(len(characters)):
        string = string.replace(characters[x],"")
    return string
def aff_col_produits(index_select):
    if index_select not in st.session_state:
        st.session_state[index_select] = df_produits.loc[index_select,'quantite_achat']
    col2.number_input(index_select,min_value=0, max_value=20,value = int(df_produits.loc[index_select,['quantite_achat']]),step=1,key = index_select)
    df_produits['quantite_achat'][index_select] = st.session_state[index_select]

def aff_col_repas(index_select):
    if index_select not in st.session_state:
        st.session_state[index_select] = meals_to_show.loc[index_select,'quantite']
    col1.number_input(index_select,min_value=0, max_value=20,value = int(meals_to_show.loc[index_select,['quantite']]),step=1,key = index_select)
    meals_to_show['quantite'][index_select] = st.session_state[index_select]

st.set_page_config(layout="wide")

st.title('Application de repas')
st.header('Choix des repas')

my_meal_list = pd.read_csv("Repas.csv", sep=';')
my_meal_list = my_meal_list.set_index('plats')
liste_achats = pd.read_csv("Achats.csv", sep=';')
liste_achats = liste_achats.set_index('achats')

meals_selected = []
characters = "'!?[]"
meals_to_show = pd.DataFrame()
df_produits = pd.DataFrame()
repas_semaine = pd.DataFrame(index=['Midi','Soir'],columns=['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche'])
col_lun, col_mar, col_mer, col_jeu, col_ven, col_sam, col_dim = st.columns(7)

col_lun.header("Lundi")
col_lun.multiselect("midi :",list(my_meal_list.index),key = "lun_midi")
col_lun.multiselect("soir :",list(my_meal_list.index),key = "lun_soir")
meals_selected = meals_selected + st.session_state['lun_midi']
meals_selected = meals_selected + st.session_state['lun_soir']
repas_semaine['Lundi']['Midi'] = suppr_carac(str(st.session_state['lun_midi']))
repas_semaine['Lundi']['Soir'] = suppr_carac(str(st.session_state['lun_soir']))


col_mar.header("Mardi")
col_mar.multiselect("midi :",list(my_meal_list.index),key = "mar_midi")
col_mar.multiselect("soir :",list(my_meal_list.index),key = "mar_soir")
meals_selected = meals_selected + st.session_state['mar_midi']
meals_selected = meals_selected + st.session_state['mar_soir']
repas_semaine['Mardi']['Midi'] = suppr_carac(str(st.session_state['mar_midi']))
repas_semaine['Mardi']['Soir'] = suppr_carac(str(st.session_state['mar_soir']))

col_mer.header("Mercredi")
col_mer.multiselect("midi :",list(my_meal_list.index),key = "mer_midi")
col_mer.multiselect("soir :",list(my_meal_list.index),key = "mer_soir")
meals_selected = meals_selected + st.session_state['mer_midi']
meals_selected = meals_selected + st.session_state['mer_soir']
repas_semaine['Mercredi']['Midi'] = suppr_carac(str(st.session_state['mer_midi']))
repas_semaine['Mercredi']['Soir'] = suppr_carac(str(st.session_state['mer_soir']))

col_jeu.header("jeudi")
col_jeu.multiselect("midi :",list(my_meal_list.index),key = "jeu_midi")
col_jeu.multiselect("soir :",list(my_meal_list.index),key = "jeu_soir")
meals_selected = meals_selected + st.session_state['jeu_midi']
meals_selected = meals_selected + st.session_state['jeu_soir']
repas_semaine['Jeudi']['Midi'] = suppr_carac(str(st.session_state['jeu_midi']))
repas_semaine['Jeudi']['Soir'] = suppr_carac(str(st.session_state['jeu_soir']))

col_ven.header("vendredi")
col_ven.multiselect("midi :",list(my_meal_list.index),key = "ven_midi")
col_ven.multiselect("soir :",list(my_meal_list.index),key = "ven_soir")
meals_selected = meals_selected + st.session_state['ven_midi']
meals_selected = meals_selected + st.session_state['ven_soir']
repas_semaine['Vendredi']['Midi'] = suppr_carac(str(st.session_state['ven_midi']))
repas_semaine['Vendredi']['Soir'] = suppr_carac(str(st.session_state['ven_soir']))

col_sam.header("Samedi")
col_sam.multiselect("midi :",list(my_meal_list.index),key = "sam_midi")
col_sam.multiselect("soir :",list(my_meal_list.index),key = "sam_soir")
meals_selected = meals_selected + st.session_state['sam_midi']
meals_selected = meals_selected + st.session_state['sam_soir']
repas_semaine['Samedi']['Midi'] = suppr_carac(str(st.session_state['sam_midi']))
repas_semaine['Samedi']['Soir'] = suppr_carac(str(st.session_state['sam_soir']))

col_dim.header("dimanche")
col_dim.multiselect("midi :",list(my_meal_list.index),key = "dim_midi")
col_dim.multiselect("soir :",list(my_meal_list.index),key = "dim_soir")
meals_selected = meals_selected + st.session_state['dim_midi']
meals_selected = meals_selected + st.session_state['dim_soir']
repas_semaine['Dimanche']['Midi'] = suppr_carac(str(st.session_state['dim_midi']))
repas_semaine['Dimanche']['Soir'] = suppr_carac(str(st.session_state['dim_soir']))

st.header('Choix des produits complémentaires')
liste_select_achats = st.multiselect("produits :",list(liste_achats.index),key = "produits_comp")

df_produits =  liste_achats[liste_achats.index.isin(liste_select_achats)]
col1, col2 = st.columns([2,2])
col1.header('Repas choisis')
col2.header('Produits complémentaires')
col_dl1, col_dl2,col_dl3,col_dl4,col_dl5 = st.columns([1,2,1,2,1])

for taille in range(len(meals_selected)):
    if meals_selected[taille] not in meals_to_show.index :
        meals_to_show=meals_to_show.append(my_meal_list.loc[meals_selected[taille]])
    else:
        meals_to_show ['quantite'][meals_selected[taille]] = meals_to_show ['quantite'][meals_selected[taille]] + 1




liste_courses=pd.DataFrame(columns=['Ingredient','Quantite','Unite'])
liste_produits = df_produits.index
liste_index = meals_to_show.index



for z in range(len(liste_produits)):
    
    nom_produit = liste_produits[z]
    quantite_produit = df_produits.loc[nom_produit,'quantite_achat']
    unite_produit = df_produits.loc[nom_produit,'unite_achat']
    aff_col_produits(nom_produit)
    
    if nom_produit in liste_courses['Ingredient'].values :
        st.text('dans le if')
        temp_index = liste_courses.index[(liste_courses['Ingredient'] == nom_produit)]
        
        liste_courses['Quantite'][temp_index] = df_produits.loc[nom_produit,'quantite_achat']
    else :
        st.text('dans le else')
        
        liste_courses = liste_courses.append({'Ingredient':nom_produit,'Quantite': quantite_produit * df_produits.loc[nom_produit,'quantite_achat'] ,'Unite': unite_produit}, ignore_index=True)


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
liste_courses.drop(indexNames , inplace=True)
st.header('Liste de courses')
st.dataframe(liste_courses)



csv = liste_courses.to_csv().encode('utf-8')

col_dl2.download_button(
     label="Télécharger la liste de courses",
     data=csv,
     file_name='liste_courses.csv',
     mime='text/csv',
 )

csv2 = repas_semaine.to_csv(sep = ";").encode('utf-8')

col_dl4.download_button(
     label="Télécharger les repas de la semaine",
     data=csv2,
     file_name='repas_de_la_semaine.csv',
     mime='text/csv',
 )