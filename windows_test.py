# importing libraries
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
# from PySide import QtGui
from datetime import datetime
import hashlib
import sys

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import locale
locale.setlocale(locale.LC_ALL, ("es_ES", "UTF-8"))
  


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
  
        # setting title
        self.setWindowTitle("Aplicación para unificar archivos")
        # self.setStyleSheet("background-color: lead;")
        self.setStyleSheet('background-color: #050A2C;')
        self.w = None
        # setting geometry
        self.setGeometry(0, 0, 1200, 1000)

        # self.resize(pixmap.width(), pixmap.height())
  
        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.showMaximized()
  
    # method for widgets
    def UiComponents(self):
        
        # creating a label
        label = QLabel('Aplicación para unificar  \n archivos', self)
        label.setStyleSheet('color: #FFFFFF;')
        label.move(250, 100)
        label.resize(750, 300)
        label.setFont(QFont('Arial', 50))
        label.setAlignment(Qt.AlignCenter)


        # creating a push button
        button1 = QPushButton("Docs Cruz Verde", self)
        button1.setStyleSheet("background-color: #050A2C;"
                            "color: #939395;" 
                            "font-size: 16px;" 
                            "font-weight: bold;" 
                            "border :2px solid;" 
                            "border-top-color : #939395;"
                            "border-left-color : #939395;"
                            "border-right-color : #939395;"
                            "border-bottom-color : #939395;"
                            )
        button1.move(500, 500)
        button1.resize(300, 100)

        # adding action to a button
        button1.clicked.connect(self.clickme1)


    def load_files(self):
            ### Carga de datos correspondientes al inventario del 2021
            Inventario_data1 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Inventario_CruzVerde_800093391_Consumo_Farma_A_202101.xlsx"
            )
            Inventario_data2 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Inventario_CruzVerde_800093391_Consumo_Farma_A_202102.xlsx"
            )
            Inventario_data3 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Inventario_CruzVerde_800093391_Consumo_Farma_A_202103.xlsx"
            )
            Inventario_data4 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Inventario_CruzVerde_800093391_Consumo_Farma_A_202104.xlsx"
            )
            Inventario_data5 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Inventario_CruzVerde_800093391_Consumo_Farma_A_202105.xlsx"
            )
            Inventario_data6 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Inventario_CruzVerde_800093391_Consumo_Farma_A_202106.xlsx"
            )
            Inventario_data7 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Inventario_CruzVerde_800093391_Consumo_Farma_A_202107.xlsx"
            )
            Inventario_data8 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Inventario_CruzVerde_800093391_Consumo_Farma_A_202108.xlsx"
            )
            Inventario_data9 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Inventario_CruzVerde_800093391_Consumo_Farma_A_202109.xlsx"
            )
            Inventario_data10 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Inventario_CruzVerde_800093391_Consumo_Farma_A_202110.xlsx"
            )
            Inventario_data11 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Inventario_CruzVerde_800093391_Consumo_Farma_A_202111.xlsx"
            )
            Inventario_data12 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Inventario_CruzVerde_800093391_Consumo_Farma_A_202112.xlsx"
            )

            ##### Carga de datos correspondientes a la rotación del 2021
            rotacion_data1 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Rotacion_CruzVerde_800093391_Consumo_Farma_A_202101.xlsx"
            )
            rotacion_data2 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Rotacion_CruzVerde_800093391_Consumo_Farma_A_202102.xlsx"
            )
            rotacion_data3 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Rotacion_CruzVerde_800093391_Consumo_Farma_A_202103.xlsx"
            )
            rotacion_data4 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Rotacion_CruzVerde_800093391_Consumo_Farma_A_202104.xlsx"
            )
            rotacion_data5 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Rotacion_CruzVerde_800093391_Consumo_Farma_A_202105.xlsx"
            )
            rotacion_data6 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Rotacion_CruzVerde_800093391_Consumo_Farma_A_202106.xlsx"
            )
            rotacion_data7 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Rotacion_CruzVerde_800093391_Consumo_Farma_A_202107.xlsx"
            )
            rotacion_data8 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Rotacion_CruzVerde_800093391_Consumo_Farma_A_202108.xlsx"
            )
            rotacion_data9 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Rotacion_CruzVerde_800093391_Consumo_Farma_A_202109.xlsx"
            )
            rotacion_data10 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Rotacion_CruzVerde_800093391_Consumo_Farma_A_202110.xlsx"
            )
            rotacion_data11 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Rotacion_CruzVerde_800093391_Consumo_Farma_A_202111.xlsx"
            )
            rotacion_data12 = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Data Original\Rotacion_CruzVerde_800093391_Consumo_Farma_A_202112.xlsx"
            )

            ####### Carga del portafolio de productos
            portafolio = pd.read_excel(
                r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Portafolio Novamed.xlsx"
            )

            return (
                Inventario_data1,
                Inventario_data2,
                Inventario_data3,
                Inventario_data4,
                Inventario_data5,
                Inventario_data6,
                Inventario_data7,
                Inventario_data8,
                Inventario_data9,
                Inventario_data10,
                Inventario_data11,
                Inventario_data12,
                rotacion_data1,
                rotacion_data2,
                rotacion_data3,
                rotacion_data4,
                rotacion_data5,
                rotacion_data6,
                rotacion_data7,
                rotacion_data8,
                rotacion_data9,
                rotacion_data10,
                rotacion_data11,
                rotacion_data12,
                portafolio,
            )

