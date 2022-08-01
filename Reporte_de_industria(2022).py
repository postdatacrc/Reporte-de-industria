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

nombresComerciales={'ALMACENES EXITO INVERSIONES S.A.S.':'Móvil Éxito',
 'AVANTEL S.A.S.':'Avantel',
 'COLOMBIA MOVIL S.A. E.S.P.':'Tigo',
 'COLOMBIA TELECOMUNICACIONES S.A. ESP':'Telefónica',
 'COLOMBIA TELECOMUNICACIONES S.A. E.S.P.':'Movistar',
 'COMUNICACION CELULAR S A COMCEL S A':'Claro',
 'EMPRESA DE TELECOMUNICACIONES DE BOGOTÁ S.A. ESP.':'ETB',
 'EMPRESA DE TELECOMUNICACIONES DE BOGOTA S.A. ESP':'ETB',
 'LOGISTICA FLASH COLOMBIA S.A.S':'Flash',
 'PARTNERS TELECOM COLOMBIA SAS':'WOM',
 'SETROC MOBILE GROUP SAS':'Setroc',
 'SUMA MOVIL SAS':'Suma',
 'VIRGIN MOBILE COLOMBIA S.A.S.':'Virgin',
 'DIRECTV COLOMBIA LTDA':'Directv',
 'EDATEL S.A.':'Edatel',
 'EMPRESAS MUNICIPALES DE CALI EICE E.S.P':'Emcali',
 'H V TELEVISION S.A.S.':'H V',
 'UNE EPM TELECOMUNICACIONES S.A.':'Tigo-Une'}
Colores_pie={'Claro':'rgba(255,0,0,0.7)','Telefónica':'rgba(154,205,50,0.7)','Tigo':'rgba(100,149,237,0.7)','Virgin':'rgb(255,102,178)',
         'Móvil Éxito':'rgba(241, 196, 15,0.7)','WOM':'rgb(198,84,206)',
        'Avantel':'rgba(240, 128, 128,0.7)','ETB':'rgba(26, 82, 118,0.7)','Flash':'black','Setroc':'black','Suma':'black'}
Colores_pie2={'Claro':'rgba(255,0,0,0.7)','Movistar':'rgba(154,205,50,0.7)','Tigo-Une':'rgba(100,149,237,0.7)','Otros':'rgb(192,192,192)','ETB':'rgba(26, 82, 118,0.7)'}

def Participacion(df,column):
    part=df[column]/df[column].sum()
    return part
def PColoresEmp(id_empresa):
    if id_empresa == '800153993':
        return 'rgb(255,75,75)'
    elif id_empresa == '830114921':
        return 'rgb(153,175,255)'
    elif id_empresa == '830122566':
        return 'rgb(178,255,102)'
    elif id_empresa=='899999115':
        return 'rgb(53,128,138)'
    elif id_empresa=='900420122':
        return 'rgb(255,102,178)'
    elif id_empresa=='901354361':
        return 'rgb(198,84,206)'
    elif id_empresa=='830016046':
        return 'rgb(240, 128, 128)'
    elif id_empresa=='900092385':
        return 'rgb(153,175,255)'
    elif id_empresa=='805006014':
        return 'rgb(0,255,255)'
    else:
        pass            
def periodoformato(x):
    return "{1}-{0}".format(*x.split('-')).replace('-','<br>')

