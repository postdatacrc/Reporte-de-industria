import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from plotly.subplots import make_subplots
import glob
import os
from urllib.request import urlopen
import json
from streamlit_folium import folium_static
from st_aggrid import AgGrid
import geopandas as gpd
import folium

LogoComision="data:image/png;base64,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"
LogoComision2="https://www.postdata.gov.co/sites/all/themes/nuboot_radix/logo-crc-blanco.png"

#API 
consulta_anno = '2017,2018,2019,2020,2021,2022,2023,2024,2025'
## INTERNET MÓVIL
    #TRAFICO 
@st.cache(allow_output_mutation=True)      
def ReadApiIMTraf():
    resourceid_cf = 'd40c5e75-db56-4ec1-a441-0314c47bd71d'
    consulta_cf='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid_cf + ''\
                '&filters[anno]=' + consulta_anno + ''\
                '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
                '&group_by=anno,trimestre,id_empresa,empresa'\
                '&sum=trafico' 
    response_base_cf = urlopen(consulta_cf + '&limit=10000000') 
    json_base_cf = json.loads(response_base_cf.read())
    IMCF_TRAF = pd.DataFrame(json_base_cf['result']['records'])
    IMCF_TRAF.sum_trafico = IMCF_TRAF.sum_trafico.astype('int64')
    resourceid_dda = 'c0be7034-29f8-4400-be54-c4aafe5df606'
    consulta_dda='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid_dda + ''\
                '&filters[anno]=' + consulta_anno + ''\
                '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
                '&group_by=anno,trimestre,id_empresa,empresa'\
                '&sum=trafico' 
    response_base_dda = urlopen(consulta_dda + '&limit=10000000') 
    json_base_dda = json.loads(response_base_dda.read())
    IMDDA_TRAF = pd.DataFrame(json_base_dda['result']['records'])
    IMDDA_TRAF.sum_trafico = IMDDA_TRAF.sum_trafico.astype('int64')
    IM_TRAF=IMDDA_TRAF.merge(IMCF_TRAF, on=['anno','trimestre','id_empresa','empresa'])
    IM_TRAF['trafico']=IM_TRAF['sum_trafico_y'].fillna(0)+IM_TRAF['sum_trafico_x']
    IM_TRAF.drop(columns=['sum_trafico_y','sum_trafico_x'], inplace=True)
    return IM_TRAF
    #INGRESOS
@st.cache(allow_output_mutation=True) 
def ReadApiIMIng():
    resourceid_cf = '8366e39c-6a14-483a-80f4-7278ceb39f88'
    consulta_cf='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid_cf + ''\
                '&filters[anno]=' + consulta_anno + ''\
                '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
                '&group_by=anno,trimestre,id_empresa,empresa'\
                '&sum=ingresos' 
    response_base_cf = urlopen(consulta_cf + '&limit=10000000') 
    json_base_cf = json.loads(response_base_cf.read())
    IMCF_ING = pd.DataFrame(json_base_cf['result']['records'])
    IMCF_ING.sum_ingresos = IMCF_ING.sum_ingresos.astype('int64')
    resourceid_dda = '60a55889-ba71-45ff-b68f-33b503da36f2'
    consulta_dda='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid_dda + ''\
                '&filters[anno]=' + consulta_anno + ''\
                '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
                '&group_by=anno,trimestre,id_empresa,empresa'\
                '&sum=ingresos' 
    response_base_dda = urlopen(consulta_dda + '&limit=10000000') 
    json_base_dda = json.loads(response_base_dda.read())
    IMDDA_ING = pd.DataFrame(json_base_dda['result']['records'])
    IMDDA_ING.sum_ingresos = IMDDA_ING.sum_ingresos.astype('int64')
    IM_ING=IMDDA_ING.merge(IMCF_ING, on=['anno','trimestre','id_empresa','empresa'])
    IM_ING['ingresos']=IM_ING['sum_ingresos_y'].fillna(0)+IM_ING['sum_ingresos_x']
    IM_ING.drop(columns=['sum_ingresos_y','sum_ingresos_x'], inplace=True)
    return IM_ING
    #ACCESOS