####### FUNCION PARA GARANTIZAR EL MISMO TAMAÑO EN TODOS LOS ARCHIVOS DE INVENTARIOS
    def same_shape_inventario(self,df):
        order_columns = ['FECHA', 'DIVISION', 'CODIGO ORGANIZACION', 'ORGANIZACION', 'Regional', 'Ciudad', 'Direccion', 'nit_proveedor', 'nombre_proveedor', 'ARTICULO',
        'EAN', 'DESCRIPCION', 'FACTOR', 'UDM', 'CANTIDAD ARTICULO', 'COSTO TOTAL ARTICULO']
        if len(df.columns) < 16:
            Columns = df.columns
            for name in Columns:
                separate_name = name.split(' ')
                if separate_name[0] == 'Unnamed:':
                    df.drop(name, axis=1, inplace=True)
            new_columns = df.columns
            for exist_column in range(len(order_columns)):
                if order_columns[exist_column] in new_columns:
                    pass
                else:
                    df[order_columns[exist_column]] = 'NO ASIGNADO'

        Output = df.reindex(columns=order_columns)
        return Output

### fUNCION PARA UNIFORMAR LAS REGIONES Y DEJAR UN SOLO NOMBRE 
    def uniform_regions(self,df, Nombre_Columna_con_Regiones):
        uniform_regions = []
        for reg in range(len(df[Nombre_Columna_con_Regiones])):
            if df[Nombre_Columna_con_Regiones][reg] == 'Bogota':
                uniform_regions.append('Bogota D.C.')
            elif df[Nombre_Columna_con_Regiones][reg] == 'Cali':
                uniform_regions.append('Cali')
            elif df[Nombre_Columna_con_Regiones][reg] == 'Costa':
                uniform_regions.append('Costa')
            elif df[Nombre_Columna_con_Regiones][reg] == 'Medellin':
                uniform_regions.append('Medellin')
            elif df[Nombre_Columna_con_Regiones][reg] == 'Bucaramanga':
                uniform_regions.append('Bucaramanga')
            elif df[Nombre_Columna_con_Regiones][reg] == 'Bogotá D.C.':
                uniform_regions.append('Bogota D.C.')
            elif df[Nombre_Columna_con_Regiones][reg] == 'Antioquia':
                uniform_regions.append('Antioquia')
            elif df[Nombre_Columna_con_Regiones][reg] == 'Santander':
                uniform_regions.append('Santander')
            elif df[Nombre_Columna_con_Regiones][reg] == 'Valle':
                uniform_regions.append('Valle')
            elif df[Nombre_Columna_con_Regiones][reg] == 'Eje Cafetero':
                uniform_regions.append('Eje Cafetero')
            elif df[Nombre_Columna_con_Regiones][reg] == 'Centro Oriente':
                uniform_regions.append('Centro Oriente')
            elif df[Nombre_Columna_con_Regiones][reg] == 'Tolima - Huila':
                uniform_regions.append('Tolima - Huila')
            else:
                uniform_regions.append(df['Regional'][reg])
        df['Regional Correcta'] = uniform_regions
        return df

