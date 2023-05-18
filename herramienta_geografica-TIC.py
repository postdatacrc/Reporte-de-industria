import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from plotly.subplots import make_subplots
import glob
import math
import re
import os
from urllib.request import urlopen
import json
from streamlit_folium import folium_static
from st_aggrid import AgGrid
import geopandas as gpd
import folium
from folium.plugins import FloatImage
import urllib
from functools import partial, reduce

LogoComision="data:image/png;base64,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"
LogoComision2="https://postdata.gov.co/sites/all/themes/nuboot_radix/logo-crc-blanco.png"

st.set_page_config(
    page_title="Herramienta geográfica TIC", page_icon=LogoComision,layout="wide",initial_sidebar_state="expanded")  

Estilo_css="""<style type="text/css">
    @import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap'); 

    html, body, [class*="css"] ,[class*="st-ae"]{
        font-family: 'Poppins', serif; 
    }  
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 250px;}
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 250px;
        top:100px;
        margin-left: -300px;}
    h1{ background: rgb(215,235,252);
        text-align: center;
        padding: 15px;
        font-family: Poppins;
        font-size:1.60rem;
        color: black;
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
    .e16nr0p31 {display:none}
    .css-2ewto4 {width : 10%}
    .css-y3whyl, .css-xqnn38 {background-color:#ccc}
    .e8zbici0 {display:none}
    .e8zbici2 {display:none} 
    .e19lei0e1 {display:none}
    .css-1uvyptr:hover,.css-1uvyptr {background: #ccc}
    .e1tzin5v2 {
        display:flex;
        align-items:center;
    }
    .e1fqkh3o2{
        padding-top:2.5rem;   
    }
    .css-52bwht{
        gap:0.01rem;
    }
    .block-container {
        padding-top:0;
        } 
    .main > div {
        padding-left:30px;
        padding-right:30px;
    }        
    h2{
        background: #fffdf7;
        text-align: center;
        padding: 10px;
        color: #7a44f2;
        font-weight: bold;
    }    
    h6{
        background: #fffdf7;
        color: #7a44f2;
        font-weight: bold;
    }        
    .titulo {
      background: #fffdf7;
      display: flex;
      color: #7a44f2;
      font-size:25px;
      padding:10px;
      text-align:center;
    }
    .titulo:before,
    .titulo:after {
      content: '';
      margin: auto 1em;
      border-bottom: solid 3px;
      flex: 1;
    }   
    .stButton{
        text-align:center;
    }
    .edgvbvh9:hover {
      color:rgb(255,255,255);
      border-color:rgb(255,75,75);
    }
    .edgvbvh9 {
      font-weight: 600;
      background-color: rgb(215,235,252);
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
    }
    .IconoTitulo{
        text-align:center;
    }
    .IconoTitulo h4, .IconoTitulo img {
        display:inline-block;
        vertical-align:middle;
    }    
    .css-17m3m1o{text-align:left}
    .st-b4 {display: inline-flex}
    .stRadio{text-align:center}
    ul {
        list-style-type: square;
        text-align:left;
    }      
    mark.title {
        color:#7a44f2;
        background:none;
    }
    </style>"""
Barra_superior="""
<div class="barra-superior">
    <div class="imagen-flotar" style="height: 70px; left: 10px; padding:15px">
        <a class="imagen-flotar" style="float:left;" href="https://www.crcom.gov.co" title="CRC">
            <img src="https://www.postdata.gov.co/sites/all/themes/nuboot_radix/logo-crc-blanco.png" alt="CRC" style="height:40px">
        </a>
        <a class="imagen-flotar" style="padding-left:10px;" href="https://www.postdata.gov.co" title="Postdata">
            <img src="https://www.postdata.gov.co/sites/default/files/postdata-logo.png" alt="Inicio" style="height:40px">
        </a>
    </div>
</div>"""
Tabla_html=r"""<style> 
.styled-table thead tr {
    background-color: #E3371E;
    color: #ffffff;
    text-align: left;
}
.styled-table th,
.styled-table th {resize:horizontal; overflow:auto;}
.styled-table td {
    padding: 12px 15px;
}
.styled-table tbody tr {
    border-bottom: 1px solid #dddddd;
}
.styled-table tbody tr:nth-of-type(even) {
    background-color: #f3f3f3;
}
.styled-table tbody tr:last-of-type {
    border-bottom: 2px solid #E3371E;
}
.styled-table th:nth-child(1),
.styled-table td:nth-child(1) {
display: none;
}
</style> 
"""


