import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
import math
from collections import Counter
from plotly.figure_factory import create_gantt
from random import randint
import numpy as np


def lineplot(df, x_Name, y_Name, title, Color=None, list_Color_sequence=None):
    fig = px.line(df, x=x_Name, y=y_Name, title=title, color=Color, color_discrete_sequence = list_Color_sequence)
    return fig

def barplot(df, x_Name, y_Name, title, Color=None, list_Color_sequence=None):
    fig = px.bar(df, x=x_Name, y=y_Name, title=title, color=Color, color_discrete_sequence = list_Color_sequence)
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
    st.write(barplot(df_reporte_inventario, 'Mes', 'COSTO TOTAL ARTICULO', 'Reporte del total de costo de los articulos mes a mes', list_Color_sequence=['#1f77b4']))

    df_display_df_reporte_total_regionales = st.checkbox("Informacion de Regionales General", value=False)

    if df_display_df_reporte_total_regionales:
        st.dataframe(df_reporte_inventario_regional_general)
    st.write(barplot(df_reporte_inventario_regional_general, 'Regional Correcta', 'COSTO TOTAL ARTICULO', 'Reporte del comportamiento mes a mes por region', list_Color_sequence=['#92341F']))

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
    top_10_costo = top_10_costo.sort_values(by=['COSTO TOTAL ARTICULO'], ascending=False).reset_index(drop=True)

    top_10_costo_cb = st.checkbox("Informacion Top 10 Medicamentos por Costo", value=False)

    if top_10_costo_cb:
         st.dataframe(top_10_costo)

    st.write(barplot(top_10_costo[0:11], 'NOMPROD', 'COSTO TOTAL ARTICULO', 'Reporte Top 10 medicamentos por Costo', list_Color_sequence=['green']))

    top_10_cantidad = df_inventario_completo.groupby(['NOMPROD'])['CANTIDAD ARTICULO'].sum().reset_index()
    top_10_cantidad = top_10_cantidad.sort_values(by=['CANTIDAD ARTICULO'], ascending=False).reset_index(drop=True)

    top_10_cantidad_cb = st.checkbox("Informacion Top 10 Medicamentos por Cantidad", value=False)

    if top_10_cantidad_cb:
         st.dataframe(top_10_cantidad)

    st.write(barplot(top_10_cantidad[0:11], 'NOMPROD', 'CANTIDAD ARTICULO', 'Reporte Top 10 medicamentos por Cantidad', list_Color_sequence=['yellow']))

############################################################################################################################################################
#########################-------------------------------REVISION POR REGIONALES Y FILTROS-------------------------------#########################
############################################################################################################################################################
    st.markdown ("""
    <h1 style="text-align: center;">Información discriminada por Regional</h1>
    """, unsafe_allow_html=True)

    regionales_inventario= df_inventario_completo.sort_values(by=['Regional Correcta'], ascending=True)
    Regional_select_inventario = st.selectbox("Seleccione una Regional", regionales_inventario['Regional Correcta'].unique())

    reg_select = Regional_select_inventario

    numer_cityes_shops_by_region = regionales_inventario[regionales_inventario['Regional Correcta'] == reg_select]

    regional_shops =str(int(len(numer_cityes_shops_by_region['ORGANIZACION'].unique())))
    ciudades_total =str(int(len(numer_cityes_shops_by_region['Ciudad'].unique())))


    html_str_regional = f"""
    <style>
    p.a {{
    font: bold 16px Arial;
    }}
    </style>
    <p class="a">La regional {str(reg_select)} tiene {regional_shops} puntos en {ciudades_total} ciudades</p>
    """
    st.markdown(html_str_regional, unsafe_allow_html=True)