###### FUNCION PARA EXTRAER EL NUMERO Y MES POR FECHAINDICADA 
    def EXTRAER_MES(self,df,columna_fecha,columna_precio):
        """
        Función que permite obtener el mes de una dataframe
        """
        columns = df.columns
        date = []
        numeric_month = []
        s = df[columna_fecha]
        for i in range(len(s)):
            transform_date = len(str(s[i]))
            # print(transform_date)
            if transform_date == 19:
                # date.append(s[i])
                temp = str(s[i])
                x = datetime(year=int(temp[0:4]), month=int(temp[8:10]), day=1)
                if int(x.strftime("%Y")) > 2021:
                    numeric_month.append(int(x.strftime("%m"))+12)
                    month = x.strftime("%B"+" "+"%Y")
                    date.append(month)
                else:
                    numeric_month.append(int(x.strftime("%m")))
                    month = x.strftime("%B")
                    date.append(month)
            elif transform_date == 26:
                temp = str(s[i])
                x = datetime(year=int(temp[0:4]), month=int(temp[8:10]), day=1)
                if int(x.strftime("%Y")) > 2021:
                    numeric_month.append(int(x.strftime("%m"))+12)
                    month = x.strftime("%B"+" "+"%Y")
                    date.append(month)
                else:
                    numeric_month.append(int(x.strftime("%m")))
                    month = x.strftime("%B")
                    date.append(month)
            elif transform_date == 'NO ASIGNADO':
                date.append(s[i])
                numeric_month.append(20)
            else:
                # date.append(s[i])
                temp = str(s[i])
                x = datetime(year=int(temp[0:4]), month=int(temp[4:6]), day=1)
                numeric_month.append(int(x.strftime("%m")))
                month = x.strftime("%B")
                date.append(month)


        df['Mes Numerico'] = numeric_month
        # corregir_precios = []
        # for entero in df[columna_precio]:
        #     corregir_precios.append(int(entero))

        # df['Precio en Entero'] = corregir_precios

        if 'Mes' in columns:
            df['MONTH'] = date
            x = df.groupby(['MONTH','Mes Numerico'])[columna_precio].sum().reset_index()
            final = x.sort_values('Mes Numerico', ascending=True).reset_index(drop=True).drop(columns=['Mes Numerico'])
        else:
            df['Mes'] = date
            x = df.groupby(['Mes','Mes Numerico'])[columna_precio].sum().reset_index()
            final = x.sort_values('Mes Numerico', ascending=True).reset_index(drop=True).drop(columns=['Mes Numerico'])
        return final, df

###### FUNCION PARA OBTENER LA INFORMACION QUE NO SE ENCUENTRA EN EL PORTAFOLIO
    def not_in_portafolio(self,df_portafolio, df_total_rotation_data,columna_codigo_barras,nombre_producto):
        x = df_total_rotation_data[columna_codigo_barras].unique() 
        y = df_portafolio[columna_codigo_barras].unique()
        not_in_portafolio = []
        for i in range(len(x)):
            if x[i] not in y:
                not_in_portafolio.append(x[i])

        cod_barras_name = df_total_rotation_data[df_total_rotation_data[columna_codigo_barras].isin(not_in_portafolio)]
        not_be = pd.DataFrame({'Codigo de barras':cod_barras_name[columna_codigo_barras],'Descripción Producto':cod_barras_name[nombre_producto]}).reset_index(drop=True)

        output = not_be.groupby('Codigo de barras')['Descripción Producto'].unique()
        # output.to_csv(r'C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Not_in_portafolio.csv')
        return output

