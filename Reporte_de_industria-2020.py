import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

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
        margin-left: -300px;
    }
    </style>
    """,
    unsafe_allow_html=True)   
st.markdown("""<style type="text/css">
    h1{ background: #4f87f6;
    text-align: center;
    padding: 15px;
    font-family: sans-serif;
    font-size:1.60rem;
    color: white;
    position:fixed;
    width:100%;
    z-index:9999;
    top:80px;
    left:0;}
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
    .main, .css-1lcbmhc > div{margin-top:135px;}
    .css-y3whyl, .css-xqnn38 {background-color:#ccc}
    .css-1uvyptr:hover,.css-1uvyptr {background: #ccc}
    .block-container {padding-top:0;}
    h2{
    background: #fffdf7;
    text-align: center;
    padding: 10px;
    text-decoration: underline;
    text-decoration-style: double;
    color: #27348b;}
    h3{ border-bottom: 2px solid #27348b;
    border-left: 10px solid #27348b;
    background: #fffdf7;
    padding: 10px;
    color: black;}
    .imagen-flotar{float:left;}
    @media (max-width:1230px){
        .barra-superior{height:160px;} 
        .main, .css-1lcbmhc > div{margin-top:215px;}
        .imagen-flotar{float:none}
        h1{top:160px;}
    }    
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

st.sidebar.markdown("""<b>Índice</b>""", unsafe_allow_html=True)
select_seccion = st.sidebar.selectbox('Escoja la sección del reporte',
                                    ['INTRODUCCIÓN','RESUMEN EJECUTIVO','ENTORNO MACROECONÓMICO','DINÁMICA DEL SECTOR TIC','DINÁMICA DEL SECTOR POSTAL','CONCLUSIONES'])
if select_seccion == 'INTRODUCCIÓN':
    st.title("Reporte de industria 2020")
    st.image("https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria-2020/main/reporte%20de%20industria%202021.jpg")        
    st.markdown("""<div style="text-align: justify">En este reporte se destacan las tendencias 
    mundiales de los sectores TIC y Postal, así como su evolución en el país durante los últimos años. 
    Concretamente, se presenta la evolución del número de líneas, accesos y conexiones, el tráfico, 
    los ingresos y las participaciones de los operadores, entre otras variables, para los servicios TIC en Colombia, 
    considerando los efectos de las medidas de confinamiento y distanciamiento social en respuesta a la pandemia del COVID-19. 
    De igual forma, se presentan los principales indicadores de los servicios del sector Postal, entre ellos, el número de envíos, 
    los ingresos asociados, la participación de los operadores y la presencia de dichos actores en las diferentes regiones del país.</div>""",unsafe_allow_html=True)    
if select_seccion =='RESUMEN EJECUTIVO':
    st.title("Resumen ejecutivo")
    st.markdown("En el año 2020")
if select_seccion =='ENTORNO MACROECONÓMICO':
    st.title("Entorno macroeconómico")
    st.markdown("En el año 2020")
if select_seccion =='DINÁMICA DEL SECTOR TIC':
    st.title("Dinámica del sector TIC")
    st.markdown("En el año 2020")
if select_seccion =='DINÁMICA DEL SECTOR POSTAL':
    st.title("Dinámica del sector Postal")
    st.markdown("En el año 2020")    
                
if select_seccion =='CONCLUSIONES':
    st.title("Conclusiones")
    st.markdown("En el año 2020")