############################################################################################################################################################
#########################-------------------------------FILTROS POR CIUDAD-------------------------------#########################
    allow_info_ciudad = st.checkbox("Ver información por ciudad detallada", value=False)

    if allow_info_ciudad:

        filter_region = df_inventario_completo[df_inventario_completo['Regional Correcta'] == reg_select]
        cities = filter_region.sort_values(by=['Ciudad'], ascending=True)
        cities_select = st.selectbox("Seleccione una Ciudad", cities['Ciudad'].unique())

        city_selected = cities_select

        df_filter_city_region = filter_region[filter_region['Ciudad'] == city_selected]

        top_10_costo_city = df_filter_city_region.groupby(['NOMPROD'])['COSTO TOTAL ARTICULO'].sum().reset_index()
        top_10_costo_city = top_10_costo_city.sort_values(by=['COSTO TOTAL ARTICULO'], ascending=True).reset_index(drop=True)
        
        city_info_shops =str(int(len(df_filter_city_region['ORGANIZACION'].unique())))
        
        html_str_regional = f"""
        <style>
        p.a {{
        font: bold 16px Arial;
        }}
        </style>
        <p class="a">La ciudad de {str(city_selected)} tiene {city_info_shops} puntos </p>
        """
        st.markdown(html_str_regional, unsafe_allow_html=True)

        top_10_costo_cb_city = st.checkbox(f"Informacion Medicamentos menos vendidos por menor Costo en ciudad de {city_selected}", value=False)

        if top_10_costo_cb_city:
            st.dataframe(top_10_costo_city)

        st.write(barplot(top_10_costo_city[0:10], 'NOMPROD', 'COSTO TOTAL ARTICULO', f'Reporte Top 10 medicamentos por menor Costo en ciudad de {city_selected}', list_Color_sequence=['green']))

    #####   CANTIDAD POR REGIONALES  #####
        top_10_cantidad_city = df_filter_city_region.groupby(['NOMPROD'])['CANTIDAD ARTICULO'].sum().reset_index()
        top_10_cantidad_city = top_10_cantidad_city.sort_values(by=['CANTIDAD ARTICULO'], ascending=True).reset_index(drop=True)

        top_10_cantidad_cb_city = st.checkbox(f"Informacion Top 10 Medicamentos por menor cantidad en ciudad de {city_selected}", value=False)

        if top_10_cantidad_cb_city:
            st.dataframe(top_10_cantidad_city)

        st.write(barplot(top_10_cantidad_city[0:11], 'NOMPROD', 'CANTIDAD ARTICULO', f'Reporte Top 10 medicamentos por menor Cantidad en ciudad de {city_selected}', list_Color_sequence=['yellow']))


############################################################################################################################################################
#########################-------------------------------DISCRIMINACION POR PUNTO DE VENTA-------------------------------#########################
        top_10_cantidad_shop = df_filter_city_region.groupby(['ORGANIZACION'])['CANTIDAD ARTICULO'].sum().reset_index()
        top_10_cantidad_shop = top_10_cantidad_shop.sort_values(by=['CANTIDAD ARTICULO'], ascending=True).reset_index(drop=True)[0:11]

        top_10_cantidad_cb_shop = st.checkbox(f"Informacion Top 10 Puntos de venta por menor cantidad en ciudad de {city_selected}", value=False)

        if top_10_cantidad_cb_city:
            st.dataframe(top_10_cantidad_shop)

        st.write(barplot(top_10_cantidad_shop, 'ORGANIZACION', 'CANTIDAD ARTICULO', f'Reporte Top 10 medicamentos por menor Cantidad en los punto de venta de {city_selected}', list_Color_sequence=['#431684']))


        allow_info_shop = st.checkbox("Ver información por punto de venta detallada", value=False)

        if allow_info_shop:

            shops = df_filter_city_region.sort_values(by=['ORGANIZACION'], ascending=True)
            shops_select = st.selectbox(f"Seleccione un punto de venta de la ciudad de {city_selected}", shops['ORGANIZACION'].unique())

            shop_selected = shops_select

            df_filter_city_region_shop = df_filter_city_region[df_filter_city_region['ORGANIZACION'] == shop_selected]

            shops_info_products =str(int(len(df_filter_city_region_shop['NOMPROD'].unique())))
        
            html_str_regional = f"""
            <style>
            p.a {{
            font: bold 16px Arial;
            }}
            </style>
            <p class="a">La Ciudad de {city_selected} en {str(shop_selected)} tiene {shops_info_products} productos </p>
            """
            st.markdown(html_str_regional, unsafe_allow_html=True)