###FUNCION PARA VER COMO ES EL COMPORTAMIENTO MES A MES DE LAS REGIONES
    def report_regional_months(self,df,header_region, header_month,header_number_month,cost):
        regional_behaviour = df.groupby([header_region, header_month,header_number_month])[cost].sum().reset_index()
        Regionales = regional_behaviour[header_region].unique()
        # print(Regionales)

        for region in range(len(Regionales)):
            if region == 0:
                temp = regional_behaviour[regional_behaviour[header_region] == Regionales[region]]
                temp = temp.sort_values(header_number_month, ascending=True).reset_index(drop=True)
                # print(temp)
            else:
                temp1 = regional_behaviour[regional_behaviour[header_region] == Regionales[region]]
                temp1 = temp1.sort_values(header_number_month, ascending=True).reset_index(drop=True)
                if region == 1:
                    temp = pd.concat([temp,temp1])
                else:
                    temp = pd.concat([temp,temp1])
        return temp
  
    # action method
    def clickme1(self):
        ##### ASIGNAR LOS DATOS A VARIABLES
        ( Inventario_data1, Inventario_data2, Inventario_data3, Inventario_data4, Inventario_data5, Inventario_data6, Inventario_data7, Inventario_data8,
            Inventario_data9, Inventario_data10, Inventario_data11, Inventario_data12,
            rotacion_data1, rotacion_data2, rotacion_data3, rotacion_data4, rotacion_data5, rotacion_data6, rotacion_data7, rotacion_data8,rotacion_data9,
            rotacion_data10, rotacion_data11, rotacion_data12,
            portafolio,
        ) = self.load_files()


        ####CONCATENAR TODOS LOS ARCHIVOS DE ROTACION PARA TENER AL FINAL UNO SOLO CON TODOS LOS DATOS
        rotation_data = pd.concat(
            [rotacion_data1, rotacion_data2, rotacion_data3, rotacion_data4, rotacion_data5, rotacion_data6, rotacion_data7, rotacion_data8,
                rotacion_data9, rotacion_data10, rotacion_data11, rotacion_data12]
        ).reset_index(drop=True)

        rotation_data.to_csv(r'C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\rotacion_Unificado_2021.csv')
        ####------------------------------------PROCESO PARA INFORMA DE INVENTARIO----------------------------------------####

        Inventario_data1 = self.same_shape_inventario(Inventario_data1)
        Inventario_data2 = self.same_shape_inventario(Inventario_data2)
        Inventario_data3 = self.same_shape_inventario(Inventario_data3)
        Inventario_data4 = self.same_shape_inventario(Inventario_data4)
        Inventario_data5 = self.same_shape_inventario(Inventario_data5)
        Inventario_data6 = self.same_shape_inventario(Inventario_data6)
        Inventario_data7 = self.same_shape_inventario(Inventario_data7)
        Inventario_data8 = self.same_shape_inventario(Inventario_data8)
        Inventario_data9 = self.same_shape_inventario(Inventario_data9)
        Inventario_data10 = self.same_shape_inventario(Inventario_data10)
        Inventario_data11 = self.same_shape_inventario(Inventario_data11)
        Inventario_data12 = self.same_shape_inventario(Inventario_data12)

        Inventario_data = pd.concat([Inventario_data1, Inventario_data2, Inventario_data3, Inventario_data4, Inventario_data5, Inventario_data6, Inventario_data7, Inventario_data8,
                                        Inventario_data9, Inventario_data10, Inventario_data11, Inventario_data12]).reset_index(drop=True)

        Inventario_data.to_csv(r'C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Inventario_Unificado_2021.csv')

        #-----------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------
        ####-------------------------------------PROCESO PARA INFORMACION DE INVENTARIO-------------------------------------####
        #-----------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------

        ################################### UNIFORMACIÓN DE DATOS PARA INVENTARIO #############################################
        Uniform_Names_Inventario = self.uniform_regions(Inventario_data,'Regional')

        ##################################### REPORTE Y ORDEN POR MES EN INVENTARIO 
        month_inform_inventario, general_df_inventrio = self.EXTRAER_MES(Uniform_Names_Inventario,'FECHA','COSTO TOTAL ARTICULO')
        month_inform_inventario.to_csv(r'C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Reporte_Mes_Inventario.csv')

        ###########UNIFICAR DF CON EL PORTAFOLIO
        portafolio['EAN'] = portafolio['COD_EAN13']
        merge_df_inventario = pd.merge(general_df_inventrio, portafolio, on='EAN', how='left')
        merge_df_inventario.to_csv(r'C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Reporte_Merge_Inventario_Portafolio.csv')

        ############ PRODUCTOS QUE SE ENCUENTRAN EN EL LISTADO DE INVENTARIO PERO NO EN EL PORTAFOLIO
        not_portafolio_inventario = self.not_in_portafolio(portafolio, merge_df_inventario,'EAN','DESCRIPCION')
        not_portafolio_inventario.to_csv(r'C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Inventario_No_in_portafolio.csv')

        #### DIFERENTES REPORTES DE INVENTARIO
        Regional_report_total_Inventario = general_df_inventrio.groupby(general_df_inventrio['Regional Correcta'])['COSTO TOTAL ARTICULO'].sum().reset_index()
        Regional_report_total_Inventario.to_csv(r'C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Reporte_Regional_Inventario.csv')

        ############# REPORTE MES A MES DE CADA UNA DE LAS REGIONALES #######################################################################
        df_report_months_inventario = self.report_regional_months(merge_df_inventario,'Regional Correcta','Mes','Mes Numerico', 'COSTO TOTAL ARTICULO')
        df_report_months_inventario.to_csv(r'C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Reporte_Mes_Regionales_Inventario.csv')

        #-----------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------
        ####-------------------------------------PROCESO PARA INFORMACION DE ROTACION-------------------------------------####
        #-----------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------
        Uniform_Names = self.uniform_regions(rotation_data,'Regional')

        ######## ORDENAR POR MES 
        month_inform, general_df_rotation = self.EXTRAER_MES(Uniform_Names,'Periodo','Costo Compra')
        month_inform.to_csv(r"C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Reporte_Mes_Rotacion.csv")
        # print(month_inform)

        #### UNIFICAR ARCHIVO DE ROTACION CON PORTAFOLIO
        portafolio['Código de Barras'] = portafolio['COD_EAN13']
        merge_df_rotacion = pd.merge(general_df_rotation, portafolio, on='Código de Barras', how='left')
        merge_df_rotacion.to_csv(r'C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Reporte_Merge_Rotacion_Portafolio.csv')


        ## GUARDAR ARCHIVO PARA SABER QUE NO SE ENCUENTRA EN EL DF DE ROTACION
        not_portafolio_rotacion = self.not_in_portafolio(portafolio, general_df_rotation,'Código de Barras','Descripción Producto')
        not_portafolio_rotacion.to_csv(r'C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Rotation_No_in_portafolio.csv')
        #### DIFERENTES REPORTES DE ROTACION
        Regional_report_total_Rotacion = general_df_rotation.groupby(general_df_rotation['Regional Correcta'])['Costo Compra'].sum().reset_index()
        Regional_report_total_Rotacion.to_csv(r'C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Reporte_Regional_Rotacion.csv')
        # print(Regional_report_total)

        ############# REPORTE MES A MES DE CADA UNA DE LAS REGIONALES #######################################################################
        df_report_months_rotation = self.report_regional_months(general_df_rotation,'Regional Correcta','Mes','Mes Numerico', 'Costo Compra')
        df_report_months_rotation.to_csv(r'C:\Users\fcoy\Documents\Personal Docs\Farma\Medical_Data\Data\Reporte_Mes_Regionales_Rotacion.csv')

        #################REPORTE POR LINEA DE PRODUCTO #####################################################################################
        correct_line = []
        for line in range(len(merge_df_rotacion['LINEA'])):
            if type(merge_df_rotacion['LINEA'][line]) != str:
                correct_line.append('NO ASIGNADO')
            else: 
                correct_line.append(merge_df_rotacion['LINEA'][line]) 
        merge_df_rotacion['LINEA DE PRODUCTO'] = correct_line
        Resumen_Linea_Producto = merge_df_rotacion.groupby(['LINEA DE PRODUCTO'])['Costo Compra'].sum().reset_index()

        self.close()
        if self.w is None:
            self.w = Validacion(True)
            self.w.show()

  
