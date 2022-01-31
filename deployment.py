import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
import math
from collections import Counter
from plotly.figure_factory import create_gantt
from random import randint
import numpy as np


def lineplot(df, x_Name, y_Name, title, Color=None):
    fig = px.line(df, x=x_Name, y=y_Name, title=title, color=Color)
    return fig

def barplot(df, x_Name, y_Name, title, Color=None):
    fig = px.bar(df, x=x_Name, y=y_Name, title=title, color=Color)
    return fig   

def histplot(df, x_Name, y_Name, title, Color=None,x_range=None):
    fig = px.bar(df, x=x_Name, y=y_Name, title=title, color=Color,barmode='group')
    return fig   

############### ARCHIVOS DE INVETARIO ################
df_inventario_completo = pd.read_csv(r'C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Reporte_Merge_Inventario_Portafolio.csv')
df_rotacion_completo  = pd.read_csv(r'C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Reporte_Merge_Rotacion_Portafolio.csv')

df_reporte_inventario = pd.read_csv(r'C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Reporte_Mes_Inventario.csv')
df_reporte_inventario = df_reporte_inventario.drop(['Unnamed: 0'], axis=1)

df_reporte_inventario_regional_general = pd.read_csv(r'C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Reporte_Regional_Inventario.csv')
df_reporte_inventario_regional_general = df_reporte_inventario_regional_general.drop(['Unnamed: 0'], axis=1)
df_reporte_inventario_regional_general = df_reporte_inventario_regional_general.sort_values(by=['COSTO TOTAL ARTICULO'], ascending=False)

df_reporte_inventario_regionales = pd.read_csv(r'C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Reporte_Mes_Regionales_Inventario.csv')
df_reporte_inventario_regionales = df_reporte_inventario_regionales.drop(['Unnamed: 0'], axis=1)
df_reporte_inventario_regionales = df_reporte_inventario_regionales.sort_values(by=['Mes Numerico'], ascending=True)

################# ARCHIVOS DE ROTACION #####################

df_reporte_rotacion = pd.read_csv(r'C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Reporte_Mes_Rotacion.csv')
df_reporte_rotacion = df_reporte_rotacion.drop(['Unnamed: 0'], axis=1)

df_reporte_rotacion_regional_general = pd.read_csv(r'C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Reporte_Regional_Rotacion.csv')
df_reporte_rotacion_regional_general = df_reporte_rotacion_regional_general.drop(['Unnamed: 0'], axis=1)
df_reporte_rotacion_regional_general = df_reporte_rotacion_regional_general.sort_values(by=['Costo Compra'], ascending=False)

df_reporte_rotacion_regionales = pd.read_csv(r'C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Reporte_Mes_Regionales_Rotacion.csv')
df_reporte_rotacion_regionales = df_reporte_rotacion_regionales.drop(['Unnamed: 0'], axis=1)
df_reporte_rotacion_regionales = df_reporte_rotacion_regionales.sort_values(by=['Mes Numerico'], ascending=True)


title = "Información de Cruz Verde 2021"
st.title(title) 

option = st.selectbox("Seleccione una opción", [" ","Inventario", "Rotacion"])

if option == "Inventario":

    st.markdown ("""
    <h1 style="text-align: center;">Información de Inventario</h1>
    """, unsafe_allow_html=True)

    df_display_df_reporte_total = st.checkbox("Informacion Total General", value=False)

    if df_display_df_reporte_total:
        st.dataframe(df_reporte_inventario)
    st.write(barplot(df_reporte_inventario, 'Mes', 'COSTO TOTAL ARTICULO', 'Reporte del total de costo de los articulos mes a mes'))

    df_display_df_reporte_total_regionales = st.checkbox("Informacion de Regionales General", value=False)

    if df_display_df_reporte_total_regionales:
        st.dataframe(df_reporte_inventario_regional_general)
    st.write(barplot(df_reporte_inventario_regional_general, 'Regional Correcta', 'COSTO TOTAL ARTICULO', 'Reporte del comportamiento mes a mes por region'))

    df_display_df_regionales_inventario_mes = st.checkbox("Informacion mes a mes por Regionales detallado", value=False)

    if df_display_df_regionales_inventario_mes:
        st.dataframe(df_reporte_inventario_regionales)
    st.write(histplot(df_reporte_inventario_regionales, 'Mes', 'COSTO TOTAL ARTICULO', 'Reporte del total de costo de los articulos mes a mes','Regional Correcta'))