st.markdown(Estilo_css+Barra_superior+Tabla_html,unsafe_allow_html=True)
#st.markdown("""<h1>Herramienta geográfica Telecomunicaciones</h1>""",unsafe_allow_html=True)
st.title("Herramienta geográfica Telecomunicaciones")


#st.sidebar.markdown(r"""<b style="font-size: 26px;text-align:center"> Herramienta geográfica TIC</b> """,unsafe_allow_html=True)
#st.sidebar.markdown(r"""<hr>""",unsafe_allow_html=True)
st.sidebar.markdown("""<b>Menú</b>""", unsafe_allow_html=True)

#Función para traer base
@st.cache()
def T13(allow_output_mutation=True):
    url_bases = 'https://raw.githubusercontent.com/postdatacrc/Herrammienta_geografica/main/Bases_T13/'
    dfT13 = []
    for i in range(9):
        file_name = f'T1_3-{i}.csv'
        file_url = os.path.join(url_bases, file_name)
        base = pd.read_csv(file_url, delimiter=';')
        dfT13.append(base)
    FT_13 = pd.concat(dfT13)
    FT_13['CODIGO_DEPARTAMENTO']=FT_13['DEPARTAMENTO']+'-'+FT_13['ID_DEPARTAMENTO'].astype('str')
    FT_13['CODIGO_MUNICIPIO']=FT_13['MUNICIPIO']+'-'+FT_13['ID_MUNICIPIO'].astype('str')
    FT_13['PERIODO']=FT_13['ANNO'].astype('str')+'-T'+FT_13['TRIMESTRE'].astype('str')
    FT_13['CODSEG']=np.where(FT_13['ID_SEGMENTO'].isin([101,102,103,104,105,106]),'Residencial','Corporativo')
    return FT_13
FT1_3=T13()

MUNICIPIOS=sorted(FT1_3['CODIGO_MUNICIPIO'].unique().tolist())
DEPARTAMENTOS=sorted(FT1_3['CODIGO_DEPARTAMENTO'].unique().tolist())

fact_escala={'ACCESOS':1e6,'VALOR FACTURADO':1e9,'NÚMERO EMPRESAS':1}

    
def orderOfMagnitude(number):
    return math.floor(math.log(number, 10))