###################################################################################################################################################
#########################-------------------------------INFORMACION POR MEDICAMENTO INVENTARIO-------------------------------#########################
############################################################################################################################################################
            allow_info_product = st.checkbox(f"Ver información por productos en el punto {shop_selected}", value=False)

            if allow_info_product:


                st.markdown ("""
                <h1 style="text-align: center;">Información discriminada por medicamento</h1>
                """, unsafe_allow_html=True)

                names_inventario = df_filter_city_region_shop.sort_values(by=['NOMPROD'], ascending=True)
                Medicamento = st.selectbox("Seleccione un Medicamento", names_inventario['NOMPROD'].unique())
                seleccionado = Medicamento

                if names_inventario[names_inventario['NOMPROD']== seleccionado].shape[0] < 2:

                    html_str_producto_1regis = f"""
                    <style>
                    p.a {{
                    font: bold 16px Arial;
                    }}
                    </style>
                    <p class="a">La Ciudad de {city_selected} en {str(shop_selected)} tiene {shops_info_products} productos del medicamento{seleccionado} solo tiene un registro </p>
                    """
                    st.markdown(html_str_producto_1regis, unsafe_allow_html=True)

                else:
                    st.markdown ("""
                    <h1 style="text-align: left;">COSTO</h1>
                    """, unsafe_allow_html=True)


                    if Medicamento == seleccionado:

                        filtro_medicamento_mes = df_filter_city_region_shop[df_filter_city_region_shop['NOMPROD']== Medicamento].groupby(['Mes','Mes Numerico','Año'])['COSTO TOTAL ARTICULO'].sum().reset_index()
                        filtro_medicamento_mes = filtro_medicamento_mes.sort_values(by=['Año','Mes Numerico'], ascending=True).reset_index(drop=True)

                        name_medicamento_mes = st.checkbox(f"Informacion del medicamento {seleccionado} por mes-Costo", value=False)
                        if name_medicamento_mes:
                            filtro_medicamento_mes.drop(['Mes Numerico'], axis=1, inplace=True)
                            st.dataframe(filtro_medicamento_mes)

                        st.write(lineplot(filtro_medicamento_mes, 'Mes', 'COSTO TOTAL ARTICULO', f'Reporte Regionales del medicamento {Medicamento}',list_Color_sequence=['green']))

###################################################################################################################################################################
#######################################################################################################################################################################
############################################################ GRAFICAS DE CANTIDAD ###################################################################################################
################################################################################################################################################################
###############################################################################################################################################################
                        
                        st.markdown ("""
                        <h1 style="text-align: left;">Cantidad</h1>
                        """, unsafe_allow_html=True)

                        filtro_medicamento_mes_inv_cantidad = df_filter_city_region_shop[df_filter_city_region_shop['NOMPROD']== Medicamento].groupby(['Mes','Mes Numerico','Año'])['CANTIDAD ARTICULO'].sum().reset_index()
                        filtro_medicamento_mes_inv_cantidad = filtro_medicamento_mes_inv_cantidad.sort_values(by=['Año','Mes Numerico'], ascending=True).reset_index(drop=True)

                        name_medicamento_mes_inv_cantidad = st.checkbox(f"Informacion del medicamento {seleccionado} por Mes-Cantidad", value=False)
                        if name_medicamento_mes_inv_cantidad:
                            filtro_medicamento_mes_inv_cantidad.drop(['Mes Numerico'], axis=1, inplace=True)
                            st.dataframe(filtro_medicamento_mes_inv_cantidad)

                        st.write(lineplot(filtro_medicamento_mes_inv_cantidad, 'Mes', 'CANTIDAD ARTICULO', f'Reporte Regionales del medicamento {Medicamento} por CANTIDAD', list_Color_sequence=['yellow']))


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

    st.write(barplot(df_reporte_rotacion, 'Mes', 'Costo Compra', 'Reporte del total de costo de los articulos mes a mes', list_Color_sequence=['#1f77b4']))
    
    df_display_df_reporte_total_regionales_rotacion = st.checkbox("Información de regionales por mes", value=False)

    if df_display_df_reporte_total_regionales_rotacion:
        st.dataframe(df_reporte_rotacion_regional_general)
    st.write(barplot(df_reporte_rotacion_regional_general, 'Regional Correcta', 'Costo Compra', 'Reporte del comportamiento mes a mes por region', list_Color_sequence=['#92341F']))


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

    st.write(barplot(top_10_costo_rot, 'NOMPROD', 'Costo Compra', 'Reporte Top 10 medicamentos por Costo', list_Color_sequence=['green']))

    top_10_cantidad_rot = df_rotacion_completo.groupby(['NOMPROD'])['Unidades vendidas'].sum().reset_index()
    top_10_cantidad_rot = top_10_cantidad_rot.sort_values(by=['Unidades vendidas'], ascending=False).reset_index(drop=True)

    top_10_cantidad_cb_rot = st.checkbox("Informacion Top 10 Medicamentos por Cantidad", value=False)

    if top_10_cantidad_cb_rot:
         st.dataframe(top_10_cantidad_rot)

    st.write(barplot(top_10_cantidad_rot[0:11], 'NOMPROD', 'Unidades vendidas', 'Reporte Top 10 medicamentos por Cantidad',list_Color_sequence=['yellow']))