class Validacion(QWidget):
    def __init__(self,User_Register):
        super().__init__()
        self.User_Register = User_Register

        # setting title
        self.setWindowTitle("Validación")
        self.setStyleSheet('background-color: #0C0C24;')
        self.w = None
        # setting geometry
        self.setGeometry(0, 0, 1200, 800)

        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.showMaximized()
  
    # method for widgets
    def UiComponents(self):
  
        # creating a push button
        label = QLabel('Archivos  \n Creados', self)
        label.setStyleSheet('color: #FFFFFF;')
        label.move(250, 100)
        label.resize(750, 300)
        label.setFont(QFont('Arial', 50))
        label.setAlignment(Qt.AlignCenter)

        button1 = QPushButton("Volver", self)
        button1.setStyleSheet("background-color: #050A2C;"
                            "color: #939395;" 
                            "font-size: 16px;" 
                            "font-weight: bold;" 
                            "border :2px solid;" 
                            "border-top-color : #939395;"
                            "border-left-color : #939395;"
                            "border-right-color : #939395;"
                            "border-bottom-color : #939395;"
                            )
        button1.move(500, 500)
        button1.resize(300, 100)

        # adding action to a button
        button1.clicked.connect(self.clickme1)

    def clickme1(self):
        self.close()
        if self.w is None:
            self.w = MainWindow(True)
            self.w.show()

# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = MainWindow()
  
# start the app
sys.exit(App.exec())