@st.cache(allow_output_mutation=True) 
def ReadApiIMAccesos():
    resourceid_cf = '47d07e20-b257-4aaf-9309-1501c75a826c'
    consulta_cf='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid_cf + ''\
                '&filters[anno]=' + consulta_anno + ''\
                '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
                '&group_by=anno,trimestre,id_empresa,empresa'\
                '&sum=cantidad_suscriptores' 
    response_base_cf = urlopen(consulta_cf + '&limit=10000000') 
    json_base_cf = json.loads(response_base_cf.read())
    IMCF_SUS = pd.DataFrame(json_base_cf['result']['records'])
    IMCF_SUS.sum_cantidad_suscriptores = IMCF_SUS.sum_cantidad_suscriptores.astype('int64')
    resourceid_dda = '3df620f6-deec-42a0-a6af-44ca23c2b73c'
    consulta_dda='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid_dda + ''\
                '&filters[anno]=' + consulta_anno + ''\
                '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
                '&group_by=anno,trimestre,id_empresa,empresa'\
                '&sum=cantidad_abonados' 
    response_base_dda = urlopen(consulta_dda + '&limit=10000000') 
    json_base_dda = json.loads(response_base_dda.read())
    IMDDA_ABO = pd.DataFrame(json_base_dda['result']['records'])
    IMDDA_ABO.sum_cantidad_abonados = IMDDA_ABO.sum_cantidad_abonados.astype('int64')
    IM_ACCESOS=IMDDA_ABO.merge(IMCF_SUS, on=['anno','trimestre','id_empresa','empresa'])
    IM_ACCESOS['accesos']=IM_ACCESOS['sum_cantidad_suscriptores'].fillna(0)+IM_ACCESOS['sum_cantidad_abonados']
    IM_ACCESOS.drop(columns=['sum_cantidad_suscriptores','sum_cantidad_abonados'], inplace=True)
    return IM_ACCESOS

def PColoresEmpINTMovil(id_empresa):
    if id_empresa == '800153993':
        return 'red'
    if id_empresa == '800153993':
        return 'red'
    else:
        pass    

def Plotlylineatiempo(df,column):
    empresasdf=df['id_empresa'].unique().tolist()
    fig = make_subplots(rows=1, cols=1)
    for elem in empresasdf:
        fig.add_trace(go.Scatter(x=df[df['id_empresa']==elem]['periodo'],
        y=df[df['id_empresa']==elem][column],text=df[df['id_empresa']==elem]['empresa'],
        mode='lines+markers',line = dict(width=0.8,color=PColoresEmpINTMovil(elem)),name='',hovertemplate =
        '<br><b>Empresa</b>:<br>'+'%{text}'+
        '<br><b>Periodo</b>: %{x}<br>'+                         
        column+': %{y:.4f}<br>'))   
    fig.update_xaxes(tickangle=0, tickfont=dict(family='Helvetica', color='black', size=12),title_text=None,row=1, col=1)
    fig.update_yaxes(tickfont=dict(family='Helvetica', color='black', size=14),titlefont_size=14, title_text=column, row=1, col=1)
    fig.update_layout(height=550,title=column.capitalize() +" por periodo y por empresa",title_x=0.5,legend_title=None,font=dict(family="Helvetica",color=" black"))
    fig.update_layout(showlegend=False,paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    fig.update_xaxes(tickangle=-90,showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.4)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.4)')
    return fig


st.set_page_config(
    page_title="Reporte de industria 2020", page_icon=LogoComision,layout="wide",initial_sidebar_state="expanded")