############################################################################################################################################################
#########################-------------------------------REVISION POR REGIONALES Y FILTROS-------------------------------#########################
############################################################################################################################################################
    st.markdown ("""
    <h1 style="text-align: center;">Información discriminada por Regional</h1>
    """, unsafe_allow_html=True)

    regionales_rotacion= df_rotacion_completo.sort_values(by=['Regional Correcta'], ascending=True)
    Regional_select_rotacion = st.selectbox("Seleccione una Regional", regionales_rotacion['Regional Correcta'].unique())

    reg_select_rotacion = Regional_select_rotacion

    numer_cityes_shops_by_region_rotacion = regionales_rotacion[regionales_rotacion['Regional Correcta'] == reg_select_rotacion]

    regional_shops_rotacion =str(int(len(numer_cityes_shops_by_region_rotacion['Nombre Org Inventario'].unique())))
    ciudades_total_rotacion =str(int(len(numer_cityes_shops_by_region_rotacion['Ciudad'].unique())))


    html_str_regional_rotacion = f"""
    <style>
    p.a {{
    font: bold 16px Arial;
    }}
    </style>
    <p class="a">La regional {str(reg_select_rotacion)} tiene {regional_shops_rotacion} puntos en {ciudades_total_rotacion} ciudades</p>
    """
    st.markdown(html_str_regional_rotacion, unsafe_allow_html=True)