###################################################################################################################################################
#########################-------------------------------TOP 10 MEDICAMENTOS EN INVENTARIO-------------------------------#########################
############################################################################################################################################################

    st.markdown ("""
    <h1 style="text-align: left;">Top 10 Medicamentos</h1>
    """, unsafe_allow_html=True)

    top_10_costo = df_inventario_completo.groupby(['NOMPROD'])['COSTO TOTAL ARTICULO'].sum().reset_index()
    top_10_costo = top_10_costo.sort_values(by=['COSTO TOTAL ARTICULO'], ascending=False).reset_index(drop=True)[0:11]

    top_10_costo_cb = st.checkbox("Informacion Top 10 Medicamentos por Costo", value=False)

    if top_10_costo_cb:
         st.dataframe(top_10_costo)

    st.write(barplot(top_10_costo, 'NOMPROD', 'COSTO TOTAL ARTICULO', 'Reporte Top 10 medicamentos por Costo'))

    top_10_cantidad = df_inventario_completo.groupby(['NOMPROD'])['CANTIDAD ARTICULO'].sum().reset_index()
    top_10_cantidad = top_10_cantidad.sort_values(by=['CANTIDAD ARTICULO'], ascending=False).reset_index(drop=True)[0:11]

    top_10_cantidad_cb = st.checkbox("Informacion Top 10 Medicamentos por Cantidad", value=False)

    if top_10_cantidad_cb:
         st.dataframe(top_10_cantidad)

    st.write(barplot(top_10_cantidad, 'NOMPROD', 'CANTIDAD ARTICULO', 'Reporte Top 10 medicamentos por Cantidad'))


###################################################################################################################################################
#########################-------------------------------INFORMACION POR MEDICAMENTO INVENTARIO-------------------------------#########################
############################################################################################################################################################

    st.markdown ("""
    <h1 style="text-align: center;">Información discriminada por medicamento</h1>
    """, unsafe_allow_html=True)

    names_inventario = df_inventario_completo.sort_values(by=['NOMPROD'], ascending=True)
    Medicamento = st.selectbox("Seleccione un Medicamento", names_inventario['NOMPROD'].unique())
    seleccionado = Medicamento

    st.markdown ("""
    <h1 style="text-align: left;">COSTO</h1>
    """, unsafe_allow_html=True)


    if Medicamento == seleccionado:
        regional_behaviour = df_inventario_completo.groupby(['NOMPROD','Regional Correcta', 'Mes','Mes Numerico'])['COSTO TOTAL ARTICULO'].sum().reset_index()
        filtro_medicamento_region = regional_behaviour[regional_behaviour['NOMPROD']== Medicamento].groupby(['Regional Correcta'])['COSTO TOTAL ARTICULO'].sum().reset_index()
        filtro_medicamento_region = filtro_medicamento_region.sort_values(by=['COSTO TOTAL ARTICULO'], ascending=False)

        filtro_medicamento_mes = regional_behaviour[regional_behaviour['NOMPROD']== Medicamento].groupby(['Mes','Mes Numerico'])['COSTO TOTAL ARTICULO'].sum().reset_index()
        filtro_medicamento_mes = filtro_medicamento_mes.sort_values(by=['Mes Numerico'], ascending=True).reset_index(drop=True)

        name_medicamento_region = st.checkbox("Informacion del medicamento por Region", value=False)

        if name_medicamento_region:
            st.dataframe(filtro_medicamento_region)

        st.write(barplot(filtro_medicamento_region, 'Regional Correcta', 'COSTO TOTAL ARTICULO', f'Reporte Regionales del medicamento {Medicamento}'))

        name_medicamento_mes = st.checkbox("Informacion del medicamento por mes", value=False)
        if name_medicamento_mes:
            st.dataframe(filtro_medicamento_mes)

        st.write(lineplot(filtro_medicamento_mes, 'Mes', 'COSTO TOTAL ARTICULO', f'Reporte Regionales del medicamento {Medicamento}'))

       ###############################################################################################################################################################
        ###############################################################################################################################################################
        ########################################### GRAFICAS DE CANTIDAD ###################################################################################################
        ###############################################################################################################################################################
        ###############################################################################################################################################################
        
        st.markdown ("""
        <h1 style="text-align: left;">Cantidad</h1>
        """, unsafe_allow_html=True)

        regional_behaviour_inventario_cantidad = df_inventario_completo.groupby(['NOMPROD','Regional Correcta', 'Mes','Mes Numerico'])['CANTIDAD ARTICULO'].sum().reset_index()
        filtro_medicamento_region_inv_cantidad = regional_behaviour_inventario_cantidad[regional_behaviour_inventario_cantidad['NOMPROD']== Medicamento].groupby(['Regional Correcta'])['CANTIDAD ARTICULO'].sum().reset_index()
        filtro_medicamento_region_inv_cantidad = filtro_medicamento_region_inv_cantidad.sort_values(by=['CANTIDAD ARTICULO'], ascending=False)

        filtro_medicamento_mes_inv_cantidad = regional_behaviour_inventario_cantidad[regional_behaviour_inventario_cantidad['NOMPROD']== Medicamento].groupby(['Mes','Mes Numerico'])['CANTIDAD ARTICULO'].sum().reset_index()
        filtro_medicamento_mes_inv_cantidad = filtro_medicamento_mes_inv_cantidad.sort_values(by=['Mes Numerico'], ascending=True).reset_index(drop=True)

        name_medicamento_region_inv_cantidad = st.checkbox("Informacion del medicamento por Region-Cantidad", value=False)

        if name_medicamento_region_inv_cantidad:
            st.dataframe(filtro_medicamento_region_inv_cantidad)

        st.write(barplot(filtro_medicamento_region_inv_cantidad, 'Regional Correcta', 'CANTIDAD ARTICULO', f'Reporte Regionales del medicamento {Medicamento} por CANTIDAD'))

        name_medicamento_mes_inv_cantidad = st.checkbox("Informacion del medicamento por Mes-Cantidad", value=False)
        if name_medicamento_mes_inv_cantidad:
            st.dataframe(filtro_medicamento_mes_inv_cantidad)

        st.write(lineplot(filtro_medicamento_mes_inv_cantidad, 'Mes', 'CANTIDAD ARTICULO', f'Reporte Regionales del medicamento {Medicamento} por CANTIDAD'))


