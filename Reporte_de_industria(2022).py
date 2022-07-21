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


def PColoresEmpINTMovil(id_empresa):
    if id_empresa == '800153993':
        return 'red'
    elif id_empresa == '830114921':
        return 'rgb(0,102,204)'
    elif id_empresa == '830122566':
        return 'rgb(102,204,0)'
    elif id_empresa=='899999115':
        return 'rgb(0,204,204)'
    else:
        pass    

def Plotlylineatiempo(df,column):
    empresasdf=df['id_empresa'].unique().tolist()
    fig = make_subplots(rows=1, cols=1)
    for elem in empresasdf:
        fig.add_trace(go.Scatter(x=df[df['id_empresa']==elem]['periodo'],
        y=df[df['id_empresa']==elem][column],text=df[df['id_empresa']==elem]['empresa'],
        mode='lines+markers',line = dict(width=0.8,color=PColoresEmpINTMovil(elem)),name=df[df['id_empresa']==elem]['empresa'].unique().tolist()[0],hovertemplate =
        '<br><b>Empresa</b>:<br><extra></extra>'+'%{text}'+
        '<br><b>Periodo</b>: %{x}<br>'+                         
        column+': %{y:.0f}<br>'))   
    fig.update_xaxes(tickangle=-90, tickfont=dict(family='Boston', color='black', size=16),title_text=None,row=1, col=1,ticks="outside", tickwidth=1, tickcolor='black', ticklen=5,
    zeroline=True,linecolor = "#000000",zerolinewidth=2,  # Sets color of X-axis line
    showgrid = True, 
    showline = True,
    gridwidth=1,       
    gridcolor='lightpink',
    showticklabels=True)
    fig.update_yaxes(tickfont=dict(family='Boston', color='black', size=16),titlefont_size=18, title_text=column, row=1, col=1,ticks="outside", tickwidth=1, tickcolor='black', ticklen=5,
    zeroline=True,linecolor = "#000000",zerolinewidth=2,  # Sets color of X-axis line
    showgrid = True, 
    showline = True,
    gridwidth=1,       
    gridcolor='lightpink',
    showticklabels=True)
    fig.update_layout(height=550,legend_title=None)
    fig.update_layout(font_color="Black",title_font_family="NexaBlack",title_font_color="Black",titlefont_size=20,
    title={
    'text': column.capitalize() +" por periodo y por empresa",
    'y':0.95,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})        
    fig.update_layout(legend=dict(orientation="h",y=1.1,x=0.02),showlegend=True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.4)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.4)')
    return fig

def PlotlyBarras(df,column):   
    fig = make_subplots(rows=1, cols=1) 
    for empresa in df['empresa'].unique().tolist():
        fig.add_trace(go.Bar(x=df[df['empresa']==empresa]['anno'].values.tolist(),y=df[df['empresa']==empresa][column].values.tolist()
                             ,marker_color=PColoresEmpINTMovil(df[df['empresa']==empresa]['id_empresa'].unique()[0]),
                            name=empresa,hovertemplate='<br><b>Empresa</b>:<br><extra></extra>'+empresa+'<br>'+                       
        column+': %{y:.0f}<br>'))
    fig.update_layout(barmode='group')
    fig.update_xaxes(tickangle=0, tickfont=dict(family='Boston', color='black', size=16),title_text=None,row=1, col=1,ticks="outside", tickwidth=1, tickcolor='black', ticklen=5,
    zeroline=True,linecolor = "#000000",zerolinewidth=2,  # Sets color of X-axis line
    showgrid = True, 
    showline = True,
    gridwidth=1,       
    gridcolor='lightpink',
    showticklabels=True)
    fig.update_yaxes(tickfont=dict(family='Boston', color='black', size=16),titlefont_size=18, title_text=column, row=1, col=1,ticks="outside", tickwidth=1, tickcolor='black', ticklen=5,
    zeroline=True,linecolor = "#000000",zerolinewidth=2,  # Sets color of X-axis line
    showgrid = True, 
    showline = True,
    gridwidth=1,       
    gridcolor='lightpink',
    showticklabels=True)
    fig.update_layout(height=550,legend_title=None)
    fig.update_layout(font_color="Black",title_font_family="NexaBlack",title_font_color="Black",titlefont_size=20,
    title={
    'text': column.capitalize() +" de forma anual por empresa",
    'y':0.95,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})        
    fig.update_layout(legend=dict(orientation="h",y=1.1,x=0.02),showlegend=True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.4)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.4)')
    return fig