############################################################################################################################################################
#########################-------------------------------REVISION PINFORMACION POR CIUDADES-------------------------------#########################
############################################################################################################################################################

    allow_info_ciudad_rotacion = st.checkbox("Ver información por ciudad detallada", value=False)

    if allow_info_ciudad_rotacion:

        filter_region_rotacion = df_rotacion_completo[df_rotacion_completo['Regional Correcta'] == reg_select_rotacion]
        cities_rotacion = filter_region_rotacion.sort_values(by=['Ciudad'], ascending=True)
        cities_select_rotacion = st.selectbox("Seleccione una Ciudad", cities_rotacion['Ciudad'].unique())

        city_selectedrotacion = cities_select_rotacion

        df_filter_city_region_rotacion = filter_region_rotacion[filter_region_rotacion['Ciudad'] == city_selectedrotacion]

        top_10_costo_city_rotacion = df_filter_city_region_rotacion.groupby(['NOMPROD'])['Costo Compra'].sum().reset_index()
        top_10_costo_city_rotacion = top_10_costo_city_rotacion.sort_values(by=['Costo Compra'], ascending=True).reset_index(drop=True)
        
        city_info_shops_rotacion =str(int(len(df_filter_city_region_rotacion['Nombre Org Inventario'].unique())))
        
        html_str_reg_rotacion = f"""
        <style>
        p.a {{
        font: bold 16px Arial;
        }}
        </style>
        <p class="a">La ciudad de {str(city_selectedrotacion)} tiene {city_info_shops_rotacion} puntos </p>
        """
        st.markdown(html_str_reg_rotacion, unsafe_allow_html=True)

        top_10_costo_cb_city_rotacion = st.checkbox(f"Informacion Top 10 Medicamentos menos vendidos por menor Costo en ciudad de {city_selectedrotacion}", value=False)

        if top_10_costo_cb_city_rotacion:
            st.dataframe(top_10_costo_city_rotacion)

        st.write(barplot(top_10_costo_city_rotacion[0:11], 'NOMPROD', 'Costo Compra', f'Reporte Top 10 medicamentos por menor Costo en ciudad de {city_selectedrotacion}', list_Color_sequence=['green']))

    #####   CANTIDAD POR REGIONALES  #####
        top_10_cantidad_city_rotacion = df_filter_city_region_rotacion.groupby(['NOMPROD'])['Unidades vendidas'].sum().reset_index()
        top_10_cantidad_city_rotacion = top_10_cantidad_city_rotacion.sort_values(by=['Unidades vendidas'], ascending=True).reset_index(drop=True)

        top_10_cantidad_cb_city_rotacion = st.checkbox(f"Informacion Top 10 Medicamentos por menor cantidad en ciudad de {city_selectedrotacion}", value=False)

        if top_10_cantidad_cb_city_rotacion:
            st.dataframe(top_10_cantidad_city_rotacion)

        st.write(barplot(top_10_cantidad_city_rotacion[0:11], 'NOMPROD', 'Unidades vendidas', f'Reporte Top 10 medicamentos por menor Cantidad en ciudad de {city_selectedrotacion}', list_Color_sequence=['yellow']))

        top_10_cantidad_shop_rotacion = df_filter_city_region_rotacion.groupby(['Nombre Org Inventario'])['Unidades vendidas'].sum().reset_index()
        top_10_cantidad_shop_rotacion = top_10_cantidad_shop_rotacion.sort_values(by=['Unidades vendidas'], ascending=True).reset_index(drop=True)

        top_10_cantidad_cb_shop_rot = st.checkbox(f"Informacion Top 10 Puntos de venta por menor cantidad en ciudad de {city_selectedrotacion}", value=False)

        if top_10_cantidad_cb_shop_rot:
            st.dataframe(top_10_cantidad_shop_rotacion)

        st.write(barplot(top_10_cantidad_shop_rotacion[0:11], 'Nombre Org Inventario', 'Unidades vendidas', f'Reporte Top 10 medicamentos por menor Cantidad en los punto de venta de {city_selectedrotacion}', list_Color_sequence=['#431684']))


        allow_info_shop_rotacion = st.checkbox("Ver información por punto de venta detallada", value=False)

        if allow_info_shop_rotacion:

            shops_rotation = df_filter_city_region_rotacion.sort_values(by=['Nombre Org Inventario'], ascending=True)
            shops_select_rotation = st.selectbox(f"Seleccione un punto de venta de la ciudad de {city_selectedrotacion}", shops_rotation['Nombre Org Inventario'].unique())

            shop_selected_rotation = shops_select_rotation

            df_filter_city_region_shop_rotation = df_filter_city_region_rotacion[df_filter_city_region_rotacion['Nombre Org Inventario'] == shop_selected_rotation]

            shops_info_products_rotation =str(int(len(df_filter_city_region_rotacion['NOMPROD'].unique())))
        
            html_str_regional_rota = f"""
            <style>
            p.a {{
            font: bold 16px Arial;
            }}
            </style>
            <p class="a">La Ciudad de {city_selectedrotacion} en {str(shop_selected_rotation)} tiene {shops_info_products_rotation} productos </p>
            """
            st.markdown(html_str_regional_rota, unsafe_allow_html=True)

 