##############################################################################################################################################################
##############################################################################################################################################################
################################################################################################################################################
##############################################################################################################################################################
############################################################## DESPLIEGUE DE TODA LA INFORMACION DE ROTACION ##############################################################################
if option == "Rotacion":

    st.markdown ("""
    <h1 style="text-align: center;">Información de Rotación</h1>
    """, unsafe_allow_html=True)

    df_display_df = st.checkbox("Informacion Total discriminada por mes", value=False)

    if df_display_df:
        st.dataframe(df_reporte_rotacion)

    st.write(barplot(df_reporte_rotacion, 'Mes', 'Costo Compra', 'Reporte del total de costo de los articulos mes a mes'))
    
    df_display_df_reporte_total_regionales_rotacion = st.checkbox("Información de regionales por mes", value=False)

    if df_display_df_reporte_total_regionales_rotacion:
        st.dataframe(df_reporte_rotacion_regional_general)
    st.write(barplot(df_reporte_rotacion_regional_general, 'Regional Correcta', 'Costo Compra', 'Reporte del comportamiento mes a mes por region'))


    df_display_df_regionales = st.checkbox("Informacion mes a mes por Regionales", value=False)

    if df_display_df_regionales:
        st.dataframe(df_reporte_rotacion_regionales)
    st.write(histplot(df_reporte_rotacion_regionales, 'Mes', 'Costo Compra', 'Reporte del total de costo de los articulos mes a mes','Regional Correcta'))

###################################################################################################################################################
#########################-------------------------------TOP 10 MEDICAMENTOS EN ROTACION---------------------------------#########################
############################################################################################################################################################

    st.markdown ("""
    <h1 style="text-align: left;">Top 10 Medicamentos</h1>
    """, unsafe_allow_html=True)

    top_10_costo_rot = df_rotacion_completo.groupby(['NOMPROD'])['Costo Compra'].sum().reset_index()
    top_10_costo_rot = top_10_costo_rot.sort_values(by=['Costo Compra'], ascending=False).reset_index(drop=True)[0:11]

    top_10_costo_rot_cb = st.checkbox("Informacion Top 10 Medicamentos por Costo", value=False)

    if top_10_costo_rot_cb:
         st.dataframe(top_10_costo_rot)

    st.write(barplot(top_10_costo_rot, 'NOMPROD', 'Costo Compra', 'Reporte Top 10 medicamentos por Costo'))

    top_10_cantidad_rot = df_rotacion_completo.groupby(['NOMPROD'])['Unidades vendidas'].sum().reset_index()
    top_10_cantidad_rot = top_10_cantidad_rot.sort_values(by=['Unidades vendidas'], ascending=False).reset_index(drop=True)[0:11]

    top_10_cantidad_cb_rot = st.checkbox("Informacion Top 10 Medicamentos por Cantidad", value=False)

    if top_10_cantidad_cb_rot:
         st.dataframe(top_10_cantidad_rot)

    st.write(barplot(top_10_cantidad_rot, 'NOMPROD', 'Unidades vendidas', 'Reporte Top 10 medicamentos por Cantidad'))



