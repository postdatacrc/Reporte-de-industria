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
    h1{ background: #b560f3;
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
    select_secResumenEj = st.selectbox('Seleccione el resumen ejecutivo del sector a consultar',['PANORAMA MACROECONOMICO Y EL SECTOR TIC',
    'SERVICIOS MÓVILES EN COLOMBIA','SERVICIOS FIJOS EN COLOMBIA','SERVICIOS POSTALES EN COLOMBIA'])
    if select_secResumenEj == 'PANORAMA MACROECONOMICO Y EL SECTOR TIC':
        col1, col2= st.columns(2)
        with col1:
            st.markdown(r"""<ul><li><div style="text-align: justify">
En un difícil entorno económico global producto
del <b>COVID-19</b>, los sectores de telecomunicaciones y
postales absorbieron en menor magnitud el choque
global. El <b>COVID-19</b> aceleró el crecimiento en el
número de conexiones de Internet fijo y móvil       
</div></li>
<li><div style="text-align: justify">
En Colombia los servicios de telecomunicaciones
continúan presentando crecimientos. El mayor
crecimiento en usuarios se da en Internet fijo
(<b>11,47%</b>) cerrando en año 2020 en <b>7,77 millones</b> </div></li>
<li><div style="text-align: justify">
Los ingresos operacionales del sector (Internet fijo y
móvil, Telefonía fija y móvil, televisión por suscripción
y abierta) crecieron en términos reales un <b>1,56%</b>
en 2020, llegando a <b>$22,1 billones</b>, principalmente
debido a los servicios de Internet fijo y móvil, cuyos
ingresos se incrementaron en un <b>9,36%</b> y <b>8,90%</b>
respectivamente.</div></li>
<li><div style="text-align: justify">
La tecnología <b>4G</b> presentó una mayor cantidad de
accesos para el año 2020 en contraste a los accesos
de las tecnologías 2G y 3G, las cuales presentan una
tendencia decreciente </div></li>
<li><div style="text-align: justify">
El tráfico en Colombia continúa presentando
crecimientos. El mayor aumento se dio en los
servicios móviles, donde el de Internet móvil creció
un <b>47,6%</b> y el de telefonía móvil un <b>17,5%</b>.</div></li>
</ul>
        """,unsafe_allow_html=True)
        with col2:
            st.markdown(r"""<ul> 
<li><div style="text-align: justify">Los ingresos por unidad de tráfico mantienen
un comportamiento descendente. El Internet
móvil y la telefonía de larga distancia nacional
presentaron un ingreso mensual de <b>$5.768</b> por
GB y <b>$27,40</b> por minuto, respectivamente.</div></li>            
<li><div style="text-align: justify">El IPC del sector fue menor que el del consolidado
nacional para 2020 (<b>0,68%</b> en el sector
Comunicaciones TIC vs <b>1,61%</b> nacional).</div></li>
<li><div style="text-align: justify">La economía colombiana decreció en su conjunto
a una tasa del <b>6,8%</b> en el año 2020 y el sector de
los servicios de información y comunicaciones en
<b>2,6%.</b></div></li>
<li><div style="text-align: justify">El <b>88,7%</b>del valor agregado de la industria TIC
en Colombia se concentró en 3 actividades:
Telecomunicaciones (<b>47,7%</b>), Servicios TI (<b>34%</b>) y
en las de Contenido y media (<b>7%</b>).</div></li>  
<li><div style="text-align: justify">La penetración de abonados de los servicios
móviles continua en aumento. Al cierre de 2020,
la telefonía móvil alcanzó un <b>134,3%</b> y el Internet
móvil un <b>64,4%</b> por persona. Por su parte el
Internet Fijo estuvo presente en el <b>47,4%</b> de los
hogares.</div></li>   
<li><div style="text-align: justify">Los ingresos promedio mensuales por accesos
continúan a la baja. Los servicios de telefonía fija
y móvil presentaron un ingreso promedio mensual
por acceso, al cierre de 2020, de <b>$21.803</b>y
<b>$3.502</b>, respectivamente. El Internet fijo presentó
un leve incremento del <b>1,7%</b> con un ingreso de
<b>$185.793</b> por mes</div></li>        
            </ul>""", unsafe_allow_html=True)

    if select_secResumenEj=='SERVICIOS MÓVILES EN COLOMBIA':
        col1, col2= st.columns(2)
        with col1:
            st.markdown(r"""<ul><li><div style="text-align: justify">
En los últimos años Colombia ha
experimentado aumentos en el despliegue
de infraestructura, la cual se ha venido
fortaleciendo en las zonas geográficas
con menor densidad poblacional o mayor
superficie. El número de estaciones base
de servicios móviles a nivel nacional
aumentó a una tasa de crecimiento anual
del <b>2,4%</b> pasando de <b>22.390</b> estaciones
en el 2019 a <b>22.925</b> en el 2020.      
</div></li>
<li><div style="text-align: justify">
La tecnología 4G alcanzó las <b>17.549</b>
estaciones desplegadas en 2020, lo que
evidencia la migración tecnológica del
país. </div></li>
<li><div style="text-align: justify">
Las redes 4G son las más utilizadas
para acceder a Internet móvil con <b>24,44
millones</b> de accesos en 2020, superando
las tecnologías 2G y 3G sumadas. Esto
corresponde al <b>75,15%</b> de los accesos
totales a Internet móvil.</div></li>
<li><div style="text-align: justify">
En el 2020, el tráfico promedio por acceso
fue de <b>3,5 GB</b>, un <b>50,2%</b> más que en el
2019. Este crecimiento se fundamenta
principalmente por el aumento del
consumo de Internet móvil durante los
periodos de cuarentena. </div></li>
</ul>
        """,unsafe_allow_html=True)
        with col2:
            st.markdown(r"""<ul> 
<li><div style="text-align: justify">
En el año 2020, se contabilizaron un total
de <b>67,67</b> millones de líneas de voz móvil,
lo que significa una penetración en el
país del <b>134,3%</b>. De estas líneas el <b>21,5%</b>
corresponde a la modalidad pospago y el
restante <b>78,4%</b> a la modalidad prepago.
Esto se traduce en que, en promedio, 1 de
cada 5 líneas de telefonía móvil pertenece
a la modalidad de pospago, manteniendo
esta participación de forma constante a
lo largo de los últimos años.</div></li>            
<li><div style="text-align: justify">
En el 2020 se realizaron <b>3,97</b> millones
de operaciones de portación. Esto
corresponde al <b>14,98%</b> de las <b>26,5</b>
millones operaciones de portación
realizadas desde agosto de 2011 cuando
se implementó la medida. </div></li>
<li><div style="text-align: justify">
En 2020, la inversión pública en proyectos
de despliegue y mejoramiento de la
infraestructura para la prestación de los
servicios de telecomunicaciones muestra
un notable aumento al superar los <b>$222
mil millones</b>, que corresponde a los
recursos destinados para el desarrollo
y masificación del acceso a Internet
Nacional.</div></li>
            </ul>""", unsafe_allow_html=True)

    if select_secResumenEj=='SERVICIOS FIJOS EN COLOMBIA':
        col1, col2= st.columns(2)
        with col1:
            st.markdown(r"""<ul><li><div style="text-align: justify">
Los accesos de Internet fijo en
Colombia llegaron a <b>7,78 millones</b> al
cierre de 2020, representando ello
una penetración del <b>47,4%</b> a nivel
de hogares. La velocidad promedio
de descarga contratada por los
usuarios, a nivel nacional, fue de <b>34,4
Mbps</b>, lo que refleja un incremento
en <b>15,5 Mbps</b> en comparación con
el cierre del 2019, mientras que
la velocidad promedio de carga
fue de <b>11,4 Mbps</b>, presentando un
incremento de <b>5,1 Mbps</b> frente al año
anterior      
</div></li>
<li><div style="text-align: justify">
El número de líneas de telefonía fija
en Colombia fue de <b>7,24 millones</b>
al cierre de 2020, de las cuales <b>6,18
millones (85,32%)</b> eran residenciales.
Así, la tasa de penetración
residencial del servicio fue del <b>44,2%</b>,
manteniéndose prácticamente
inalterada durante los últimos cinco
años.</div></li>
</ul>
        """,unsafe_allow_html=True)
        with col2:
            st.markdown(r"""<ul> 
<li><div style="text-align: justify">
Las conexiones de televisión
por suscripción en Colombia
llegaron a <b>6,06 millones</b> en 2020,
representando ello un crecimiento
del <b>2,2%</b> frente a 2019. Con esto,
la tasa de penetración del servicio,
en términos de hogares, se ubicó
en el <b>37%</b>. Los ingresos percibidos
por la prestación de este servicio
registraron un leve aumento del
<b>1,59%</b> en términos reales, llegando
a <b>$3,26 billones</b> en 2020.
</div></li>            
<li><div style="text-align: justify">
A finales de 2020 había <b>1.470</b>
emisoras de radiodifusión sonora
asignadas en Colombia, de las
cuales <b>341</b> tienen frecuencia
asignada en banda AM y las
restantes <b>1.129</b> en la banda FM.
El <b>54,9%</b> de las frecuencias en
FM están asignada a emisoras
comunitarias.  </div></li>
            </ul>""", unsafe_allow_html=True)

    if select_secResumenEj=='SERVICIOS POSTALES EN COLOMBIA':
        col1, col2= st.columns(2)
        with col1:
            st.markdown(r"""<ul><li><div style="text-align: justify">
Los ingresos del sector postal llegaron
a los <b>$2,19 billones</b> en el año 2020,
lo que representa un incremento del
<b>2,90%</b> con respecto al año 2019.</div></li>
<li><div style="text-align: justify">
Los ingresos de correo y de giros
postales nacionales disminuyeron
frente al 2019 en un <b>14,6%</b> y <b>9%</b>
respectivamente, mientras que la
mensajería expresa aumentó en un
<b>14,4 %</b>, esta última marcada por un
incremento (<b>23,1%</b>) en los ingresos de
mensajería individual que cerro en el
año 2020 en <b>$1,1 billones</b>.</div></li>
<li><div style="text-align: justify">
En el año 2020, los servicios
postales realizaron <b>516 millones</b> de
transacciones en todo el territorio
nacional, mostrando un descenso
del <b>17,6%</b> con respecto al 2019. Esta
baja puede estar relacionada con
las restricciones de movilidad para
la prevención de <b>COVID-19</b>, así
como la digitalización de trámites y
documentos de los últimos años.</div></li>
</ul>
        """,unsafe_allow_html=True)
        with col2:
            st.markdown(r"""<ul> 
<li><div style="text-align: justify">
El <b>54,1%</b> de las transacciones fueron
realizadas a través de las empresas
de mensajería expresa, el <b>26%</b> fueron
envíos de dinero en la modalidad
de giros nacionales y el <b>19,7%</b> de las
transacciones fueron envíos de correo
realizados a través del Operador Postal
Oficial (4-72). </div></li>            
<li><div style="text-align: justify">
En el 2020 se realizaron <b>134,7</b> millones
de giros, cifra que representa una baja
del <b>0,9%</b> con respecto al 2019. Sin
embargo, se evidencia un crecimiento
del <b>17,08%</b> de los montos girados
durante el 2020, año en el que la cifra
alcanzó los <b>$22,12 billones</b>.</div></li>
<li><div style="text-align: justify">
El sector postal cuenta con más de
<b>44 mil puntos de atención</b>, ubicados
en el territorio nacional, capilaridad
que facilita el acceso de los servicios
postales a la población en general.</div></li>
            </ul>""", unsafe_allow_html=True)        
    
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