page_bg_img = '''
<style>
body {
background-image: url("https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria-2020/main/reporte%20de%20industria%202021.jpg");
background-size: cover;
}
</style>
'''
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 300px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 300px;
        top:100px;
        margin-left: -300px;
    }
    </style>
    """,
    unsafe_allow_html=True)   
st.markdown("""<style type="text/css">
    h1{ background: #b560f3;
        text-align: center;
        padding: 15px;
        font-family: sans-serif;
        font-size:1.60rem;
        color: white;
        position:fixed;
        width:100%;
        z-index:9999999;
        top:80px;
        left:0;
    }
    .barra-superior{top: 0;
        position: fixed;
        background-color: #7a44f2;
        width: 100%;
        color:white;
        z-index: 999;
        height: 80px;
        left: 0px;
        text-align: center;
        padding: 0px;
        font-size: 36px;
        font-weight: 700;
    }
    .main, .css-1k0ckh2 > div{
        margin-top:135px;
    }
    .e16nr0p31 {display:none}
    .css-y3whyl, .css-xqnn38 {background-color:#ccc}
    .e8zbici0 {display:none}
    .e8zbici2 {display:none}
    .css-1uvyptr:hover,.css-1uvyptr {background: #ccc}
    .e1fqkh3o2{
        padding-top:2.5rem;   
    }
    .css-52bwht{
        gap:0.01rem;
    }
    .block-container {padding-top:0;}
    h2{
        background: #fffdf7;
        text-align: center;
        padding: 10px;
        text-decoration: underline;
        text-decoration-style: double;
        color: #27348b;
    }    
    header {
      background: #fffdf7;
      display: flex;
      color: #4c83f3;
      font-size:25px;
      padding:10px;
    }
    header:before,
    header:after {
      content: '';
      margin: auto 1em;
      border-bottom: solid 3px;
      flex: 1;
    }   
    .e1tzin5v0{
      text-align:center;  
    }
    .edgvbvh9:hover {
      color:rgb(255,255,255);
      border-color:rgb(255,75,75);
    }
    .edgvbvh9 {
      font-weight: 600;
      background-color: rgb(122, 68, 242);
      border: 2px solid rgba(0, 0, 0, 1); 
      color:white;
      padding: 0.6rem 0.6rem;
      font-size: 18px;
    }
    .imagen-flotar{float:left;}
    @media (max-width:1230px){
        .barra-superior{height:160px;} 
        .main, .css-1k0ckh2 > div{margin-top:215px;}
        .imagen-flotar{float:none}
        h1{top:160px;}}       
    </style>""", unsafe_allow_html=True)  
st.markdown("""
<div class="barra-superior">
    <div class="imagen-flotar" style="height: 70px; left: 10px; padding:15px">
        <a class="imagen-flotar" style="float:left;" href="https://www.crcom.gov.co" title="CRC">
            <img src="https://www.postdata.gov.co/sites/all/themes/nuboot_radix/logo-crc-blanco.png" alt="CRC" style="height:40px">
        </a>
        <a class="imagen-flotar" style="padding-left:10px;" href="https://www.postdata.gov.co" title="Postdata">
            <img src="https://www.postdata.gov.co/sites/default/files/postdata-logo.png" alt="Inicio" style="height:40px">
        </a>
    </div>
</div>""",unsafe_allow_html=True)



st.markdown(page_bg_img, unsafe_allow_html=True)
st.sidebar.markdown(r"""<b style="font-size: 26px"> Reporte de industria CRC </b> """,unsafe_allow_html=True)
st.sidebar.markdown(r"""<hr>""",unsafe_allow_html=True)
st.sidebar.markdown("""<b>Índice</b>""", unsafe_allow_html=True)
select_seccion = st.sidebar.selectbox('Escoja la sección del reporte',
                                    ['Resumen ejecutivo','Dinámica telecomunicaciones','Dinámica postal'])
       
if select_seccion =='Resumen ejecutivo':
    st.title("Resumen ejecutivo")
    
    
if select_seccion =='Dinámica telecomunicaciones':
    st.title("Dinámica del sector de telecomunicaciones")
    select_secResumenDinTic = st.sidebar.selectbox('Seleccione el el sector a consultar',['Información general',
    'Servicios móviles','Servicios fijos','Contenidos audiovisuales','Radio'])
    if select_secResumenDinTic == 'Información general':
        st.markdown(r"""<header><h3>Información general</h3></header>""",unsafe_allow_html=True)
        st.write("")
        col1, col2, = st.columns([4,6])
        with col1:
            st.markdown(r"""<div style="text-align: justify">
Durante 2020, los ingresos del sector TIC por
la prestación de servicios fijos, móviles y de
televisión abierta radiodifundida ascendió
a $22,1 billones. El 33,9% de los ingresos fue
generado en la prestación del servicio de
Internet móvil, seguido del 24,3% de Internet fijo y el
14,8% en televisión por suscripción. Con respecto a
2019, el sector presentó un crecimiento nominal de
2,2% y de 1,6% en términos constantes.
<br>
<br>
En el año 2020, 5 operadores (Claro, Telefónica, Tigo,
DirecTV y ETB) concentraron el 86,0% de los ingresos
del sector. En el servicio de Telefonía fija, entre 2019
y 2020 resaltan los incrementos en la participación
de Claro y de ETB de 4,7 y 0,6 puntos porcentuales
(pp). En Internet fijo, Claro aumentó su participación
en 1,3 pp alcanzando en 2020 el 28,7% de los ingresos
asociados a este servicio, así como la agrupación “otros” que aumnetó 1,3%.
<br>
<br>
En tanto, en la prestación de televisión por suscripción
Claro aumentó su participación, pasando de 37,7% en
2019 a 40% en 2020.</div>
        """,unsafe_allow_html=True)
        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")            
            st.image("https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria-2020/main/.DINAMICASECTORTIC/DinamicaIndustriaTic.PNG")   
        st.image("https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria-2020/main/.DINAMICASECTORTIC/EvolucionPartServOp.PNG")    
        st.image("https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria-2020/main/.DINAMICASECTORTIC/EvolucionPartNusuarios.PNG")
    if select_secResumenDinTic == 'Servicios móviles':
        st.markdown(r"""<header><h3>Servicios móviles</h3></header>""",unsafe_allow_html=True)
        st.markdown("Para continuar, por favor seleccione el botón con el servicio del cual desea conocer la información")

        col1,col2,col3 = st.columns(3)
        with col1:
            BotonTelMovil=st.button("Telefonía móvil")
            st.image("https://github.com/postdatacrc/Reporte-de-industria/blob/main/Iconos/VozTelMovil.jpg?raw=true",width=100)
         
        with col2:
            BotonIntMovil=st.button("Internet móvil")
            st.image("https://github.com/postdatacrc/Reporte-de-industria/blob/main/Iconos/InternetTelMovil.jpg?raw=true",width=100)
        with col3:
            BotonSMSMovil=st.button("Mensajería móvil")
            st.image("https://github.com/postdatacrc/Reporte-de-industria/blob/main/Iconos/SMSTelMovil.jpg?raw=true",width=170)
         
        st.markdown(r"""<header><h3> </h3></header>""",unsafe_allow_html=True) 
        #select_subsectSerMov=st.radio("Subsección",['Telefonía móvil','Mensajería','Internet móvil'],horizontal=True)

        if BotonIntMovil:
            st.markdown(r"""<center><h4>Internet móvil</h4></center>""",unsafe_allow_html=True)        
            Trafico=ReadApiIMTraf()
            Ingresos=ReadApiIMIng()
            Accesos=ReadApiIMAccesos()

            Trafico=Trafico[Trafico['trafico']>0]
            Ingresos=Ingresos[Ingresos['ingresos']>0]
            Accesos=Accesos[Accesos['accesos']>0]
            Trafico.insert(0,'periodo',Trafico['anno']+'-T'+Trafico['trimestre'])
            Ingresos.insert(0,'periodo',Ingresos['anno']+'-T'+Ingresos['trimestre'])
            Accesos.insert(0,'periodo',Accesos['anno']+'-T'+Accesos['trimestre'])   
            
            ServiciosIntMovil=st.selectbox('Escoja el servicio',['Accesos','Tráfico','Ingresos'])
                            
            if ServiciosIntMovil=='Accesos':
                Accnac=Accesos.groupby(['periodo','empresa','id_empresa'])['accesos'].sum().reset_index()              
                st.plotly_chart(Plotlylineatiempo(Accnac,'accesos'), use_container_width=True)
                AgGrid(Accnac)
            if ServiciosIntMovil=='Tráfico':
                Trafnac=Trafico.groupby(['periodo','empresa','id_empresa'])['trafico'].sum().reset_index()              
                st.plotly_chart(Plotlylineatiempo(Trafnac,'trafico'), use_container_width=True)
                AgGrid(Trafnac)
            if ServiciosIntMovil=='Ingresos':
                Ingnac=Ingresos.groupby(['periodo','empresa','id_empresa'])['ingresos'].sum().reset_index()              
                st.plotly_chart(Plotlylineatiempo(Ingnac,'ingresos'), use_container_width=True)
                AgGrid(Ingnac)    
        
if select_seccion =='Dinámica postal':
    st.title("Dinámica del sector Postal")
    st.markdown("En el año 2020")    
                