###################################################################################################################################################
#########################-------------------------------INFORMACION POR MEDICAMENTO INVENTARIO-------------------------------#########################
############################################################################################################################################################
            allow_info_product_rotacion = st.checkbox(f"Ver información por productos en el punto {shop_selected_rotation}", value=False)

            if allow_info_product_rotacion:


                st.markdown ("""
                <h1 style="text-align: center;">Información discriminada por medicamento</h1>
                """, unsafe_allow_html=True)

                names_rotacion = df_filter_city_region_shop_rotation.sort_values(by=['NOMPROD'], ascending=True)
                Medicamento_rotacion = st.selectbox("Seleccione un Medicamento", names_rotacion['NOMPROD'].unique())
                seleccionado_rotacion = Medicamento_rotacion

                if names_rotacion[names_rotacion['NOMPROD']== seleccionado_rotacion].shape[0] < 2:

                    html_str_producto_1regis_rot = f"""
                    <style>
                    p.a {{
                    font: bold 16px Arial;
                    }}
                    </style>
                    <p class="a">La Ciudad de {city_selectedrotacion} en {str(shop_selected_rotation)} tiene {shops_info_products_rotation} productos del medicamento{seleccionado} solo tiene un registro </p>
                    """
                    st.markdown(html_str_producto_1regis_rot, unsafe_allow_html=True)

                else:
                    st.markdown ("""
                    <h1 style="text-align: left;">COSTO</h1>
                    """, unsafe_allow_html=True)


                    if Medicamento_rotacion == seleccionado_rotacion:

                        filtro_medicamento_mes_rotacion = df_filter_city_region_shop_rotation[df_filter_city_region_shop_rotation['NOMPROD']== Medicamento_rotacion].groupby(['Mes','Mes Numerico','Año'])['Costo Compra'].sum().reset_index()
                        filtro_medicamento_mes_rotacion = filtro_medicamento_mes_rotacion.sort_values(by=['Año','Mes Numerico'], ascending=True).reset_index(drop=True)

                        name_medicamento_mes_rot = st.checkbox(f"Informacion del medicamento {seleccionado_rotacion} por mes-Costo", value=False)
                        if name_medicamento_mes_rot:
                            filtro_medicamento_mes_rotacion.drop(['Mes Numerico'], axis=1, inplace=True)
                            st.dataframe(filtro_medicamento_mes_rotacion)

                        st.write(lineplot(filtro_medicamento_mes_rotacion, 'Mes', 'Costo Compra', f'Reporte Regionales del medicamento {Medicamento_rotacion}',list_Color_sequence=['green']))

###################################################################################################################################################################
#######################################################################################################################################################################
############################################################ GRAFICAS DE CANTIDAD ###################################################################################################
################################################################################################################################################################
###############################################################################################################################################################
                        
                        st.markdown ("""
                        <h1 style="text-align: left;">Cantidad</h1>
                        """, unsafe_allow_html=True)

                        filtro_medicamento_mes_rot_cantidad = df_filter_city_region_shop_rotation[df_filter_city_region_shop_rotation['NOMPROD']== Medicamento_rotacion].groupby(['Mes','Mes Numerico','Año'])['Unidades vendidas'].sum().reset_index()
                        filtro_medicamento_mes_rot_cantidad = filtro_medicamento_mes_rot_cantidad.sort_values(by=['Año','Mes Numerico'], ascending=True).reset_index(drop=True)

                        name_medicamento_mes_rot_cantidad = st.checkbox(f"Informacion del medicamento {seleccionado_rotacion} por Mes-Cantidad", value=False)
                        if name_medicamento_mes_rot_cantidad:
                            filtro_medicamento_mes_rot_cantidad.drop(['Mes Numerico'], axis=1, inplace=True)
                            st.dataframe(filtro_medicamento_mes_rot_cantidad)

                        st.write(lineplot(filtro_medicamento_mes_rot_cantidad, 'Mes', 'Unidades vendidas', f'Reporte Regionales del medicamento {Medicamento_rotacion} por CANTIDAD', list_Color_sequence=['yellow']))