st.set_page_config(
    page_title="Reporte de industria 2021", page_icon=LogoComision,layout="wide",initial_sidebar_state="expanded")

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
    .css-1wrcr25{
        margin-top:135px;
    }
    .css-ocqkz7 {text-align:center}
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
    .titulo {
      background: #fffdf7;
      display: flex;
      color: #4c83f3;
      font-size:25px;
      padding:10px;
    }
    .titulo:before,
    .titulo:after {
      content: '';
      margin: auto 1em;
      border-bottom: solid 3px;
      flex: 1;
    }   

    .edgvbvh9:hover {
      color:rgb(255,255,255);
      border-color:rgb(255,75,75);
    }
    .edgvbvh9 {
      font-weight: 600;
      background-color: rgb(163,196,251);
      border: 0px solid rgba(0, 0, 0, 1); 
      color:black;
      padding: 0.6rem 0.6rem;
      font-size: 16px;
    }
    .imagen-flotar{float:left;}
    @media (max-width:1230px){
        .barra-superior{height:160px;} 
        .main, .e1fqkh3o9 > div{margin-top:215px;}
        .imagen-flotar{float:none}
        h1{top:160px;}}       
    .IconoTitulo img {
        margin-right:10px;
        text-align:center;
    }
    .IconoTitulo h4, .IconoTitulo img {
        display:inline-block;
        vertical-align:middle;
        text-align:center;
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


########################################### APIs
## Telefonía móvil
#@st.cache()
def APISTelMovil():
    from APIs import AbonadosTelMovil,TraficoTelMovil,IngresosTelMovil,TraficoSMSTelMovil,IngresosSMSTelMovil
    return AbonadosTelMovil,TraficoTelMovil,IngresosTelMovil,TraficoSMSTelMovil,IngresosSMSTelMovil
AbonadosTelMovil,TraficoTelMovil,IngresosTelMovil,TraficoSMSTelMovil,IngresosSMSTelMovil = APISTelMovil()
## Internet móvil
#@st.cache()
def APISIntMovil():
    from APIs import AccesosInternetmovil,IngresosInternetmovil,TraficoInternetMovil
    return AccesosInternetmovil,IngresosInternetmovil,TraficoInternetMovil
AccesosInternetmovil,IngresosInternetmovil,TraficoInternetMovil=APISIntMovil()

st.markdown(page_bg_img, unsafe_allow_html=True)
st.sidebar.markdown(r"""<b style="font-size: 26px;text-align:center"> Reporte de industria CRC </b> """,unsafe_allow_html=True)
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
        st.markdown(r"""<div class="titulo"><h3>Información general</h3></div>""",unsafe_allow_html=True)
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
        bla="https://github.com/postdatacrc/Reporte-de-industria/blob/main/Iconos/VozTelMovil.jpg?raw=true"
        st.markdown(r"""<div class="titulo"><h3>Servicios móviles</h3></div>""",unsafe_allow_html=True)
        st.markdown("<center>Para continuar, por favor seleccione el botón con el servicio del cual desea conocer la información</center>",unsafe_allow_html=True)

        ServiciosMóviles=st.radio('Servicios',['Telefonía móvil','Internet móvil','Mensajería móvil'],horizontal=True)
            
        st.markdown(r"""<hr>""",unsafe_allow_html=True)    
            
            
        if ServiciosMóviles=='Telefonía móvil':
            EmpresasTelMovil=['830122566','800153993','830114921','899999115']
            st.markdown(r"""<div class='IconoTitulo'><img height="50px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/Iconos/VozTelMovil.jpg?raw=true'/><h4 style="text-align:left">Telefonía móvil</h4></div>""",unsafe_allow_html=True)   
            #st.image("https://github.com/postdatacrc/Reporte-de-industria/blob/main/Iconos/VozTelMovil.jpg?raw=true",width=100)          
            AbonadosTelMovil=AbonadosTelMovil[AbonadosTelMovil['abonados']>0]
            AbonadosTelMovil.insert(0,'periodo',AbonadosTelMovil['anno']+'-T'+AbonadosTelMovil['trimestre'])
            #
            TraficoTelMovil=TraficoTelMovil[TraficoTelMovil['trafico']>0]
            TraficoTelMovil.insert(0,'periodo',TraficoTelMovil['anno']+'-T'+TraficoTelMovil['trimestre'])    
            #        
            IngresosTelMovil=IngresosTelMovil[IngresosTelMovil['ingresos_totales']>0]
            IngresosTelMovil.insert(0,'periodo',IngresosTelMovil['anno']+'-T'+IngresosTelMovil['trimestre'])
            #
            TraficoSMSTelMovil=TraficoSMSTelMovil[TraficoSMSTelMovil['cantidad']>0]
            TraficoSMSTelMovil.insert(0,'periodo',TraficoSMSTelMovil['anno']+'-T'+TraficoSMSTelMovil['trimestre'])
            #
            IngresosSMSTelMovil=IngresosSMSTelMovil[IngresosSMSTelMovil['ingresos']>0]
            IngresosSMSTelMovil.insert(0,'periodo',IngresosSMSTelMovil['anno']+'-T'+IngresosSMSTelMovil['trimestre'])

            ServiciosTelMovil=st.selectbox('Escoja el servicio de Telefonía móvil',['Abonados','Tráfico','Ingresos','Tráfico SMS','Ingresos SMS'])

            if ServiciosTelMovil=='Abonados':
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoAbonadosTelmovil=st.button('Línea de tiempo')
                with col2:
                    BarrasAbonadosTelmovil=st.button('Diagrama de barras')
                if LineaTiempoAbonadosTelmovil:    
                    AboTrimTelMovil=AbonadosTelMovil.groupby(['periodo','empresa','id_empresa'])['abonados'].sum().reset_index()
                    AboTrimTelMovil=AboTrimTelMovil[AboTrimTelMovil['id_empresa'].isin(EmpresasTelMovil)]
                    st.plotly_chart(Plotlylineatiempo(AboTrimTelMovil,'abonados'), use_container_width=True)
                if BarrasAbonadosTelmovil:
                    AboAnualTelMovl=AbonadosTelMovil.groupby(['anno','empresa','id_empresa'])['abonados'].sum().reset_index()
                    AboAnualTelMovl=AboAnualTelMovl[(AboAnualTelMovl['id_empresa'].isin(['830122566','800153993','830114921']))&(AboAnualTelMovl['anno'].isin(['2020','2021']))]
                    st.plotly_chart(PlotlyBarras(AboAnualTelMovl,'abonados'),use_container_width=True)
            
            if ServiciosTelMovil=='Tráfico':
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoTraficoTelmovil=st.button('Línea de tiempo')
                with col2:
                    BarrasTraficoTelmovil=st.button('Diagrama de barras')
                if LineaTiempoTraficoTelmovil:    
                    TrafTrimTelMovil=TraficoTelMovil.groupby(['periodo','empresa','id_empresa'])['trafico'].sum().reset_index()
                    TrafTrimTelMovil=TrafTrimTelMovil[TrafTrimTelMovil['id_empresa'].isin(EmpresasTelMovil)]
                    st.plotly_chart(Plotlylineatiempo(TrafTrimTelMovil,'trafico'), use_container_width=True)
                if BarrasTraficoTelmovil:
                    TrafAnualTelMovl=TraficoTelMovil.groupby(['anno','empresa','id_empresa'])['trafico'].sum().reset_index()
                    TrafAnualTelMovl=TrafAnualTelMovl[(TrafAnualTelMovl['id_empresa'].isin(['830122566','800153993','830114921']))&(TrafAnualTelMovl['anno'].isin(['2020','2021']))]
                    st.plotly_chart(PlotlyBarras(TrafAnualTelMovl,'trafico'),use_container_width=True)  
 
                    
                    
        if ServiciosMóviles=='Internet móvil':

            TraficoInternetMovil=TraficoInternetMovil[TraficoInternetMovil['trafico']>0]
            IngresosInternetmovil=IngresosInternetmovil[IngresosInternetmovil['ingresos']>0]
            AccesosInternetmovil=AccesosInternetmovil[AccesosInternetmovil['accesos']>0]
            
            TraficoInternetMovil.insert(0,'periodo',TraficoInternetMovil['anno']+'-T'+TraficoInternetMovil['trimestre'])
            IngresosInternetmovil.insert(0,'periodo',IngresosInternetmovil['anno']+'-T'+IngresosInternetmovil['trimestre'])
            AccesosInternetmovil.insert(0,'periodo',AccesosInternetmovil['anno']+'-T'+AccesosInternetmovil['trimestre'])   
            
            col1,col2 = st.columns(2)
            #with col1:
            st.markdown(r"""<div class='IconoTitulo'><img height="60px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/Iconos/InternetTelMovil.jpg?raw=true'/><h4>Internet móvil</h4></div>""",unsafe_allow_html=True) 
            #st.image("https://github.com/postdatacrc/Reporte-de-industria/blob/main/Iconos/InternetTelMovil.jpg?raw=true",width=100)        
            #with col2:
            ServiciosIntMovil=st.selectbox('Escoja el servicio de Internet móvil',['Accesos','Tráfico','Ingresos'])
                            
            if ServiciosIntMovil=='Accesos':
                Accnac=AccesosInternetmovil.groupby(['periodo','empresa','id_empresa'])['accesos'].sum().reset_index()              
                st.plotly_chart(Plotlylineatiempo(Accnac,'accesos'), use_container_width=True)
                AgGrid(Accnac)
            if ServiciosIntMovil=='Tráfico':
                Trafnac=TraficoInternetMovil.groupby(['periodo','empresa','id_empresa'])['trafico'].sum().reset_index()              
                st.plotly_chart(Plotlylineatiempo(Trafnac,'trafico'), use_container_width=True)
                AgGrid(Trafnac)
            if ServiciosIntMovil=='Ingresos':
                Ingnac=IngresosInternetmovil.groupby(['periodo','empresa','id_empresa'])['ingresos'].sum().reset_index()              
                st.plotly_chart(Plotlylineatiempo(Ingnac,'ingresos'), use_container_width=True)
                AgGrid(Ingnac)    
 
        if ServiciosMóviles=='Mensajería móvil':
            st.markdown(r"""<div class='IconoTitulo'><img height="50px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/Iconos/SMSTelMovil.jpg?raw=true'/><h4>Mensajería móvil</h4></div>""",unsafe_allow_html=True)
            #st.image("https://github.com/postdatacrc/Reporte-de-industria/blob/main/Iconos/SMSTelMovil.jpg?raw=true",width=170)
 
if select_seccion =='Dinámica postal':
    st.title("Dinámica del sector Postal")
    st.markdown("En el año 2020")    
                