###################################################################################################################################################
#########################-------------------------------INFORMACION POR MEDICAMENTO ROTACION-------------------------------#########################
############################################################################################################################################################

    st.markdown ("""
    <h1 style="text-align: center;">Información discriminada por medicamento</h1>
    """, unsafe_allow_html=True)
    names_rotacion = df_rotacion_completo.sort_values(by=['NOMPROD'], ascending=True)

 

    Medicamento_rot = st.selectbox("Seleccione un Medicamento", names_rotacion['NOMPROD'].unique())
    seleccionado_rot = Medicamento_rot

    st.markdown ("""
    <h1 style="text-align: left;">Costos</h1>
    """, unsafe_allow_html=True)

    if Medicamento_rot == seleccionado_rot:
        regional_behaviour_rotacion = df_rotacion_completo.groupby(['NOMPROD','Regional Correcta', 'Mes','Mes Numerico'])['Costo Compra'].sum().reset_index()
        filtro_medicamento_region_rot_cantidad = regional_behaviour_rotacion[regional_behaviour_rotacion['NOMPROD']== Medicamento_rot].groupby(['Regional Correcta'])['Costo Compra'].sum().reset_index()
        filtro_medicamento_region_rot_cantidad = filtro_medicamento_region_rot_cantidad.sort_values(by=['Costo Compra'], ascending=False)

        filtro_medicamento_mes_rot = regional_behaviour_rotacion[regional_behaviour_rotacion['NOMPROD']== Medicamento_rot].groupby(['Mes','Mes Numerico'])['Costo Compra'].sum().reset_index()
        filtro_medicamento_mes_rot = filtro_medicamento_mes_rot.sort_values(by=['Mes Numerico'], ascending=True).reset_index(drop=True)

        name_medicamento_region_rot = st.checkbox("Informacion del medicamento por Region", value=False)

        if name_medicamento_region_rot:
            st.dataframe(filtro_medicamento_region_rot_cantidad)

        st.write(barplot(filtro_medicamento_region_rot_cantidad, 'Regional Correcta', 'Costo Compra', f'Reporte Regionales del medicamento {Medicamento_rot} por COSTOS'))

        name_medicamento_mes_rot = st.checkbox("Informacion del medicamento por mes", value=False)
        if name_medicamento_mes_rot:
            st.dataframe(filtro_medicamento_mes_rot)

        st.write(lineplot(filtro_medicamento_mes_rot, 'Mes', 'Costo Compra', f'Reporte Regionales del medicamento {Medicamento_rot} por COSTOS'))

        ###############################################################################################################################################################
        ###############################################################################################################################################################
        ########################################### GRAFICAS DE CANTIDAD ###################################################################################################
        ###############################################################################################################################################################
        ###############################################################################################################################################################

        st.markdown ("""
        <h1 style="text-align: left;">Cantidad</h1>
        """, unsafe_allow_html=True)

        regional_behaviour_rotacion_cantidad = df_rotacion_completo.groupby(['NOMPROD','Regional Correcta', 'Mes','Mes Numerico'])['Unidades vendidas'].sum().reset_index()
        filtro_medicamento_region_rot_cantidad = regional_behaviour_rotacion_cantidad[regional_behaviour_rotacion_cantidad['NOMPROD']== Medicamento_rot].groupby(['Regional Correcta'])['Unidades vendidas'].sum().reset_index()
        filtro_medicamento_region_rot_cantidad = filtro_medicamento_region_rot_cantidad.sort_values(by=['Unidades vendidas'], ascending=False)

        filtro_medicamento_mes_rot_cantidad = regional_behaviour_rotacion_cantidad[regional_behaviour_rotacion_cantidad['NOMPROD']== Medicamento_rot].groupby(['Mes','Mes Numerico'])['Unidades vendidas'].sum().reset_index()
        filtro_medicamento_mes_rot_cantidad = filtro_medicamento_mes_rot_cantidad.sort_values(by=['Mes Numerico'], ascending=True).reset_index(drop=True)

        name_medicamento_region_rot_cantidad = st.checkbox("Informacion del medicamento por Region-Cantidad", value=False)

        if name_medicamento_region_rot:
            st.dataframe(filtro_medicamento_region_rot_cantidad)

        st.write(barplot(filtro_medicamento_region_rot_cantidad, 'Regional Correcta', 'Unidades vendidas', f'Reporte Regionales del medicamento {Medicamento_rot} por CANTIDAD'))

        name_medicamento_mes_rot_cantidad = st.checkbox("Informacion del medicamento por Mes-Cantidad", value=False)
        if name_medicamento_mes_rot:
            st.dataframe(filtro_medicamento_mes_rot_cantidad)

        st.write(lineplot(filtro_medicamento_mes_rot_cantidad, 'Mes', 'Unidades vendidas', f'Reporte Regionales del medicamento {Medicamento_rot} por CANTIDAD'))