def PlotlyBarrasSegmento(df,column):
    fig=make_subplots(rows=1,cols=1)
    mean_val = df[column].mean()
    if mean_val >= 1e9:
        y_title = f"{column} (Miles de Millones)"
        df[column] = round(df[column] / 1e9,2)
    elif mean_val >= 1e6:
        y_title = f"{column} (Millones)"
        df[column] = round(df[column] / 1e6,2)
    else:
        y_title = f"{column}"
    
    factor_escalamiento=orderOfMagnitude(df[column].max())
    paleta_colores={'Residencial':"#FF7A48","Corporativo":"#0593A2","Total":"#E3371E"}
    if column=='NÚMERO EMPRESAS':
        SEG=["Residencial","Corporativo","Total"]
    else:    
        SEG=["Residencial","Corporativo"]
    for segmento in SEG:
        fig.add_trace(go.Bar(x=df[df['SEGMENTO']==segmento]['PERIODO'],
                            y=df[df['SEGMENTO']==segmento][column],name=segmento,marker_color=paleta_colores[segmento]))
    fig.update_yaxes(tickfont=dict(family='Tahoma', color='black', size=16),title_font=dict(family="Tahoma"),titlefont_size=16, title_text=y_title, row=1, col=1)                        
    fig.update_xaxes(tickangle=0, tickfont=dict(family='Tahoma', color='black', size=14),title_font=dict(family="Tahoma"),title_text=None,row=1, col=1
    ,zeroline=True,linecolor = 'rgba(192, 192, 192, 0.8)',zerolinewidth=2)
    fig.update_layout(height=550,legend_title=None)
    fig.update_layout(font_color="Black",font_family="Tahoma",title_font_color="Black",titlefont_size=20,
    title={
    'text':"<b>"+select_variable.capitalize()+" ("+select_servicio+")</b>",
    'y':0.95,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})        
    
    fig.update_layout(legend=dict(orientation="h",xanchor='center',y=1.1,x=0.5,font_size=11),showlegend=True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
    fig.update_layout(yaxis_tickformat ='d')
    if column!='NÚMERO EMPRESAS':       
        fig.update_layout(barmode='stack')   
        fig.add_trace(go.Scatter(x=df[df['SEGMENTO']==segmento]['PERIODO'],y=df[df['SEGMENTO']=='Total'][column],
                                 mode='text',text=df[df['SEGMENTO']=='Total'][column],textposition='top center',
                    textfont=dict(color='black', size=14),name=None,showlegend=False))        
    return fig

def PlotlyBarrasEmpaquetados(df,column):
    fig=make_subplots(rows=1,cols=1)

    paleta_colores=["#CAA8F5", "#230C33", "#F5D05C", "#BF1363", "#F39273", "#5FBFAB", "#0E79B2"]
    Servicios=df['SERVICIO_PAQUETE'].unique().tolist()
    for i,servicio in enumerate(Servicios):
        fig.add_trace(go.Bar(x=df[df['SERVICIO_PAQUETE']==servicio]['PERIODO'],
                            y=df[df['SERVICIO_PAQUETE']==servicio][column],name=servicio,marker_color=paleta_colores[i]))
    fig.update_yaxes(tickfont=dict(family='Tahoma', color='black', size=16),title_font=dict(family="Tahoma"),titlefont_size=16, title_text=f"{column}", row=1, col=1)                        
    fig.update_xaxes(tickangle=0, tickfont=dict(family='Tahoma', color='black', size=14),title_font=dict(family="Tahoma"),title_text=None,row=1, col=1
    ,zeroline=True,linecolor = 'rgba(192, 192, 192, 0.8)',zerolinewidth=2)
    fig.update_layout(height=550,legend_title=None)
    fig.update_layout(font_color="Black",font_family="Tahoma",title_font_color="Black",titlefont_size=20,
    title={
    'text':"<b>"+select_variable.capitalize()+" ("+select_servicio+")</b>",
    'y':0.95,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})        
    
    fig.update_layout(legend=dict(orientation="h",xanchor='center',y=1.1,x=0.2,font_size=11),showlegend=True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
    fig.update_layout(yaxis_tickformat ='d')      
    fig.update_layout(barmode='stack')          
    return fig


def Nac_info(df):
    dfNac=pd.concat([df.groupby(['PERIODO', 'CODSEG']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).reset_index(),
    df.groupby(['PERIODO']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).assign(CODSEG='Total').reset_index()]).sort_values(by=['PERIODO'])
    dfNac=dfNac.rename(columns=dict_variables)
    dfNac2=pd.pivot(dfNac[['PERIODO','SEGMENTO',select_variable]], index=['PERIODO'], columns=['SEGMENTO'], values=select_variable).reset_index().fillna(0)
    dfNac2_html = f'<div class="styled-table">{dfNac2.to_html(index=False)}</div>'
    return dfNac, dfNac2_html 

def Dep_info(df):
    dfDep=pd.concat([df.groupby(['PERIODO', 'CODSEG','CODIGO_DEPARTAMENTO']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).reset_index(),
    df.groupby(['PERIODO','CODIGO_DEPARTAMENTO']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).assign(CODSEG='Total').reset_index()]).sort_values(by=['PERIODO'])
    dfDep=dfDep.rename(columns=dict_variables)
    dfDep=dfDep[dfDep['CODIGO_DEPARTAMENTO']==select_dpto]
    dfDep2=pd.pivot(dfDep[['PERIODO','SEGMENTO',select_variable]], index=['PERIODO'], columns=['SEGMENTO'], values=select_variable).reset_index().fillna(0)
    dfDep2_html = f'<div class="styled-table">{dfDep2.to_html(index=False)}</div>'
    return dfDep,dfDep2_html

def Muni_info(df):
    dfMUNI=pd.concat([df.groupby(['PERIODO', 'CODSEG','CODIGO_MUNICIPIO']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).reset_index(),
    df.groupby(['PERIODO','CODIGO_MUNICIPIO']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).assign(CODSEG='Total').reset_index()]).sort_values(by=['PERIODO'])
    dfMUNI=dfMUNI.rename(columns=dict_variables)
    dfMUNI=dfMUNI[dfMUNI['CODIGO_MUNICIPIO']==select_muni]
    dfMUNI2=pd.pivot(dfMUNI[['PERIODO','SEGMENTO',select_variable]], index=['PERIODO'], columns=['SEGMENTO'], values=select_variable).reset_index().fillna(0)
    dfMUNI2_html = f'<div class="styled-table">{dfMUNI2.to_html(index=False)}</div>' 
    return dfMUNI, dfMUNI2_html

select_servicio=st.sidebar.selectbox('Servicio',['Internet Fijo','TV por suscripción','Telefonía fija', 'Empaquetados'])
select_ambito=st.sidebar.selectbox('Ámbito',['Nacional','Departamental','Municipal'])
dict_variables={'CANTIDAD_LINEAS_ACCESOS': 'ACCESOS', 'VALOR_FACTURADO_O_COBRADO': 'VALOR FACTURADO', 'ID_EMPRESA': 'NÚMERO EMPRESAS','CODSEG': 'SEGMENTO'}

if select_servicio=='Internet Fijo':
    st.markdown(r"""<div class="titulo"><h2>Internet fijo</h2></div>""",unsafe_allow_html=True)
    InternetFijo=FT1_3[FT1_3['SERVICIO_PAQUETE'].isin(['Triple Play (Telefonía fija + Internet fijo + TV por suscripción)',
       'Duo Play 1 (Telefonía fija + Internet fijo)',
       'Duo Play 2 (Internet fijo y TV por suscripción)', 'Internet fijo'])]
    
    if select_ambito=='Nacional':
        select_variable=st.sidebar.selectbox('Variable',['ACCESOS','VALOR FACTURADO', 'NÚMERO EMPRESAS'])        
        col1,col2=st.columns([1.5,1], gap="large")
        with col1:
            st.plotly_chart(PlotlyBarrasSegmento(Nac_info(InternetFijo)[0],select_variable), use_column_width=True)
        with col2:
            st.markdown("<center><b>"+select_variable.capitalize()+" (Internet fijo)</b></center>",unsafe_allow_html=True)
            st.markdown(Nac_info(InternetFijo)[1],unsafe_allow_html=True)
            
    if select_ambito=='Departamental':
        select_dpto=st.sidebar.selectbox('Departamento',DEPARTAMENTOS)
        select_variable=st.sidebar.selectbox('Variable',['ACCESOS','VALOR FACTURADO', 'NÚMERO EMPRESAS'])        
        st.markdown(r"""<div><center><h3>"""+select_dpto.split('-')[0]+"""</h3></center></div>""",unsafe_allow_html=True)        
        col1,col2=st.columns([2,1])
        with col1:
            st.plotly_chart(PlotlyBarrasSegmento(Dep_info(InternetFijo)[0],select_variable), use_column_width=True)
        with col2:
            st.markdown("<center><b>"+select_variable.capitalize()+" (Internet fijo)</b></center>",unsafe_allow_html=True)
            st.markdown(Dep_info(InternetFijo)[1],unsafe_allow_html=True)
        
    if select_ambito=='Municipal':
        select_muni=st.sidebar.selectbox('Municipio',MUNICIPIOS)        
        select_variable=st.sidebar.selectbox('Variable',['ACCESOS','VALOR FACTURADO', 'NÚMERO EMPRESAS'])
        st.markdown(r"""<div><center><h3>"""+select_muni.split('-')[0]+"""</h3></center></div>""",unsafe_allow_html=True)        
        col1,col2=st.columns([2,1])
        with col1:
            st.plotly_chart(PlotlyBarrasSegmento(Muni_info(InternetFijo)[0],select_variable), use_column_width=True)
        with col2:
            st.markdown("<center><b>"+select_variable.capitalize()+" (Internet fijo)</b></center>",unsafe_allow_html=True)
            st.markdown(Muni_info(InternetFijo)[1],unsafe_allow_html=True)
        
if select_servicio=='TV por suscripción':
    st.markdown(r"""<div class="titulo"><h2>Televisión por suscripción</h2></div>""",unsafe_allow_html=True)
    TVporSus=FT1_3[FT1_3['SERVICIO_PAQUETE'].isin(['Triple Play (Telefonía fija + Internet fijo + TV por suscripción)',
    'Duo Play 2 (Internet fijo y TV por suscripción)','Televisión por suscripción',
       'Duo Play 3 (Telefonía fija y TV por suscripción)'])]    

    if select_ambito=='Nacional':
        select_variable=st.sidebar.selectbox('Variable',['ACCESOS','VALOR FACTURADO', 'NÚMERO EMPRESAS'])        
        col1,col2=st.columns([1.5,1], gap="large")
        with col1:
            st.plotly_chart(PlotlyBarrasSegmento(Nac_info(TVporSus)[0],select_variable), use_column_width=True)
        with col2:
            st.markdown("<center><b>"+select_variable.capitalize()+" (Televisión por suscripción)</b></center>",unsafe_allow_html=True)
            st.markdown(Nac_info(TVporSus)[1],unsafe_allow_html=True)

    if select_ambito=='Departamental':
        select_dpto=st.sidebar.selectbox('Departamento',DEPARTAMENTOS)
        select_variable=st.sidebar.selectbox('Variable',['ACCESOS','VALOR FACTURADO', 'NÚMERO EMPRESAS'])
        
        st.markdown(r"""<div><center><h3>"""+select_dpto.split('-')[0]+"""</h3></center></div>""",unsafe_allow_html=True)        
        col1,col2=st.columns([2,1])
        with col1:
            st.plotly_chart(PlotlyBarrasSegmento(Dep_info(TVporSus)[0],select_variable), use_column_width=True)
        with col2:
            st.markdown("<center><b>"+select_variable.capitalize()+" (Televisión por suscripción)</b></center>",unsafe_allow_html=True)
            st.markdown(Dep_info(TVporSus)[1],unsafe_allow_html=True)

    if select_ambito=='Municipal':
        select_muni=st.sidebar.selectbox('Municipio',MUNICIPIOS)        
        select_variable=st.sidebar.selectbox('Variable',['ACCESOS','VALOR FACTURADO', 'NÚMERO EMPRESAS'])
        st.markdown(r"""<div><center><h3>"""+select_muni.split('-')[0]+"""</h3></center></div>""",unsafe_allow_html=True)        
        col1,col2=st.columns([2,1])
        with col1:
            st.plotly_chart(PlotlyBarrasSegmento(Muni_info(TVporSus)[0],select_variable), use_column_width=True)
        with col2:
            st.markdown("<center><b>"+select_variable.capitalize()+" (Televisión por suscripción)</b></center>",unsafe_allow_html=True)
            st.markdown(Muni_info(TVporSus)[1],unsafe_allow_html=True)
       
if select_servicio=='Telefonía fija':
    st.markdown(r"""<div class="titulo"><h2>Telefonía fija</h2></div>""",unsafe_allow_html=True)
    Telfija=FT1_3[FT1_3['SERVICIO_PAQUETE'].isin(['Triple Play (Telefonía fija + Internet fijo + TV por suscripción)',
       'Duo Play 1 (Telefonía fija + Internet fijo)','Duo Play 3 (Telefonía fija y TV por suscripción)',
       'Telefonía fija'])]       
   
    if select_ambito=='Nacional':
        select_variable=st.sidebar.selectbox('Variable',['ACCESOS','VALOR FACTURADO', 'NÚMERO EMPRESAS'])
        col1,col2=st.columns([1.5,1], gap="large")
        with col1:
            st.plotly_chart(PlotlyBarrasSegmento(Nac_info(Telfija)[0],select_variable), use_column_width=True)
        with col2:
            st.markdown("<center><b>"+select_variable.capitalize()+" (Telefonía fija)</b></center>",unsafe_allow_html=True)
            st.markdown(Nac_info(Telfija)[1],unsafe_allow_html=True)   

    if select_ambito=='Departamental':
        select_dpto=st.sidebar.selectbox('Departamento',DEPARTAMENTOS)
        select_variable=st.sidebar.selectbox('Variable',['ACCESOS','VALOR FACTURADO', 'NÚMERO EMPRESAS'])        
        st.markdown(r"""<div><center><h3>"""+select_dpto.split('-')[0]+"""</h3></center></div>""",unsafe_allow_html=True)

        col1,col2=st.columns([2,1])
        with col1:
            st.plotly_chart(PlotlyBarrasSegmento(Dep_info(Telfija)[0],select_variable), use_column_width=True)
        with col2:
            st.markdown("<center><b>"+select_variable.capitalize()+" (Telefonía fija)</b></center>",unsafe_allow_html=True)
            st.markdown(Dep_info(Telfija)[1],unsafe_allow_html=True)            
            
    if select_ambito=='Municipal':
        select_muni=st.sidebar.selectbox('Municipio',MUNICIPIOS)        
        select_variable=st.sidebar.selectbox('Variable',['ACCESOS','VALOR FACTURADO', 'NÚMERO EMPRESAS'])
        st.markdown(r"""<div><center><h3>"""+select_muni.split('-')[0]+"""</h3></center></div>""",unsafe_allow_html=True)        
        col1,col2=st.columns([2,1])
        with col1:
            st.plotly_chart(PlotlyBarrasSegmento(Muni_info(Telfija)[0],select_variable), use_column_width=True)
        with col2:
            st.markdown("<center><b>"+select_variable.capitalize()+" (Telefonía fija)</b></center>",unsafe_allow_html=True)
            st.markdown(Muni_info(Telfija)[1],unsafe_allow_html=True)
                

if select_servicio=='Empaquetados':
    st.markdown(r"""<div class="titulo"><h2>Empaquetados fijos</h2></div>""",unsafe_allow_html=True)
    if select_ambito=='Nacional':
        select_variable=st.sidebar.selectbox('Variable',['ACCESOS','VALOR FACTURADO', 'NÚMERO EMPRESAS'])
        Empaquetados_Nac=FT1_3.groupby(['PERIODO','SERVICIO_PAQUETE']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).reset_index()   
        Empaquetados_Nac=Empaquetados_Nac.rename(columns=dict_variables)
        
        col1,col2=st.columns([2,1])
        with col1:
            st.plotly_chart(PlotlyBarrasEmpaquetados(Empaquetados_Nac,select_variable),use_container_width=True)
        Empaquetados_Nac2=pd.concat([FT1_3.groupby(['PERIODO','SERVICIO_PAQUETE','CODSEG']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).reset_index(),
        FT1_3.groupby(['PERIODO','SERVICIO_PAQUETE']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).assign(CODSEG='Total').reset_index()]).sort_values(by=['PERIODO'])
        Empaquetados_Nac2=Empaquetados_Nac2.rename(columns=dict_variables)
        Empaquetados_Nac3=pd.pivot(Empaquetados_Nac2[['PERIODO','SEGMENTO','SERVICIO_PAQUETE',select_variable]], index=['PERIODO','SERVICIO_PAQUETE'], columns=['SEGMENTO'], values=select_variable).reset_index().fillna(0)
        with col2:
            select_servpaquete=st.selectbox('',Empaquetados_Nac3['SERVICIO_PAQUETE'].unique().tolist())
            Empaquetados_Nac3=Empaquetados_Nac3[Empaquetados_Nac3['SERVICIO_PAQUETE']==select_servpaquete].drop(columns=['SERVICIO_PAQUETE'],axis=1)
            Empaquetados_Nac3_html = f'<div class="styled-table">{Empaquetados_Nac3.to_html(index=False)}</div>'  
            st.markdown(Empaquetados_Nac3_html,unsafe_allow_html=True) 
                              