def Plotlylineatiempo(df,column,unidad,escalamiento,colores):
    fig = make_subplots(rows=1, cols=1)
    if 'modalidad' in df.columns.tolist():
        maxdf=df[column].max()/escalamiento+(df[column].max()/escalamiento)*0.3  
        modalidad=df['modalidad'].unique().tolist()
        for i,elem in enumerate(modalidad):
            fig.add_trace(go.Scatter(x=df[df['modalidad']==elem]['periodo_formato'],
            y=df[df['modalidad']==elem][column]/escalamiento,text=df[df['modalidad']=='elem']['modalidad'],line=dict(color=colores[i]),
            mode='lines+markers',name=elem,marker=dict(size=7),hovertemplate =
            '<br><b>Modalidad</b>:<br><extra></extra>'+elem+
            '<br><b>Periodo</b>: %{x}<br>'+                         
            column.capitalize()+'-'+unidad+': %{y:.2f}<br>'))
        fig.update_yaxes(range=[0,maxdf],tickfont=dict(family='Boton', color='black', size=16),titlefont_size=16, title_text=unidad, row=1, col=1)
    
    else:
        maxdf=df[column].max()/escalamiento+(df[column].max()/escalamiento)*0.1  
        mindf=df[column].min()/escalamiento-(df[column].min()/escalamiento)*0.1  
        fig.add_trace(go.Bar(x=df['periodo_formato'],
                                y=df[column]/escalamiento,marker_color='rgb(102,204,0)',name=column,
                                hovertemplate ='<br><b>Periodo</b>: %{x}<br><extra></extra>'+                         
            column.capitalize()+'-'+unidad+': %{y:.2f}<br>'))
        fig.update_yaxes(range=[mindf,maxdf],tickfont=dict(family='Boton', color='black', size=16),titlefont_size=16, title_text=unidad, row=1, col=1)                        
    fig.update_xaxes(tickangle=0, tickfont=dict(family='Boston', color='black', size=14),title_text=None,row=1, col=1
    ,zeroline=True,linecolor = 'rgba(192, 192, 192, 0.8)',zerolinewidth=2)
    fig.update_layout(height=550,legend_title=None)
    fig.update_layout(font_color="Black",title_font_family="NexaBlack",title_font_color="Black",titlefont_size=20,
    title={
    'text':column.capitalize() +" por periodo",
    'y':0.95,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})        
    fig.update_layout(legend=dict(orientation="h",xanchor='center',y=1.1,x=0.5),showlegend=True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    #fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.4)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
    fig.update_layout(yaxis_tickformat ='d')
    return fig

def PlotlylineatiempoTec(df,column,unidad,escalamiento,colores):
    fig = make_subplots(rows=1, cols=1)
    maxdf=df[column].max()/escalamiento+(df[column].max()/escalamiento)*0.3  
    tecnologia=df['CodTec'].unique().tolist()
    for i,elem in enumerate(tecnologia):
        fig.add_trace(go.Scatter(x=df[df['CodTec']==elem]['periodo_formato'],
        y=df[df['CodTec']==elem][column]/escalamiento,text=df[df['CodTec']=='elem']['CodTec'],line=dict(color=colores[i]),
        mode='lines+markers',name=elem,marker=dict(size=7),hovertemplate =
        '<br><b>Modalidad</b>:<br><extra></extra>'+elem+
        '<br><b>Periodo</b>: %{x}<br>'+                         
        column.capitalize()+' '+unidad+': %{y:.2f}<br>'))
    fig.update_yaxes(range=[0,maxdf],tickfont=dict(family='Boton', color='black', size=16),titlefont_size=16, title_text=unidad, row=1, col=1)                    
    fig.update_xaxes(tickangle=0, tickfont=dict(family='Boston', color='black', size=14),title_text=None,row=1, col=1
    ,zeroline=True,linecolor = 'rgba(192, 192, 192, 0.8)',zerolinewidth=2)
    fig.update_layout(height=550,legend_title=None)
    fig.update_layout(font_color="Black",title_font_family="NexaBlack",title_font_color="Black",titlefont_size=20,
    title={
    'text':column.capitalize() +" por periodo",
    'y':0.95,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})        
    fig.update_layout(legend=dict(orientation="h",xanchor='center',y=1.1,x=0.5),showlegend=True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    #fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.4)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
    fig.update_layout(yaxis_tickformat ='d')
    return fig
    
def PlotlyBarras(df,column,unidad,escalamiento,titulo):   
    fig = make_subplots(rows=1, cols=1) 
    maxdf=df[column].max()/escalamiento+(df[column].max()/escalamiento)*0.5
    for empresa in df['empresa'].unique().tolist():
        fig.add_trace(go.Bar(x=df[df['empresa']==empresa]['anno'],y=df[df['empresa']==empresa][column]/escalamiento
                             ,marker_color=PColoresEmp(df[df['empresa']==empresa]['id_empresa'].unique()[0]),
                            name=empresa,hovertemplate='<br><b>Empresa</b>:<br><extra></extra>'+empresa+'<br>'+                       
        column.capitalize()+' '+unidad+': %{y:.3f}<br>'))
    fig.update_layout(barmode='group')
    fig.update_xaxes(tickangle=0, tickfont=dict(family='Boston', color='black', size=16),title_text=None,row=1, col=1,
    zeroline=True,linecolor = "rgba(192, 192, 192, 0.8)",zerolinewidth=2)
    fig.update_yaxes(tickfont=dict(family='Boston', color='black', size=16),titlefont_size=18, title_text=unidad, row=1, col=1)
    fig.update_layout(height=550,legend_title=None)
    fig.update_layout(font_color="Black",title_font_family="NexaBlack",title_font_color="Black",titlefont_size=20,
    title={
    'text': titulo,
    'y':0.98,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})        
    fig.update_layout(legend=dict(orientation="h",y=1.2,xanchor='center',x=0.5,font_size=12),showlegend=True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',yaxis_tickformat='d')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
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
 
st.markdown("""<style type="text/css">
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 300px;}
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 300px;
        top:100px;
        margin-left: -300px;}
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
    }
    .IconoTitulo{
        text-align:center;
    }
    .IconoTitulo h4, .IconoTitulo img {
        display:inline-block;
        vertical-align:middle;
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
@st.cache(ttl=24*3600,allow_output_mutation=True)
def APISTelMovil():
    from APIs import AbonadosTelMovil,TraficoTelMovil,IngresosTelMovil,TraficoSMSTelMovil,IngresosSMSTelMovil
    return AbonadosTelMovil,TraficoTelMovil,IngresosTelMovil,TraficoSMSTelMovil,IngresosSMSTelMovil
AbonadosTelMovil,TraficoTelMovil,IngresosTelMovil,TraficoSMSTelMovil,IngresosSMSTelMovil = APISTelMovil()
## Internet móvil
@st.cache(ttl=24*3600,allow_output_mutation=True)
def APISIntMovil():
    from APIs import AccesosInternetmovil,IngresosInternetmovil,TraficoInternetMovil
    return AccesosInternetmovil,IngresosInternetmovil,TraficoInternetMovil
AccesosInternetmovil,IngresosInternetmovil,TraficoInternetMovil=APISIntMovil()
## Internet fijo
@st.cache(ttl=24*3600,allow_output_mutation=True)
def APIsIntFijo():
    from APIs import AccesosCorpIntFijo,AccesosResIntFijo,IngresosInternetFijo
    return AccesosCorpIntFijo,AccesosResIntFijo,IngresosInternetFijo
AccesosCorpIntFijo,AccesosResIntFijo,IngresosInternetFijo=APIsIntFijo()    
## Telefonía fija
@st.cache(ttl=24*3600,allow_output_mutation=True)
def APIsTelFija():
    from APIs import LineasTelefoníaLocal,TraficoTelefoniaFija,IngresosTelefoniaFija
    return LineasTelefoníaLocal,TraficoTelefoniaFija,IngresosTelefoniaFija
LineasTelefoníaLocal,TraficoTelefoniaFija,IngresosTelefoniaFija=APIsTelFija()    
## TV por suscripción
@st.cache(ttl=24*3600,allow_output_mutation=True)
def APIsTVSus():
    from APIs import SuscriptoresTVSus,IngresosTVSus
    return SuscriptoresTVSus,IngresosTVSus
SuscriptoresTVSus,IngresosTVSus=APIsTVSus()    


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
        
        ServiciosMóviles=st.radio('Servicios',['Telefonía','Internet','Mensajería'],horizontal=True)
            
        st.markdown(r"""<hr>""",unsafe_allow_html=True)    
            
            
        if ServiciosMóviles=='Telefonía':
            dfAbonadosTelMovil=[];
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

            ServiciosTelMovil=st.selectbox('Escoja el ámbito de Telefonía móvil',['Abonados','Tráfico','Ingresos'])
            
            if ServiciosTelMovil=='Abonados':
                col1,col2,col3=st.columns(3)
                with col1:
                    LineaTiempoAbonadosTelmovil=st.button('Modalidad')
                with col2:
                    BarrasAbonadosTelmovil=st.button('Operadores')
                with col3:
                    PieAbonadosTelmovil=st.button('Participaciones')
                    
                if LineaTiempoAbonadosTelmovil:    
                    AboTrimTelMovil=AbonadosTelMovil.groupby(['periodo','empresa','id_empresa'])['abonados'].sum().reset_index()
                    AboTrimTelMovilA=AbonadosTelMovil.groupby(['periodo','modalidad'])['abonados'].sum().reset_index()
                    AboTrimTelMovilB=AbonadosTelMovil.groupby(['periodo'])['abonados'].sum().reset_index()
                    AboTrimTelMovilB['modalidad']='TOTAL'
                    AboTrimTelMovilTOTAL=pd.concat([AboTrimTelMovilA,AboTrimTelMovilB]).sort_values(by=['periodo'])
                    AboTrimTelMovilTOTAL['periodo_formato']=AboTrimTelMovilTOTAL['periodo'].apply(periodoformato)
                    st.plotly_chart(Plotlylineatiempo(AboTrimTelMovilTOTAL,'abonados','Millones',1e6,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
                if BarrasAbonadosTelmovil:
                    AbonadosTelMovil=AbonadosTelMovil[AbonadosTelMovil['trimestre']=='4']
                    AboAnualTelMovl=AbonadosTelMovil.groupby(['anno','empresa','id_empresa'])['abonados'].sum().reset_index()  
                    EmpTelMovilAbonados=AboAnualTelMovl[AboAnualTelMovl['anno']=='2021'].sort_values(by='abonados',ascending=False)['id_empresa'].to_list()[0:4]
                    AboAnualTelMovl=AboAnualTelMovl[(AboAnualTelMovl['id_empresa'].isin(EmpTelMovilAbonados))&(AboAnualTelMovl['anno'].isin(['2020','2021']))]
                    st.plotly_chart(PlotlyBarras(AboAnualTelMovl,'abonados','Millones',1e6,'Abonados anuales por empresa'),use_container_width=True)
                if PieAbonadosTelmovil:
                    AbonadosTelMovil=AbonadosTelMovil[AbonadosTelMovil['trimestre']=='4']
                    AboAnualTelMovl=AbonadosTelMovil.groupby(['anno','empresa','id_empresa'])['abonados'].sum().reset_index()  
                    AboAnualTelMovl=AboAnualTelMovl[(AboAnualTelMovl['anno']=='2021')]
                    AboAnualTelMovl['empresa']=AboAnualTelMovl['empresa'].replace(nombresComerciales)
                    AboAnualTelMovl['participacion']=round(100*AboAnualTelMovl['abonados']/AboAnualTelMovl['abonados'].sum(),1)
                    figPieTelMovil = px.pie(AboAnualTelMovl, values='abonados', names='empresa', color='empresa',
                                 color_discrete_map=Colores_pie, title='<b>Participación en abonados de telefonía móvil<br>(2021-T4)')
                    figPieTelMovil.update_traces(textposition='inside',textinfo='percent+label',hoverinfo='label+percent',textfont_color='black')
                    figPieTelMovil.update_layout(uniformtext_minsize=20,uniformtext_mode='hide',showlegend=True,legend=dict(x=0.9,y=0.3),title_x=0.5)
                    figPieTelMovil.update_layout(font_color="Black",title_font_family="NexaBlack",title_font_color="Black",titlefont_size=20)
                    st.plotly_chart(figPieTelMovil)
                               
            if ServiciosTelMovil=='Tráfico':
                
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoTraficoTelmovil=st.button('Modalidad')
                with col2:
                    BarrasTraficoTelmovil=st.button('Operadores')
                    
                if LineaTiempoTraficoTelmovil:    
                    TraficoTelMovil=TraficoTelMovil.rename(columns={'tipo_trafico':'modalidad'})
                    TraficoTelMovil['modalidad']=TraficoTelMovil['modalidad'].replace({'Tráfico pospago':'POSPAGO','Tráfico prepago':'PREPAGO'})
                    TrafTrimTelMovil=TraficoTelMovil.groupby(['periodo','empresa','id_empresa','modalidad'])['trafico'].sum().reset_index()                    
                    TrafTrimTelMovilA=TraficoTelMovil.groupby(['periodo','modalidad'])['trafico'].sum().reset_index()
                    TrafTrimTelMovilB=TraficoTelMovil.groupby(['periodo'])['trafico'].sum().reset_index()
                    TrafTrimTelMovilB['modalidad']='TOTAL'
                    TrafTrimTelMovilTOTAL=pd.concat([TrafTrimTelMovilA,TrafTrimTelMovilB]).sort_values(by=['periodo'])
                    TrafTrimTelMovilTOTAL['periodo_formato']=TrafTrimTelMovilTOTAL['periodo'].apply(periodoformato)
                    st.plotly_chart(Plotlylineatiempo(TrafTrimTelMovilTOTAL,'trafico','Miles de Millones de minutos',1e9,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
                if BarrasTraficoTelmovil:
                    TrafAnualTelMovl=TraficoTelMovil.groupby(['anno','empresa','id_empresa'])['trafico'].sum().reset_index()
                    EmpTelMovilTragfico=TrafAnualTelMovl[TrafAnualTelMovl['anno']=='2021'].sort_values(by='trafico',ascending=False)['id_empresa'].to_list()[0:4]
                    TrafAnualTelMovl=TrafAnualTelMovl[(TrafAnualTelMovl['id_empresa'].isin(EmpTelMovilTragfico))&(TrafAnualTelMovl['anno'].isin(['2020','2021']))]
                    st.plotly_chart(PlotlyBarras(TrafAnualTelMovl,'trafico','Miles de Millones de minutos',1e9,'Tráfico anual por empresa'),use_container_width=True)  
            
            if ServiciosTelMovil=='Ingresos':
                    
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoIngresosTelmovil=st.button('Modalidad')
                with col2:
                    BarrasIngresosTelmovil=st.button('Operadores')
                
                IngresosTelMovil=IngresosTelMovil.astype({'ingresos_totales':'int64','ingresos_prepago':'int64','ingresos_pospago':'int64'})
                IngresosTelMovil2=pd.melt(IngresosTelMovil,id_vars=['periodo','id_empresa','empresa'],value_vars=['ingresos_totales','ingresos_prepago',
                                                                                        'ingresos_pospago'],var_name='modalidad', value_name='ingresos')
                IngresosTelMovil2['modalidad']=IngresosTelMovil2['modalidad'].replace({'ingresos_totales':'TOTAL','ingresos_prepago':'PREPAGO','ingresos_pospago':'POSPAGO'})
                IngresosTelMovil2=IngresosTelMovil2[IngresosTelMovil2['ingresos']>0]
                IngresosTelMovil2Agg=IngresosTelMovil2.groupby(['periodo','modalidad'])['ingresos'].sum().reset_index()
                IngresosTelMovil2Agg['periodo_formato']=IngresosTelMovil2Agg['periodo'].apply(periodoformato)
                
                ## Limpieza Abonados
                AbonadosTelMovilB2=AbonadosTelMovil.groupby(['periodo','anno','trimestre','empresa','id_empresa'])['abonados'].sum().reset_index()
                AbonadosTelMovilB2['modalidad']='TOTAL'
                AbonadosTelMovilTOTAL2=pd.concat([AbonadosTelMovil,AbonadosTelMovilB2])
                ## Ingresos por Abonado
                IngresosPorAbonadoTelMovil=IngresosTelMovil2.merge(AbonadosTelMovilTOTAL2,left_on=['periodo','id_empresa','modalidad'],right_on=['periodo','id_empresa','modalidad'])
                IngresosPorAbonadoTelMovil2=IngresosPorAbonadoTelMovil.groupby(['periodo','modalidad']).agg({'ingresos':'sum','abonados':'sum'}).reset_index()
                IngresosPorAbonadoTelMovil2['Ingresos/Abonado']=round(IngresosPorAbonadoTelMovil2['ingresos']/IngresosPorAbonadoTelMovil2['abonados'],1)
                IngresosPorAbonadoTelMovil2['periodo_formato']=IngresosPorAbonadoTelMovil2['periodo'].apply(periodoformato)
                ## Limpieza tráfico
                TraficoTelMovil=TraficoTelMovil.rename(columns={'tipo_trafico':'modalidad'})
                TraficoTelMovil['modalidad']=TraficoTelMovil['modalidad'].replace({'Tráfico pospago':'POSPAGO','Tráfico prepago':'PREPAGO'})
                TraficoTelMovilB2=TraficoTelMovil.groupby(['periodo','anno','trimestre','empresa','id_empresa'])['trafico'].sum().reset_index()
                TraficoTelMovilB2['modalidad']='TOTAL'
                TraficoTelMovilTOTAL2=pd.concat([TraficoTelMovil,TraficoTelMovilB2])
                ##Ingresos por Tráfico
                IngresosPorTraficoTelMovil=IngresosTelMovil2.merge(TraficoTelMovilTOTAL2,left_on=['periodo','id_empresa','modalidad'],right_on=['periodo','id_empresa','modalidad'])
                IngresosPorTraficoTelMovil2=IngresosPorTraficoTelMovil.groupby(['periodo','modalidad']).agg({'ingresos':'sum','trafico':'sum'}).reset_index()
                IngresosPorTraficoTelMovil2['Ingresos/Trafico']=round(IngresosPorTraficoTelMovil2['ingresos']/IngresosPorTraficoTelMovil2['trafico'],1)
                IngresosPorTraficoTelMovil2['periodo_formato']=IngresosPorTraficoTelMovil2['periodo'].apply(periodoformato)

                if LineaTiempoIngresosTelmovil:
                    st.plotly_chart(Plotlylineatiempo(IngresosTelMovil2Agg,'ingresos','Miles de Millones de pesos',1e9,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
                    col1,col2=st.columns(2)
                    with col1:
                        st.plotly_chart(Plotlylineatiempo(IngresosPorAbonadoTelMovil2,'Ingresos/Abonado','Pesos',1,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
                    with col2:
                        st.plotly_chart(Plotlylineatiempo(IngresosPorTraficoTelMovil2,'Ingresos/Trafico','Pesos/Min',1,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
  
                if BarrasIngresosTelmovil:
                    IngresosTelMovil3=pd.melt(IngresosTelMovil,id_vars=['anno','id_empresa','empresa'],value_vars=['ingresos_totales','ingresos_prepago',
                                                                                        'ingresos_pospago'],var_name='modalidad', value_name='ingresos')
                    IngresosTelMovil3=IngresosTelMovil3[IngresosTelMovil3['modalidad']=='ingresos_totales']                                                                  
                    IngresosTelMovil3Agg=IngresosTelMovil3.groupby(['anno','id_empresa','empresa'])['ingresos'].sum().reset_index()   
                    EmpTelMovilIngresos=IngresosTelMovil3Agg[IngresosTelMovil3Agg['anno']=='2021'].sort_values(by='ingresos',ascending=False)['id_empresa'].to_list()[0:4]
                    IngresosTelMovil3Agg=IngresosTelMovil3Agg[(IngresosTelMovil3Agg['id_empresa'].isin(EmpTelMovilIngresos))&(IngresosTelMovil3Agg['anno'].isin(['2020','2021']))]
                    st.plotly_chart(PlotlyBarras(IngresosTelMovil3Agg,'ingresos','(Miles de Millones de COP)',1e9,'Ingresos anuales por empresa'),use_container_width=True)  
                    ##
                    IngresosPorAbonadoTelMovil=IngresosPorAbonadoTelMovil[(IngresosPorAbonadoTelMovil['trimestre']=='4')&(IngresosPorAbonadoTelMovil['modalidad']=='TOTAL')]
                    IngresosPorAbonadoTelMovil3=IngresosPorAbonadoTelMovil.groupby(['anno','empresa_x','id_empresa']).agg({'ingresos':'sum','abonados':'sum'}).reset_index()
                    IngresosPorAbonadoTelMovil3['Ingresos/Abonado']=round(IngresosPorAbonadoTelMovil3['ingresos']/IngresosPorAbonadoTelMovil3['abonados'],2)
                    IngresosPorAbonadoTelMovil3=IngresosPorAbonadoTelMovil3[(IngresosPorAbonadoTelMovil3['id_empresa'].isin(EmpTelMovilIngresos))&(IngresosPorAbonadoTelMovil3['anno'].isin(['2020','2021']))]
                    IngresosPorAbonadoTelMovil3=IngresosPorAbonadoTelMovil3.rename(columns={'empresa_x':'empresa'})
                    ##
                    IngresosPorTraficoTelMovil3=IngresosPorTraficoTelMovil.groupby(['anno','empresa_x','id_empresa']).agg({'ingresos':'sum','trafico':'sum'}).reset_index()
                    IngresosPorTraficoTelMovil3['Ingresos/Trafico']=round(IngresosPorTraficoTelMovil3['ingresos']/IngresosPorTraficoTelMovil3['trafico'],2)
                    IngresosPorTraficoTelMovil3=IngresosPorTraficoTelMovil3[(IngresosPorTraficoTelMovil3['id_empresa'].isin(EmpTelMovilIngresos))&(IngresosPorTraficoTelMovil3['anno'].isin(['2020','2021']))]
                    IngresosPorTraficoTelMovil3=IngresosPorTraficoTelMovil3.rename(columns={'empresa_x':'empresa'})
                    
                    
                    col1,col2=st.columns(2)
                    with col1:
                        st.plotly_chart(PlotlyBarras(IngresosPorAbonadoTelMovil3,'Ingresos/Abonado','(COP)',1,'Ingresos/Abonado anual por empresa'),use_container_width=True)  
                    with col2:
                        st.plotly_chart(PlotlyBarras(IngresosPorTraficoTelMovil3,'Ingresos/Trafico','(COP/Min)',1,'Ingresos/Trafico anual por empresa'),use_container_width=True)  
                                                                                                 
        if ServiciosMóviles=='Internet':

            TraficoInternetMovil=TraficoInternetMovil[TraficoInternetMovil['trafico']>0]
            TraficoInternetMovil=TraficoInternetMovil.rename(columns={'trafico demanda':'DEMANDA','trafico cargo fijo':'CARGO FIJO','trafico':'TOTAL'})
            IngresosInternetmovil=IngresosInternetmovil[IngresosInternetmovil['ingresos']>0]
            AccesosInternetmovil=AccesosInternetmovil[AccesosInternetmovil['accesos']>0]
            AccesosInternetmovil=AccesosInternetmovil.rename(columns={'sum_cantidad_abonados':'ABONADOS','sum_cantidad_suscriptores':'SUSCRIPTORES','accesos':'TOTAL'})
            AccesosInternetmovil['empresa']=AccesosInternetmovil['empresa'].replace({'COLOMBIA TELECOMUNICACIONES S.A. E.S.P.':'COLOMBIA TELECOMUNICACIONES S.A. ESP',
            AccesosInternetmovil['empresa'].unique().tolist()[2]:'COLOMBIA MOVIL S.A. E.S.P.','EMPRESA DE TELECOMUNICACIONES DE BOGOTA S.A. ESP':'EMPRESA DE TELECOMUNICACIONES DE BOGOTÁ S.A. ESP.',
            'AVANTEL S.A.S':'AVANTEL S.A.S.'})
            
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
                AccesosInternetmovil2=pd.melt(AccesosInternetmovil,id_vars=['periodo','anno','trimestre','id_empresa','empresa'],value_vars=['ABONADOS','SUSCRIPTORES',
                                                                                        'TOTAL'],var_name='modalidad', value_name='accesos')

                col1,col2,col3=st.columns(3)
                with col1:
                    LineaTiempoAccesosIntmovil=st.button('Modalidad')
                with col2:
                    BarrasAccesosIntmovil=st.button('Operadores')
                with col3:
                    PieAccesosIntmovil=st.button('Participaciones')    
                 
                if LineaTiempoAccesosIntmovil:
                    AccesosInternetmovilNac=AccesosInternetmovil2.groupby(['periodo','modalidad'])['accesos'].sum().reset_index()
                    AccesosInternetmovilNac['periodo_formato']=AccesosInternetmovilNac['periodo'].apply(periodoformato)
                    st.plotly_chart(Plotlylineatiempo(AccesosInternetmovilNac,'accesos','Millones',1e6,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
                if BarrasAccesosIntmovil:
                    AccesosInternetmovilEmp=AccesosInternetmovil2[(AccesosInternetmovil2['modalidad']=='TOTAL')&(AccesosInternetmovil2['trimestre']=='4')&(AccesosInternetmovil2['anno'].isin(['2020','2021']))]
                    EmpIntMovilAccesos=AccesosInternetmovilEmp[AccesosInternetmovilEmp['anno']=='2021'].sort_values(by='accesos',ascending=False)['id_empresa'].to_list()[0:4]
                    AccesosInternetmovilEmp=AccesosInternetmovilEmp[AccesosInternetmovilEmp['id_empresa'].isin(EmpIntMovilAccesos)]
                    AccesosInternetmovilEmp=AccesosInternetmovilEmp.groupby(['anno','empresa','id_empresa'])['accesos'].sum().reset_index()
                    st.plotly_chart(PlotlyBarras(AccesosInternetmovilEmp,'accesos','Millones',1e6,'Accesos anuales por empresa'),use_container_width=True)
                if PieAccesosIntmovil:
                    AccesosInternetmovilPie=AccesosInternetmovil2[(AccesosInternetmovil2['modalidad']=='TOTAL')&(AccesosInternetmovil2['trimestre']=='4')&(AccesosInternetmovil2['anno'].isin(['2021']))]
                    AccesosInternetmovilPie=AccesosInternetmovilPie.groupby(['anno','empresa','id_empresa'])['accesos'].sum().reset_index()
                    AccesosInternetmovilPie['empresa']=AccesosInternetmovilPie['empresa'].replace(nombresComerciales)
                    AccesosInternetmovilPie['participacion']=round(100*AccesosInternetmovilPie['accesos']/AccesosInternetmovilPie['accesos'].sum(),1)
                    figPieIntMovil = px.pie(AccesosInternetmovilPie, values='accesos', names='empresa', color='empresa',
                                 color_discrete_map=Colores_pie,title='<b>Participación en accesos de Internet móvil<br>(2021-T4)')
                    figPieIntMovil.update_traces(textposition='inside',textinfo='percent+label',hoverinfo='label+percent',textfont_color='black')
                    figPieIntMovil.update_layout(uniformtext_minsize=20,uniformtext_mode='hide',showlegend=True,legend=dict(x=0.9,y=0.3),title_x=0.5)
                    figPieIntMovil.update_layout(font_color="Black",title_font_family="NexaBlack",title_font_color="Black",titlefont_size=20)
                    st.plotly_chart(figPieIntMovil)
                
            if ServiciosIntMovil=='Tráfico':
                
                TraficoInternetMovil2=pd.melt(TraficoInternetMovil,id_vars=['periodo','anno','trimestre','id_empresa','empresa'],value_vars=['DEMANDA','CARGO FIJO',
                                                                                        'TOTAL'],var_name='modalidad', value_name='trafico')
                TraficoInternetMovil2['trafico']=TraficoInternetMovil2['trafico']/1000                                                                        
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoTraficoIntmovil=st.button('Modalidad')
                with col2:
                    BarrasTraficoIntmovil=st.button('Operadores')
                if LineaTiempoTraficoIntmovil:             
                    TraficoInternetMovilNac=TraficoInternetMovil2.groupby(['periodo','modalidad'])['trafico'].sum().reset_index()
                    TraficoInternetMovilNac['periodo_formato']=TraficoInternetMovilNac['periodo'].apply(periodoformato)
                    st.plotly_chart(Plotlylineatiempo(TraficoInternetMovilNac,'trafico','Millones de GB',1e6,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
                if BarrasTraficoIntmovil:
                    TraficoInternetMovilEmp=TraficoInternetMovil2.groupby(['anno','modalidad','empresa','id_empresa'])['trafico'].sum().reset_index()
                    TraficoInternetMovilEmp=TraficoInternetMovilEmp[(TraficoInternetMovilEmp['modalidad']=='TOTAL')&(TraficoInternetMovilEmp['anno'].isin(['2020','2021']))]
                    EmpIntMovilTrafico=TraficoInternetMovilEmp[TraficoInternetMovilEmp['anno']=='2021'].sort_values(by='trafico',ascending=False)['id_empresa'].to_list()[0:4]
                    TraficoInternetMovilEmp=TraficoInternetMovilEmp[TraficoInternetMovilEmp['id_empresa'].isin(EmpIntMovilTrafico)]
                    st.plotly_chart(PlotlyBarras(TraficoInternetMovilEmp,'trafico','Millones de GB',1e6,'Tráfico anual por empresa'),use_container_width=True)

            if ServiciosIntMovil=='Ingresos':
                IngresosInternetmovil=IngresosInternetmovil.rename(columns={'ingresos':'TOTAL'})
                IngresosInternetmovil2=pd.melt(IngresosInternetmovil,id_vars=['periodo','anno','trimestre','id_empresa','empresa'],value_vars=['DEMANDA','CARGO FIJO',
                                                                                        'TOTAL'],var_name='modalidad', value_name='ingresos')
                
                IngresosInternetmovilNac=IngresosInternetmovil2.groupby(['periodo','modalidad'])['ingresos'].sum().reset_index()
                IngresosInternetmovilNac['periodo_formato']=IngresosInternetmovilNac['periodo'].apply(periodoformato)
                
                IngresosInternetmovilEmp=IngresosInternetmovil2.groupby(['anno','modalidad','empresa','id_empresa'])['ingresos'].sum().reset_index() 
                IngresosInternetmovilEmp=IngresosInternetmovilEmp[(IngresosInternetmovilEmp['anno'].isin(['2020','2021']))&(IngresosInternetmovilEmp['modalidad']=='TOTAL')]
                EmpIntMovilIngresos=IngresosInternetmovilEmp[IngresosInternetmovilEmp['anno']=='2021'].sort_values(by='ingresos',ascending=False)['id_empresa'].to_list()[0:4]
                IngresosInternetmovilEmp=IngresosInternetmovilEmp[IngresosInternetmovilEmp['id_empresa'].isin(EmpIntMovilIngresos)]
                ## Limpieza accesos
                AccesosInternetmovil2=pd.melt(AccesosInternetmovil,id_vars=['periodo','anno','trimestre','id_empresa','empresa'],value_vars=['ABONADOS','SUSCRIPTORES',
                                                                                        'TOTAL'],var_name='modalidad', value_name='accesos')                
                AccesosInternetmovilNac=AccesosInternetmovil2.groupby(['periodo','modalidad'])['accesos'].sum().reset_index()
                AccesosInternetmovilNac['modalidad']=AccesosInternetmovilNac['modalidad'].replace({'ABONADOS':'DEMANDA','SUSCRIPTORES':'CARGO FIJO'})
                AccesosInternetmovilEmp=AccesosInternetmovil2[(AccesosInternetmovil2['modalidad']=='TOTAL')&(AccesosInternetmovil2['trimestre']=='4')&(AccesosInternetmovil2['anno'].isin(['2020','2021']))&(AccesosInternetmovil2['id_empresa'].isin(EmpIntMovilIngresos))]
                AccesosInternetmovilEmp=AccesosInternetmovilEmp.groupby(['anno','empresa','modalidad','id_empresa'])['accesos'].sum().reset_index()  
                AccesosInternetmovilEmp=AccesosInternetmovilEmp[(AccesosInternetmovilEmp['anno'].isin(['2020','2021']))&(AccesosInternetmovilEmp['id_empresa'].isin(EmpIntMovilIngresos))]

                ## Limpieza tráfico
                TraficoInternetMovil2=pd.melt(TraficoInternetMovil,id_vars=['periodo','anno','trimestre','id_empresa','empresa'],value_vars=['DEMANDA','CARGO FIJO',
                                                                                        'TOTAL'],var_name='modalidad', value_name='trafico')
                TraficoInternetMovil2['trafico']=TraficoInternetMovil2['trafico']/1000              
                TraficoInternetMovilNac=TraficoInternetMovil2.groupby(['periodo','modalidad'])['trafico'].sum().reset_index() 
                TraficoInternetMovilEmp=TraficoInternetMovil2.groupby(['anno','modalidad','id_empresa','empresa'])['trafico'].sum().reset_index()                 
                TraficoInternetMovilEmp=TraficoInternetMovilEmp[(TraficoInternetMovilEmp['anno'].isin(['2020','2021']))&(TraficoInternetMovilEmp['id_empresa'].isin(EmpIntMovilIngresos))]
                
                IngPorTraficoIntMovilEmp=IngresosInternetmovilEmp.merge(TraficoInternetMovilEmp,left_on=['anno','modalidad','id_empresa'],right_on=['anno','modalidad','id_empresa'])
                IngPorTraficoIntMovilEmp['Ingresos/Trafico']=round(IngPorTraficoIntMovilEmp['ingresos']/IngPorTraficoIntMovilEmp['trafico'],2)
                IngPorTraficoIntMovilEmp=IngPorTraficoIntMovilEmp[IngPorTraficoIntMovilEmp['modalidad']=='TOTAL']
                ## Ingresos por acceso
                IngPorAccesosIntMovil=IngresosInternetmovilNac.merge(AccesosInternetmovilNac,left_on=['periodo','modalidad'],right_on=['periodo','modalidad'])
                IngPorAccesosIntMovil['Ingresos/Acceso']=round(IngPorAccesosIntMovil['ingresos']/IngPorAccesosIntMovil['accesos'],2)
                IngPorAccesosIntMovil['periodo_formato']=IngPorAccesosIntMovil['periodo'].apply(periodoformato)
                IngPorAccesosIntMovilEmp=IngresosInternetmovilEmp.merge(AccesosInternetmovilEmp,left_on=['anno','modalidad','id_empresa'],right_on=['anno','modalidad','id_empresa'])
                IngPorAccesosIntMovilEmp['Ingresos/Acceso']=round(IngPorAccesosIntMovilEmp['ingresos']/IngPorAccesosIntMovilEmp['accesos'],2)
                IngPorAccesosIntMovilEmp=IngPorAccesosIntMovilEmp[IngPorAccesosIntMovilEmp['modalidad']=='TOTAL']

                ## Ingresos por tráfico
                IngPorTraficoIntMovil=IngresosInternetmovilNac.merge(TraficoInternetMovilNac,left_on=['periodo','modalidad'],right_on=['periodo','modalidad'])
                IngPorTraficoIntMovil['Ingresos/Trafico']=round(IngPorTraficoIntMovil['ingresos']/IngPorTraficoIntMovil['trafico'],2)
                IngPorTraficoIntMovil['periodo_formato']=IngPorTraficoIntMovil['periodo'].apply(periodoformato)     
                
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoIngresosIntmovil=st.button('Modalidad')
                with col2:
                    BarrasIngresosIntmovil=st.button('Operadores')            
                
                if LineaTiempoIngresosIntmovil:
                                                                                                    
                    st.plotly_chart(Plotlylineatiempo(IngresosInternetmovilNac,'ingresos','Miles de Millones de pesos',1e9,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
                    col1,col2=st.columns(2)
                    with col1:
                        st.plotly_chart(Plotlylineatiempo(IngPorAccesosIntMovil,'Ingresos/Acceso','Pesos',1,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
                    with col2:    
                        st.plotly_chart(Plotlylineatiempo(IngPorTraficoIntMovil,'Ingresos/Trafico','Pesos/GB',1,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
 
                if BarrasIngresosIntmovil:
                    st.plotly_chart(PlotlyBarras(IngresosInternetmovilEmp,'ingresos','Miles de Millones de pesos',1e9,'Ingresos anuales por empresa'),use_container_width=True)
                    col1,col2=st.columns(2)
                    with col1:
                        IngPorAccesosIntMovilEmp=IngPorAccesosIntMovilEmp.rename(columns={'empresa_x':'empresa'})
                        st.plotly_chart(PlotlyBarras(IngPorAccesosIntMovilEmp,'Ingresos/Acceso','Pesos',1,'Ingresos/Accesos anuales por empresa'),use_container_width=True)
                    with col2:
                        IngPorTraficoIntMovilEmp=IngPorTraficoIntMovilEmp.rename(columns={'empresa_x':'empresa'})
                        st.plotly_chart(PlotlyBarras(IngPorTraficoIntMovilEmp,'Ingresos/Trafico','Pesos/GB',1,'Ingresos/Tráfico anual por empresa'),use_container_width=True)
 
        if ServiciosMóviles=='Mensajería':
            st.markdown(r"""<div class='IconoTitulo'><img height="50px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/Iconos/SMSTelMovil.jpg?raw=true'/><h4>Mensajería móvil</h4></div>""",unsafe_allow_html=True)

            ServiciosMenMovil=st.selectbox('Escoja el ámbito de Mensajería móvil',['Tráfico','Ingresos']) 
            
            if ServiciosMenMovil=='Tráfico':
                TraficoSMSTelMovil['periodo']=TraficoSMSTelMovil['anno']+'-T'+TraficoSMSTelMovil['trimestre']
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoTraficoSMSTelmovil=st.button('Evolución temporal')
                with col2:
                    BarrasTraficoSMSTelmovil=st.button('Operadores') 
                        
                if LineaTiempoTraficoSMSTelmovil:
                    TraficoSMSTelMovil=TraficoSMSTelMovil.rename(columns={'cantidad':'tráfico (SMS)'})
                    TraficoSMSTelMovilAgg=TraficoSMSTelMovil.groupby(['periodo'])['tráfico (SMS)'].sum().reset_index()
                    TraficoSMSTelMovilAgg['periodo_formato']=TraficoSMSTelMovilAgg['periodo'].apply(periodoformato)
                    st.plotly_chart(Plotlylineatiempo(TraficoSMSTelMovilAgg,'tráfico (SMS)','Millones de mensajes',1e6,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
                if BarrasTraficoSMSTelmovil:
                    TraficoSMSTelMovil=TraficoSMSTelMovil.rename(columns={'cantidad':'tráfico (SMS)'})
                    TraficoSMSTelMovilEmpresa=TraficoSMSTelMovil.groupby(['anno','empresa','id_empresa'])['tráfico (SMS)'].sum().reset_index() 
                    EmpMenMovilTraficoSMS=TraficoSMSTelMovilEmpresa[TraficoSMSTelMovilEmpresa['anno']=='2021'].sort_values(by='tráfico (SMS)',ascending=False)['id_empresa'].to_list()[0:4]
                    TraficoSMSTelMovilEmpresa=TraficoSMSTelMovilEmpresa[(TraficoSMSTelMovilEmpresa['id_empresa'].isin(EmpMenMovilTraficoSMS))&(TraficoSMSTelMovilEmpresa['anno'].isin(['2020','2021']))]
                    st.plotly_chart(PlotlyBarras(TraficoSMSTelMovilEmpresa,'tráfico (SMS)','Millones de mensajes',1e6,'Tráfico (SMS) anual por empresa'),use_container_width=True)  
                
            if ServiciosMenMovil=='Ingresos':
                IngresosSMSTelMovil['periodo']=IngresosSMSTelMovil['anno']+'-T'+IngresosSMSTelMovil['trimestre']
                
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoIngresosSMSTelmovil=st.button('Evolución temporal')
                with col2:
                    BarrasIngresosSMSTelmovil=st.button('Operadores')
                ## Limpieza Ingresos SMS    
                IngresosSMSTelMovilAgg=IngresosSMSTelMovil.groupby(['periodo'])['ingresos'].sum().reset_index()
                IngresosSMSTelMovilAgg['periodo_formato']=IngresosSMSTelMovilAgg['periodo'].apply(periodoformato)
                IngresosSMSTelMovilEmpresa=IngresosSMSTelMovil.groupby(['anno','empresa','id_empresa'])['ingresos'].sum().reset_index()
                EmpMenMovilTraficoSMS=IngresosSMSTelMovilEmpresa[IngresosSMSTelMovilEmpresa['anno']=='2021'].sort_values(by='ingresos',ascending=False)['id_empresa'].to_list()[0:4]
                IngresosSMSTelMovilEmpresa=IngresosSMSTelMovilEmpresa[(IngresosSMSTelMovilEmpresa['id_empresa'].isin(EmpMenMovilTraficoSMS))&(IngresosSMSTelMovilEmpresa['anno'].isin(['2020','2021']))]

                ## Limpieza Tráfico SMS
                TraficoSMSTelMovil=TraficoSMSTelMovil.rename(columns={'cantidad':'tráfico'})
                TraficoSMSTelMovilAgg=TraficoSMSTelMovil.groupby(['periodo'])['tráfico'].sum().reset_index()
                ## Ingresos/TraficoSMS
                IngresosPorTraficoSMSTelMovil=IngresosSMSTelMovil.merge(TraficoSMSTelMovil, left_on=['periodo','anno','trimestre','empresa','id_empresa'],right_on=['periodo','anno','trimestre','empresa','id_empresa'])
                IngresosPorTraficoSMSTelMovilAgg=IngresosPorTraficoSMSTelMovil.groupby(['periodo']).agg({'ingresos':'sum','tráfico':'sum'}).reset_index()
                IngresosPorTraficoSMSTelMovilAgg['Ingresos/Tráfico']=round(IngresosPorTraficoSMSTelMovilAgg['ingresos']/IngresosPorTraficoSMSTelMovilAgg['tráfico'],2)
                IngresosPorTraficoSMSTelMovilAgg['periodo_formato']=IngresosPorTraficoSMSTelMovilAgg['periodo'].apply(periodoformato)
                
                IngresosPorTraficoSMSTelMovilEmp=IngresosPorTraficoSMSTelMovil.groupby(['anno','empresa','id_empresa']).agg({'ingresos':'sum','tráfico':'sum'}).reset_index()
                IngresosPorTraficoSMSTelMovilEmp=IngresosPorTraficoSMSTelMovilEmp[(IngresosPorTraficoSMSTelMovilEmp['id_empresa'].isin(['830122566','800153993','830114921']))&(IngresosPorTraficoSMSTelMovilEmp['anno'].isin(['2020','2021']))]
                IngresosPorTraficoSMSTelMovilEmp['Ingresos/Tráfico']=round(IngresosPorTraficoSMSTelMovilEmp['ingresos']/IngresosPorTraficoSMSTelMovilEmp['tráfico'],2)

                ## 
                if LineaTiempoIngresosSMSTelmovil:
                    st.plotly_chart(Plotlylineatiempo(IngresosSMSTelMovilAgg,'ingresos','Miles de Millones de pesos',1e9,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
                    st.plotly_chart(Plotlylineatiempo(IngresosPorTraficoSMSTelMovilAgg,'Ingresos/Tráfico','Pesos/Min',1,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
                if BarrasIngresosSMSTelmovil:                    
                    st.plotly_chart(PlotlyBarras(IngresosSMSTelMovilEmpresa,'ingresos','Miles de Millones de pesos',1e9,'Ingresos (SMS) anuales por empresa'),use_container_width=True)  
                    st.plotly_chart(PlotlyBarras(IngresosPorTraficoSMSTelMovilEmp,'Ingresos/Tráfico','Pesos/Min',1,'Ingresos/Tráfico (SMS) anual por empresa'),use_container_width=True)  
                        
    if select_secResumenDinTic == 'Servicios fijos': 
        st.markdown(r"""<div class="titulo"><h3>Servicios fijos</h3></div>""",unsafe_allow_html=True)
        st.markdown("<center>Para continuar, por favor seleccione el botón con el servicio del cual desea conocer la información</center>",unsafe_allow_html=True)

        ServiciosFijos=st.radio('Servicios',['Telefonía fija','Internet fijo'],horizontal=True)
        st.markdown(r"""<hr>""",unsafe_allow_html=True)   
        if ServiciosFijos == 'Internet fijo':
            st.markdown(r"""<div class='IconoTitulo'><img height="50px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/Iconos/VozTelMovil.jpg?raw=true'/><h4 style="text-align:left">Internet fijo</h4></div>""",unsafe_allow_html=True)   
            
            AccesosCorpIntFijo=AccesosCorpIntFijo[AccesosCorpIntFijo['accesos']>0]
            AccesosCorpIntFijo=AccesosCorpIntFijo.rename(columns={'accesos':'CORPORATIVOS'})
            AccesosCorpIntFijo['periodo']=AccesosCorpIntFijo['anno']+'-T'+AccesosCorpIntFijo['trimestre']
            AccesosResIntFijo=AccesosResIntFijo[AccesosResIntFijo['accesos']>0]
            AccesosResIntFijo=AccesosResIntFijo.rename(columns={'accesos':'RESIDENCIALES'})
            AccesosResIntFijo['periodo']=AccesosResIntFijo['anno']+'-T'+AccesosResIntFijo['trimestre']
            ##
            AccesosCorpIntFijoNac=AccesosCorpIntFijo.groupby(['periodo'])['CORPORATIVOS'].sum().reset_index()
            AccesosResIntFijoNac=AccesosResIntFijo.groupby(['periodo'])['RESIDENCIALES'].sum().reset_index()
            AccesosCorpIntFijoEmp=AccesosCorpIntFijo.groupby(['anno','id_empresa','empresa'])['CORPORATIVOS'].sum().reset_index()
            AccesosResIntFijoEmp=AccesosResIntFijo.groupby(['anno','id_empresa','empresa'])['RESIDENCIALES'].sum().reset_index()
            ##
            AccesosCorpIntFijoPie=AccesosCorpIntFijo.groupby(['periodo','id_empresa','empresa'])['CORPORATIVOS'].sum().reset_index()
            AccesosCorpIntFijoPie['modalidad']='CORPORATIVO'
            AccesosCorpIntFijoPie=AccesosCorpIntFijoPie.rename(columns={'CORPORATIVOS':'accesos'})
            AccesosResIntFijoPie=AccesosResIntFijo.groupby(['periodo','id_empresa','empresa'])['RESIDENCIALES'].sum().reset_index()
            AccesosResIntFijoPie['modalidad']='RESIDENCIAL'
            AccesosResIntFijoPie=AccesosResIntFijoPie.rename(columns={'RESIDENCIALES':'accesos'})            
            ##
            AccesosCorpIntFijoTec=AccesosCorpIntFijo.groupby(['periodo','id_empresa','empresa','id_tecnologia','tecnologia'])['CORPORATIVOS'].sum().reset_index()
            AccesosCorpIntFijoTec['modalidad']='CORPORATIVO'
            AccesosCorpIntFijoTec=AccesosCorpIntFijoTec.rename(columns={'CORPORATIVOS':'accesos'})
            AccesosResIntFijoTec=AccesosResIntFijo.groupby(['periodo','id_empresa','empresa','id_tecnologia','tecnologia'])['RESIDENCIALES'].sum().reset_index()
            AccesosResIntFijoTec['modalidad']='RESIDENCIAL'
            AccesosResIntFijoTec=AccesosResIntFijoTec.rename(columns={'RESIDENCIALES':'accesos'})    
            ##
            IngresosInternetFijo=IngresosInternetFijo[IngresosInternetFijo['ingresos']>0]
            IngresosInternetFijo['periodo']=IngresosInternetFijo['anno']+'-T'+IngresosInternetFijo['trimestre']
            
            IngresosInternetFijoNac=IngresosInternetFijo.groupby(['periodo'])['ingresos'].sum().reset_index()
            IngresosInternetFijoNacProm=IngresosInternetFijo.groupby(['periodo'])['ingresos'].mean().reset_index()
            IngresosInternetFijoEmp=IngresosInternetFijo.groupby(['anno','empresa','id_empresa'])['ingresos'].sum().reset_index()
            
            ServiciosIntFijo=st.selectbox('Escoja el servicio de Internet fijo',['Accesos','Ingresos'])
            st.markdown('Escoja la dimensión del análisis')
            
            if ServiciosIntFijo=='Accesos':
                col1,col2,col3,col4=st.columns(4)
                with col1:
                    LineaTiempoAccesosIntFijo=st.button('Modalidad')
                with col2:
                    BarrasAccesosIntFijo=st.button('Operadores')
                with col3:
                    PieAccesosIntFijo=st.button('Participaciones')
                with col4:
                    TecnologiaAccesosIntFijo=st.button('Tecnología')    
                    
                AccesosInternetFijoNac=AccesosCorpIntFijoNac.merge(AccesosResIntFijoNac,left_on=['periodo'],right_on=['periodo'])
                AccesosInternetFijoNac['TOTAL']=AccesosInternetFijoNac['CORPORATIVOS']+AccesosInternetFijoNac['RESIDENCIALES']
                AccesosInternetFijoNac2=pd.melt(AccesosInternetFijoNac,id_vars=['periodo'],value_vars=['CORPORATIVOS',
                'RESIDENCIALES','TOTAL'],var_name='modalidad',value_name='accesos')
                ##
                AccesosInternetFijoEmp=AccesosCorpIntFijoEmp.merge(AccesosResIntFijoEmp,left_on=['anno','id_empresa'],right_on=['anno','id_empresa'])
                AccesosInternetFijoEmp['TOTAL']=AccesosInternetFijoEmp['CORPORATIVOS']+AccesosInternetFijoEmp['RESIDENCIALES']
                AccesosInternetFijoEmp=AccesosInternetFijoEmp.rename(columns={'empresa_x':'empresa'})
                AccesosInternetFijoEmp=AccesosInternetFijoEmp.drop(columns=['empresa_y'])
                AccesosInternetFijoEmp2=pd.melt(AccesosInternetFijoEmp,id_vars=['anno','id_empresa','empresa'],value_vars=['CORPORATIVOS',
                'RESIDENCIALES','TOTAL'],var_name='modalidad',value_name='accesos')
                AccesosInternetFijoEmp2=AccesosInternetFijoEmp2[AccesosInternetFijoEmp2['modalidad']=='TOTAL']    
                EmpIntFijoAccesos=AccesosInternetFijoEmp2[AccesosInternetFijoEmp2['anno']=='2021'].sort_values(by='accesos',ascending=False)['id_empresa'].to_list()[0:4]
                AccesosInternetFijoEmp2=AccesosInternetFijoEmp2[(AccesosInternetFijoEmp2['id_empresa'].isin(EmpIntFijoAccesos))&(AccesosInternetFijoEmp2['anno'].isin(['2020','2021']))]
                ##
                AccesosInternetFijoPie=pd.concat([AccesosCorpIntFijoPie,AccesosResIntFijoPie])
                AccesosInternetFijoPieAgg=AccesosInternetFijoPie.groupby(['periodo','id_empresa','empresa'])['accesos'].sum().reset_index()
                AccesosInternetFijoPieAgg=AccesosInternetFijoPieAgg[AccesosInternetFijoPieAgg['periodo']=='2021-T4']
                AccesosInternetFijoPieAgg['participacion']=round(100*AccesosInternetFijoPieAgg['accesos']/AccesosInternetFijoPieAgg['accesos'].sum(),1)
                AccesosInternetFijoPieAgg.loc[AccesosInternetFijoPieAgg['participacion']<=1,'empresa']='Otros'
                AccesosInternetFijoPieAgg['empresa']=AccesosInternetFijoPieAgg['empresa'].replace(nombresComerciales)
                ##
                AccesosInternetFijoTec=pd.concat([AccesosCorpIntFijoTec,AccesosResIntFijoTec])
                AccesosInternetFijoTec=AccesosInternetFijoTec.groupby(['periodo','id_empresa','empresa','id_tecnologia','tecnologia'])['accesos'].sum().reset_index()
                AccesosInternetFijoTec['id_tecnologia']=AccesosInternetFijoTec['id_tecnologia'].astype('int64')
                AccesosInternetFijoTec['CodTec']=None
                AccesosInternetFijoTec['CodTec']=np.where(AccesosInternetFijoTec.id_tecnologia.isin([1,4,7,9,114,105,104]),'Inalambrico',AccesosInternetFijoTec['CodTec'])
                AccesosInternetFijoTec['CodTec']=np.where(AccesosInternetFijoTec.id_tecnologia.isin([5,102,106]),'Cable',AccesosInternetFijoTec['CodTec'])
                AccesosInternetFijoTec['CodTec']=np.where(AccesosInternetFijoTec.id_tecnologia.isin([6,103]),'Satelital',AccesosInternetFijoTec['CodTec'])
                AccesosInternetFijoTec['CodTec']=np.where(AccesosInternetFijoTec.id_tecnologia.isin([8,41,42,107,108,109,110,111,112,113]),'Fibra Óptica',AccesosInternetFijoTec['CodTec'])
                AccesosInternetFijoTec['CodTec']=np.where(AccesosInternetFijoTec.id_tecnologia.isin([2,101]),'xDSL',AccesosInternetFijoTec['CodTec'])
                AccesosInternetFijoTec['CodTec']=np.where(AccesosInternetFijoTec.id_tecnologia.isin([3,10,31,115]),'Otras',AccesosInternetFijoTec['CodTec'])
                AccesosInternetFijoTecAgg=AccesosInternetFijoTec.groupby(['periodo','CodTec'])['accesos'].sum().reset_index()
                
                if LineaTiempoAccesosIntFijo:
                    AccesosInternetFijoNac2['periodo_formato']=AccesosInternetFijoNac2['periodo'].apply(periodoformato)
                    st.plotly_chart(Plotlylineatiempo(AccesosInternetFijoNac2,'accesos','Millones',1e6,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
                if BarrasAccesosIntFijo:
                    st.plotly_chart(PlotlyBarras(AccesosInternetFijoEmp2,'accesos','Millones',1e6,'Accesos anuales por empresa'),use_container_width=True)
                if PieAccesosIntFijo:
                    figPieIntFijo = px.pie(AccesosInternetFijoPieAgg, values='accesos', names='empresa', color='empresa',
                                 color_discrete_map=Colores_pie2, title='<b>Participación en accesos de Internet fijo<br>(2021-T4)')
                    figPieIntFijo.update_traces(textposition='inside',textinfo='percent+label',hoverinfo='label+percent',textfont_color='black')
                    figPieIntFijo.update_layout(uniformtext_minsize=18,uniformtext_mode='hide',showlegend=True,legend=dict(x=0.9,y=0.3),title_x=0.5)
                    figPieIntFijo.update_layout(font_color="Black",title_font_family="NexaBlack",title_font_color="Black",titlefont_size=20)
                    st.plotly_chart(figPieIntFijo)
                if TecnologiaAccesosIntFijo:
                    AccesosInternetFijoTecAgg['periodo_formato']=AccesosInternetFijoTecAgg['periodo'].apply(periodoformato)
                    st.plotly_chart(PlotlylineatiempoTec(AccesosInternetFijoTecAgg,'accesos','Millones',1e6,['rgb(255, 51, 51)','rgb(255, 153, 51)','rgb(153,255,51)','rgb(160, 160, 160)','rgb(51, 153, 255)','rgb(153,51,255)']), use_container_width=True)

            if ServiciosIntFijo=='Ingresos':
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoIngresosIntFijo=st.button('Evolución temporal')
                with col2:
                    BarrasIngresosIntFijo=st.button('Operadores')

                ## Ingresos/Accceso total
                AccesosInternetFijoNac=AccesosCorpIntFijoNac.merge(AccesosResIntFijoNac,left_on=['periodo'],right_on=['periodo'])
                AccesosInternetFijoNac['TOTAL']=AccesosInternetFijoNac['CORPORATIVOS']+AccesosInternetFijoNac['RESIDENCIALES']
                IngresosPorAccesoIntFijo=IngresosInternetFijoNac.merge(AccesosInternetFijoNac,left_on=['periodo'],right_on=['periodo'])
                IngresosPorAccesoIntFijo['Ingresos/Accceso']=round(IngresosPorAccesoIntFijo['ingresos']/IngresosPorAccesoIntFijo['TOTAL'],2)
                
                if LineaTiempoIngresosIntFijo: 
                    IngresosInternetFijoNac['periodo_formato']=IngresosInternetFijoNac['periodo'].apply(periodoformato)
                    IngresosPorAccesoIntFijo['periodo_formato']=IngresosPorAccesoIntFijo['periodo'].apply(periodoformato)
                    st.plotly_chart(Plotlylineatiempo(IngresosInternetFijoNac,'ingresos','Miles de Millones de pesos',1e9,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
                    st.plotly_chart(Plotlylineatiempo(IngresosPorAccesoIntFijo,'Ingresos/Accceso','Pesos',1,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
                if BarrasIngresosIntFijo:
                    EmpIntFijoIngresos=IngresosInternetFijoEmp[IngresosInternetFijoEmp['anno']=='2021'].sort_values(by='ingresos',ascending=False)['id_empresa'].to_list()[0:4]
                    IngresosInternetFijoEmp=IngresosInternetFijoEmp[(IngresosInternetFijoEmp['id_empresa'].isin(EmpIntFijoIngresos))&(IngresosInternetFijoEmp['anno'].isin(['2020','2021']))]
                    st.plotly_chart(PlotlyBarras(IngresosInternetFijoEmp,'ingresos','(Miles de Millones de COP)',1e9,'Ingresos anuales por empresa'),use_container_width=True)                  
 
        if ServiciosFijos == 'Telefonía fija':
            st.markdown(r"""<div class='IconoTitulo'><img height="50px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/Iconos/VozTelMovil.jpg?raw=true'/><h4 style="text-align:left">Telefonía fija</h4></div>""",unsafe_allow_html=True)   

            ServiciosTelFija=st.selectbox('Escoja el servicio de Internet fijo',['Líneas','Tráfico','Ingresos','Ingresos por tráfico','Ingresos por líneas'])
            st.markdown('Escoja la dimensión del análisis')
            
            ## Líneas
            LineasTelefoníaLocal=LineasTelefoníaLocal[LineasTelefoníaLocal['lineas']>0]
            LineasTelefoníaLocal['modalidad']=None
            LineasTelefoníaLocal['modalidad']=np.where(LineasTelefoníaLocal.id_segmento.isin(['101','102','103','104','105','106']),'Residenciales',LineasTelefoníaLocal['modalidad'])
            LineasTelefoníaLocal['modalidad']=np.where(LineasTelefoníaLocal.id_segmento.isin(['107','109']),'Corporativo',LineasTelefoníaLocal['modalidad'])
            LineasTelefoníaLocalNac=LineasTelefoníaLocal.groupby(['periodo','modalidad'])['lineas'].sum().reset_index()
            #
            LineasTelefoníaLocalEmp=LineasTelefoníaLocal.groupby(['anno','trimestre','id_empresa','empresa'])['lineas'].sum().reset_index()
            LineasTelefoníaLocalEmp=LineasTelefoníaLocalEmp[(LineasTelefoníaLocalEmp['anno'].isin(['2020','2021']))&(LineasTelefoníaLocalEmp['trimestre']=='4')]
            EmpTelfijaLineas=LineasTelefoníaLocalEmp[LineasTelefoníaLocalEmp['anno']=='2021'].sort_values(by='lineas',ascending=False)['id_empresa'].to_list()[0:4]
            LineasTelefoníaLocalEmp=LineasTelefoníaLocalEmp[LineasTelefoníaLocalEmp['id_empresa'].isin(EmpTelfijaLineas)]
            #
            LineasTelefoníaLocalPie=LineasTelefoníaLocal.groupby(['periodo','id_empresa','empresa'])['lineas'].sum().reset_index()
            LineasTelefoníaLocalPie=LineasTelefoníaLocalPie[LineasTelefoníaLocalPie['periodo']=='2021-T4']
            LineasTelefoníaLocalPie['participacion']=round(100*LineasTelefoníaLocalPie['lineas']/LineasTelefoníaLocalPie['lineas'].sum(),1)
            LineasTelefoníaLocalPie.loc[LineasTelefoníaLocalPie['participacion']<=1,'empresa']='Otros'
            LineasTelefoníaLocalPie['empresa']=LineasTelefoníaLocalPie['empresa'].replace(nombresComerciales)    
            ## Tráfico
            TraficoTelefoniaFijaNac=TraficoTelefoniaFija.groupby(['periodo','modalidad'])['trafico'].sum().reset_index()
            TraficoTelefoniaFijaEmp=TraficoTelefoniaFija[TraficoTelefoniaFija['anno'].isin(['2020','2021'])].groupby(['anno','modalidad','id_empresa','empresa'])['trafico'].sum().reset_index()
            
            TraficoTelefoniaFijaEmpTL=TraficoTelefoniaFijaEmp[TraficoTelefoniaFijaEmp['modalidad']=='Local']
            EmpTelfijaLocal=TraficoTelefoniaFijaEmpTL[TraficoTelefoniaFijaEmpTL['anno']=='2021'].sort_values(by='trafico',ascending=False)['id_empresa'].to_list()[0:4]
            TraficoTelefoniaFijaEmpTL=TraficoTelefoniaFijaEmpTL[TraficoTelefoniaFijaEmpTL['id_empresa'].isin(EmpTelfijaLocal)]            
            
            TraficoTelefoniaFijaEmpTLDN=TraficoTelefoniaFijaEmp[TraficoTelefoniaFijaEmp['modalidad']=='Larga distancia nacional']
            EmpTelfijaLDN=TraficoTelefoniaFijaEmpTLDN[TraficoTelefoniaFijaEmpTLDN['anno']=='2021'].sort_values(by='trafico',ascending=False)['id_empresa'].to_list()[0:4]
            TraficoTelefoniaFijaEmpTLDN=TraficoTelefoniaFijaEmpTLDN[TraficoTelefoniaFijaEmpTLDN['id_empresa'].isin(EmpTelfijaLDN)]            
            
            TraficoTelefoniaFijaEmpTLDI=TraficoTelefoniaFijaEmp[TraficoTelefoniaFijaEmp['modalidad']=='Larga distancia internacional']
            EmpTelfijaLDI=TraficoTelefoniaFijaEmpTLDI[TraficoTelefoniaFijaEmpTLDI['anno']=='2021'].sort_values(by='trafico',ascending=False)['id_empresa'].to_list()[0:4]
            TraficoTelefoniaFijaEmpTLDI=TraficoTelefoniaFijaEmpTLDI[TraficoTelefoniaFijaEmpTLDI['id_empresa'].isin(EmpTelfijaLDI)]
            ##Ingresos 
            IngresosTelefoniaFijaNac=IngresosTelefoniaFija.groupby(['periodo','modalidad'])['ingresos'].sum().reset_index()
            IngresosTelefoniaFijaEmp=IngresosTelefoniaFija[IngresosTelefoniaFija['anno'].isin(['2020','2021'])].groupby(['anno','modalidad','id_empresa','empresa'])['ingresos'].sum().reset_index()
            
            IngresosTelefoniaFijaEmpTL=IngresosTelefoniaFijaEmp[IngresosTelefoniaFijaEmp['modalidad']=='Local']
            EmpTelfijaLocalIng=IngresosTelefoniaFijaEmpTL[IngresosTelefoniaFijaEmpTL['anno']=='2021'].sort_values(by='ingresos',ascending=False)['id_empresa'].to_list()[0:4]
            IngresosTelefoniaFijaEmpTL=IngresosTelefoniaFijaEmpTL[IngresosTelefoniaFijaEmpTL['id_empresa'].isin(EmpTelfijaLocalIng)]            
            
            IngresosTelefoniaFijaEmpTLDN=IngresosTelefoniaFijaEmp[IngresosTelefoniaFijaEmp['modalidad']=='Larga distancia nacional']
            EmpTelfijaLDNIng=IngresosTelefoniaFijaEmpTLDN[IngresosTelefoniaFijaEmpTLDN['anno']=='2021'].sort_values(by='ingresos',ascending=False)['id_empresa'].to_list()[0:4]
            IngresosTelefoniaFijaEmpTLDN=IngresosTelefoniaFijaEmpTLDN[IngresosTelefoniaFijaEmpTLDN['id_empresa'].isin(EmpTelfijaLDNIng)]            
            
            IngresosTelefoniaFijaEmpTLDI=IngresosTelefoniaFijaEmp[IngresosTelefoniaFijaEmp['modalidad']=='Larga distancia internacional']
            EmpTelfijaLDIIng=IngresosTelefoniaFijaEmpTLDI[IngresosTelefoniaFijaEmpTLDI['anno']=='2021'].sort_values(by='ingresos',ascending=False)['id_empresa'].to_list()[0:4]
            IngresosTelefoniaFijaEmpTLDI=IngresosTelefoniaFijaEmpTLDI[IngresosTelefoniaFijaEmpTLDI['id_empresa'].isin(EmpTelfijaLDIIng)]
            
            ## Ingresos por tráfico
            IngresosPorTraficoTelFijo=IngresosTelefoniaFijaNac.merge(TraficoTelefoniaFijaNac,left_on=['periodo','modalidad'],right_on=['periodo','modalidad'])
            IngresosPorTraficoTelFijo['Ingresos/Tráfico']=round(IngresosPorTraficoTelFijo['ingresos']/IngresosPorTraficoTelFijo['trafico'],2)
            
            IngresosPorTraficoTelLocalEmp=IngresosTelefoniaFijaEmpTL.merge(TraficoTelefoniaFijaEmpTL,left_on=['anno','id_empresa','empresa'],right_on=['anno','id_empresa','empresa'])
            IngresosPorTraficoTelLocalEmp['Ingresos/Tráfico']=round(IngresosPorTraficoTelLocalEmp['ingresos']/IngresosPorTraficoTelLocalEmp['trafico'],2)            
            IngresosPorTraficoTelLDNEmp=IngresosTelefoniaFijaEmpTLDN.merge(TraficoTelefoniaFijaEmpTLDN,left_on=['anno','id_empresa','empresa'],right_on=['anno','id_empresa','empresa'])
            IngresosPorTraficoTelLDNEmp['Ingresos/Tráfico']=round(IngresosPorTraficoTelLDNEmp['ingresos']/IngresosPorTraficoTelLDNEmp['trafico'],2)
            IngresosPorTraficoTelLDIEmp=IngresosTelefoniaFijaEmpTLDI.merge(TraficoTelefoniaFijaEmpTLDI,left_on=['anno','id_empresa','empresa'],right_on=['anno','id_empresa','empresa'])
            IngresosPorTraficoTelLDIEmp['Ingresos/Tráfico']=round(IngresosPorTraficoTelLDIEmp['ingresos']/IngresosPorTraficoTelLDIEmp['trafico'],2)
 
            ## Ingresos por líneas
            LineasTelefoníaLocalTotalTL=LineasTelefoníaLocalNac.groupby(['periodo'])['lineas'].sum().reset_index()
            IngresosTelefoniaLocal=IngresosTelefoniaFijaNac[IngresosTelefoniaFijaNac['modalidad']=='Local'].drop('modalidad',axis=1)
            IngresosPorLineaTelLocal=IngresosTelefoniaLocal.merge(LineasTelefoníaLocalTotalTL,left_on=['periodo'],right_on=['periodo'])
            IngresosPorLineaTelLocal['Ingresos/Líneas']=round(IngresosPorLineaTelLocal['ingresos']/IngresosPorLineaTelLocal['lineas'],2)

            IngresosPorLineaTelLocalEmp=IngresosTelefoniaFijaEmpTL.merge(LineasTelefoníaLocalEmp,left_on=['anno','empresa','id_empresa'],right_on=['anno','empresa','id_empresa'])
            IngresosPorLineaTelLocalEmp['Ingresos/Líneas']=round(IngresosPorLineaTelLocalEmp['ingresos']/IngresosPorLineaTelLocalEmp['lineas'],2)
 
            if ServiciosTelFija=='Líneas':
                col1,col2,col3=st.columns(3)
                with col1:
                    LineaTiempoLineasTelFija=st.button('Modalidad')
                with col2:
                    BarrasLineasTelFija=st.button('Operadores')
                with col3:
                    PieLineasTelFija=st.button('Participaciones')            
                
                if LineaTiempoLineasTelFija:
                    LineasTelefoníaLocalNac['periodo_formato']=LineasTelefoníaLocalNac['periodo'].apply(periodoformato)
                    st.plotly_chart(Plotlylineatiempo(LineasTelefoníaLocalNac,'lineas','Millones',1e6,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
                if BarrasLineasTelFija:
                    st.plotly_chart(PlotlyBarras(LineasTelefoníaLocalEmp,'lineas','',1,'Líneas anuales por empresa'),use_container_width=True)
                if PieLineasTelFija:
                    figPieTelFija = px.pie(LineasTelefoníaLocalPie, values='lineas', names='empresa', color='empresa',
                                 color_discrete_map=Colores_pie2, title='<b>Participación en líneas de Telefonía local<br>(2021-T4)')
                    figPieTelFija.update_traces(textposition='inside',textinfo='percent+label',hoverinfo='label+percent',textfont_color='black')
                    figPieTelFija.update_layout(uniformtext_minsize=18,uniformtext_mode='hide',showlegend=True,legend=dict(x=0.9,y=0.3),title_x=0.5)
                    figPieTelFija.update_layout(font_color="Black",title_font_family="NexaBlack",title_font_color="Black",titlefont_size=20)
                    st.plotly_chart(figPieTelFija)                            
            
            if ServiciosTelFija=='Tráfico':
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoTraficoTelFija=st.button('Modalidad')
                with col2:
                    BarrasTraficoTelFija=st.button('Operadores')   
                    
                if LineaTiempoTraficoTelFija:
                    TraficoTelefoniaFijaNac['periodo_formato']=TraficoTelefoniaFijaNac['periodo'].apply(periodoformato)                    
                    st.plotly_chart(Plotlylineatiempo(TraficoTelefoniaFijaNac,'trafico','Millones de minutos',1e6,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
                if BarrasTraficoTelFija:
                    st.plotly_chart(PlotlyBarras(TraficoTelefoniaFijaEmpTL,'trafico','Millones de minutos',1e6,'Tráfico anual de Telefonía local por empresa'),use_container_width=True)
                    col1,col2=st.columns(2)
                    with col1:
                        st.plotly_chart(PlotlyBarras(TraficoTelefoniaFijaEmpTLDN,'trafico','Millones de minutos',1e6,'Tráfico anual de Telefonía LDN por empresa'),use_container_width=True)
                    with col2:
                        st.plotly_chart(PlotlyBarras(TraficoTelefoniaFijaEmpTLDI,'trafico','Millones de minutos',1e6,'Tráfico anual de Telefonía LDI por empresa'),use_container_width=True)

            if ServiciosTelFija=='Ingresos':
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoIngresosTelFija=st.button('Modalidad')
                with col2:
                    BarrasIngresosTelFija=st.button('Operadores')   
                
                if LineaTiempoIngresosTelFija:
                    IngresosTelefoniaFijaNac['periodo_formato']=IngresosTelefoniaFijaNac['periodo'].apply(periodoformato)                    
                    st.plotly_chart(Plotlylineatiempo(IngresosTelefoniaFijaNac,'ingresos','Millones de Millones pesos',1e9,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
                if BarrasIngresosTelFija:
                    st.plotly_chart(PlotlyBarras(IngresosTelefoniaFijaEmpTL,'ingresos','Miles de Millones de pesos',1e9,'Ingresos anuales de Telefonía local por empresa'),use_container_width=True)
                    col1,col2=st.columns(2)
                    with col1:
                        st.plotly_chart(PlotlyBarras(IngresosTelefoniaFijaEmpTLDN,'ingresos','Miles de Millones de pesos',1e9,'Ingresos anuales de Telefonía LDN por empresa'),use_container_width=True)
                    with col2:
                        st.plotly_chart(PlotlyBarras(IngresosTelefoniaFijaEmpTLDI,'ingresos','Miles de Millones de pesos',1e9,'Ingresos anuales de Telefonía LDI por empresa'),use_container_width=True)
                    
            if ServiciosTelFija=='Ingresos por tráfico':
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoIngresosportraficoTelFija=st.button('Modalidad')
                with col2:
                    BarrasIngresosportraficoTelFija=st.button('Operadores') 
                
                if LineaTiempoIngresosportraficoTelFija:
                    IngresosPorTraficoTelFijo['periodo_formato']=IngresosPorTraficoTelFijo['periodo'].apply(periodoformato)                    
                    st.plotly_chart(Plotlylineatiempo(IngresosPorTraficoTelFijo,'Ingresos/Tráfico','Pesos/Min',1,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
                if BarrasIngresosportraficoTelFija:
                    st.plotly_chart(PlotlyBarras(IngresosPorTraficoTelLocalEmp,'Ingresos/Tráfico','Pesos/Min',1,'Ingresos/Tráfico anual de Telefonía local por empresa'),use_container_width=True)
                    col1,col2=st.columns(2)
                    with col1:
                        st.plotly_chart(PlotlyBarras(IngresosPorTraficoTelLDNEmp,'Ingresos/Tráfico','Pesos/Min',1,'Ingresos/Tráfico anual de Telefonía LDN por empresa'),use_container_width=True)
                    with col2:
                        st.plotly_chart(PlotlyBarras(IngresosPorTraficoTelLDIEmp,'Ingresos/Tráfico','Pesos/Min',1,'Ingresos/Tráfico anual de Telefonía LDI por empresa'),use_container_width=True)

            if ServiciosTelFija=='Ingresos por líneas':
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoIngresosporlineaTelFija=st.button('Modalidad')
                with col2:
                    BarrasIngresosporlineaTelFija=st.button('Operadores')  

                if LineaTiempoIngresosporlineaTelFija:
                    IngresosPorLineaTelLocal['periodo_formato']=IngresosPorLineaTelLocal['periodo'].apply(periodoformato)                    
                    st.plotly_chart(Plotlylineatiempo(IngresosPorLineaTelLocal,'Ingresos/Líneas','Pesos',1,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
                if BarrasIngresosporlineaTelFija:
                    st.plotly_chart(PlotlyBarras(IngresosPorLineaTelLocalEmp,'Ingresos/Líneas','Pesos',1,'Ingresos/Líneas anuales de Telefonía local por empresa'),use_container_width=True)

    if select_secResumenDinTic == 'Contenidos audiovisuales':
        st.markdown(r"""<div class="titulo"><h3>Contenidos audiovisuales</h3></div>""",unsafe_allow_html=True)
        st.markdown("<center>Para continuar, por favor seleccione el botón con el servicio del cual desea conocer la información</center>",unsafe_allow_html=True)

        ServiciosAudiovisuales=st.radio('Servicios',['TV abierta','TV por suscripción','TV comunitaria','OTT'],horizontal=True)
        st.markdown(r"""<hr>""",unsafe_allow_html=True)
        
        if ServiciosAudiovisuales == 'TV por suscripción':
            st.markdown(r"""<div class='IconoTitulo'><img height="50px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/Iconos/VozTelMovil.jpg?raw=true'/><h4 style="text-align:left">TV por suscripción</h4></div>""",unsafe_allow_html=True)   
            ##Suscriptores
            SuscriptoresTVSusNac=SuscriptoresTVSus.groupby(['periodo'])['suscriptores'].sum().reset_index()
            #
            SuscriptoresTVSusEmp=SuscriptoresTVSus.groupby(['anno','trimestre','id_empresa','empresa'])['suscriptores'].sum().reset_index()
            SuscriptoresTVSusEmp=SuscriptoresTVSusEmp[(SuscriptoresTVSusEmp['anno'].isin(['2020','2021']))&(SuscriptoresTVSusEmp['trimestre']=='4')]
            EmpSuscriptoresTVSusEmp=SuscriptoresTVSusEmp[SuscriptoresTVSusEmp['anno']=='2021'].sort_values(by='suscriptores',ascending=False)['id_empresa'].to_list()[0:4]
            SuscriptoresTVSusEmp=SuscriptoresTVSusEmp[SuscriptoresTVSusEmp['id_empresa'].isin(EmpSuscriptoresTVSusEmp)]
            #
            SuscriptoresTVSusPie=SuscriptoresTVSus.groupby(['periodo','id_empresa','empresa'])['suscriptores'].sum().reset_index()
            SuscriptoresTVSusPie=SuscriptoresTVSusPie[SuscriptoresTVSusPie['periodo']=='2021-T4']
            SuscriptoresTVSusPie['participacion']=round(100*SuscriptoresTVSusPie['suscriptores']/SuscriptoresTVSusPie['suscriptores'].sum(),1)
            SuscriptoresTVSusPie.loc[SuscriptoresTVSusPie['participacion']<=1,'empresa']='Otros'
            SuscriptoresTVSusPie['empresa']=SuscriptoresTVSusPie['empresa'].replace(nombresComerciales) 
            #
            SuscriptoresTVSusTec=SuscriptoresTVSus[SuscriptoresTVSus['anno']=='2021'].groupby(['periodo','id_tecnologia','tecnologia'])['suscriptores'].sum().reset_index()
            SuscriptoresTVSusTec=SuscriptoresTVSusTec.rename(columns={'tecnologia':'CodTec'})
            ##Ingresos
            IngresosTVSus['concepto']=IngresosTVSus['concepto'].replace({'Cargo fijo plan básico de televisión por suscripción':'Cargo fijo plan básico',
            'Otros ingresos operacionales televisión por suscripción':'Otros ingresos operacionales','Cargo fijo plan premium de televisión por suscripción':'Cargo fijo plan premium',
            'Provisión de contenidos audiovisuales a través del servicio de televisión por suscripción':'Provisión de contenidos audiovisuales'})
            IngresosTVSusNac=IngresosTVSus.groupby(['periodo'])['ingresos'].sum().reset_index()
            #
            IngresosTVSusEmp=IngresosTVSus.groupby(['anno','trimestre','empresa','id_empresa'])['ingresos'].sum().reset_index()
            IngresosTVSusEmp=IngresosTVSusEmp[(IngresosTVSusEmp['anno'].isin(['2020','2021']))&(IngresosTVSusEmp['trimestre']=='4')]
            EmpIngresosTVSusEmp=IngresosTVSusEmp[IngresosTVSusEmp['anno']=='2021'].sort_values(by='ingresos',ascending=False)['id_empresa'].to_list()[0:4]
            IngresosTVSusEmp=IngresosTVSusEmp[IngresosTVSusEmp['id_empresa'].isin(EmpIngresosTVSusEmp)]
            #
            IngresosTVSusConcep=IngresosTVSus.groupby(['periodo','id_concepto','concepto'])['ingresos'].sum().reset_index()
            IngresosTVSusConcep=IngresosTVSusConcep.rename(columns={'concepto':'modalidad'})
            ##Ingresos por suscriptores
            IngresosPorSuscriptoresTV=IngresosTVSusNac.merge(SuscriptoresTVSusNac,left_on=['periodo'],right_on=['periodo'])
            IngresosPorSuscriptoresTV['Ingresos/Suscriptores']=round(IngresosPorSuscriptoresTV['ingresos']/IngresosPorSuscriptoresTV['suscriptores'],2)                    
            #
            IngresosPorSuscriptoresTVEmp=IngresosTVSusEmp.merge(SuscriptoresTVSusEmp,left_on=['anno','id_empresa','empresa'],right_on=['anno','id_empresa','empresa'])
            IngresosPorSuscriptoresTVEmp['Ingresos/Suscriptores']=round(IngresosPorSuscriptoresTVEmp['ingresos']/IngresosPorSuscriptoresTVEmp['suscriptores'],2)
            
            ServiciosTVporSus=st.selectbox('Escoja el servicio de TV por suscripción',['Suscriptores','Ingresos'])
            st.markdown('Escoja la dimensión del análisis')
            if ServiciosTVporSus=='Suscriptores':
                
                col1,col2,col3,col4=st.columns(4)
                with col1:
                    LineaTiempoSuscriptoresTVSus=st.button('Evolución temporal')
                with col2:
                    BarrasSuscriptoresTVSus=st.button('Operadores')
                with col3:
                    PieSuscriptoresTVSus=st.button('Participaciones')
                with col4:
                    TecnologiaSuscriptoresTVSus=st.button('Tecnología')    
                
                if LineaTiempoSuscriptoresTVSus:
                    SuscriptoresTVSusNac['periodo_formato']=SuscriptoresTVSusNac['periodo'].apply(periodoformato)
                    st.plotly_chart(Plotlylineatiempo(SuscriptoresTVSusNac,'suscriptores','',1,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
            
                if BarrasSuscriptoresTVSus:
                    st.plotly_chart(PlotlyBarras(SuscriptoresTVSusEmp,'suscriptores','',1,'Suscriptores anuales por empresa'),use_container_width=True)
                
                if PieSuscriptoresTVSus:
                    figPieTVSus = px.pie(SuscriptoresTVSusPie, values='suscriptores', names='empresa', color='empresa',
                                 color_discrete_map=Colores_pie2, title='<b>Participación en suscriptores de TV por suscripción<br>(2021-T4)')
                    figPieTVSus.update_traces(textposition='inside',textinfo='percent+label',hoverinfo='label+percent',textfont_color='black')
                    figPieTVSus.update_layout(uniformtext_minsize=18,uniformtext_mode='hide',showlegend=True,legend=dict(x=0.9,y=0.3),title_x=0.5)
                    figPieTVSus.update_layout(font_color="Black",title_font_family="NexaBlack",title_font_color="Black",titlefont_size=20)
                    st.plotly_chart(figPieTVSus)   

                if TecnologiaSuscriptoresTVSus:
                    SuscriptoresTVSusTec['periodo_formato']=SuscriptoresTVSusTec['periodo'].apply(periodoformato)
                    st.plotly_chart(PlotlylineatiempoTec(SuscriptoresTVSusTec,'suscriptores','',1,['rgb(255, 51, 51)','rgb(255, 153, 51)','rgb(153,255,51)','rgb(160, 160, 160)','rgb(51, 153, 255)','rgb(153,51,255)']), use_container_width=True)

            if ServiciosTVporSus=='Ingresos':

                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoIngresosTVSus=st.button('Evolución temporal')
                with col2:
                    BarrasIngresosTVSus=st.button('Operadores')
                # with col3:
                    # ConceptoIngresosTVSus=st.button('Concepto')
                
                if LineaTiempoIngresosTVSus:
                    IngresosTVSusNac['periodo_formato']=IngresosTVSusNac['periodo'].apply(periodoformato)
                    st.plotly_chart(Plotlylineatiempo(IngresosTVSusNac,'ingresos','Miles de Millones de pesos',1e9,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)
                    IngresosPorSuscriptoresTV['periodo_formato']=IngresosPorSuscriptoresTV['periodo'].apply(periodoformato)
                    st.plotly_chart(Plotlylineatiempo(IngresosPorSuscriptoresTV,'Ingresos/Suscriptores','Pesos',1,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)']), use_container_width=True)

                if BarrasIngresosTVSus:
                    st.plotly_chart(PlotlyBarras(IngresosTVSusEmp,'ingresos','Miles de Millones de pesos',1e9,'Suscriptores anuales por empresa'),use_container_width=True)
                    st.plotly_chart(PlotlyBarras(IngresosPorSuscriptoresTVEmp,'Ingresos/Suscriptores','Pesos',1,'Ingresos/Suscriptores anuales por empresa'),use_container_width=True)
                
                # if ConceptoIngresosTVSus:        
                    # IngresosTVSusConcep['periodo_formato']=IngresosTVSusConcep['periodo'].apply(periodoformato)
                    # st.plotly_chart(Plotlylineatiempo(IngresosTVSusConcep,'ingresos','Miles de Millones de pesos',1e9,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)','rgb(255,0,0)']), use_container_width=True)
        
if select_seccion =='Dinámica postal':
    st.title("Dinámica del sector Postal")
    st.markdown("En el año 2020")    
                

