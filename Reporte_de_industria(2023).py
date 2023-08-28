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
from folium.plugins import FloatImage
import urllib

    
LogoComision="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAkFBMVEX/////K2b/AFf/J2T/AFb/ImL/IGH/G1//Fl3/BVn/EVv//f7/mK//9/n/1+D/7fH/PXH/w9D/0tz/aY3/tsb/qr3/4uj/iKP/6u//y9b/RHX/5ev/ssP/8/b/dZX/NWz/UX3/hqL/XYX/obb/fJv/u8r/VH//XIT/gJ3/lKz/Snn/l6//ZYr/bpH/dpb/AEtCvlPnAAAR2UlEQVR4nO1d2XrqPK9eiXEcO8xjoUxlLHzQff93tzFQCrFsy0po1/qfvkc9KIkVy5ol//nzi1/84he/+MXfgUZ/2Bovd7vBBbvqsttqv05+elll4GXYGxxmSkqlUiFEcsHpr1QpqdLmcTdu/7OEvqx3WxGrNOEssoHxE6mVqLMc/mtkvo6nkVSCW0nL06lk8239r1CZDQeRTBP7xlnITJQcVes/vXovauujUsHU3agUkr0Pf5oGF4Yn8pCc6dhKPvhLd/J1J4qS90mknC3/vjPZ2saCypwAkamc/lUbmfWicrbvDoncr3+ark/Udiotb/u+wFQ0/mnaNGoDJZ5A3pVG1vtp+rLq8+g705hG3R8lcCzQ9J0Ml7MxerLj+BknY1Vbq4nvd6r5cxpy2FSI86dtT1nh8+Outx7WXye1WnZGrdbot1u9dx+JEZOL1x+hb9KRXvq0wck6u3W9Zn3MUPk/Eo9330jYJ3rS8/FPJli6rQ4bnucsUXwuou9m1de589OfbK/KZlnPEE9aebn08sR4aueDJ2AZOxT8iTzx0cKuZ49VpUnyfds42Tg2kCsR4h5kuC28bOP782h6QCu1biATlUMLw5s3vEg0hafTOOs/i6h7vMU2vjqZWcE+AUaU3m/j8+24yT61vJ3LTSv8eb1Akyj+KJ+mB9RtsRde6ZDcHaQo/YIYPdV1HFdgDuXySDwh82CvhKdP9BwHMfhOFh/IEiDoGF5fV3ma43gEl8PUiP5Rg0TpDfGyRKq+kM1BoSBYEfcmTJTeIN9KI+sLtREkE1jlLUj95TG2SWYP1LQsum6ozSAhmjaDGLRRX/d279PtfnbGaPOBttmMNx9KJrABEcjkf9jfv7SW070652cSzm5wpDR8EItSCZxEAIFYG6q97OgkBjkS/h0kgiwqV4hf9pcLnaF5RiguEuUxatY0CWTKr5Tag0hi808UpKWJm7kpRZPZi+dH9QGTZTNmHqokpXEw9aDquH9S6zVliUF+K2S1DALfTZXlCQz1358TBAdQhgHXM+wqVnFaMe2FL0ZVJuLCZviwYhAoXUGK9lw+UbaYYKkvmOeBaRkzl/NS31oDAM8CbxajsJlfMEvs8efG8Xv37wJRSGdM82KUJXYtUY29OQienJMX6lxd4ypDCYEskJ8a53nUsYPtmctNYEmqYjE6rKrLcWs4HLa6vepqMYsJRRsAiWT/+zUvZew7mK3sB5CnUm0G3TogErJ6d9CU9OKN67JmVArzh5BZP1Y7soTMdPy703NL9EnrPSpmHwhiAG6QZzvZtvznzrKBiYwGbZSHXN9FRaSUJMQxTy/N82hsecwEztKwNH23fRIIwyN9I5mgpG1muddJS/inDboPXI66ofGNSZVTrb3EYyhDGOROVmpxB8EQKo+3Idt3QzZmRBrD+bSfC40mG/j/3oBwIJNburU45qTgFGOhHJMLETEGM3oHOIIFSwuyqqJY7mIQ9ppxbuUVcFOyjakkeBET44JGh2LdVoL0fpY7DfCqs735seWhjMTJ0KZfHeCWcwQjJ2ZgSZU1DQKZLCm/57KRbAgRNjmfiXHoFGdmEFw0fdEbPByZZgtCjLfj49pjUPKbLIqKL6Ix2YQKVYWWAP1Ha0aAEa2FcVIqZVfZWZJ5VrAE++TDA3/Am/+R/8Du4AYNa0tC1oYUmXWrP346AQmP/wzPUfiFdaM93k0XoxkXfDZaTHfjti/GUg+zVJnAUdjJHXFlxg7XhucYeYrr+r3jTF7zMvr/tbufKjk79pxf5gVKmNiRog5K3l7TObTcKvrGDjLnbgzfmUzBmAU7uccnD8v+05qpkhxgDEMhUB3BKg+x5SzKu8bCQWB/kLideHZyI6vWBwBKyQGFSEhPjACpRjq628ZO7p1M2TmttcFkL5iQR5uxXhsFMCpDxBarsL3EvqoDjCi4Pe7cavprUK/g8cLyGDj9bAFCojPbktT+IkyMQ2jNHdT3aPrONFaOMK9O8qfC9RBvUrFlL45gFy8/H58CRO0ZBNMyseSSXgO+lPQZjlsXR+htzMenbPGDIacU8Rti+4I2KBxACE/C7cVtKHH1X26P2Qz2rd8CzZHb8+BqIDMDZn1A5KbQIme+kBfdsN9pr2D0Qy2gb2bkF6zwyJqAM31ZDmhE1IM9n3skoH1k5IisP3eGh+uBZWYJWPHRChKhJpgCjJxXtKMhXTGpfAjRBwWFLLp4sWABg4LPPWwJnHL5+oFMKiFN2CtMYATr2A2S9fnRTmAgk3KIRw23g4aKuRHoSk1hZ1OvJH2EBEyQYaBfbgUQOlkiBbSyS9NREJMKQHP1CwqZLzBlStR8KsWCxFpI1Aj7/qn5BMOvKgAWGcw2xPGpPei2DlPTbGY4A9syK2kS04he4IRNbAs4hHYG5Bzj00Gh1TTboIxjUMdxWWqLS1sdJ/saNvfCpl+OGP1CbJiE+RgSjMRSgPJKqJvn90WYaMMKC9NjN4NI4O8sgdPAY3jFV5sOnkfPFdCY/zNTXriTKOGDOKCJCRFdljHBsABLUllJRvP5PqpI5YmGpkAaBCdOUzjsQK2bvwqcqf8DJZKtuv1PJfDS2rmqUFkMqjXUUUjAdGlGd+l0SsYvZoT8MOyU/s5WnMBT2IDuYZbJwFyiEWHCQxfaHD0HhMcDMHea9cCefjW3ZFonKFkD5gNpgkaD7f1CTh7sMd+BEbJisT3acsDIGlDU7MjjH7TGcFsLTDpj0fVccCRhjjg/aidAHxGnTKHliz9/ak4W5768Tba4X7Y8uCqc3K+6AvIK6PpaCy7n+U/2/pqs1U2ZMl8xB0YlJlDbN1nQ6KC+y+9K9phinvcrif5eI4w0ZVvzd7Rex+jiq7jkMJvhquo6Zzkg/YWUGKEPRU3bVL9AFyO5hltYLCgTp2PCEb1GOA8hNn9GVhY69Ocwh9xS9B6vMh2hqlUwMhFwEVG2AoQ0+9Ow840/F/SFJXIqBGYcijJTdVR1yLfOhBUUrSoKTPMwoBCDW/+v0Lkeu1cCVgy2dtPOavncBnDAzacqfB26s48NkKZ1uVNKcJ4IOSN3ZSFMU0Dlhw83uNLw4lCliVEH1o9u553FB2IfOMI4EWbelmrSKFfSROZZsf0QT02atLlBCH4DYqbIaGsebOQ4+YbebeQCxsmcROEbwtk2qwiJgoZPHWMDjA9p5NDx5YT3QGQfuBluIyoLbXZbFU0+XNI2e/0SylFE6O7yKBSnTbAOlcsbbEAoB2Wm5YGYNVEehVrvTG0HX+beAVRHuXPSFnS/lcK13WHLCxqo0ENLqmA4bKjyKdQK30rh/PEVdWhh/F+mMG91QylmXL0kgUIz1U3M/GkKbXVUPFcuBeUn4chmcQoBfUjU+NqGt5kYxuqBd8DRaQ8QkgYI1BBj+unJwf2waAsjdQQUs8CdDh4gtAXw5VCBVoDCnsOIUrl3mAYspuLVBGKMHeBb2DYC8SSrz224v2/5j18htTAgrDbAP0RYsxA0v1uPhVn2katLV5RT6DCi7ig0bSXcLFgDWiOAek7DrPWsNe9fQ20j8mWBokt8LAfiXDFtt8DF79ElZZNDNq18Lk+QOxURUhForCfOhotkzRHAhEqS251YpWkq0wE5SIXYjNj0ranpQ+3GW31uuCS5Nuz21gXmymBSiEB/UI1YKqIVovUM+0qSaUBsBnA+yGabFqb2mkb1jJmxiPA8WIG5JQZqtM62yuGwTZwuUR4/IngNHg+EkgGh1bpdfKfowYMnGRSnHNNBiDC/UihbQk1c6Ic5+CZgeMzJMGep8KsQRO7JCGNqUNNrmuUdmWe85bk6Mx9LfXdaYKrTFBSIRdU0QdC18Y4YrXCUXd+j96kDfDQifCfLZyV6iOdwmasYC2d8tu60FUu5g0ZEDskS30JYeyDOBe0uXSMRJLZyIwBS+x0zCLVm6ZYNHR7+RcGLp8pceUOGY3Pwne0eHUwBJihowhtmbtB5nsxZZyj2bht0Bb2aKQbRiGkosLXNkKsxdIOD+8XcZdzUZ7Y5WioyBxUhGgqs4S1n76ELmu0zj7JRe0tEpjF1dDCw/8tXHGA8BGsPItEJvlYd+/qSWAzdLFD/qLhEozmxAsOkUGfY5W3ksqiz7PLmWE8H6611l/bO2tWmexIoMMMLo9OATpAryIMMWVrTZqX//xI9RmGwHI97u4+R8o4vM08vpgo6H4m+A7Ue48pNKxSXn+dF6MGQ/s8JjA3CBD2t7RaoaLkNZwO7xJ6gy0MNHePpU7b97IYancJzlswY01cMQMEYxsUD/ftPkKtoT6yhJfSSXituQpixRpR3AFbPfmJdoHHpbCkdy7tJjwO50zfM4yuu8r+sQH/kZWhd0CQS5+O4WU7lqBC8+6GLScnZCw2e6E0MGtPhWic0LwXRtOKUpBrIHkbowfvLN2+UMx0YGvKHE2RAKd0DqAJf3jKSDVZ8Fxk4DBbVxJv4QgqBzc6fK7q/S6sxK3oWGVD/im3I9w6oQR3mPDh/ODS1fTGJysGJ0w0UgYjBe4RYRrrJ28fHInoxhdsz5qiFIaZ9mbVnPkBddEvi8Bb9ODipiOzfdA7FuCKsKd9WjF8nzOfU4OAkCnSPM2pOa6D5DQoFjXfCmFUmt7DVXEPqIO8MpTPC4qbgcIwz2qjLdO8hhK05A3cIrU3cOXTDNlEALUZX9ETIZOckHtgOEXbCELY/J1DrO0jMqmgahVxZ3bod8ps7nPtHBG6ii0R9sTxinDxLlSOrj/bJKui7n0MzGMJZfjc8SufcKCbk3DW/vYd1eAKqcVuhOlG4Wwxr66OQ4M1dTCi5WToFIJrAoA6k4PaSZO7TtPVlh1f0ANOEc8Z5ch5fKre7lscVwIcNgmaWI/XrPYmY5pBJfb0cvHcO88Xh463aHSKUFzTVHgZzDE8CEO4Jc2SraBgOeKEXWPaBapjOkRiVfo1to4k3/YJL4tHT0e7ewcubV35G0GS78Mu7CDXDjJd6bfZbiDAIvRrhD21gkPM+r9D325KK8JspJf9VQn1NeWPLB2EOZoV0JUqoo3ghkXRrTx6tQO9SIHukc6DMjTp9zSIXIF/Q3wbOtSNfaYUf/PpAYsELBF4+KqGhIvgGFQwOpLAg/pZgAK+r8PshzbluaBCHBNJvza53vPfvmQBm8wW8kRYVpN2anY1HlJvJWFTIXDTuB8SBcGt2e5XSLrMKuyPIxIpWdSq83tQjeQNBuuTphLiw7N4Qe2lGWN556U4F/QZEYtfNPTJiUSaPEB53v/velGmBRE4pd3M3iHe9eezw+niwkUUv6Uzc+V4sqKVScI7sEwU48+sNZXnd5q3HyAW47PASRoGypLThNy1qnYzDSKXOUrkjMEWHR/1YU2s04JsONJAjgV0ElupvkwetS9s17NSq8huBlkpnMsij1m013vQqwQuB5e7gmUQqo1osOGJX7ieB5YaELhhSr02HLbjQaxgegDInwhF4CdoXkiYQSaWVtVwfOCo9NHvBi3EHCxI8MiOp5KLyE9+D97SUgtqc2N8GhBmJndXRffnVM7AiyhvTvEH0Z8FPKv0iyRx65FuOclUkxIprnpIioyGoM+JhrDyaNzQKU9uI6DJRC8h4PeDRvKE0dLJKcX8XBWpJ14N5Q+j/T0T5V51a0G/SxER6V10UHFFnsvOMHKwNO5qBI77KDlGdE3dIwPbsJ6I/Ip3GZPYpKcLajk8b+A0iJoclKf7HkqvJHNQWkEalpLRC0ThSJM7tUjW8O5bEu6eZaR60R6HVh5rE63Vc2D1kcafk+oAgrGcEGi92F47HmZw/3YjxYGy7gsOBs+7HRJqZHH2bCnSgx4L3Uet+fxKdy9GPCBgA3WZoWuyk+33TYpJ4+zfs3yeGi0pYBEBsFs6brNN49YRITCG87rgK2UjXCJZENpffaaGh0epIYhbnHlyJ1U+LTzsm402lyD2yutf7+LdIFxsm3Y7wXcZl2Twho9XfTt4F2XC3j5UIufT9RJ1aFLhM4AdQG1YXqVRgcfcDbSwRSvLjsv1TpmchvLaqx2YilZ4vwO+FJ2N67sCJNMn2q+XwKQHs70PWaK+Xu+liP+Np5YxYRM35YbXrterf7/T94he/+MUvfvGL/0n8PxO8HWcj0wB/AAAAAElFTkSuQmCC"
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
 'UNE EPM TELECOMUNICACIONES S.A.':'Tigo-Une',
 'SERVIENTREGA S.A.':'Servientrega',
 'INTER RAPIDISIMO S.A':'InterRapidisimo',
 'COLVANES S.A.S.':'Colvanes',
 'COORDINADORA MERCANTIL S. A.':'Coordinadora',
 'DHL EXPRESS COLOMBIA LTDA':'DHL',
 'UPS SERVICIOS EXPRESOS S.A.S.':'UPS',
 'DOMINA ENTREGA TOTAL S.A.S.':'Domina',
 'DOMESA DE COLOMBIA S.A.':'Domesa',
 'CADENA COURRIER S.A.S.':'Cadena',
 'DATACURRIER S A S':'Datacurrier',
 'ENTREGA INMEDIATA SEGURA S.A':'EIS',
 'SUPERGIROS S.A':'Supergiros',
 'EFECTIVO LTDA':'Efecty',
 'MATRIX GIROS Y SERVICIOS SAS':'Matrix',
 'MOVIIRED S.A.S.':'Moviired',
 'SERVICIOS POSTALES NACIONALES S.A.':'4-72'}
 
Colores_pie={'Claro':'rgba(255,0,0,0.7)','Telefónica':'rgba(154,205,50,0.7)','Tigo':'rgba(100,149,237,0.7)','Virgin':'rgb(255,102,178)',
         'Móvil Éxito':'rgba(241, 196, 15,0.7)','WOM':'rgb(198,84,206)',
        'Avantel':'rgba(240, 128, 128,0.7)','ETB':'rgba(26, 82, 118,0.7)','Flash':'black','Setroc':'black','Suma':'black'}
Colores_pie2={'Claro':'rgba(255,0,0,0.7)','Movistar':'rgba(154,205,50,0.7)','Tigo-Une':'rgba(100,149,237,0.7)','Otros':'rgb(192,192,192)','ETB':'rgba(26, 82, 118,0.7)'}
Colores_pie3={'Colvantes':'rgb(204,0,0)','InterRapidisimo':'rgb(255,128,0)','DHL':'rgb(255,255,0)','Servientrega':'rgb(31,226,109)',
             'Coordinadora':'rgb(51,51,255)','UPS':'rgb(255,181,0)','Otros':'rgb(192,192,192)','Domina':'rgb(19,114,209)','Domesa':'rgb(76,0,153)',
             'EIS':'rgb(0,102,102)','Cadena':'rgb(255,51,51)','Datacurrier':'rgb(153,255,51)','Efecty':'rgb(255,213,30)','Matrix':'rgb(153,255,51)',
             '4-72':'rgb(0,0,255)','Supergiros':'rgb(0,102,204)','Moviired':'rgb(255,0,127)'}

Colores_pais={'Argentina':'rgb(116,172,223)','Bolivia':'rgb(0,128,0)','Brasil':'rgb(153,255,51)','Chile':'rgb(255, 51, 51)'
              ,'Colombia':'rgb(255,205,0)','Costa Rica':'rgb(0,43,127)','República Dominicana':'rgb(0,45,98)',
             'Ecuador':'rgb(255,153,51)','El Salvador':'rgb(0,71,171)','Guatemala':'rgb(0,163,230)',
             'Honduras':'rgb(2,190,230)','Mexico':'rgb(0,104,71)','Nicaragua':'rgb(0,103,198)',
             'Panama':'rgb(218,18,26)','Peru':'rgb(153,51,255)','Uruguay':'rgb(0,56,168)','Paraguay':'rgb(221,0,35)'}



def Participacion(df,column):
    part=df[column]/df[column].sum()
    return part
def trim(x):
    if x in ['1','2','3']:
        return '1'
    if x in ['4','5','6']:
        return '2'
    if x in ['7','8','9']:
        return '3'
    if x in ['10','11','12']:
        return '4'    
    else:
        pass    
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
    elif id_empresa=='800088155':
        return 'rgb(19,114,209)'
    elif id_empresa=='800185306':
        return 'rgb(204,0,0)'    
    elif id_empresa=='800251569':
        return 'rgb(255,128,0)'
    elif id_empresa=='860512330':
        return 'rgb(31,226,109)'
    elif id_empresa=='890904713':
        return 'rgb(51,51,255)'     
    elif id_empresa=='830131993':
        return 'rgb(255,213,30)'  
    elif id_empresa=='900327256':
        return 'rgb(153,255,51)' 
    elif id_empresa=='900084777':
        return 'rgb(0,102,204)' 
    elif id_empresa=='900392611':
        return 'rgb(255,0,127)' 
    elif id_empresa=='860014923':
        return 'rgb(220,11,11)'   
    elif id_empresa=='860025674':
        return 'rgb(51,51,255)' 
    elif id_empresa=='900163045':
        return 'rgb(255,128,0)'   
    elif id_empresa=='901032662':
        return 'rgb(220,20,60)' 
    elif id_empresa=='830029703':
        return 'rgb(102,204,0)'  
    elif id_empresa=='Otros':
        return 'rgb(192,192,192)'          
    else:
        pass            
def periodoformato(x):
    return "{1}-{0}".format(*x.split('-')).replace('-','<br>')
def convert_df(df):
     return df.to_csv().encode('latin-1')

def Plotlylineatiempo(df,column,unidad,escalamiento,colores,titulo,textofuente):
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
            column.capitalize()+'-'+unidad+': %{y:.3f}<br>'))
        fig.update_yaxes(range=[0,maxdf],tickfont=dict(family='Poppins', color='black', size=16),titlefont_size=16, title_text=unidad, row=1, col=1)
    
    else:
        maxdf=df[column].max()/escalamiento+(df[column].max()/escalamiento)*0.1  
        mindf=df[column].min()/escalamiento-(df[column].min()/escalamiento)*0.1  
        fig.add_trace(go.Bar(x=df['periodo_formato'],
                                y=df[column]/escalamiento,marker_color='rgb(102,204,0)',name=column,
                                hovertemplate ='<br><b>Periodo</b>: %{x}<br><extra></extra>'+                         
            column.capitalize()+'-'+unidad+': %{y:.2f}<br>'))
        fig.update_yaxes(range=[mindf,maxdf],tickfont=dict(family='Poppins', color='black', size=16),titlefont_size=16, title_text=unidad, row=1, col=1)                        
    fig.update_xaxes(tickangle=0, tickfont=dict(family='Poppins', color='black', size=14),title_text=None,row=1, col=1
    ,zeroline=True,linecolor = 'rgba(192, 192, 192, 0.8)',zerolinewidth=2)
    fig.update_layout(height=550,legend_title=None)
    fig.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20,
    title={
    'text':titulo,
    'y':0.95,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})        
    fig.update_layout(legend=dict(orientation="h",xanchor='center',y=1.1,x=0.5,font_size=11),showlegend=True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
    fig.update_layout(yaxis_tickformat ='d')
    fig.add_annotation(
    showarrow=False,
    text=textofuente,
    font=dict(size=11), xref='x domain',x=0.5,yref='y domain',y=-0.2)
    return fig

def PlotlyIngresosPorAcceso(df,column,unidad,escalamiento,colores,titulo,textofuente):
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
        fig.update_yaxes(range=[0,maxdf],tickfont=dict(family='Poppins', color='black', size=16),titlefont_size=16, title_text=unidad, row=1, col=1)
    
    else:
        maxdf=df[column].max()/escalamiento+(df[column].max()/escalamiento)*0.1  
        mindf=df[column].min()/escalamiento-(df[column].min()/escalamiento)*0.1  
        fig.add_trace(go.Bar(x=df['periodo_formato'],
                                y=df[column]/escalamiento,marker_color='rgb(102,204,0)',name=column,
                                hovertemplate ='<br><b>Periodo</b>: %{x}<br><extra></extra>'+                         
            column.capitalize()+'-'+unidad+': %{y:.2f}<br>'))
        fig.update_yaxes(range=[mindf,maxdf],tickfont=dict(family='Poppins', color='black', size=16),titlefont_size=16, title_text=unidad, row=1, col=1)                        
    fig.update_xaxes(tickangle=0, tickfont=dict(family='Poppins', color='black', size=14),title_text=None,row=1, col=1
    ,zeroline=True,linecolor = 'rgba(192, 192, 192, 0.8)',zerolinewidth=2)
    fig.update_layout(height=550,legend_title=None)
    fig.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20,
    title={
    'text':titulo,
    'y':0.95,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})        
    fig.update_layout(legend=dict(orientation="h",xanchor='center',y=1.1,x=0.5,font_size=11),showlegend=True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
    fig.update_xaxes(tickvals=['T2<br>2018','T4<br>2018','T2<br>2019','T4<br>2019','T2<br>2020','T4<br>2020','T2<br>2021','T4<br>2021','T2<br>2022','T4<br>2022'])
    fig.update_layout(yaxis_tickformat ='d')
    fig.add_annotation(
    showarrow=False,
    text=textofuente,
    font=dict(size=11), xref='x domain',x=0.5,yref='y domain',y=-0.4)
    return fig

def PlotlylineatiempoTec(df,column,unidad,escalamiento,colores,titulo,textofuente):
    fig = make_subplots(rows=1, cols=1)
    maxdf=df[column].max()/escalamiento+(df[column].max()/escalamiento)*0.3  
    tecnologia=df['CodTec'].unique().tolist()
    for i,elem in enumerate(tecnologia):
        fig.add_trace(go.Scatter(x=df[df['CodTec']==elem]['periodo_formato'],
        y=df[df['CodTec']==elem][column]/escalamiento,text=df[df['CodTec']=='elem']['CodTec'],line=dict(color=colores[i]),
        name=elem,hovertemplate =
        '<br><b>Tecnología</b>:<br><extra></extra>'+elem+
        '<br><b>Periodo</b>: %{x}<br>'+                         
        column.capitalize()+' '+unidad+': %{y:.2f}<br>',mode='lines+markers',marker=dict(size=7)))
    fig.update_layout(barmode='group')    
    fig.update_yaxes(range=[0,maxdf],tickfont=dict(family='Poppins', color='black', size=16),titlefont_size=16, title_text=unidad, row=1, col=1)                    
    fig.update_xaxes(tickangle=0, tickfont=dict(family='Poppins', color='black', size=14),title_text=None,row=1, col=1
    ,zeroline=True,linecolor = 'rgba(192, 192, 192, 0.8)',zerolinewidth=2)
    fig.update_layout(height=550,legend_title=None)
    fig.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20,
    title={
    'text':titulo,
    'y':0.95,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})        
    fig.update_layout(legend=dict(orientation="h",xanchor='center',y=1.1,x=0.5,font_size=11),showlegend=True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    #fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.4)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
    fig.update_layout(yaxis_tickformat ='d')
    fig.add_annotation(
    showarrow=False,
    text=textofuente,
    font=dict(size=11), xref='x domain',x=0.5,yref='y domain',y=-0.2)    
    return fig

def PlotlylineatiempoEmp(df,column,unidad,colores,titulo,textofuente):
    fig = make_subplots(rows=1, cols=1)
    maxdf=df[column].max()+df[column].max()*0.4
    empresa=df['empresa'].unique().tolist()
    for i,elem in enumerate(empresa):
        fig.add_trace(go.Scatter(x=df[df['empresa']==elem]['periodo_formato'],
        y=df[df['empresa']==elem][column],text=df[df['empresa']=='elem']['empresa'],line=dict(color=colores[i]),
        mode='lines+markers',name=elem,marker=dict(size=7),hovertemplate =
        '<br><b>Empresa</b>:<br><extra></extra>'+elem+
        '<br><b>Periodo</b>: %{x}<br>'+                         
        column.capitalize()+' '+unidad+': %{y:.2f}<br>'))
    fig.update_yaxes(range=[0,maxdf],tickfont=dict(family='Poppins', color='black', size=16),titlefont_size=16, title_text=unidad, row=1, col=1)                    
    fig.update_xaxes(tickangle=0, tickfont=dict(family='Poppins', color='black', size=14),title_text=None,row=1, col=1
    ,zeroline=True,linecolor = 'rgba(192, 192, 192, 0.8)',zerolinewidth=2)
    fig.update_layout(height=550,legend_title=None)
    fig.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20,
    title={
    'text':titulo,
    'y':0.95,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})        
    fig.update_layout(legend=dict(orientation="h",xanchor='center',y=1.1,x=0.5,font_size=11),showlegend=True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    #fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.4)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
    fig.update_layout(yaxis_tickformat ='d')
    fig.add_annotation(
    showarrow=False,
    text=textofuente,
    font=dict(size=11), xref='x domain',x=0.5,yref='y domain',y=-0.4)
    return fig
 
def PlotlylineatiempoDep(df,column,unidad,titulo,textofuente):
    fig = make_subplots(rows=1, cols=1)
    departamentos=df['departamento'].unique().tolist()
    for i,elem in enumerate(departamentos):
        fig.add_trace(go.Bar(x=df[df['departamento']==elem]['periodo_formato'],
        y=df[df['departamento']==elem][column],text=df[df['departamento']=='elem']['departamento'],name=elem,hovertemplate =
        '<br><b>Departamento</b>:<br><extra></extra>'+elem+
        '<br><b>Periodo</b>: %{x}<br>'+                         
        column.capitalize()+' '+unidad+': %{y:.2f}<br>'))
    fig.update_yaxes(tickfont=dict(family='Poppins', color='black', size=16),titlefont_size=16, title_text=unidad, row=1, col=1)                    
    fig.update_xaxes(tickangle=0, tickfont=dict(family='Poppins', color='black', size=14),title_text=None,row=1, col=1
    ,zeroline=True,linecolor = 'rgba(192, 192, 192, 0.8)',zerolinewidth=2)
    fig.update_layout(height=550,legend_title=None)
    fig.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20,
    title={
    'text':titulo,
    'y':0.95,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})        
    fig.update_layout(barmode='stack',legend=dict(orientation="h",xanchor='center',y=1.1,x=0.5,font_size=11),showlegend=True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    #fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.4)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
    fig.update_layout(yaxis_tickformat ='d')
    fig.add_annotation(
    showarrow=False,
    text=textofuente,
    font=dict(size=11), xref='x domain',x=0.5,yref='y domain',y=-0.4)    
    return fig

def PlotlylineatiempoInt(df,column,unidad,escalamiento,titulo,textofuente):
    fig = make_subplots(rows=1, cols=1)
    maxdf=df[column].max()/escalamiento+(df[column].max()/escalamiento)*0.3  
    pais=df['País'].unique().tolist()
    for i,pais in enumerate(pais):
        df2=df[df['País']==pais]
        fig.add_trace(go.Scatter(x=df2['Año'],
        y=round(df2[column]/escalamiento,2),text=df[column],
        name=pais,hovertemplate ='<br><b>País</b>:<extra></extra>'+pais+
        '<br><b>Accesos</b>: %{y:3f}',mode='lines+markers',marker=dict(size=7,color=Colores_pais[pais])))  
    fig.update_yaxes(range=[0,maxdf],tickfont=dict(family='Poppins', color='black', size=16),titlefont_size=16, title_text=unidad, row=1, col=1)                    
    fig.update_xaxes(tickangle=0, tickfont=dict(family='Poppins', color='black', size=14),title_text=None,row=1, col=1
    ,zeroline=True,linecolor = 'rgba(192, 192, 192, 0.8)',zerolinewidth=2)
    fig.update_layout(height=550,legend_title=None)
    fig.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20,
    title={
    'text':titulo,
    'y':0.95,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})        
    fig.update_layout(legend=dict(orientation="h",xanchor='center',y=1.1,x=0.5,font_size=11),showlegend=True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    #fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.4)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
    fig.update_layout(yaxis_tickformat ='d',hovermode='x')
    fig.add_annotation(
    showarrow=False,
    text=textofuente,
    font=dict(size=11), xref='x domain',x=0.5,yref='y domain',y=-0.2)    
    return fig
 
def PlotlyBarras(df,column,unidad,escalamiento,titulo,textofuente):   
    fig = make_subplots(rows=1, cols=1) 
    maxdf=df[column].max()/escalamiento+(df[column].max()/escalamiento)*0.5
    for empresa in df['empresa'].unique().tolist():
        fig.add_trace(go.Bar(x=df[df['empresa']==empresa]['anno'],y=df[df['empresa']==empresa][column]/escalamiento
                             ,marker_color=PColoresEmp(df[df['empresa']==empresa]['id_empresa'].unique()[0]),
                            name=empresa,hovertemplate='<br><b>Empresa</b>:<br><extra></extra>'+empresa+'<br>'+                       
        column.capitalize()+' '+unidad+': %{y:.3f}<br>'))
    fig.update_layout(barmode='group')
    fig.update_xaxes(tickangle=0, tickfont=dict(family='Poppins', color='black', size=16),title_text=None,row=1, col=1,
    zeroline=True,linecolor = "rgba(192, 192, 192, 0.8)",zerolinewidth=2)
    fig.update_yaxes(tickfont=dict(family='Poppins', color='black', size=16),titlefont_size=18, title_text=unidad, row=1, col=1)
    fig.update_layout(height=550,legend_title=None)
    fig.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20,
    title={
    'text': titulo,
    'y':0.98,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})        
    fig.update_layout(legend=dict(orientation="h",y=1.2,xanchor='center',x=0.5,font_size=11),showlegend=True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',yaxis_tickformat='d')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
    fig.add_annotation(
    showarrow=False,
    text=textofuente,
    font=dict(size=11), xref='x domain',x=0.5,yref='y domain',y=-0.15)    
    return fig

def PlotyMultiIndexBarra(df,column,unidad,titulo,escalamiento,textofuente):
    color_ambito={'Internacional de entrada':'rgb(255,102,102)','Internacional de salida':'rgb(102,255,102)',
                 'Local':'rgb(102,178,255)','Nacional':'rgb(178,102,255)'}
    fig = make_subplots(rows=1,cols=1)
    for ambito in df['ambito'].unique().tolist():
        df2=df[df['ambito']==ambito]    
        X=[df2['anno'].tolist(),df2['tipo_envio'].tolist()]
        fig.add_trace(go.Bar(x=X,y=df[df['ambito']==ambito][column]/escalamiento,name=ambito,marker_color=color_ambito[ambito],
        hovertemplate='<br><b>Ámbito</b>:<br><extra></extra>'+ambito+'<br>'+                       
        column.capitalize()+' '+unidad+': %{y:.3f}<br>'))
    fig.update_layout(barmode='group')
    fig.update_xaxes(tickangle=0, tickfont=dict(family='Poppins', color='black', size=16),title_text=None,row=1, col=1,
    zeroline=True,linecolor = "rgba(192, 192, 192, 0.8)",zerolinewidth=2)
    fig.update_yaxes(tickfont=dict(family='Poppins', color='black', size=16),titlefont_size=18, title_text=unidad, row=1, col=1)
    fig.update_layout(height=550,legend_title=None)
    fig.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20,
    title={
    'text': titulo,
    'y':0.98,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})        
    fig.update_layout(legend=dict(orientation="h",y=1.1,xanchor='center',x=0.5,font_size=11),showlegend=True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',yaxis_tickformat='d')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
    fig.add_annotation(
    showarrow=False,
    text=textofuente,
    font=dict(size=11), xref='x domain',x=0.5,yref='y domain',y=-0.2)
    return fig

def PlotlyBarras2(df,column,modalidad,unidad,escalamiento,titulo,colores,textofuente):
    fig = make_subplots(rows=1, cols=1) 
    maxdf=df[column].max()/escalamiento+(df[column].max()/escalamiento)*0.5    
    for i,elem in enumerate(df[modalidad].unique().tolist()):
        fig.add_trace(go.Bar(x=df[df[modalidad]==elem]['anno'],y=df[df[modalidad]==elem][column]/escalamiento
                             ,marker_color=colores[i],name=elem,hovertemplate=modalidad.capitalize()+':'+elem+'<br>'+                       
        column.capitalize()+'-'+unidad+': %{y:.3f}<br>'))      
    fig.update_layout(barmode='group')
    fig.update_xaxes(tickangle=0, tickfont=dict(family='Poppins', color='black', size=16),title_text=None,row=1, col=1,
    zeroline=True,linecolor = "rgba(192, 192, 192, 0.8)",zerolinewidth=2)
    fig.update_yaxes(tickfont=dict(family='Poppins', color='black', size=16),titlefont_size=18, title_text=unidad, row=1, col=1)
    fig.update_layout(height=550,legend_title=None)
    fig.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20,
    title={
    'text': titulo,
    'y':0.95,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})        
    fig.update_layout(legend=dict(orientation="h",y=1.05,xanchor='center',x=0.5,font_size=11),showlegend=True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',yaxis_tickformat='d')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
    fig.add_annotation(
    showarrow=False,
    text=textofuente,
    font=dict(size=11), xref='x domain',x=0.5,yref='y domain',y=-0.2)
    return fig

def PlotlyBarrasEmp(df,column,unidad,escalamiento,titulo,colores,textofuente):   
    fig = make_subplots(rows=1, cols=1) 
    maxdf=df[column].max()/escalamiento+(df[column].max()/escalamiento)*0.5
    for i,empresa in enumerate(df['empresa'].unique().tolist()):
        fig.add_trace(go.Bar(y=df[df['empresa']==empresa]['anno'],x=df[df['empresa']==empresa][column]/escalamiento
                             ,orientation='h',marker_color=colores[i],
                            name=empresa,hovertemplate='<br><b>Empresa</b>:<br><extra></extra>'+empresa+'<br>'+                       
        column.capitalize()+' '+unidad+': %{x:.3f}<br>'))
    fig.update_layout(barmode='group')
    fig.update_yaxes(tickangle=0, tickfont=dict(family='Poppins', color='black', size=16),title_text=None,row=1, col=1,
    zeroline=True,linecolor = "rgba(192, 192, 192, 0.8)",zerolinewidth=2)
    fig.update_xaxes(tickfont=dict(family='Poppins', color='black', size=16),titlefont_size=18, title_text=unidad, row=1, col=1)
    fig.update_layout(height=550,legend_title=None)
    fig.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20,
    title={
    'text': titulo,
    'y':0.91,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})        
    fig.update_layout(legend=dict(orientation="v",y=1,x=0.95,font_size=11),showlegend=True,barmode='stack',yaxis={'categoryorder':'category descending'})
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',xaxis_tickformat='d')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
    fig.add_annotation(
    showarrow=False,
    text=textofuente,
    font=dict(size=11), xref='x domain',x=0.5,yref='y domain',y=-0.2)
    return fig

def PlotlyBarrasInt(df,column,unidad,escalamiento,titulo,textofuente):       
    fig = make_subplots(rows=1, cols=1)
    df=df.sort_values(by=column,ascending=False)
    maxdf=df[column].max()/escalamiento+(df[column].max()/escalamiento)*0.3  
    pais=df['País'].unique().tolist()
    for i,pais in enumerate(pais):
        df2=df[df['País']==pais]
        fig.add_trace(go.Bar(x=df2['Cod_pais'],
        y=df2[column]/escalamiento,
        name=pais,hovertemplate ='<br><b>País</b>:<extra></extra>'+pais+
        '<br><b>Penetración (%)</b>: %{y:3f}',marker_color=Colores_pais[pais]))
    fig.update_layout(barmode='group')
    fig.update_yaxes(tickangle=0, tickfont=dict(family='Poppins', color='black', size=16),title_text=unidad,row=1, col=1,
    zeroline=True,linecolor = "rgba(192, 192, 192, 0.8)",zerolinewidth=2)
    fig.update_xaxes(tickangle=0,tickfont=dict(family='Poppins', color='black', size=11),titlefont_size=18, title_text=None, row=1, col=1)
    fig.update_layout(height=550,legend_title=None)
    fig.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20,
    title={
    'text': titulo,
    'y':0.91,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})        
    fig.update_layout(showlegend=False,barmode='stack',yaxis={'categoryorder':'total ascending'})
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',xaxis_tickformat='d')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
    fig.add_annotation(
    showarrow=False,
    text=textofuente,
    font=dict(size=10), xref='x domain',x=0.5,yref='y domain',y=-0.2)    
    return fig

st.set_page_config(
    page_title="Reporte de industria 2022", page_icon=LogoComision,layout="wide",initial_sidebar_state="expanded")
 
Estilo_css="""<style type="text/css">
    @import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap'); 

    html, body, [class*="css"] ,[class*="st-ae"]{
        font-family: 'Poppins', serif; 
    }  
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 300px;}
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 300px;
        top:100px;
        margin-left: -300px;}
    h1{ background: #a6c6fcff;
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
    h2{
        background: #fffdf7;
        text-align: center;
        padding: 10px;
        color: #fb771cff;
        font-weight: bold;
    }    
    h6{
        background: #fffdf7;
        color: #5f7efbff;
        font-weight: bold;
    }      
    .barra-superior{top: 0;
        position: fixed;
        background-color: #5f7efbff;
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
    .titulo {
      background: #fffdf7;
      display: flex;
      color: #5f7efbff;
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
      background-color: #a6c6fcff;
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
        </a>
    </div>
    <div class="imagen-flotar" style="height: 80px; left: 300px; padding:2px">
        <a class="imagen-flotar" href="https://www.crcom.gov.co" title="CRC">
            <img src="https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria/main/2023/Iconos/reporte-de-industria-2023-02.jpg" alt="CRC" style="">
        </a>
    </div>    
</div>"""
st.markdown(Estilo_css+Barra_superior,unsafe_allow_html=True)


########################################### APIs
## Telefonía móvil
#@st.cache
def APISTelMovil():
    from APIs_2023 import AbonadosTelMovil,TraficoTelMovil,IngresosTelMovil,TraficoSMSTelMovil,IngresosSMSTelMovil,IngresosSMSCodigosCortos,TraficoSMSCodigosCortos
    return AbonadosTelMovil,TraficoTelMovil,IngresosTelMovil,TraficoSMSTelMovil,IngresosSMSTelMovil,IngresosSMSCodigosCortos,TraficoSMSCodigosCortos
AbonadosTelMovil,TraficoTelMovil,IngresosTelMovil,TraficoSMSTelMovil,IngresosSMSTelMovil,IngresosSMSCodigosCortos,TraficoSMSCodigosCortos = APISTelMovil()
## Internet móvil
#@st.cache
def APISIntMovil():
    from APIs_2023 import AccesosInternetmovil,IngresosInternetmovil,TraficoInternetMovil
    return AccesosInternetmovil,IngresosInternetmovil,TraficoInternetMovil
AccesosInternetmovil,IngresosInternetmovil,TraficoInternetMovil=APISIntMovil()
## Internet fijo
#@st.cache
def APIsIntFijo():
    from APIs_2023 import AccesosCorpIntFijo,AccesosResIntFijo,IngresosInternetFijo
    return AccesosCorpIntFijo,AccesosResIntFijo,IngresosInternetFijo
AccesosCorpIntFijo,AccesosResIntFijo,IngresosInternetFijo=APIsIntFijo()    
## Telefonía fija
#@st.cache
def APIsTelFija():
    from APIs_2023 import LineasTelefoníaLocal,TraficoTelefoniaFija,IngresosTelefoniaFija
    return LineasTelefoníaLocal,TraficoTelefoniaFija,IngresosTelefoniaFija
LineasTelefoníaLocal,TraficoTelefoniaFija,IngresosTelefoniaFija=APIsTelFija()    
## TV por suscripción
#@st.cache
def APIsTVSus():
    from APIs_2023 import SuscriptoresTVSus,IngresosTVSus
    return SuscriptoresTVSus,IngresosTVSus
SuscriptoresTVSus,IngresosTVSus=APIsTVSus()    
## TV comunitaria
#@st.cache
def APIsTVCom():
    from APIs_2023 import AsociadosTVComunitaria,IngresosTVComunitariaIng
    return AsociadosTVComunitaria,IngresosTVComunitariaIng
AsociadosTVComunitaria,IngresosTVComunitariaIng=APIsTVCom()  
## Dinámica postal
#@st.cache
def APIsDinPostal():
    from APIs_2023 import IngresosyEnviosCorreo,IngresosyEnviosMExpresa,IngresosGiros
    return IngresosyEnviosCorreo,IngresosyEnviosMExpresa,IngresosGiros
IngresosyEnviosCorreo,IngresosyEnviosMExpresa,IngresosGiros=APIsDinPostal()
##TV abierta
#@st.cache
def TVabierta():
    TVabierta=pd.read_csv('https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria/main/2023/Datos_Sin_API/tv_abierta.csv',delimiter=';')
    TVabierta['ingresos']=TVabierta['ingresos'].str.replace('.','').astype('float')
    return TVabierta    
TVabierta=TVabierta()
#@st.cache
def TVpublica():
    TVPublica=pd.read_csv('https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria/main/2023/Datos_Sin_API/tv_publica.csv',delimiter=';')
    TVPublica=TVPublica.fillna(0)
    TVPublica=TVPublica.rename(columns={'Operador':'empresa'})
    return TVPublica
TVPublica=TVpublica()

## IPC
IPC=pd.read_csv('https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria/main/2023/Datos_Sin_API/IPC.csv',delimiter=';')
IPC=IPC.fillna(0)
IPC['anno']=IPC['anno'].astype('int64').astype('str')
IPC['mes']=IPC['mes'].astype('int64').astype('str')
IPC['subclase-cod']=IPC['subclase-cod'].astype('int64').astype('str')
IPC['fecha']=IPC['anno']+'-'+IPC['mes'].str.zfill(2)
IPC['trimestre']=IPC['mes'].apply(trim)
IPC['periodo']=IPC['anno']+'-T'+IPC['trimestre']
IPC['indice2018']=IPC['indice2018'].str.replace(',','.').astype('float')
IPC['indice2022']=IPC['indice2022'].str.replace(',','.').astype('float')
IPCTrim=IPC.groupby(['periodo','anno','trimestre','subclase-cod'])['indice2022'].mean().reset_index()
IPCTrimMov=IPCTrim[IPCTrim['subclase-cod']=='8310400'].drop(columns={'subclase-cod'})
IPCTrimTot=IPCTrim[IPCTrim['subclase-cod']=='0'].drop(columns={'subclase-cod'})
IPCAnu=IPC.groupby(['anno','subclase-cod'])['indice2022'].mean().reset_index()
IPCAnuTot=IPCAnu[IPCAnu['subclase-cod']=='0'].drop(columns={'subclase-cod'})
##
#@st.cache
def gdf_Suramerica():
    gdf_Int = gpd.read_file("https://raw.githubusercontent.com/postdatacrc/Mediciones_QoE/main/Suramerica.geo.json")
    gdf_Int=gdf_Int.rename(columns=({'admin':'País'}))
    return gdf_Int
gdf_Int=gdf_Suramerica()
#@st.cache
def data_Suramerica():    
    with urllib.request.urlopen("https://raw.githubusercontent.com/postdatacrc/Mediciones_QoE/main/Suramerica.geo.json") as url:
        SURAMERICA = json.loads(url.read().decode())
    return SURAMERICA
SURAMERICA=data_Suramerica()  
    
st.sidebar.markdown(r"""<b style="font-size: 26px;text-align:center"> Reporte de industria </b> """,unsafe_allow_html=True)
st.sidebar.markdown(r"""<hr>""",unsafe_allow_html=True)
st.sidebar.markdown("""<b>Índice</b>""", unsafe_allow_html=True)
select_seccion = st.sidebar.selectbox('Escoja la sección del reporte',
                                    ['Portada','Carta editorial','Introducción','Telecomunicaciones','Postal'])

IntroReporteSec1=r"""<p style='text-align:justify'>
El 2022 la economía colombiana registró un crecimiento del Producto Interno Bruto -PIB- de 7,3% apalancado en la demanda interna. La senda evidenciada permitió ubicar 
el nivel del producto en un valor superior en 10,44% a lo evidenciado en 2019, previo a la pandemia del COVID-19. En tanto, la recuperación en el mercado laboral había 
estado rezagado respecto del evidenciado en el PIB. El número de ocupados en todos los meses de 2022 fue superior a los mismos periodos de 2019. La tasa de desempleo continuó 
con la tendencia decreciente hasta cerrar el 2022 con una tasa anual de 11,2%, inferior en 2,6 puntos porcentuales a la registrada en 2021.</p>
"""
IntroReporteSec2=r"""<p style='text-align:justify'>
En tanto, presiones inflacionarias internas como externas llevaron a que la inflación de 2022 alcanzara la cifra más alta en 23 años, llegando hasta el 13,1%. En este contexto, 
el Banco de la República continuó con el proceso de normalización monetaria para contener presiones inflacionarias. Este proceso inició en octubre de 2021, llevando la tasa de 
intervención del 1,75% hasta 11% en diciembre de 2022. Los incrementos en la tasa de intervención incluso han continuado en el primer semestre de 2023.</p>
"""
IntroReporteSec3=r"""<p style='text-align:justify'>
En este contexto, las actividades económicas de Información y comunicaciones tuvieron un crecimiento más robusto, y no se observó el traslado de las presiones inflacionarias a
estos servicios. Así, el crecimiento del valor agregado de estas actividades fue de 11,3%, superior en 6,7 puntos porcentuales al total de PIB y en materia de inflación, los 
servicios de comunicación fija y móvil y provisión a internet fue de 0% en 2022, en contraste a las variaciones negativas observadas en 2021.</p>
"""
IntroReporteSec4=r"""<p style='text-align:justify'>
A continuación, la Comisión de Regulación de Comunicaciones presenta el Reporte de Industria de los sectores TIC y Postal de 2022, cuyo objetivo es presentar la información más 
relevante de estos sectores, para profundizar en el conocimiento de la industria y facilitar la toma de decisiones.<br>
Además de una versión escrita que contiene los datos más relevantes, la CRC dispone de ésta versión interactiva con información más detallada sobre los servicios de telecomunicaciones 
y postales. Así mismo, toda esta información se complementa con diferentes documentos (Data Flash) publicados por la CRC sobre los diferentes servicios, que pueden ser consultados en la 
plataforma de datos abiertos de la CRC <a href='www.postdata.gov.co'>Postdata</a>, así como también con los conjuntos de datos y tableros interactivos contenidos en el portal."""
IntroReporteSec5=r"""<p style='text-align:justify'>
A continuación, se muestra la evolución de los indicadores agregados más relevantes del sector de telecomunicaciones en el país, con una descripción detallada de estos servicios en Colombia 
durante los últimos años, a partir del comportamiento del número de accesos, conexiones, tráfico, ingresos y participaciones de los operadores, entre otras variables."""
IntroReporteSec6=r"""<p style='text-align:justify'> 
Finalmente, se presenta una descripción de indicadores para el sector postal, a partir de los ingresos y tráficos de los servicios de correo, mensajería expresa y giros postales.
</p>
"""


CartaEditorialSec1=r"""<p style='text-align:justify'>
Luego de vivir en el año 2020 un periodo complejo y lleno de incertidumbre derivado de la emergencia del COVID 19, en 2021 los servicios prestados por la industria TIC y Postal desempeñaron un rol fundamental para impulsar la reactivación económica. En este nuevo contexto, dichas industrias siguen evolucionando de manera positiva, sentando las bases para la transformación digital del país.</p>
"""
CartaEditorialSec2=r"""<p style='text-align:justify'>
Mientras apoyaban transversalmente el proceso de recuperación de Colombia, las empresas que hacen parte de estos sectores registraron importantes avances en múltiples aspectos, entre otros, mayores velocidades de las conexiones de Internet, aumento en el despliegue de infraestructura de Internet móvil 4G y fibra óptica, mayor capilaridad y disponibilidad de puntos para giros postales y acciones para soportar un incrementos en el número de envíos del comercio electrónico a través de operadores postales ajustando sus servicios a los nuevos hábitos de consumo de los colombianos y permitiendo la adaptación del resto de actividades económicas.</p>
"""
CartaEditorialSec3=r"""<p style='text-align:justify'> 
A su vez, en su calidad de autoridad regulatoria, la CRC es cada vez más consciente de la importancia de contar con información y datos de calidad para el conocimiento de los mercados. Es por esta razón que el presente reporte constituye una herramienta que facilita la toma de decisiones por parte los usuarios y demás agentes, y es fundamental para el diseño de regulación colaborativa, inclusiva, simplificada y basada en los datos, que continue impulsando la mejora de los servicios de comunicaciones y postales en el país.

Teniendo en cuenta lo anterior, y en alineación con su política de mejora regulatoria, la Comisión pone a disposición de sus grupos de interés a nivel nacional e internacional el Reporte de Industria de los sectores TIC y Postal de 2021, el cual expone de manera general y amplia el panorama de estas industrias en el país, con la rigurosidad técnica y la transparencia que caracteriza al regulador.

El presente informe exhibe los principales datos de relevancia relacionados con los sectores regulados por la entidad, disponiendo por primera vez de una versión interactiva, a través de la cual es posible la profundización del contenido publicado, mediante la exploración de diferentes indicadores analizados</p>
"""

if select_seccion == 'Portada':
    st.title("Reporte de industria 2022")    
    st.image("https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Iconos/reporte%20de%20industria%202023-01.png?raw=true")
    st.markdown("La Comisión de Regulación de Comunicaciones (CRC) pone a disposición del sector y los agentes interesados el tablero interactivo del reporte de industria 2022, donde se destacan las tendencias de los sectores TIC y Postal y su evolución en los últimos años en el país, con el objetivo de profundizar en el conocimiento de la industria y facilitar la toma de decisiones.")
    
if select_seccion =='Carta editorial':
    st.title("Carta editorial")
    col1,col2=st.columns([2,1])
    with col1:
        st.markdown("Nicolás Silva Cortés<br><b>Comisionado y Director Ejecutivo</b>",unsafe_allow_html=True)
        #st.markdown(CartaEditorialSec1,unsafe_allow_html=True)
    with col2:
        st.image('https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Imagenes_adicionales/Nicolas_Silva_Dir.jpg?raw=true', width=250)        
    #st.markdown(CartaEditorialSec2,unsafe_allow_html=True)
    #st.markdown(CartaEditorialSec3,unsafe_allow_html=True)

if select_seccion =='Introducción':
    st.title("Introducción")
    st.markdown("")
    st.markdown(r"""<center><h2>Aspectos generales de los sectores <br>TIC y postal en 2022</h2></center>""",unsafe_allow_html=True)
    st.markdown("<hr>",unsafe_allow_html=True)
    st.markdown(IntroReporteSec1,unsafe_allow_html=True)
    st.markdown(IntroReporteSec2,unsafe_allow_html=True)
    st.markdown(IntroReporteSec3,unsafe_allow_html=True)
    st.markdown(IntroReporteSec4,unsafe_allow_html=True)
    st.markdown(IntroReporteSec5,unsafe_allow_html=True)
    st.markdown(IntroReporteSec6,unsafe_allow_html=True)
    
if select_seccion =='Telecomunicaciones':
    st.title("Sector de telecomunicaciones")
    select_secResumenDinTic = st.sidebar.selectbox('Seleccione el sector a consultar',['Información general',
    'Servicios móviles','Servicios fijos','Servicios de radiodifusión','Servicios OTT','Comparación internacional'])
    
    if select_secResumenDinTic == 'Información general':
        st.markdown(r"""<div class="titulo"><h3>Información general</h3></div>""",unsafe_allow_html=True)

        col1, col2, col3,col4,col5,col6 = st.columns(6)
        with col2:
            st.markdown(r"""<div><img height="100px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Iconos/internet%20movil.png?raw=true'/></div>""",unsafe_allow_html=True) 
        with col3:
            st.markdown(r"""<div><img height="100px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Iconos/telefonia%20movil.png?raw=true'/></div>""",unsafe_allow_html=True) 
        with col4:
            st.markdown(r"""<div><img height="100px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Iconos/internet%20fijo.png?raw=true'/></div>""",unsafe_allow_html=True) 
        with col5:
            st.markdown(r"""<div><img height="100px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Iconos/telefonia%20fija.png?raw=true'/></div>""",unsafe_allow_html=True) 
        with col6:
            st.markdown(r"""<div><img height="100px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Iconos/tv%20suscripcion.png?raw=true'/></div>""",unsafe_allow_html=True) 
        with col1:
            st.markdown("<h2>Accesos por servicio</h2>",unsafe_allow_html=True)
        col2.metric("Internet móvil", "40,11 M", "5,6%")
        col3.metric("Telefonía móvil", "80,81 M", "7,7%")
        col4.metric("Internet fijo", "8,9M", "5,3%")
        col5.metric("Telefonía fija", "7,58M", "0,2%")
        col6.metric("TV por suscripción", "6,30M", "2,15%")
        st.markdown("<p style='font-size:12px'><b>Nota:</b> Variación porcentual calculada respecto de los accesos registrados en 2021 </p>",unsafe_allow_html=True)
        st.markdown('')
        st.markdown('<hr>',unsafe_allow_html=True)
        st.markdown(r"""<h2>Panorama del sector</h2>""",unsafe_allow_html=True)
        st.markdown('')
        col1,col2=st.columns(2)
        with col1:
            st.markdown("<p style='text-align:justify'>En 2022 los servicios de telecomunicaciones obtuvieron ingresos por 25,4 billones de pesos, un 9,9% más, en términos reales  que en 2021. Los servicios de Internet fijo y móvil representaron el 59,7% del total de ingresos de 2022. En tanto, la variación real en los ingresos de los servicios voz fija y móvil presentó comportamientos contrarios. Mientras telefonía fija se contrajo 0,9%, la telefonía móvil creció 2,9%. <br><br>De otra parte, los sectores expuestos a ingresos por pauta publicitaria, es decir, los servicios radiodifundidos de televisión y radio, mostraron variaciones reales en tendencias contrarias. En TV abierta, el crecimiento en los ingresos no fue suficiente para compensar la inflación del año 2022 y cayeron en términos reales el 0,2%. En tanto, los ingresos de radio crecieron en términos reales el 6,5%.</p>",unsafe_allow_html=True)       
        with col2:
            st.image('https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Imagenes_adicionales/Ingresos_servicio_2022.png?raw=true')
            st.markdown("<p style='font-size:10px'><b>Fuente:</b> Elaboración CRC con base en los reportes de información al sistema Colombia TIC, Contaduría General de la Nación – CHIP.", unsafe_allow_html=True)

        col1,col2=st.columns(2)
        with col1:
            st.markdown("<p style='text-align:justify'>En materia de accesos, todos los servicios de telecomunicaciones mostraron tasas de crecimientos positivas en 2022. El servicio con mayor crecimiento en accesos fue Internet móvil con 12,6%. El servicio con mayor penetración en móviles fue la telefonía, con 156 accesos por cada 100 personas, mientras que en servicios fijos el de mayor penetración fue el Internet, con 51 accesos por cada 100 hogares</p>",unsafe_allow_html=True)
        with col2:
            st.image('https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Imagenes_adicionales/Accesos_TIC.png?raw=true')
            st.markdown("<p style='font-size:10px'><b>Fuente:</b> Elaboración CRC con base en los reportes de información al sistema Colombia TIC, proyecciones de población y hogares de DANE.", unsafe_allow_html=True)
            
    if select_secResumenDinTic == 'Servicios móviles':
        bla="https://github.com/postdatacrc/Reporte-de-industria/blob/main/Iconos/VozTelMovil.jpg?raw=true"
        st.markdown(r"""<div class="titulo"><h3>Servicios móviles</h3></div>""",unsafe_allow_html=True)
        st.markdown("<center>Para continuar, por favor seleccione el botón con el servicio del cual desea conocer la información</center>",unsafe_allow_html=True)
        
        ServiciosMóviles=st.radio('',['Telefonía','Mensajería','Internet'],horizontal=True)
            
        st.markdown(r"""<hr>""",unsafe_allow_html=True)    
            
            
        if ServiciosMóviles=='Telefonía':
            dfAbonadosTelMovil=[];
            EmpresasTelMovil=['830122566','800153993','830114921','899999115']
            col1,col2=st.columns(2)
            with col1:                
                st.markdown(r"""<div class='IconoTitulo'><img height="200px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Iconos/telefonia%20movil.png?raw=true'/><h4 style="text-align:left">Telefonía móvil</h4></div>""",unsafe_allow_html=True)   
            with col2:                
                with st.expander("Datos relevantes de Telefonía móvil"):
                    st.markdown(r"""<ul>
                    <li>El total de abonados a telefonía móvil alcanzó los 80,81 millones al cierre de 2022, 5,7 millones más que en 2021.</li>
                    <li>En tráfico, en el 2022 se obtuvo un valor de 135,6 miles de millones de minutos, lo que corresponde a un decrecimiento del 16,2% respecto al valor de 2021.</li>
                    <li>En 2022, el servicio de telefonía móvil generó ingresos por un valor de 2,334.6 miles de millones de pesos, lo que equivale a un reducción de 2,4% respecto a 2021. El 70,4% correspondió a la modalidad pospago.</li>
                    </ul>""",unsafe_allow_html=True)

     
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
                    LineaTiempoAbonadosTelmovil=st.button('Evolución temporal',key='1')
                with col2:
                    BarrasAbonadosTelmovil=st.button('Información por operadores',key='2')
                with col3:
                    PieAbonadosTelmovil=st.button('Participaciones',key='3')

                
                if LineaTiempoAbonadosTelmovil:    
                    AboTrimTelMovil=AbonadosTelMovil.groupby(['periodo','empresa','id_empresa'])['abonados'].sum().reset_index()
                    AboTrimTelMovilA=AbonadosTelMovil.groupby(['periodo','modalidad'])['abonados'].sum().reset_index()
                    AboTrimTelMovilB=AbonadosTelMovil.groupby(['periodo'])['abonados'].sum().reset_index()
                    AboTrimTelMovilB['modalidad']='TOTAL'
                    AboTrimTelMovilTOTAL=pd.concat([AboTrimTelMovilA,AboTrimTelMovilB]).sort_values(by=['periodo'])
                    AboTrimTelMovilTOTAL['periodo_formato']=AboTrimTelMovilTOTAL['periodo'].apply(periodoformato)
                    st.plotly_chart(Plotlylineatiempo(AboTrimTelMovilTOTAL,'abonados','Millones',1e6,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Abonados Telefonía móvil por periodo','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)
                if BarrasAbonadosTelmovil:
                    AbonadosTelMovil=AbonadosTelMovil[AbonadosTelMovil['trimestre']=='4']
                    AboAnualTelMovl=AbonadosTelMovil.groupby(['anno','empresa','id_empresa'])['abonados'].sum().reset_index()  
                    EmpTelMovilAbonados=AboAnualTelMovl[AboAnualTelMovl['anno']=='2022'].sort_values(by='abonados',ascending=False)['id_empresa'].to_list()[0:5]
                    AboAnualTelMovl.loc[AboAnualTelMovl['id_empresa'].isin(EmpTelMovilAbonados)==False,'empresa']='Otros'
                    AboAnualTelMovl.loc[AboAnualTelMovl['id_empresa'].isin(EmpTelMovilAbonados)==False,'id_empresa']='Otros'
                    AboAnualTelMovl=AboAnualTelMovl[(AboAnualTelMovl['anno'].isin(['2021','2022']))].groupby(['anno','empresa','id_empresa'])['abonados'].sum().reset_index()
                    st.plotly_chart(PlotlyBarras(AboAnualTelMovl,'abonados','Millones',1e6,'<b>Abonados anuales por empresa','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)
                if PieAbonadosTelmovil:
                    AbonadosTelMovil=AbonadosTelMovil[AbonadosTelMovil['trimestre']=='4']
                    AboAnualTelMovl=AbonadosTelMovil.groupby(['anno','empresa','id_empresa'])['abonados'].sum().reset_index()  
                    AboAnualTelMovl=AboAnualTelMovl[(AboAnualTelMovl['anno']=='2022')]
                    AboAnualTelMovl['empresa']=AboAnualTelMovl['empresa'].replace(nombresComerciales)
                    AboAnualTelMovl['participacion']=round(100*AboAnualTelMovl['abonados']/AboAnualTelMovl['abonados'].sum(),1)
                    figPieTelMovil = px.pie(AboAnualTelMovl, values='abonados', names='empresa', color='empresa',
                                 color_discrete_map=Colores_pie, title='<b>Participación en abonados de telefonía móvil<br>(2022-T4)')
                    figPieTelMovil.update_traces(textposition='inside',textinfo='percent',hoverinfo='label+percent',textfont_color='black')
                    figPieTelMovil.update_layout(uniformtext_minsize=20,uniformtext_mode='hide',showlegend=True,legend=dict(x=0.9,y=0.3),title_x=0.5)
                    figPieTelMovil.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20)
                    figPieTelMovil.add_annotation(
                    showarrow=False,
                    text='<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC',
                    font=dict(size=11), xref='x domain',x=0.5,yref='y domain',y=-0.2)
                    st.plotly_chart(figPieTelMovil,use_container_width=True)
                               
            if ServiciosTelMovil=='Tráfico':
                
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoTraficoTelmovil=st.button('Evolución temporal')
                with col2:
                    BarrasTraficoTelmovil=st.button('Información por operadores')
                    
                if LineaTiempoTraficoTelmovil:    
                    TraficoTelMovil=TraficoTelMovil.rename(columns={'tipo_trafico':'modalidad'})
                    TraficoTelMovil['modalidad']=TraficoTelMovil['modalidad'].replace({'Tráfico pospago':'POSPAGO','Tráfico prepago':'PREPAGO'})
                    TrafTrimTelMovil=TraficoTelMovil.groupby(['periodo','empresa','id_empresa','modalidad'])['trafico'].sum().reset_index()                    
                    TrafTrimTelMovilA=TraficoTelMovil.groupby(['periodo','modalidad'])['trafico'].sum().reset_index()
                    TrafTrimTelMovilB=TraficoTelMovil.groupby(['periodo'])['trafico'].sum().reset_index()
                    TrafTrimTelMovilB['modalidad']='TOTAL'
                    TrafTrimTelMovilTOTAL=pd.concat([TrafTrimTelMovilA,TrafTrimTelMovilB]).sort_values(by=['periodo'])
                    TrafTrimTelMovilTOTAL['periodo_formato']=TrafTrimTelMovilTOTAL['periodo'].apply(periodoformato)
                    st.plotly_chart(Plotlylineatiempo(TrafTrimTelMovilTOTAL,'trafico','Miles de Millones de minutos',1e9,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Tráfico Telefonía móvil por periodo</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)
                if BarrasTraficoTelmovil:
                    TrafAnualTelMovl=TraficoTelMovil.groupby(['anno','empresa','id_empresa'])['trafico'].sum().reset_index()
                    EmpTelMovilTrafico=TrafAnualTelMovl[TrafAnualTelMovl['anno']=='2022'].sort_values(by='trafico',ascending=False)['id_empresa'].to_list()[0:5]
                    TrafAnualTelMovl.loc[TrafAnualTelMovl['id_empresa'].isin(EmpTelMovilTrafico)==False,'empresa']='Otros'
                    TrafAnualTelMovl.loc[TrafAnualTelMovl['id_empresa'].isin(EmpTelMovilTrafico)==False,'id_empresa']='Otros'                    
                    TrafAnualTelMovl=TrafAnualTelMovl[(TrafAnualTelMovl['anno'].isin(['2021','2022']))].groupby(['anno','empresa','id_empresa'])['trafico'].sum().reset_index()
                    st.plotly_chart(PlotlyBarras(TrafAnualTelMovl,'trafico','Miles de Millones de minutos',1e9,'<b>Tráfico anual por empresa</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)  
            
            if ServiciosTelMovil=='Ingresos':
                st.markdown("""<center><p style="font-size:12px"><b>Nota:</b> Ingresos ajustados por inflación, usando el IPC de la subclase "Servicios de comunicación fija y movil y provisión a internet". Periodo base, diciembre 2022</p></center>""",unsafe_allow_html=True)
                    
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoIngresosTelmovil=st.button('Evolución temporal')
                with col2:
                    BarrasIngresosTelmovil=st.button('Información por operadores')
                
                IngresosTelMovil=IngresosTelMovil.merge(IPCTrimMov,left_on=['anno','trimestre','periodo'],right_on=['anno','trimestre','periodo'])
                IngresosTelMovil['ingresos_totales']=IngresosTelMovil['ingresos_totales']/IngresosTelMovil['indice2022']
                IngresosTelMovil=IngresosTelMovil.astype({'ingresos_totales':'int64','ingresos_prepago':'int64','ingresos_pospago':'int64'})
                IngresosTelMovil['ingresos_pospago']=IngresosTelMovil['ingresos_pospago']/IngresosTelMovil['indice2022']
                IngresosTelMovil['ingresos_prepago']=IngresosTelMovil['ingresos_prepago']/IngresosTelMovil['indice2022']
                
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
                    st.plotly_chart(Plotlylineatiempo(IngresosTelMovil2Agg,'ingresos','Miles de Millones de pesos',1e9,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Ingresos Telefonía móvil por periodo</b>','<b>Fuente</b>:Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)                    
                    col1,col2=st.columns(2)
                    with col1:
                        st.plotly_chart(PlotlyIngresosPorAcceso(IngresosPorAbonadoTelMovil2,'Ingresos/Abonado','Pesos',1,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Ingresos trimestrales por abonado</b>',''), use_container_width=True)
                    with col2:
                        st.plotly_chart(PlotlyIngresosPorAcceso(IngresosPorTraficoTelMovil2,'Ingresos/Trafico','Pesos/Min',1,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Ingresos trimestrales por tráfico</b>',''), use_container_width=True)
  
                if BarrasIngresosTelmovil:
                    IngresosTelMovil3=pd.melt(IngresosTelMovil,id_vars=['anno','id_empresa','empresa'],value_vars=['ingresos_totales','ingresos_prepago',
                                                                                        'ingresos_pospago'],var_name='modalidad', value_name='ingresos')
                    IngresosTelMovil3=IngresosTelMovil3[IngresosTelMovil3['modalidad']=='ingresos_totales']                                                                  
                    IngresosTelMovil3Agg=IngresosTelMovil3.groupby(['anno','id_empresa','empresa'])['ingresos'].sum().reset_index()   
                    EmpTelMovilIngresos=IngresosTelMovil3Agg[IngresosTelMovil3Agg['anno']=='2022'].sort_values(by='ingresos',ascending=False)['id_empresa'].to_list()[0:4]
                    IngresosTelMovil3Agg.loc[IngresosTelMovil3Agg['id_empresa'].isin(EmpTelMovilIngresos)==False,'empresa']='Otros'
                    IngresosTelMovil3Agg.loc[IngresosTelMovil3Agg['id_empresa'].isin(EmpTelMovilIngresos)==False,'id_empresa']='Otros'                    
                    IngresosTelMovil3Agg=IngresosTelMovil3Agg[(IngresosTelMovil3Agg['anno'].isin(['2021','2022']))].groupby(['anno','empresa','id_empresa'])['ingresos'].sum().reset_index()
                    st.plotly_chart(PlotlyBarras(IngresosTelMovil3Agg,'ingresos','Miles de Millones de pesos',1e9,'<b>Ingresos anuales por empresa</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)  
                    ##
                    IngresosPorAbonadoTelMovil=IngresosPorAbonadoTelMovil[(IngresosPorAbonadoTelMovil['trimestre']=='4')&(IngresosPorAbonadoTelMovil['modalidad']=='TOTAL')]
                    IngresosPorAbonadoTelMovil3=IngresosPorAbonadoTelMovil.groupby(['periodo','empresa_x','id_empresa']).agg({'ingresos':'sum','abonados':'sum'}).reset_index()
                    IngresosPorAbonadoTelMovil3['Ingresos/Abonado']=round(IngresosPorAbonadoTelMovil3['ingresos']/IngresosPorAbonadoTelMovil3['abonados'],2)
                    IngresosPorAbonadoTelMovil3=IngresosPorAbonadoTelMovil3[(IngresosPorAbonadoTelMovil3['id_empresa'].isin(EmpTelMovilIngresos))&(IngresosPorAbonadoTelMovil3['periodo'].isin(['2021-T4','2022-T4']))]
                    IngresosPorAbonadoTelMovil3=IngresosPorAbonadoTelMovil3.rename(columns={'empresa_x':'empresa','periodo':'anno'})
                    ##
                    IngresosPorTraficoTelMovil3=IngresosPorTraficoTelMovil.groupby(['periodo','empresa_x','id_empresa']).agg({'ingresos':'sum','trafico':'sum'}).reset_index()
                    IngresosPorTraficoTelMovil3['Ingresos/Trafico']=round(IngresosPorTraficoTelMovil3['ingresos']/IngresosPorTraficoTelMovil3['trafico'],2)
                    IngresosPorTraficoTelMovil3=IngresosPorTraficoTelMovil3[(IngresosPorTraficoTelMovil3['id_empresa'].isin(EmpTelMovilIngresos))&(IngresosPorTraficoTelMovil3['periodo'].isin(['2021-T4','2022-T4']))]
                    IngresosPorTraficoTelMovil3=IngresosPorTraficoTelMovil3.rename(columns={'empresa_x':'empresa','periodo':'anno'})
                    
                    
                    col1,col2=st.columns(2)
                    with col1:
                        st.plotly_chart(PlotlyBarras(IngresosPorAbonadoTelMovil3,'Ingresos/Abonado','Pesos',1,'<b>Ingresos por abonado y por empresa</b>',''),use_container_width=True)  
                    with col2:
                        st.plotly_chart(PlotlyBarras(IngresosPorTraficoTelMovil3,'Ingresos/Trafico','Pesos/Min',1,'<b>Ingresos por tráfico y por empresa</b>',''),use_container_width=True)  
                                                                                                 
        if ServiciosMóviles=='Internet':
            ##Tráfico
            TraficoInternetMovil=TraficoInternetMovil[TraficoInternetMovil['trafico']>0]
            TraficoInternetMovilTotal=TraficoInternetMovil.groupby(['anno','trimestre','id_empresa','empresa','periodo'])['trafico'].sum().reset_index()
            TraficoInternetMovilTotal['modalidad']='Total'
            TraficoInternetMovildf=pd.concat([TraficoInternetMovil,TraficoInternetMovilTotal]).sort_values(by=['periodo'])  
            TraficoInternetMovildf['trafico']=TraficoInternetMovildf['trafico']/1024

            ## Ingresos
            IngresosInternetmovil=IngresosInternetmovil[IngresosInternetmovil['ingresos']>0]
            IngresosInternetmovil=IngresosInternetmovil.merge(IPCTrimMov,left_on=['anno','trimestre','periodo'],right_on=['anno','trimestre','periodo'])
            IngresosInternetmovil['ingresos']=IngresosInternetmovil['ingresos']/IngresosInternetmovil['indice2022']
            IngresosInternetmovilTotal=IngresosInternetmovil.groupby(['anno','trimestre','id_empresa','empresa','periodo'])['ingresos'].sum().reset_index()
            IngresosInternetmovilTotal['modalidad']='Total'
            IngresosInternetmovildf=pd.concat([IngresosInternetmovil,IngresosInternetmovilTotal]).sort_values(by=['periodo'])

            ##Accesos
            AccesosInternetmovil=AccesosInternetmovil[AccesosInternetmovil['accesos']>0]
            AccesosInternetmovilTotal=AccesosInternetmovil.groupby(['anno','trimestre','id_empresa','empresa','periodo'])['accesos'].sum().reset_index()
            AccesosInternetmovilTotal['modalidad']='Total'
            AccesosInternetmovildf=pd.concat([AccesosInternetmovil,AccesosInternetmovilTotal]).sort_values(by=['periodo'])
            #AccesosInternetmovildf['empresa']=AccesosInternetmovildf['empresa'].replace({'COLOMBIA TELECOMUNICACIONES S.A. E.S.P.':'COLOMBIA TELECOMUNICACIONES S.A. ESP',
            #AccesosInternetmovildf['empresa'].unique().tolist()[13]:'COLOMBIA MOVIL S.A. E.S.P.','EMPRESA DE TELECOMUNICACIONES DE BOGOTA S.A. ESP':'EMPRESA DE TELECOMUNICACIONES DE BOGOTÁ S.A. ESP.',
            #'AVANTEL S.A.S':'AVANTEL S.A.S.','SUMA MOVIL S.A.S.':'SUMA'})
            AccesosInternetmovildf=AccesosInternetmovildf[(AccesosInternetmovildf['anno']>'2017')]
                        
            col1,col2 = st.columns(2)
            with col1:
                st.markdown(r"""<div class='IconoTitulo'><img height="200px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Iconos/internet%20movil.png?raw=true'/><h4>Internet móvil</h4></div>""",unsafe_allow_html=True) 
       
            with col2:             
                with st.expander("Datos relevantes de Internet móvil"):
                    st.markdown(r"""<ul>
                    <li>Entre el cuarto trimestre de 2021 y 2022, los accesos de Internet móvil se incrementaron en más de 2.15 millones, alcanzando 40.11 millones al cierre de 2022</li>
                    <li>El tráfico alcanzó un valor de 3084,5 millones de GB, lo que corresponde a un crecimiento de 62.8% frente a 2021.</li>     
                    <li>Los ingresos ascendieron a 8,7 billones de pesos, equivalente a un crecimiento de 17% frente al año anterior.</li>        
                    </ul>""",unsafe_allow_html=True)
            
            
            ServiciosIntMovil=st.selectbox('Escoja el servicio de Internet móvil',['Accesos','Tráfico','Ingresos'])
            st.markdown("""<p style="font-size:12px"><b>Nota:</b> Los servicios de Internet móvil por demanda corresponden a aquellos que se obtienen sin que medie la contratación de un plan para tal fin, mientras que los servicios de Internet móvil por cargo fijo se dan a través de la contratación de un plan que se paga de forma periódica.</p>""",unsafe_allow_html=True)

                                        
            if ServiciosIntMovil=='Accesos':  
            
                col1,col2,col3=st.columns(3)
                with col1:
                    LineaTiempoAccesosIntmovil=st.button('Evolución temporal')
                with col2:
                    BarrasAccesosIntmovil=st.button('Información por operadores')
                with col3:
                    PieAccesosIntmovil=st.button('Participaciones')    
                 
                if LineaTiempoAccesosIntmovil:
                    AccesosInternetmovilNac=AccesosInternetmovildf.groupby(['periodo','modalidad'])['accesos'].sum().reset_index()
                    AccesosInternetmovilNac['periodo_formato']=AccesosInternetmovilNac['periodo'].apply(periodoformato)
                    st.plotly_chart(Plotlylineatiempo(AccesosInternetmovilNac,'accesos','Millones',1e6,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Accesos Internet móvil por periodo</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)
                if BarrasAccesosIntmovil:
                    AccesosInternetmovilEmp=AccesosInternetmovildf[(AccesosInternetmovildf['modalidad']=='Total')&(AccesosInternetmovildf['trimestre']=='4')&(AccesosInternetmovildf['anno'].isin(['2021','2022']))]
                    EmpIntMovilAccesos=AccesosInternetmovilEmp[AccesosInternetmovilEmp['anno']=='2022'].sort_values(by='accesos',ascending=False)['id_empresa'].to_list()[0:4]
                    AccesosInternetmovilEmp.loc[AccesosInternetmovilEmp['id_empresa'].isin(EmpIntMovilAccesos)==False,'empresa']='Otros'
                    AccesosInternetmovilEmp.loc[AccesosInternetmovilEmp['id_empresa'].isin(EmpIntMovilAccesos)==False,'id_empresa']='Otros'     
                    AccesosInternetmovilEmp=AccesosInternetmovilEmp.groupby(['anno','empresa','id_empresa'])['accesos'].sum().reset_index()
                    st.plotly_chart(PlotlyBarras(AccesosInternetmovilEmp,'accesos','Millones',1e6,'<b>Accesos anuales por empresa</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)
                if PieAccesosIntmovil:
                    AccesosInternetmovilPie=AccesosInternetmovildf[(AccesosInternetmovildf['modalidad']=='Total')&(AccesosInternetmovildf['trimestre']=='4')&(AccesosInternetmovildf['anno'].isin(['2022']))]
                    AccesosInternetmovilPie=AccesosInternetmovilPie.groupby(['anno','empresa','id_empresa'])['accesos'].sum().reset_index()
                    AccesosInternetmovilPie['empresa']=AccesosInternetmovilPie['empresa'].replace(nombresComerciales)
                    AccesosInternetmovilPie['participacion']=round(100*AccesosInternetmovilPie['accesos']/AccesosInternetmovilPie['accesos'].sum(),1)
                    figPieIntMovil = px.pie(AccesosInternetmovilPie, values='accesos', names='empresa', color='empresa',
                                 color_discrete_map=Colores_pie,title='<b>Participación en accesos de Internet móvil<br>(2022-T4)')
                    figPieIntMovil.update_traces(textposition='inside',textinfo='percent',hoverinfo='label+percent',textfont_color='black')
                    figPieIntMovil.update_layout(uniformtext_minsize=20,uniformtext_mode='hide',showlegend=True,legend=dict(x=0.9,y=0.3),title_x=0.5)
                    figPieIntMovil.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20)
                    figPieIntMovil.add_annotation(
                    showarrow=False,
                    text='<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC',
                    font=dict(size=11), xref='x domain',x=0.5,yref='y domain',y=-0.2)
                    st.plotly_chart(figPieIntMovil,use_container_width=True)
                
            if ServiciosIntMovil=='Tráfico':
                
                #TraficoInternetMovildf['trafico']=TraficoInternetMovildf['trafico']/1000                                                                        
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoTraficoIntmovil=st.button('Evolución temporal')
                with col2:
                    BarrasTraficoIntmovil=st.button('Información por operadores')
                if LineaTiempoTraficoIntmovil:             
                    TraficoInternetMovilNac=TraficoInternetMovildf.groupby(['periodo','modalidad'])['trafico'].sum().reset_index()
                    TraficoInternetMovilNac['periodo_formato']=TraficoInternetMovilNac['periodo'].apply(periodoformato)
                    st.plotly_chart(Plotlylineatiempo(TraficoInternetMovilNac,'trafico','Millones de GB',1e6,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Tráfico Internet móvil por periodo</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)
                if BarrasTraficoIntmovil:
                    TraficoInternetMovilEmp=TraficoInternetMovildf.groupby(['anno','modalidad','empresa','id_empresa'])['trafico'].sum().reset_index()
                    TraficoInternetMovilEmp=TraficoInternetMovilEmp[(TraficoInternetMovilEmp['modalidad']=='Total')&(TraficoInternetMovilEmp['anno'].isin(['2021','2022']))]
                    EmpIntMovilTrafico=TraficoInternetMovilEmp[TraficoInternetMovilEmp['anno']=='2022'].sort_values(by='trafico',ascending=False)['id_empresa'].to_list()[0:4]
                    TraficoInternetMovilEmp.loc[TraficoInternetMovilEmp['id_empresa'].isin(EmpIntMovilTrafico)==False,'empresa']='Otros'
                    TraficoInternetMovilEmp.loc[TraficoInternetMovilEmp['id_empresa'].isin(EmpIntMovilTrafico)==False,'id_empresa']='Otros'     
                    TraficoInternetMovilEmp=TraficoInternetMovilEmp.groupby(['anno','empresa','id_empresa'])['trafico'].sum().reset_index()
                    st.plotly_chart(PlotlyBarras(TraficoInternetMovilEmp,'trafico','Millones de GB',1e6,'<b>Tráfico anual por empresa</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)

            if ServiciosIntMovil=='Ingresos':
                st.markdown("""<center><p style="font-size:12px"><b>Nota:</b> Ingresos ajustados por inflación, usando el IPC de la subclase "Servicios de comunicación fija y movil y provisión a internet". Periodo base, diciembre 2022</p></center>""",unsafe_allow_html=True)                
                IngresosInternetmovilNac=IngresosInternetmovildf.groupby(['periodo','modalidad'])['ingresos'].sum().reset_index()
                IngresosInternetmovilNac['periodo_formato']=IngresosInternetmovilNac['periodo'].apply(periodoformato)
                
                IngresosInternetmovilEmp=IngresosInternetmovildf.groupby(['anno','modalidad','empresa','id_empresa'])['ingresos'].sum().reset_index() 
                IngresosInternetmovilEmp=IngresosInternetmovilEmp[(IngresosInternetmovilEmp['anno'].isin(['2021','2022']))&(IngresosInternetmovilEmp['modalidad']=='Total')]
                EmpIntMovilIngresos=IngresosInternetmovilEmp[IngresosInternetmovilEmp['anno']=='2021'].sort_values(by='ingresos',ascending=False)['id_empresa'].to_list()[0:4]
                IngresosInternetmovilEmp.loc[IngresosInternetmovilEmp['id_empresa'].isin(EmpIntMovilIngresos)==False,'empresa']='Otros'
                IngresosInternetmovilEmp.loc[IngresosInternetmovilEmp['id_empresa'].isin(EmpIntMovilIngresos)==False,'id_empresa']='Otros'     
                IngresosInternetmovilEmp=IngresosInternetmovilEmp.groupby(['anno','empresa','id_empresa','modalidad'])['ingresos'].sum().reset_index()
                #
                IngresosInternetmovilEmp2=IngresosInternetmovildf.groupby(['periodo','modalidad','empresa','id_empresa'])['ingresos'].sum().reset_index() 
                IngresosInternetmovilEmp2=IngresosInternetmovilEmp2[(IngresosInternetmovilEmp2['periodo'].isin(['2021-T4','2022-T4']))&(IngresosInternetmovilEmp2['modalidad']=='Total')]
                IngresosInternetmovilEmp2.loc[IngresosInternetmovilEmp2['id_empresa'].isin(EmpIntMovilIngresos)==False,'empresa']='Otros'
                IngresosInternetmovilEmp2.loc[IngresosInternetmovilEmp2['id_empresa'].isin(EmpIntMovilIngresos)==False,'id_empresa']='Otros'     
                IngresosInternetmovilEmp2=IngresosInternetmovilEmp2.groupby(['periodo','empresa','id_empresa','modalidad'])['ingresos'].sum().reset_index()
                
                ## Limpieza accesos              
                AccesosInternetmovilNac=AccesosInternetmovildf.groupby(['periodo','modalidad'])['accesos'].sum().reset_index()
                AccesosInternetmovilEmp=AccesosInternetmovildf[(AccesosInternetmovildf['modalidad']=='Total')&(AccesosInternetmovildf['trimestre']=='4')&(AccesosInternetmovildf['anno'].isin(['2021','2022']))]
                AccesosInternetmovilEmp.loc[AccesosInternetmovilEmp['id_empresa'].isin(EmpIntMovilIngresos)==False,'empresa']='Otros'
                AccesosInternetmovilEmp.loc[AccesosInternetmovilEmp['id_empresa'].isin(EmpIntMovilIngresos)==False,'id_empresa']='Otros' 
                AccesosInternetmovilEmp=AccesosInternetmovilEmp.groupby(['periodo','empresa','modalidad','id_empresa'])['accesos'].sum().reset_index()  

                ## Limpieza tráfico
           
                TraficoInternetMovilNac=TraficoInternetMovildf.groupby(['periodo','modalidad'])['trafico'].sum().reset_index() 
                TraficoInternetMovilEmp=TraficoInternetMovildf.groupby(['periodo','modalidad','id_empresa','empresa'])['trafico'].sum().reset_index()                 
                TraficoInternetMovilEmp=TraficoInternetMovilEmp[(TraficoInternetMovilEmp['periodo'].isin(['2021-T4','2022-T4']))&(TraficoInternetMovilEmp['modalidad']=='Total')]
                TraficoInternetMovilEmp.loc[TraficoInternetMovilEmp['id_empresa'].isin(EmpIntMovilIngresos)==False,'empresa']='Otros'
                TraficoInternetMovilEmp.loc[TraficoInternetMovilEmp['id_empresa'].isin(EmpIntMovilIngresos)==False,'id_empresa']='Otros' 
                TraficoInternetMovilEmp=TraficoInternetMovilEmp.groupby(['periodo','empresa','modalidad','id_empresa'])['trafico'].sum().reset_index()  
                
                IngPorTraficoIntMovilEmp=IngresosInternetmovilEmp2.merge(TraficoInternetMovilEmp,left_on=['periodo','modalidad','id_empresa'],right_on=['periodo','modalidad','id_empresa'])
                IngPorTraficoIntMovilEmp['Ingresos/Trafico']=round(IngPorTraficoIntMovilEmp['ingresos']/IngPorTraficoIntMovilEmp['trafico'],2)
                IngPorTraficoIntMovilEmp=IngPorTraficoIntMovilEmp[IngPorTraficoIntMovilEmp['modalidad']=='Total']
                ## Ingresos por acceso
                IngPorAccesosIntMovil=IngresosInternetmovilNac.merge(AccesosInternetmovilNac,left_on=['periodo','modalidad'],right_on=['periodo','modalidad'])
                IngPorAccesosIntMovil['Ingresos/Acceso']=round(IngPorAccesosIntMovil['ingresos']/IngPorAccesosIntMovil['accesos'],2)
                IngPorAccesosIntMovil['periodo_formato']=IngPorAccesosIntMovil['periodo'].apply(periodoformato)
                IngPorAccesosIntMovilEmp=IngresosInternetmovilEmp2.merge(AccesosInternetmovilEmp,left_on=['periodo','modalidad','id_empresa'],right_on=['periodo','modalidad','id_empresa'])
                IngPorAccesosIntMovilEmp['Ingresos/Acceso']=round(IngPorAccesosIntMovilEmp['ingresos']/IngPorAccesosIntMovilEmp['accesos'],2)
                IngPorAccesosIntMovilEmp=IngPorAccesosIntMovilEmp[IngPorAccesosIntMovilEmp['modalidad']=='Total']

                ## Ingresos por tráfico
                IngPorTraficoIntMovil=IngresosInternetmovilNac.merge(TraficoInternetMovilNac,left_on=['periodo','modalidad'],right_on=['periodo','modalidad'])
                IngPorTraficoIntMovil['Ingresos/Trafico']=round(IngPorTraficoIntMovil['ingresos']/IngPorTraficoIntMovil['trafico'],2)
                IngPorTraficoIntMovil['periodo_formato']=IngPorTraficoIntMovil['periodo'].apply(periodoformato)     

                
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoIngresosIntmovil=st.button('Evolución temporal')
                with col2:
                    BarrasIngresosIntmovil=st.button('Información por operadores')            
                
                if LineaTiempoIngresosIntmovil:
                                                                                                    
                    st.plotly_chart(Plotlylineatiempo(IngresosInternetmovilNac,'ingresos','Miles de Millones de pesos',1e9,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Ingresos Internet móvil por periodo</b>','<b>Fuente</b>:Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)
                    col1,col2=st.columns(2)
                    with col1:
                        st.plotly_chart(PlotlyIngresosPorAcceso(IngPorAccesosIntMovil,'Ingresos/Acceso','Pesos',1,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Ingresos trimestrales por acceso</b>',''), use_container_width=True)
                    with col2:    
                        st.plotly_chart(PlotlyIngresosPorAcceso(IngPorTraficoIntMovil,'Ingresos/Trafico','Pesos/GB',1,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Ingresos trimestrales por tráfico</b>',''), use_container_width=True)
 
                if BarrasIngresosIntmovil:
                    st.plotly_chart(PlotlyBarras(IngresosInternetmovilEmp,'ingresos','Miles de Millones de pesos',1e9,'<b>Ingresos anuales por empresa</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)
                    col1,col2=st.columns(2)
                    with col1:
                        IngPorAccesosIntMovilEmp=IngPorAccesosIntMovilEmp.rename(columns={'empresa_x':'empresa','periodo':'anno'})
                        st.plotly_chart(PlotlyBarras(IngPorAccesosIntMovilEmp,'Ingresos/Acceso','Pesos',1,'<b>Ingresos por acceso y por empresa</b>',''),use_container_width=True)
                    with col2:
                        IngPorTraficoIntMovilEmp=IngPorTraficoIntMovilEmp.rename(columns={'empresa_x':'empresa','periodo':'anno'})
                        st.plotly_chart(PlotlyBarras(IngPorTraficoIntMovilEmp,'Ingresos/Trafico','Pesos/GB',1,'<b>Ingresos por tráfico y por empresa</b>',''),use_container_width=True)
 
        if ServiciosMóviles=='Mensajería':
        
            col1,col2=st.columns(2)
            with col1:
                st.markdown(r"""<div class='IconoTitulo'><img height="200px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Iconos/sms.png?raw=true'/><h4>Mensajería móvil</h4></div>""",unsafe_allow_html=True)
            with col2:             
                with st.expander("Datos relevantes de Mensajería móvil"):
                    st.markdown(r"""<ul>
                    <li>Lo ingresos por mensajería de texto en 2022 fueron 156,1 mil millones, de los cuales el 76,7% son generados por mensajes cursados entre usuarios.</li>
                    <li>En cuando al servicio de SMS, este se compone de los mensajes cursados entre usuarios y mensajes de texto a través de códigos cortos. El tráfico del primer tipo fue de 1.448,3 millones de mensajes en 2022 y aumentó a tasa anual de 23,7%. En tanto, los segundos fueron 45,019.7 millones de mensajes y disminuyó 7,9% frente al año anterior.</li>
                    </ul>""",unsafe_allow_html=True)
            
            ServiciosMenMovil=st.selectbox('Escoja el ámbito de Mensajería móvil',['Tráfico','Ingresos']) 

            TraficoSMSTelMovil=TraficoSMSTelMovil.rename(columns={'cantidad':'tráfico (SMS)'})
            TraficoSMSTelMovil['periodo']=TraficoSMSTelMovil['anno']+'-T'+TraficoSMSTelMovil['trimestre']
            TraficoSMSTelMovilAgg=TraficoSMSTelMovil.groupby(['periodo'])['tráfico (SMS)'].sum().reset_index()
            TraficoSMSCodigosCortosAgg=TraficoSMSCodigosCortos.groupby(['periodo']).agg({'trafico terminado':'sum','trafico originado':'sum'}).reset_index()
            TraficoSMSCodigosCortosAgg['trafico']=TraficoSMSCodigosCortosAgg['trafico terminado']+TraficoSMSCodigosCortosAgg['trafico originado']
            TraficoSMSCodigosCortosAgg=TraficoSMSCodigosCortosAgg.drop(columns=['trafico terminado','trafico originado'],axis=1)
            TraficoMensajeriaMovil=TraficoSMSTelMovilAgg.merge(TraficoSMSCodigosCortosAgg,left_on=['periodo'],right_on=['periodo'])
            TraficoMensajeriaMovil2=pd.melt(TraficoMensajeriaMovil,id_vars=['periodo'],value_vars=['tráfico (SMS)',
                            'trafico'],var_name='modalidad',value_name='tráfico')
            TraficoMensajeriaMovil2['modalidad']=TraficoMensajeriaMovil2['modalidad'].replace({'tráfico (SMS)':'SMS intercambiados entre usuarios','trafico':'Códigos cortos'})                
            TraficoMensajeriaMovil2['periodo_formato']=TraficoMensajeriaMovil2['periodo'].apply(periodoformato)
            TraficoSMSTelMovilAgg['periodo_formato']=TraficoSMSTelMovilAgg['periodo'].apply(periodoformato)
            #        
            TraficoSMSTelMovil=TraficoSMSTelMovil.rename(columns={'cantidad':'tráfico (SMS)'})
            TraficoSMSTelMovilEmpresa=TraficoSMSTelMovil.groupby(['anno','empresa','id_empresa'])['tráfico (SMS)'].sum().reset_index() 
            EmpMenMovilTraficoSMS=TraficoSMSTelMovilEmpresa[TraficoSMSTelMovilEmpresa['anno']=='2022'].sort_values(by='tráfico (SMS)',ascending=False)['id_empresa'].to_list()[0:4]
            TraficoSMSTelMovilEmpresa.loc[TraficoSMSTelMovilEmpresa['id_empresa'].isin(EmpMenMovilTraficoSMS)==False,'empresa']='Otros'
            TraficoSMSTelMovilEmpresa.loc[TraficoSMSTelMovilEmpresa['id_empresa'].isin(EmpMenMovilTraficoSMS)==False,'id_empresa']='Otros'
            TraficoSMSTelMovilEmpresa=TraficoSMSTelMovilEmpresa[(TraficoSMSTelMovilEmpresa['anno'].isin(['2021','2022']))].groupby(['anno','empresa','id_empresa'])['tráfico (SMS)'].sum().reset_index()
            #
            TraficoSMSCodigosCortosEmp=TraficoSMSCodigosCortos.groupby(['anno','empresa','id_empresa']).agg({'trafico terminado':'sum','trafico originado':'sum'}).reset_index()
            TraficoSMSCodigosCortosEmp['tráfico']=TraficoSMSCodigosCortosEmp['trafico terminado']+TraficoSMSCodigosCortosEmp['trafico originado']
            EmpMenMovilCodigosCortos=TraficoSMSCodigosCortosEmp[TraficoSMSCodigosCortosEmp['anno']=='2022'].sort_values(by='tráfico',ascending=False)['id_empresa'].to_list()[0:4]
            TraficoSMSCodigosCortosEmp.loc[TraficoSMSCodigosCortosEmp['id_empresa'].isin(EmpMenMovilCodigosCortos)==False,'empresa']='Otros'
            TraficoSMSCodigosCortosEmp.loc[TraficoSMSCodigosCortosEmp['id_empresa'].isin(EmpMenMovilCodigosCortos)==False,'id_empresa']='Otros'
            TraficoSMSCodigosCortosEmp=TraficoSMSCodigosCortosEmp[(TraficoSMSCodigosCortosEmp['anno'].isin(['2021','2022']))].groupby(['anno','empresa','id_empresa'])['tráfico'].sum().reset_index()

            
            if ServiciosMenMovil=='Tráfico':
                TraficoSMSTelMovil['periodo']=TraficoSMSTelMovil['anno']+'-T'+TraficoSMSTelMovil['trimestre']
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoTraficoSMSTelmovil=st.button('Evolución temporal')
                with col2:
                    BarrasTraficoSMSTelmovil=st.button('Información por operadores') 
                
                
                if LineaTiempoTraficoSMSTelmovil:
                    #st.plotly_chart(Plotlylineatiempo(TraficoSMSTelMovilAgg,'tráfico (SMS)','Millones de mensajes',1e6,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'Tráfico Mensajería móvil por periodo','<b>Fuente</b>:Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)
                    st.plotly_chart(Plotlylineatiempo(TraficoMensajeriaMovil2,'tráfico','Millones de mensajes',1e6,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Tráfico Mensajería móvil por periodo</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)

                if BarrasTraficoSMSTelmovil:
                    st.plotly_chart(PlotlyBarras(TraficoSMSTelMovilEmpresa,'tráfico (SMS)','Millones de mensajes',1e6,'<b>SMS intercambiados entre usuarios por empresa</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)  
                    st.plotly_chart(PlotlyBarras(TraficoSMSCodigosCortosEmp,'tráfico','Millones de mensajes',1e6,'<b>Tráfico de códigos cortos por empresa</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)  
                
            if ServiciosMenMovil=='Ingresos':
                st.markdown("""<center><p style="font-size:12px"><b>Nota:</b> Ingresos ajustados por inflación, usando el IPC de la subclase "Servicios de comunicación fija y movil y provisión a internet". Periodo base, diciembre 2022</p></center>""",unsafe_allow_html=True)
                IngresosSMSTelMovil['periodo']=IngresosSMSTelMovil['anno']+'-T'+IngresosSMSTelMovil['trimestre']
                IngresosSMSTelMovil=IngresosSMSTelMovil.merge(IPCTrimMov,left_on=['anno','trimestre','periodo'],right_on=['anno','trimestre','periodo'])
                IngresosSMSTelMovil['ingresos']=IngresosSMSTelMovil['ingresos']/IngresosSMSTelMovil['indice2022']
                IngresosSMSCodigosCortos=IngresosSMSCodigosCortos.merge(IPCTrimMov,left_on=['anno','trimestre','periodo'],right_on=['anno','trimestre','periodo'])
                IngresosSMSCodigosCortos['ingresos']=IngresosSMSCodigosCortos['ingresos']/IngresosSMSCodigosCortos['indice2022']
                
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoIngresosSMSTelmovil=st.button('Evolución temporal')
                with col2:
                    BarrasIngresosSMSTelmovil=st.button('Información por operadores')
                ## Limpieza Ingresos SMS    
                IngresosSMSTelMovilAgg=IngresosSMSTelMovil.groupby(['periodo'])['ingresos'].sum().reset_index()
                IngresosSMSTelMovilAgg['periodo_formato']=IngresosSMSTelMovilAgg['periodo'].apply(periodoformato)

                IngresosSMSTelMovilEmpresa=IngresosSMSTelMovil.groupby(['periodo','anno','empresa','id_empresa'])['ingresos'].sum().reset_index()
                IngresosSMSCodigosCortosEmpresa=IngresosSMSCodigosCortos.groupby(['periodo','anno','empresa','id_empresa'])['ingresos'].sum().reset_index()                
                IngresosMensajeríaMóvilEmpresa=pd.concat([IngresosSMSTelMovilEmpresa,IngresosSMSCodigosCortosEmpresa])
                IngresosMensajeríaMóvilEmpresa2=IngresosMensajeríaMóvilEmpresa.groupby(['anno','empresa','id_empresa'])['ingresos'].sum().reset_index()
                EmpMenMovilIngresos=IngresosMensajeríaMóvilEmpresa2[IngresosMensajeríaMóvilEmpresa2['anno']=='2022'].sort_values(by='ingresos',ascending=False)['id_empresa'].to_list()[0:4]
                IngresosMensajeríaMóvilEmpresa2.loc[IngresosMensajeríaMóvilEmpresa2['id_empresa'].isin(EmpMenMovilIngresos)==False,'empresa']='Otros'
                IngresosMensajeríaMóvilEmpresa2.loc[IngresosMensajeríaMóvilEmpresa2['id_empresa'].isin(EmpMenMovilIngresos)==False,'id_empresa']='Otros'
                IngresosMensajeríaMóvilEmpresa2=IngresosMensajeríaMóvilEmpresa2.groupby(['anno','empresa','id_empresa'])['ingresos'].sum().reset_index()
                IngresosMensajeríaMóvilEmpresa2=IngresosMensajeríaMóvilEmpresa2[IngresosMensajeríaMóvilEmpresa2['anno'].isin(['2021','2022'])]
                IngresosMensajeríaMóvilEmpresa3=IngresosMensajeríaMóvilEmpresa[IngresosMensajeríaMóvilEmpresa['periodo'].isin(['2021-T4','2022-T4'])]
                IngresosMensajeríaMóvilEmpresa3=IngresosMensajeríaMóvilEmpresa3.groupby(['anno','empresa','id_empresa'])['ingresos'].sum().reset_index()                
                IngresosMensajeríaMóvilEmpresa3.loc[IngresosMensajeríaMóvilEmpresa3['id_empresa'].isin(EmpMenMovilIngresos)==False,'empresa']='Otros'
                IngresosMensajeríaMóvilEmpresa3.loc[IngresosMensajeríaMóvilEmpresa3['id_empresa'].isin(EmpMenMovilIngresos)==False,'id_empresa']='Otros'
                IngresosMensajeríaMóvilEmpresa3=IngresosMensajeríaMóvilEmpresa3.groupby(['anno','empresa','id_empresa'])['ingresos'].sum().reset_index()
                
                TraficoSMSTelMovilEmpresa2=TraficoSMSTelMovil[TraficoSMSTelMovil['trimestre']=='4'].groupby(['anno','empresa','id_empresa'])['tráfico (SMS)'].sum().reset_index()
                TraficoSMSTelMovilEmpresa2=TraficoSMSTelMovilEmpresa2.rename(columns={'tráfico (SMS)':'tráfico'})
                TraficoSMSCodigosCortos2=TraficoSMSCodigosCortos.copy()
                TraficoSMSCodigosCortos2['tráfico']=TraficoSMSCodigosCortos2['trafico terminado']+TraficoSMSCodigosCortos2['trafico originado']                
                TraficoSMSCodigosCortosEmpresa2=TraficoSMSCodigosCortos2[TraficoSMSCodigosCortos2['trimestre']=='4'].groupby(['anno','empresa','id_empresa'])['tráfico'].sum().reset_index()                
                TraficoMensajeríaMóvilEmpresa=pd.concat([TraficoSMSTelMovilEmpresa2,TraficoSMSCodigosCortosEmpresa2])
                TraficoMensajeríaMóvilEmpresa=TraficoMensajeríaMóvilEmpresa.groupby(['anno','empresa','id_empresa'])['tráfico'].sum().reset_index()
                TraficoMensajeríaMóvilEmpresa.loc[TraficoMensajeríaMóvilEmpresa['id_empresa'].isin(EmpMenMovilIngresos)==False,'empresa']='Otros'
                TraficoMensajeríaMóvilEmpresa.loc[TraficoMensajeríaMóvilEmpresa['id_empresa'].isin(EmpMenMovilIngresos)==False,'id_empresa']='Otros'
                TraficoMensajeríaMóvilEmpresa=TraficoMensajeríaMóvilEmpresa.groupby(['anno','empresa','id_empresa'])['tráfico'].sum().reset_index()
                TraficoMensajeríaMóvilEmpresa=TraficoMensajeríaMóvilEmpresa[TraficoMensajeríaMóvilEmpresa['anno'].isin(['2021','2022'])]
                #
                IngPorTrafMensajeríaMovilEmpresa=IngresosMensajeríaMóvilEmpresa3.merge(TraficoMensajeríaMóvilEmpresa,left_on=['anno','empresa','id_empresa'],right_on=['anno','empresa','id_empresa'])
                IngPorTrafMensajeríaMovilEmpresa['Ingresos/Tráfico']=round(IngPorTrafMensajeríaMovilEmpresa['ingresos']/IngPorTrafMensajeríaMovilEmpresa['tráfico'],3)
                IngPorTrafMensajeríaMovilEmpresa['anno']=IngPorTrafMensajeríaMovilEmpresa['anno'].replace({'2021':'2021-T4','2022':'2022-T4'})

                ##Ingresos códigos cortos
                IngresosSMSCodigosCortosAgg=IngresosSMSCodigosCortos.groupby(['periodo'])['ingresos'].sum().reset_index()
                IngresosSMSCodigosCortosAgg=IngresosSMSCodigosCortosAgg.rename(columns={'ingresos':'Códigos cortos'})
                IngresosSMSTelMovilAgg2=IngresosSMSTelMovilAgg.copy()
                IngresosSMSTelMovilAgg2=IngresosSMSTelMovilAgg2.rename(columns={'ingresos':'SMS intercambiados entre usuarios'})
                IngresosMensajeríaMóvil=IngresosSMSTelMovilAgg2.merge(IngresosSMSCodigosCortosAgg,left_on=['periodo'],right_on=['periodo'])
                IngresosMensajeríaMóvil2=pd.melt(IngresosMensajeríaMóvil,id_vars=['periodo','periodo_formato'],value_vars=['SMS intercambiados entre usuarios',
                                    'Códigos cortos'],var_name='modalidad',value_name='ingresos')
                                    
                ## Ingresos por tráfico y modalidad                
                IngresosPorTraficoMensajeríaMóvil=IngresosMensajeríaMóvil2.merge(TraficoMensajeriaMovil2,left_on=['periodo','periodo_formato','modalidad'],right_on=['periodo','periodo_formato','modalidad'])    
                IngresosPorTraficoMensajeríaMóvil['Ingresos/Tráfico']=round(IngresosPorTraficoMensajeríaMóvil['ingresos']/IngresosPorTraficoMensajeríaMóvil['tráfico'],2)
                if LineaTiempoIngresosSMSTelmovil:
                    st.plotly_chart(Plotlylineatiempo(IngresosMensajeríaMóvil2,'ingresos','Miles de Millones de pesos',1e9,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Ingresos Mensajería móvil por periodo</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)
                    st.plotly_chart(Plotlylineatiempo(IngresosPorTraficoMensajeríaMóvil,'Ingresos/Tráfico','Pesos/Min',1,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Ingresos trimestrales por tráfico</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)
                if BarrasIngresosSMSTelmovil:    
                    st.plotly_chart(PlotlyBarras(IngresosMensajeríaMóvilEmpresa2,'ingresos','Miles de Millones de pesos',1e9,'<b>Ingresos Mensajería móvil por empresa</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)  
                    #
                    figIngporTrafTelMov = make_subplots(rows=1, cols=1) 
                    for empresa in IngPorTrafMensajeríaMovilEmpresa['empresa'].unique().tolist():
                        figIngporTrafTelMov.add_trace(go.Bar(x=IngPorTrafMensajeríaMovilEmpresa[IngPorTrafMensajeríaMovilEmpresa['empresa']==empresa]['anno'],y=IngPorTrafMensajeríaMovilEmpresa[IngPorTrafMensajeríaMovilEmpresa['empresa']==empresa]['Ingresos/Tráfico']
                                             ,marker_color=PColoresEmp(IngPorTrafMensajeríaMovilEmpresa[IngPorTrafMensajeríaMovilEmpresa['empresa']==empresa]['id_empresa'].unique()[0]),
                                            name=empresa,hovertemplate='<br><b>Empresa</b>:<br><extra></extra>'+empresa+'<br>'+                       
                        'Ingresos/Tráfico'+' '+'Pesos/Min'+': %{y:.3f}<br>'))
                    figIngporTrafTelMov.update_layout(barmode='group')
                    figIngporTrafTelMov.update_xaxes(tickangle=0, tickfont=dict(family='Poppins', color='black', size=16),title_text=None,row=1, col=1,
                    zeroline=True,linecolor = "rgba(192, 192, 192, 0.8)",zerolinewidth=2)
                    figIngporTrafTelMov.update_yaxes(range=[0,5],tickfont=dict(family='Poppins', color='black', size=16),titlefont_size=18, title_text='Pesos/Min', row=1, col=1)
                    figIngporTrafTelMov.update_layout(height=550,legend_title=None)
                    figIngporTrafTelMov.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20,
                    title={
                    'text': '<b>Ingresos por tráfico y por empresa</b>',
                    'y':0.98,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'})        
                    figIngporTrafTelMov.update_layout(legend=dict(orientation="h",y=1.2,xanchor='center',x=0.5,font_size=11),showlegend=True)
                    figIngporTrafTelMov.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',yaxis_tickformat='d')
                    figIngporTrafTelMov.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
                    figIngporTrafTelMov.add_annotation(
                    showarrow=False,
                    text='<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC',
                    font=dict(size=11), xref='x domain',x=0.5,yref='y domain',y=-0.2)    
                    st.plotly_chart(figIngporTrafTelMov,use_container_width=True)  
                        
    if select_secResumenDinTic == 'Servicios fijos': 
        st.markdown(r"""<div class="titulo"><h3>Servicios fijos</h3></div>""",unsafe_allow_html=True)
        st.markdown("<center>Para continuar, por favor seleccione el botón con el servicio del cual desea conocer la información</center>",unsafe_allow_html=True)

        ServiciosFijos=st.radio('',['Telefonía fija','Internet fijo', 'TV por suscripción'],horizontal=True)
        st.markdown(r"""<hr>""",unsafe_allow_html=True)   
        
        if ServiciosFijos == 'Internet fijo':

            col1,col2 = st.columns(2)
            with col1:
                st.markdown(r"""<div class='IconoTitulo'><img height="200px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Iconos/internet%20fijo.png?raw=true'/><h4 style="text-align:left">Internet fijo</h4></div>""",unsafe_allow_html=True)   
            with col2:             
                with st.expander("Datos relevantes de Internet fijo"):
                    st.markdown(r"""<ul>
                    <li>En 2022 se alcanzaron 8.9 millones de accesos, de los cuales el 88% pertenecen al segemento residencial. Esto corresponde a 447 mil accesos más que en 2021.</li>
                    <li>En 2022 los PRST alcanzaron 6475.6 miles millones de pesos, que representa un crecimiento de 12.05% respecto al año anterior</li>
                    </ul>""",unsafe_allow_html=True)

            
            AccesosCorpIntFijo=AccesosCorpIntFijo[AccesosCorpIntFijo['accesos']>0]
            AccesosCorpIntFijo=AccesosCorpIntFijo.rename(columns={'accesos':'CORPORATIVOS'})
            AccesosCorpIntFijo['periodo']=AccesosCorpIntFijo['anno']+'-T'+AccesosCorpIntFijo['trimestre']
            AccesosResIntFijo=AccesosResIntFijo[AccesosResIntFijo['accesos']>0]
            AccesosResIntFijo=AccesosResIntFijo.rename(columns={'accesos':'RESIDENCIALES'})
            AccesosResIntFijo['periodo']=AccesosResIntFijo['anno']+'-T'+AccesosResIntFijo['trimestre']
            ##
            AccesosCorpIntFijoNac=AccesosCorpIntFijo.groupby(['periodo'])['CORPORATIVOS'].sum().reset_index()
            AccesosResIntFijoNac=AccesosResIntFijo.groupby(['periodo'])['RESIDENCIALES'].sum().reset_index()
            AccesosCorpIntFijoEmp=AccesosCorpIntFijo.groupby(['anno','trimestre','id_empresa','empresa'])['CORPORATIVOS'].sum().reset_index()
            AccesosResIntFijoEmp=AccesosResIntFijo.groupby(['anno','trimestre','id_empresa','empresa'])['RESIDENCIALES'].sum().reset_index()
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
            IngresosInternetFijo=IngresosInternetFijo.merge(IPCTrimMov,left_on=['anno','trimestre','periodo'],right_on=['anno','trimestre','periodo'])
            IngresosInternetFijo['ingresos']=IngresosInternetFijo['ingresos']/IngresosInternetFijo['indice2022']
            
            IngresosInternetFijoNac=IngresosInternetFijo.groupby(['periodo'])['ingresos'].sum().reset_index()
            IngresosInternetFijoNacProm=IngresosInternetFijo.groupby(['periodo'])['ingresos'].mean().reset_index()
            IngresosInternetFijoEmp=IngresosInternetFijo.groupby(['anno','empresa','id_empresa'])['ingresos'].sum().reset_index()
            
            ServiciosIntFijo=st.selectbox('Escoja el servicio de Internet fijo',['Accesos','Ingresos','Velocidades'])
            st.markdown('Escoja la dimensión del análisis')
            
            if ServiciosIntFijo=='Accesos':
                col1,col2,col3,col4=st.columns(4)
                with col1:
                    LineaTiempoAccesosIntFijo=st.button('Evolución temporal')
                with col2:
                    BarrasAccesosIntFijo=st.button('Información por operadores')
                with col3:
                    PieAccesosIntFijo=st.button('Participaciones')
                with col4:
                    TecnologiaAccesosIntFijo=st.button('Tecnología')    
                    
                AccesosInternetFijoNac=AccesosCorpIntFijoNac.merge(AccesosResIntFijoNac,left_on=['periodo'],right_on=['periodo'])
                AccesosInternetFijoNac['TOTAL']=AccesosInternetFijoNac['CORPORATIVOS']+AccesosInternetFijoNac['RESIDENCIALES']
                AccesosInternetFijoNac2=pd.melt(AccesosInternetFijoNac,id_vars=['periodo'],value_vars=['CORPORATIVOS',
                'RESIDENCIALES','TOTAL'],var_name='modalidad',value_name='accesos')
                ##
                AccesosInternetFijoEmp=AccesosCorpIntFijoEmp.merge(AccesosResIntFijoEmp,left_on=['anno','trimestre','id_empresa'],right_on=['anno','trimestre','id_empresa'])
                AccesosInternetFijoEmp['TOTAL']=AccesosInternetFijoEmp['CORPORATIVOS']+AccesosInternetFijoEmp['RESIDENCIALES']
                AccesosInternetFijoEmp=AccesosInternetFijoEmp.rename(columns={'empresa_x':'empresa'})
                AccesosInternetFijoEmp=AccesosInternetFijoEmp.drop(columns=['empresa_y'])
                AccesosInternetFijoEmp2=pd.melt(AccesosInternetFijoEmp,id_vars=['anno','trimestre','id_empresa','empresa'],value_vars=['CORPORATIVOS',
                'RESIDENCIALES','TOTAL'],var_name='modalidad',value_name='accesos')
                AccesosInternetFijoEmp2=AccesosInternetFijoEmp2[(AccesosInternetFijoEmp2['modalidad']=='TOTAL')&(AccesosInternetFijoEmp2['trimestre']=='4')]    
                EmpIntFijoAccesos=AccesosInternetFijoEmp2[AccesosInternetFijoEmp2['anno']=='2022'].sort_values(by='accesos',ascending=False)['id_empresa'].to_list()[0:8]
                AccesosInternetFijoEmp2.loc[AccesosInternetFijoEmp2['id_empresa'].isin(EmpIntFijoAccesos)==False,'empresa']='Otros'
                AccesosInternetFijoEmp2.loc[AccesosInternetFijoEmp2['id_empresa'].isin(EmpIntFijoAccesos)==False,'id_empresa']='Otros'
                AccesosInternetFijoEmp2=AccesosInternetFijoEmp2[(AccesosInternetFijoEmp2['anno'].isin(['2021','2022']))].groupby(['anno','empresa','id_empresa'])['accesos'].sum().reset_index()
                ##
                AccesosInternetFijoPie=pd.concat([AccesosCorpIntFijoPie,AccesosResIntFijoPie])
                AccesosInternetFijoPieAgg=AccesosInternetFijoPie.groupby(['periodo','id_empresa','empresa'])['accesos'].sum().reset_index()
                AccesosInternetFijoPieAgg=AccesosInternetFijoPieAgg[AccesosInternetFijoPieAgg['periodo']=='2022-T4']
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
                AccesosInternetFijoTecAgg=AccesosInternetFijoTecAgg[AccesosInternetFijoTecAgg['CodTec']!='Otras']
                
                if LineaTiempoAccesosIntFijo:
                    AccesosInternetFijoNac2['periodo_formato']=AccesosInternetFijoNac2['periodo'].apply(periodoformato)
                    st.plotly_chart(Plotlylineatiempo(AccesosInternetFijoNac2,'accesos','Millones',1e6,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Accesos Internet fijo por periodo</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)
                if BarrasAccesosIntFijo:
                    st.plotly_chart(PlotlyBarras(AccesosInternetFijoEmp2,'accesos','',1,'<b>Accesos anuales por empresa</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)
                if PieAccesosIntFijo:
                    figPieIntFijo = px.pie(AccesosInternetFijoPieAgg, values='accesos', names='empresa', color='empresa',
                                 color_discrete_map=Colores_pie2, title='<b>Participación en accesos de Internet fijo<br>(2022-T4)')
                    figPieIntFijo.update_traces(textposition='inside',textinfo='percent',hoverinfo='label+percent',textfont_color='black')
                    figPieIntFijo.update_layout(uniformtext_minsize=18,uniformtext_mode='hide',showlegend=True,legend=dict(x=0.9,y=0.3),title_x=0.5)
                    figPieIntFijo.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20)
                    figPieIntFijo.add_annotation(
                    showarrow=False,
                    text='<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC',
                    font=dict(size=11), xref='x domain',x=0.5,yref='y domain',y=-0.2)
                    st.plotly_chart(figPieIntFijo,use_container_width=True)
                    st.markdown("""<center><p style="font-size:12px"><b>Nota:</b> Las empresas con participación menor al 1% se agrupan en la categoría Otros</p>""",unsafe_allow_html=True)
                    
                if TecnologiaAccesosIntFijo:
                    #st.download_button(label="Descargar CSV",data=convert_df(AccesosInternetFijoTecAgg),file_name='AccesosInternetFijoTecAgg.csv',mime='text/csv')                
                    AccesosInternetFijoTecAgg['periodo_formato']=AccesosInternetFijoTecAgg['periodo'].apply(periodoformato)
                    st.plotly_chart(PlotlylineatiempoTec(AccesosInternetFijoTecAgg,'accesos','Millones',1e6,['rgb(255, 51, 51)','rgb(255, 153, 51)','rgb(153,255,51)','rgb(153,51,255)','rgb(51, 153, 255)'],'<b>Accesos Internet fijo por tecnología y periodo</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)

            if ServiciosIntFijo=='Ingresos':
                st.markdown("""<center><p style="font-size:12px"><b>Nota:</b> Ingresos ajustados por inflación, usando el IPC de la subclase "Servicios de comunicación fija y movil y provisión a internet". Periodo base, diciembre 2022</p></center>""",unsafe_allow_html=True)
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoIngresosIntFijo=st.button('Evolución temporal')
                with col2:
                    BarrasIngresosIntFijo=st.button('Información por operadores')

                ## Ingresos/Accceso total
                AccesosInternetFijoNac=AccesosCorpIntFijoNac.merge(AccesosResIntFijoNac,left_on=['periodo'],right_on=['periodo'])
                AccesosInternetFijoNac['TOTAL']=AccesosInternetFijoNac['CORPORATIVOS']+AccesosInternetFijoNac['RESIDENCIALES']
                IngresosPorAccesoIntFijo=IngresosInternetFijoNac.merge(AccesosInternetFijoNac,left_on=['periodo'],right_on=['periodo'])
                IngresosPorAccesoIntFijo['Ingresos/Accceso']=round(IngresosPorAccesoIntFijo['ingresos']/IngresosPorAccesoIntFijo['TOTAL'],2)
                
                if LineaTiempoIngresosIntFijo: 
                    IngresosInternetFijoNac['periodo_formato']=IngresosInternetFijoNac['periodo'].apply(periodoformato)
                    IngresosPorAccesoIntFijo['periodo_formato']=IngresosPorAccesoIntFijo['periodo'].apply(periodoformato)
                    st.plotly_chart(Plotlylineatiempo(IngresosInternetFijoNac,'ingresos','Miles de Millones de pesos',1e9,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Ingresos Internet fijo por periodo</b>','<b>Fuente</b>:Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)
                    st.plotly_chart(Plotlylineatiempo(IngresosPorAccesoIntFijo,'Ingresos/Accceso','Pesos',1,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Ingresos trimestrales por acceso</b>','<b>Fuente</b>:Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)
                if BarrasIngresosIntFijo:
                    EmpIntFijoIngresos=IngresosInternetFijoEmp[IngresosInternetFijoEmp['anno']=='2022'].sort_values(by='ingresos',ascending=False)['id_empresa'].to_list()[0:4]
                    
                    IngresosInternetFijoEmp.loc[IngresosInternetFijoEmp['id_empresa'].isin(EmpIntFijoIngresos)==False,'empresa']='Otros'
                    IngresosInternetFijoEmp.loc[IngresosInternetFijoEmp['id_empresa'].isin(EmpIntFijoIngresos)==False,'id_empresa']='Otros'
                    IngresosInternetFijoEmp=IngresosInternetFijoEmp[(IngresosInternetFijoEmp['anno'].isin(['2021','2022']))].groupby(['anno','empresa','id_empresa'])['ingresos'].sum().reset_index()
                    st.plotly_chart(PlotlyBarras(IngresosInternetFijoEmp,'ingresos','Miles de Millones de pesos',1e9,'<b>Ingresos anuales por empresa</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)                  

            if ServiciosIntFijo=='Velocidades':
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoVelIntFijo=st.button('Evolución temporal')
                with col2:
                    TecnologíaIntFijo=st.button('Tecnología')
                        
                VelIntFijo_Tec=pd.read_csv('https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria/main/2023/Datos_Sin_API/Vel_IntFijoTec.csv' ,delimiter=';')            
                VelIntFijo_Mod=pd.read_csv('https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria/main/2023/Datos_Sin_API/Vel_IntFijoMod.csv' ,delimiter=';')            

                if TecnologíaIntFijo:
                    VelIntFijo_Tec['periodo_formato']=VelIntFijo_Tec['periodo'].apply(periodoformato)
                    VelIntFijo_Tec=VelIntFijo_Tec.rename(columns={'codtec':'CodTec'})
                    st.plotly_chart(PlotlylineatiempoTec(VelIntFijo_Tec,'Velocidad descarga promedio','Mbps',1,['rgb(255, 51, 51)','rgb(255, 153, 51)','rgb(153,255,51)','rgb(160,160,160)','rgb(51, 153, 255)','rgb(153,51,255)'],'<b>Velocidad promedio de descarga de Internet fijo por tecnología y periodo</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)
                
                if LineaTiempoVelIntFijo:
                    VelIntFijo_Mod['periodo_formato']=VelIntFijo_Mod['periodo'].apply(periodoformato)                    
                    st.plotly_chart(Plotlylineatiempo(VelIntFijo_Mod,'Velocidad descarga promedio','Mbps',1,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Velocidad promedio de descarga de Internet fijo por modalidad y periodo</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)
                                        
        if ServiciosFijos == 'Telefonía fija':

            col1,col2=st.columns(2)
            with col1:
                st.markdown(r"""<div class='IconoTitulo'><img height="200px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Iconos/telefonia%20fija.png?raw=true'/><h4 style="text-align:left">Telefonía fija</h4></div>""",unsafe_allow_html=True)   
            with col2:             
                with st.expander("Datos relevantes de Telefonía fija"):
                    st.markdown(r"""<ul>
                    <li>Al cierre de 2022 se contabilizaron 7.58 millones de líneas, de las cuales el 88% son líneas residenciales. En comparación con el año 2021, las líneas residenciales aumentaron en un 1,9% en 2022, y por contrario las líneas corporativas continúan en descenso.</li>
                    <li>Los ingresos por telefonía fija ascendieron a 1.74 billones de pesos, de los cuales el 92% se originó en telefonía fija nacional. El valor total representa una reducción real del 0,9% en comparación con 2021. </li>
                    </ul>""",unsafe_allow_html=True)


            ServiciosTelFija=st.selectbox('Escoja el servicio de Telefonía fija',['Líneas','Ingresos','Ingresos por líneas'])
            st.markdown('Escoja la dimensión del análisis')
            
            ## Líneas
            LineasTelefoníaLocal=LineasTelefoníaLocal[LineasTelefoníaLocal['lineas']>0]
            LineasTelefoníaLocal['modalidad']=None
            LineasTelefoníaLocal['modalidad']=np.where(LineasTelefoníaLocal.id_segmento.isin(['101','102','103','104','105','106']),'Residenciales',LineasTelefoníaLocal['modalidad'])
            LineasTelefoníaLocal['modalidad']=np.where(LineasTelefoníaLocal.id_segmento.isin(['107','109']),'Corporativo',LineasTelefoníaLocal['modalidad'])
            LineasTelefoníaLocalNac=LineasTelefoníaLocal.groupby(['periodo','modalidad'])['lineas'].sum().reset_index()
            #
            LineasTelefoníaLocalEmp=LineasTelefoníaLocal.groupby(['anno','trimestre','id_empresa','empresa'])['lineas'].sum().reset_index()
            LineasTelefoníaLocalEmp=LineasTelefoníaLocalEmp[(LineasTelefoníaLocalEmp['anno'].isin(['2021','2022']))&(LineasTelefoníaLocalEmp['trimestre']=='4')]
            EmpTelfijaLineas=LineasTelefoníaLocalEmp[LineasTelefoníaLocalEmp['anno']=='2022'].sort_values(by='lineas',ascending=False)['id_empresa'].to_list()[0:4]
            LineasTelefoníaLocalEmp.loc[LineasTelefoníaLocalEmp['id_empresa'].isin(EmpTelfijaLineas)==False,'empresa']='Otros'
            LineasTelefoníaLocalEmp.loc[LineasTelefoníaLocalEmp['id_empresa'].isin(EmpTelfijaLineas)==False,'id_empresa']='Otros'            
            LineasTelefoníaLocalEmp=LineasTelefoníaLocalEmp.groupby(['anno','empresa','id_empresa'])['lineas'].sum().reset_index()
            #
            LineasTelefoníaLocalPie=LineasTelefoníaLocal.groupby(['periodo','id_empresa','empresa'])['lineas'].sum().reset_index()
            LineasTelefoníaLocalPie=LineasTelefoníaLocalPie[LineasTelefoníaLocalPie['periodo']=='2022-T4']
            LineasTelefoníaLocalPie['participacion']=round(100*LineasTelefoníaLocalPie['lineas']/LineasTelefoníaLocalPie['lineas'].sum(),1)
            LineasTelefoníaLocalPie.loc[LineasTelefoníaLocalPie['participacion']<=1,'empresa']='Otros'
            LineasTelefoníaLocalPie['empresa']=LineasTelefoníaLocalPie['empresa'].replace(nombresComerciales)     
            
            ##Ingresos 
            IngresosTelefoniaFija=IngresosTelefoniaFija.merge(IPCTrimMov,left_on=['anno','trimestre','periodo'],right_on=['anno','trimestre','periodo'])
            IngresosTelefoniaFija['ingresos']=IngresosTelefoniaFija['ingresos']/IngresosTelefoniaFija['indice2022']
            IngresosTelefoniaFijaNac=IngresosTelefoniaFija.groupby(['periodo','modalidad'])['ingresos'].sum().reset_index()
            IngresosTelefoniaFijaEmp=IngresosTelefoniaFija.groupby(['anno','periodo','modalidad','id_empresa','empresa'])['ingresos'].sum().reset_index()
            
            IngresosTelefoniaFijaEmpTFN=IngresosTelefoniaFijaEmp[IngresosTelefoniaFijaEmp['modalidad']=='Fija nacional'].groupby(['anno','id_empresa','empresa'])['ingresos'].sum().reset_index()
            EmpTelfijaLocalIng=IngresosTelefoniaFijaEmpTFN[IngresosTelefoniaFijaEmpTFN['anno']=='2022'].sort_values(by='ingresos',ascending=False)['id_empresa'].to_list()[0:4]
            IngresosTelefoniaFijaEmpTFN.loc[IngresosTelefoniaFijaEmpTFN['id_empresa'].isin(EmpTelfijaLocalIng)==False,'empresa']='Otros'
            IngresosTelefoniaFijaEmpTFN.loc[IngresosTelefoniaFijaEmpTFN['id_empresa'].isin(EmpTelfijaLocalIng)==False,'id_empresa']='Otros'
            IngresosTelefoniaFijaEmpTFN=IngresosTelefoniaFijaEmpTFN[IngresosTelefoniaFijaEmpTFN['anno'].isin(['2021','2022'])].groupby(['anno','id_empresa','empresa'])['ingresos'].sum().reset_index()         
            #
            IngresosTelefoniaFijaEmpTFN2=IngresosTelefoniaFijaEmp[(IngresosTelefoniaFijaEmp['modalidad']=='Fija nacional')&(IngresosTelefoniaFijaEmp['periodo'].isin(['2021-T4','2022-T4']))].groupby(['anno','id_empresa','empresa'])['ingresos'].sum().reset_index()
            IngresosTelefoniaFijaEmpTFN2.loc[IngresosTelefoniaFijaEmpTFN2['id_empresa'].isin(EmpTelfijaLocalIng)==False,'empresa']='Otros'
            IngresosTelefoniaFijaEmpTFN2.loc[IngresosTelefoniaFijaEmpTFN2['id_empresa'].isin(EmpTelfijaLocalIng)==False,'id_empresa']='Otros'
            IngresosTelefoniaFijaEmpTFN2=IngresosTelefoniaFijaEmpTFN2[IngresosTelefoniaFijaEmpTFN2['anno'].isin(['2021','2022'])].groupby(['anno','id_empresa','empresa'])['ingresos'].sum().reset_index()     
                        
            IngresosTelefoniaFijaEmpTFNDI=IngresosTelefoniaFijaEmp[IngresosTelefoniaFijaEmp['modalidad']=='Larga distancia internacional'].groupby(['anno','id_empresa','empresa'])['ingresos'].sum().reset_index()
            EmpTelfijaLDIIng=IngresosTelefoniaFijaEmpTFNDI[IngresosTelefoniaFijaEmpTFNDI['anno']=='2021'].sort_values(by='ingresos',ascending=False)['id_empresa'].to_list()[0:4]
            IngresosTelefoniaFijaEmpTFNDI.loc[IngresosTelefoniaFijaEmpTFNDI['id_empresa'].isin(EmpTelfijaLDIIng)==False,'empresa']='Otros'
            IngresosTelefoniaFijaEmpTFNDI.loc[IngresosTelefoniaFijaEmpTFNDI['id_empresa'].isin(EmpTelfijaLDIIng)==False,'id_empresa']='Otros'
            IngresosTelefoniaFijaEmpTFNDI=IngresosTelefoniaFijaEmpTFNDI[IngresosTelefoniaFijaEmpTFNDI['anno'].isin(['2021','2022'])].groupby(['anno','id_empresa','empresa'])['ingresos'].sum().reset_index()
             
            ## Ingresos por líneas
            LineasTelefoníaLocalTotalTL=LineasTelefoníaLocalNac.groupby(['periodo'])['lineas'].sum().reset_index()
            IngresosTelefoniaLocal=IngresosTelefoniaFijaNac[IngresosTelefoniaFijaNac['modalidad']=='Fija nacional'].drop('modalidad',axis=1)
            IngresosPorLineaTelLocal=IngresosTelefoniaLocal.merge(LineasTelefoníaLocalTotalTL,left_on=['periodo'],right_on=['periodo'])
            IngresosPorLineaTelLocal['Ingresos/Líneas']=round(IngresosPorLineaTelLocal['ingresos']/IngresosPorLineaTelLocal['lineas'],2)

            IngresosPorLineaTelLocalEmp=IngresosTelefoniaFijaEmpTFN2.merge(LineasTelefoníaLocalEmp,left_on=['anno','empresa','id_empresa'],right_on=['anno','empresa','id_empresa'])       
            IngresosPorLineaTelLocalEmp['Ingresos/Líneas']=round(IngresosPorLineaTelLocalEmp['ingresos']/IngresosPorLineaTelLocalEmp['lineas'],2)

 
            if ServiciosTelFija=='Líneas':
                col1,col2,col3=st.columns(3)
                with col1:
                    LineaTiempoLineasTelFija=st.button('Evolución temporal')
                with col2:
                    BarrasLineasTelFija=st.button('Información por operadores')
                with col3:
                    PieLineasTelFija=st.button('Participaciones')            
                
                if LineaTiempoLineasTelFija:
                    LineasTelefoníaLocalNac['periodo_formato']=LineasTelefoníaLocalNac['periodo'].apply(periodoformato)
                    st.plotly_chart(Plotlylineatiempo(LineasTelefoníaLocalNac,'lineas','Millones',1e6,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Líneas Telefonía fija por periodo</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)
                if BarrasLineasTelFija:
                    st.plotly_chart(PlotlyBarras(LineasTelefoníaLocalEmp,'lineas','',1,'<b>Líneas anuales por empresa</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)
                if PieLineasTelFija:
                    figPieTelFija = px.pie(LineasTelefoníaLocalPie, values='lineas', names='empresa', color='empresa',
                                 color_discrete_map=Colores_pie2, title='<b>Participación en líneas de Telefonía local<br>(2022-T4)')
                    figPieTelFija.update_traces(textposition='inside',textinfo='percent',hoverinfo='label+percent',textfont_color='black')
                    figPieTelFija.update_layout(uniformtext_minsize=18,uniformtext_mode='hide',showlegend=True,legend=dict(x=0.9,y=0.3),title_x=0.5)
                    figPieTelFija.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20)
                    figPieTelFija.add_annotation(
                    showarrow=False,
                    text='<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC',
                    font=dict(size=11), xref='x domain',x=0.5,yref='y domain',y=-0.2)
                    st.plotly_chart(figPieTelFija,use_container_width=True)                            
            
            if ServiciosTelFija=='Ingresos':
                st.markdown("""<center><p style="font-size:12px"><b>Nota:</b> Ingresos ajustados por inflación, usando el IPC de la subclase "Servicios de comunicación fija y movil y provisión a internet". Periodo base, diciembre 2022</p></center>""",unsafe_allow_html=True)
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoIngresosTelFija=st.button('Evolución temporal')
                with col2:
                    BarrasIngresosTelFija=st.button('Información por operadores')   
                
                if LineaTiempoIngresosTelFija:
                    IngresosTelefoniaFijaNac['periodo_formato']=IngresosTelefoniaFijaNac['periodo'].apply(periodoformato)                    
                    st.plotly_chart(Plotlylineatiempo(IngresosTelefoniaFijaNac,'ingresos','Miles de Millones pesos',1e9,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Ingresos Telefonía fija por periodo</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)
                if BarrasIngresosTelFija:
                    col1,col2=st.columns(2)
                    with col1:
                        st.plotly_chart(PlotlyBarras(IngresosTelefoniaFijaEmpTFN,'ingresos','Miles de Millones de pesos',1e9,'<b>Ingresos anuales de Telefonía fija nacional por empresa</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)
                    with col2:
                        st.plotly_chart(PlotlyBarras(IngresosTelefoniaFijaEmpTFNDI,'ingresos','Miles de Millones de pesos',1e9,'<b>Ingresos anuales de Telefonía LDI por empresa</b>',''),use_container_width=True)
                    

            if ServiciosTelFija=='Ingresos por líneas':
                st.markdown("""<center><p style="font-size:12px"><b>Nota:</b> Ingresos ajustados por inflación, usando el IPC de la subclase "Servicios de comunicación fija y movil y provisión a internet". Periodo base, diciembre 2022</p></center>""",unsafe_allow_html=True)
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoIngresosporlineaTelFija=st.button('Evolución temporal')
                with col2:
                    BarrasIngresosporlineaTelFija=st.button('Información por operadores')  

                if LineaTiempoIngresosporlineaTelFija:
                    IngresosPorLineaTelLocal['periodo_formato']=IngresosPorLineaTelLocal['periodo'].apply(periodoformato)                    
                    st.plotly_chart(Plotlylineatiempo(IngresosPorLineaTelLocal,'Ingresos/Líneas','Pesos',1,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Ingresos trimestrales por líneas</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)
                if BarrasIngresosporlineaTelFija:
                    IngresosPorLineaTelLocalEmp['anno']=IngresosPorLineaTelLocalEmp['anno'].replace({'2021':'2021-T4','2022':'2022-T4'})
                    st.plotly_chart(PlotlyBarras(IngresosPorLineaTelLocalEmp,'Ingresos/Líneas','Pesos',1,'<b>Ingresos por líneas de Telefonía fija nacional por empresa</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)

        if ServiciosFijos == 'TV por suscripción':

            col1,col2=st.columns(2)
            with col1:
                st.markdown(r"""<div class='IconoTitulo'><img height="200px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Iconos/tv%20suscripcion.png?raw=true'/><h4 style="text-align:left">TV por suscripción</h4></div>""",unsafe_allow_html=True)   
            with col2:             
                with st.expander("Datos relevantes de TV por suscripción"):
                    st.markdown(r"""<ul>
                    <li>Los ingresos en 2022 fueron de 3421.1 miles de millones de pesos, es decir, un crecimiento real del 7,65% frente al año anterior</li>    
                    <li>En materia de suscriptores, al cuarto trimestre de 2022 superó 6,30 millones, 132,8 mil accesos más que en el mismo periodo de 2021</li>    
                    </ul>""",unsafe_allow_html=True)

            ##Suscriptores
            SuscriptoresTVSusNac=SuscriptoresTVSus.groupby(['periodo'])['suscriptores'].sum().reset_index()
            #
            SuscriptoresTVSusEmp=SuscriptoresTVSus.groupby(['anno','trimestre','id_empresa','empresa'])['suscriptores'].sum().reset_index()
            SuscriptoresTVSusEmp=SuscriptoresTVSusEmp[(SuscriptoresTVSusEmp['anno'].isin(['2021','2022']))&(SuscriptoresTVSusEmp['trimestre']=='4')]
            EmpSuscriptoresTVSusEmp=SuscriptoresTVSusEmp[SuscriptoresTVSusEmp['anno']=='2022'].sort_values(by='suscriptores',ascending=False)['id_empresa'].to_list()[0:4]
            SuscriptoresTVSusEmp.loc[SuscriptoresTVSusEmp['id_empresa'].isin(EmpSuscriptoresTVSusEmp)==False,'empresa']='Otros'
            SuscriptoresTVSusEmp.loc[SuscriptoresTVSusEmp['id_empresa'].isin(EmpSuscriptoresTVSusEmp)==False,'id_empresa']='Otros'
            SuscriptoresTVSusEmp=SuscriptoresTVSusEmp.groupby(['anno','id_empresa','empresa'])['suscriptores'].sum().reset_index()
            #
            SuscriptoresTVSusPie=SuscriptoresTVSus.groupby(['periodo','id_empresa','empresa'])['suscriptores'].sum().reset_index()
            SuscriptoresTVSusPie=SuscriptoresTVSusPie[SuscriptoresTVSusPie['periodo']=='2022-T4']
            SuscriptoresTVSusPie['participacion']=round(100*SuscriptoresTVSusPie['suscriptores']/SuscriptoresTVSusPie['suscriptores'].sum(),1)
            SuscriptoresTVSusPie.loc[SuscriptoresTVSusPie['participacion']<=1,'empresa']='Otros'
            SuscriptoresTVSusPie['empresa']=SuscriptoresTVSusPie['empresa'].replace(nombresComerciales) 
            #
            SuscriptoresTVSus['tecnologia']=SuscriptoresTVSus['tecnologia'].replace({'IPTV por Fibra':'IPTV'})
            SuscriptoresTVSusTec=SuscriptoresTVSus[SuscriptoresTVSus['anno']=='2022'].groupby(['periodo','tecnologia'])['suscriptores'].sum().reset_index()
            SuscriptoresTVSusTec=SuscriptoresTVSusTec.rename(columns={'tecnologia':'CodTec'})
            ##Ingresos
            IngresosTVSus=IngresosTVSus.merge(IPCTrimMov,left_on=['anno','trimestre','periodo'],right_on=['anno','trimestre','periodo'])
            IngresosTVSus['ingresos']=IngresosTVSus['ingresos']/IngresosTVSus['indice2022']

            IngresosTVSus['concepto']=IngresosTVSus['concepto'].replace({'Cargo fijo plan básico de televisión por suscripción':'Cargo fijo plan básico',
            'Otros ingresos operacionales televisión por suscripción':'Otros ingresos operacionales','Cargo fijo plan premium de televisión por suscripción':'Cargo fijo plan premium',
            'Provisión de contenidos audiovisuales a través del servicio de televisión por suscripción':'Provisión de contenidos audiovisuales'})
            IngresosTVSusNac=IngresosTVSus.groupby(['periodo'])['ingresos'].sum().reset_index()
            #
            IngresosTVSusEmp=IngresosTVSus.groupby(['anno','trimestre','empresa','id_empresa'])['ingresos'].sum().reset_index()
            IngresosTVSusEmp=IngresosTVSusEmp[(IngresosTVSusEmp['anno'].isin(['2021','2022']))]
            EmpIngresosTVSusEmp=IngresosTVSusEmp[(IngresosTVSusEmp['anno']=='2022')&(IngresosTVSusEmp['trimestre']=='4')].sort_values(by='ingresos',ascending=False)['id_empresa'].to_list()[0:4]
            IngresosTVSusEmp.loc[IngresosTVSusEmp['id_empresa'].isin(EmpIngresosTVSusEmp)==False,'empresa']='Otros'
            IngresosTVSusEmp.loc[IngresosTVSusEmp['id_empresa'].isin(EmpIngresosTVSusEmp)==False,'id_empresa']='Otros'
            IngresosTVSusEmp=IngresosTVSusEmp.groupby(['anno','id_empresa','empresa'])['ingresos'].sum().reset_index()
            
            #
            IngresosTVSusEmp2=IngresosTVSus.groupby(['anno','trimestre','empresa','id_empresa'])['ingresos'].sum().reset_index()
            IngresosTVSusEmp2=IngresosTVSusEmp2[(IngresosTVSusEmp2['anno'].isin(['2021','2022']))&(IngresosTVSusEmp2['trimestre']=='4')]
            IngresosTVSusEmp2.loc[IngresosTVSusEmp2['id_empresa'].isin(EmpIngresosTVSusEmp)==False,'empresa']='Otros'
            IngresosTVSusEmp2.loc[IngresosTVSusEmp2['id_empresa'].isin(EmpIngresosTVSusEmp)==False,'id_empresa']='Otros'
            IngresosTVSusEmp2=IngresosTVSusEmp2.groupby(['anno','id_empresa','empresa'])['ingresos'].sum().reset_index()
            #    
            IngresosTVSusConcep=IngresosTVSus.groupby(['periodo','id_concepto','concepto'])['ingresos'].sum().reset_index()
            IngresosTVSusConcep=IngresosTVSusConcep.rename(columns={'concepto':'modalidad'})
            ##Ingresos por suscriptores
            IngresosPorSuscriptoresTV=IngresosTVSusNac.merge(SuscriptoresTVSusNac,left_on=['periodo'],right_on=['periodo'])
            IngresosPorSuscriptoresTV['Ingresos/Suscriptores']=round(IngresosPorSuscriptoresTV['ingresos']/IngresosPorSuscriptoresTV['suscriptores'],2)                    
            #
            IngresosPorSuscriptoresTVEmp=IngresosTVSusEmp2.merge(SuscriptoresTVSusEmp,left_on=['anno','id_empresa','empresa'],right_on=['anno','id_empresa','empresa'])
            IngresosPorSuscriptoresTVEmp['Ingresos/Suscriptores']=round(IngresosPorSuscriptoresTVEmp['ingresos']/IngresosPorSuscriptoresTVEmp['suscriptores'],2)
            IngresosPorSuscriptoresTVEmp['anno']=IngresosPorSuscriptoresTVEmp['anno'].replace({'2021':'2021-T4','2022':'2022-T4'})
            
            ServiciosTVporSus=st.selectbox('Escoja el servicio de TV por suscripción',['Suscriptores','Ingresos'])
            st.markdown('Escoja la dimensión del análisis')
            
            if ServiciosTVporSus=='Suscriptores':
                
                col1,col2,col3,col4=st.columns(4)
                with col1:
                    LineaTiempoSuscriptoresTVSus=st.button('Evolución temporal')
                with col2:
                    BarrasSuscriptoresTVSus=st.button('Información por operadores')
                with col3:
                    PieSuscriptoresTVSus=st.button('Participaciones')
                with col4:
                    TecnologiaSuscriptoresTVSus=st.button('Tecnología')    
                
                if LineaTiempoSuscriptoresTVSus:
                    SuscriptoresTVSusNac['periodo_formato']=SuscriptoresTVSusNac['periodo'].apply(periodoformato)
                    st.plotly_chart(Plotlylineatiempo(SuscriptoresTVSusNac,'suscriptores','',1,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Suscriptores TV por suscripción por periodo</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)
                if BarrasSuscriptoresTVSus:
                    st.plotly_chart(PlotlyBarras(SuscriptoresTVSusEmp,'suscriptores','',1,'<b>Suscriptores anuales por empresa</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)
                
                if PieSuscriptoresTVSus:
                    figPieTVSus = px.pie(SuscriptoresTVSusPie, values='suscriptores', names='empresa', color='empresa',
                                 color_discrete_map=Colores_pie2, title='<b>Participación en suscriptores de TV por suscripción<br>(2022-T4)')
                    figPieTVSus.update_traces(textposition='inside',textinfo='percent',hoverinfo='label+percent',textfont_color='black')
                    figPieTVSus.update_layout(uniformtext_minsize=18,uniformtext_mode='hide',showlegend=True,legend=dict(x=0.9,y=0.3),title_x=0.5)
                    figPieTVSus.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20)
                    figPieTVSus.add_annotation(
                    showarrow=False,
                    text='<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC',
                    font=dict(size=11), xref='x domain',x=0.5,yref='y domain',y=-0.2)
                    st.plotly_chart(figPieTVSus,use_container_width=True)   
                    st.markdown("""<center><p style="font-size:12px"><b>Nota:</b>Las empresas con participación menor al 1% se agrupan en la categoría Otros</p>""",unsafe_allow_html=True)

                if TecnologiaSuscriptoresTVSus:
                    SuscriptoresTVSusTec=SuscriptoresTVSusTec[SuscriptoresTVSusTec['CodTec']!='Otro']
                    SuscriptoresTVSusTec['periodo_formato']=SuscriptoresTVSusTec['periodo'].apply(periodoformato)
                    st.plotly_chart(PlotlylineatiempoTec(SuscriptoresTVSusTec,'suscriptores','',1,['rgb(255, 51, 51)','rgb(255, 153, 51)','rgb(153,255,51)','rgb(153,51,255)','rgb(51, 153, 255)'],'Suscriptores TV por suscripción por tecnología y periodo','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)

            if ServiciosTVporSus=='Ingresos':
                st.markdown("""<center><p style="font-size:12px"><b>Nota:</b> Ingresos ajustados por inflación, usando el IPC de la subclase "Servicios de comunicación fija y movil y provisión a internet". Periodo base, diciembre 2022</p></center>""",unsafe_allow_html=True)
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoIngresosTVSus=st.button('Evolución temporal')
                with col2:
                    BarrasIngresosTVSus=st.button('Información por operadores')
                # with col3:
                    # ConceptoIngresosTVSus=st.button('Concepto')
                
                if LineaTiempoIngresosTVSus:
                    IngresosTVSusNac['periodo_formato']=IngresosTVSusNac['periodo'].apply(periodoformato)
                    st.plotly_chart(Plotlylineatiempo(IngresosTVSusNac,'ingresos','Miles de Millones de pesos',1e9,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Ingresos TV por suscripción por periodo</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)
                    IngresosPorSuscriptoresTV['periodo_formato']=IngresosPorSuscriptoresTV['periodo'].apply(periodoformato)
                    st.plotly_chart(Plotlylineatiempo(IngresosPorSuscriptoresTV,'Ingresos/Suscriptores','Pesos',1,['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102,204,0)'],'<b>Ingresos trimestrales por suscriptor</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)

                if BarrasIngresosTVSus:
                    st.plotly_chart(PlotlyBarras(IngresosTVSusEmp,'ingresos','Miles de Millones de pesos',1e9,'<b>Ingresos anuales por empresa</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)
                    st.plotly_chart(PlotlyBarras(IngresosPorSuscriptoresTVEmp,'Ingresos/Suscriptores','Pesos',1,'<b>Ingresos por suscriptores por empresa</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)

    if select_secResumenDinTic == 'Servicios OTT':
        st.markdown(r"""<div class="titulo"><h3>Servicios OTT</h3></div>""",unsafe_allow_html=True)
        
        col1,col2=st.columns(2)
        with col1:
            st.markdown(r"""<div class='IconoTitulo'><img height="200px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Iconos/ott.png?raw=true'/><h4 style="text-align:left"><center>Servicios Over the top (OTT)<br>de contenidos audiovisuales</center></h4></div>""",unsafe_allow_html=True)   
        with col2:             
            with st.expander("Datos relevantes de OTT"):
                st.markdown(r"""<ul>
                <li>En el cuarto trimestre de 2022, el 91,3% de los hogares con Internet consumieron contenidos audiovisuales a través de plataformas de servicios OTT.</li>
                <li>Los modelos de negocio de servicios OTT audiovisuales con mayor penetración en los hogares colombianos son: video por demanda gratuito o con publicidad (89%), seguido de servicios de video por demanda con suscripción (79%) y los servicios de TV everywhere (38%).</li>
                <li>De los hogares con Internet, el 13.58% manifestaron haber renunciado al servicio de TV por suscripción (cord-cutters).</li>
                <li>Del porcentaje de cord-cutters, el 27.8% de los hogares señaló que el motivo de renuncia fue que podía encontrar el mismo contenido por Internet, y 19,8% lo reemplazó por servicios pagos de contenidos en línea.</li>
                </ul>""",unsafe_allow_html=True)
        st.markdown(r"""<hr>""",unsafe_allow_html=True) 
        st.markdown('')
        OTT=pd.read_csv('https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria/main/2023/Datos_Sin_API/OTT_resumen.csv',delimiter=';')
        OTT['periodo']=OTT['periodo'].replace({r'Q':'-T'},regex=True)
        OTT['penetracion'] = OTT['penetracion'].replace({r' ': '', r'%': '', r',': '.'}, regex=True).astype(float)
        
        OTTAgg=OTT[(OTT['concepto']=='Penetracion modelo de negocio')&(OTT['periodo'].isin(['2018-T4','2019-T4','2020-T4','2021-T4','2022-T4']))].groupby(['periodo','modelo_negocio'])['penetracion'].sum().reset_index()
        OTT2=OTTAgg[OTTAgg['modelo_negocio'].isin(['AVOD','FVOD'])]
        OTTAgg2=OTT2.groupby(['periodo'])['penetracion'].sum().reset_index()
        OTTAgg2['modelo_negocio']='FVOD-AVOD'
        OTTdf=pd.concat([OTTAgg,OTTAgg2])
        OTTdf=OTTdf[OTTdf['modelo_negocio'].isin(['AVOD','FVOD'])==False]
        OTTdf['modelo_negocio']=OTTdf['modelo_negocio'].replace({'TV Everywhere pago':'TV Everywhere<br>pago'})
        #
        OTTMotivos=OTT[OTT['concepto']=='Motivos cutters']
        OTTMotivos=OTTMotivos.rename(columns={'modelo_negocio':'motivos'})
        Motivos21T4=OTTMotivos[OTTMotivos['periodo']=='2022-T4'].sort_values(by='penetracion',ascending=False)['motivos'].values.tolist()[0:5]
        OTTMotivos=OTTMotivos[OTTMotivos['motivos'].isin(Motivos21T4)]
        OTTMotivos['penetracion']=OTTMotivos['penetracion']
        reshape_motivos={'Es muy caro.':'Servicio muy caro','No lo estaba utilizando.':'No lo utilizaba',
                        'Estaba obligado a pagar por muchos canales que luego no miraba realmente.':'Obligado a pagar<br>canales que no<br>miraba',
                        'Puedo ver los mismos contenidos en internet y gratis.':'Mismo contenido gratis<br>en internet',
                        'El servicio al cliente es muy malo.':'Pésimo servicio al cliente',
                        'Me mudé y en mi nuevo hogar ya no quiero tener ese gasto.':'Mudanza',
                        'Lo reemplacé por Servicios Pagos de contenidos online (películas, series, eventos,\x85).':'Reemplazo por servicios<br>pagos de contenidos online'}
        OTTMotivos['motivos']=OTTMotivos['motivos'].replace(reshape_motivos)
        
                    
        col1,col2=st.columns(2)
        with col1:
            ModeloOTT=st.button('Modelo de negocio')
        with col2:
            MotivosOTT=st.button('Motivos corte servicio')

        if ModeloOTT:
            st.markdown("""<p style="font-size:12px"><b>Nota:</b> Los siguientes modelos son los modelos de negocio de servicios OTT de contenidos audiovisuales. SVOD: video por demanda por suscripción; FVOD: video por demanda gratuito; AVOD: video por demanda gratuito que monetizan sus servicios a través de terceros, por ejemplo publicidad; TVOD: video por demanda en la que se abona por cada contenido al que se accede por alquiler o compra; TV everywhere: hace referencia al modelo en el que se accede a las plataformas a través de una suscripción a TV, servicios de Internet o Telefonía el cual es ofrecido por programadores o cableoperadores; TV everywhere pago: se diferencia del TV everywhere ya que hay que realizar un pago adicional para el acceso a este servicio. “Ilegal”: “ilegal” se refiere las plataformas no pagan a los dueños de los derechos de los contenidos dispuestos. Un ejemplo de esto son los servicios P2P, plataformas como Cuevana, pelisplus, pelisflix y similares que no pagan por los contenidos que trasmiten. Fuente: Business Bureau.</p>""",unsafe_allow_html=True)
        
            figModeloOTT = px.bar(OTTdf, x='modelo_negocio',y='penetracion', color='periodo', height=400,color_discrete_sequence=['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102, 204,0)','#ffbf00',"#ff6666"])
            figModeloOTT.update_layout(barmode='group')
            figModeloOTT.update_xaxes(tickangle=0, tickfont=dict(family='Poppins', color='black', size=16),title_text=None,row=1, col=1,
            zeroline=True,linecolor = "rgba(192, 192, 192, 0.8)",zerolinewidth=2)
            figModeloOTT.update_yaxes(tickfont=dict(family='Poppins', color='black', size=16),titlefont_size=18, title_text='Porcentaje (%)', row=1, col=1)
            figModeloOTT.update_layout(height=550,legend_title=None)
            figModeloOTT.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20,
            title={
            'text': '<b>Penetración suscriptores OTT por modelo de servicio</b>',
            'y':0.98,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})        
            figModeloOTT.update_layout(legend=dict(orientation="h",y=1.05,xanchor='center',x=0.5,font_size=12),showlegend=True)
            figModeloOTT.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',yaxis_tickformat='d')
            figModeloOTT.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
            figModeloOTT.add_annotation(
            showarrow=False,
            text='<b>Fuente</b>: Elaboración CRC con base en los reportes de información de Business Bureau',
            font=dict(size=11), xref='x domain',x=0.5,yref='y domain',y=-0.2)
            st.plotly_chart(figModeloOTT,use_container_width=True)
            
        if MotivosOTT:
            figMotivosOTT = px.bar(OTTMotivos, x='penetracion',y='motivos',orientation='h',color='periodo', height=400,color_discrete_sequence=['rgb(122, 68, 242)','rgb(0, 128, 255)','rgb(102, 204,0)','#ffbf00',"#ff6666"])
            figMotivosOTT.update_layout(barmode='group')
            figMotivosOTT.update_xaxes(tickangle=0, tickfont=dict(family='Poppins', color='black', size=16),title_text='Porcentaje (%)',row=1, col=1,
            zeroline=True,linecolor = "rgba(192, 192, 192, 0.8)",zerolinewidth=2)
            figMotivosOTT.update_yaxes(tickfont=dict(family='Poppins', color='black', size=16),titlefont_size=18, title_text=None, row=1, col=1)
            figMotivosOTT.update_layout(height=550,legend_title=None)
            figMotivosOTT.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20,
            title={
            'text': '<b>Motivos más comunes de cancelación del servicio</b>',
            'y':0.98,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})        
            figMotivosOTT.update_layout(legend=dict(orientation="v",y=0.87,x=0.8,font_size=14),showlegend=True)
            figMotivosOTT.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',yaxis_tickformat='d')
            figMotivosOTT.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
            figMotivosOTT.update_layout(yaxis={'categoryorder':'total descending'})
            figMotivosOTT.add_annotation(
            showarrow=False,
            text='<b>Fuente</b>: Elaboración CRC con base en los reportes de información de Business Bureau',
            font=dict(size=11), xref='x domain',x=0.5,yref='y domain',y=-0.2)
            st.plotly_chart(figMotivosOTT,use_container_width=True)
                                          
    if select_secResumenDinTic == 'Servicios de radiodifusión':                   
        st.markdown(r"""<div class="titulo"><h3>Servicios de radiodifusión</h3></div>""",unsafe_allow_html=True)
        
        ServiciosRadiodifusion=st.radio('',['TV abierta','Radio'],horizontal=True)
        st.markdown(r"""<hr>""",unsafe_allow_html=True) 
        
        if ServiciosRadiodifusion=='Radio':

            col1,col2=st.columns(2)
            with col1:
                st.markdown(r"""<div class='IconoTitulo'><img height="200px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Iconos/radio.png?raw=true'/><h4 style="text-align:left">Radio</h4></div>""",unsafe_allow_html=True)   
            with col2:             
                with st.expander("Datos relevantes de Radio"):
                    st.markdown(r"""<ul>
                    <li>En el año 2022 Colombia tenía 1.718 emisoras radiales, de las cuales 770 son emisoras comunitarias, 620 son comerciales y 328 son emisoras de interés público.</li>
                    <li>328 emisoras tienen frecuencia asignada en banda AM y las restantes 1.390 en la banda FM.</li>
                    <li>Los ingresos de las principales emisoras comerciales fueron 586,1 mil millones de pesos en 2022, 6,5% más en términos constantes que los registrados el año inmediatamente anterior.</li>
                    </ul>""",unsafe_allow_html=True)

            nombres_Radio={'CARACOL PRIMERA CADENA RADIAL COLOMBIANA S.A.':'Caracol Radio','COMPANIA DE COMUNICACIONES DE COLOMBIA S.A.S':'Comunicaciones<br>de Colombia',
            'EMPRESA COLOMBIANA DE RADIO SAS':'Empresa Colombiana<br>de radio','RADIO CADENA NACIONAL SAS':'RCN Radio','DIGITAL ESTEREO SAS':'Digital estereo',
            'SERVICIO RADIAL INTEGRADO SAS':'Servicio radial<br>integrado','PRODUCCIONES WILLVIN S A':'Producciones Willvin','ORGANIZACION RADIAL OLIMPICA S.A.':'Olimpica organización<br>radial',
            'CHAR DIAZ SAS':'Char Diaz','VITAL INVERSIONES S.A.':'Vital inversiones','ALIANZA INTEGRAL COM SAS':'Alianza integral','CARACOL TELEVISIÓN S.A.':'Caracol Televisión'}
            ##Ingresos Radio
            IngresosRadio=pd.read_csv('https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria/main/2023/Datos_Sin_API/radio_ingresos.csv',delimiter=';',encoding='utf-8')
            IngresosRadio['Ingresos de actividades ordinarias']=IngresosRadio['Ingresos de actividades ordinarias'].str.replace('.','').astype('int64')
            IngresosRadio['Año']=IngresosRadio['Año'].astype('str')       
            IngresosRadio=IngresosRadio.rename(columns={'Grupo Radial':'empresa','Ingresos de actividades ordinarias':'ingresos','Año':'anno'})
            IngresosRadio=IngresosRadio.groupby(['anno','empresa'])['ingresos'].sum().reset_index()
            IngresosRadio=IngresosRadio.merge(IPCAnuTot,left_on=['anno'],right_on=['anno'])
            IngresosRadio['ingresos']=IngresosRadio['ingresos']/IngresosRadio['indice2022']
            IngresosRadio['empresa']=IngresosRadio['empresa'].replace(nombres_Radio)
           
            ##Número emisoras
            NumeroEmisoras=pd.read_csv('https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria/main/2023/Datos_Sin_API/listado_emisoras_radio.csv',delimiter=';',encoding='utf-8')
            NumeroEmisoras=NumeroEmisoras.rename(columns={'CLASE DE\nEMISORA':'CLASE DE EMISORA'})
            NumeroEmisoras['DEPARTAMENTO']=NumeroEmisoras['DEPARTAMENTO'].replace({'ARCHIPIÉLAGO DE SAN ANDRÉS, PROVIDENCIA Y SANTA CATALINA':'SAN ANDRÉS Y PROV.',
                                                                          'NORTE DE\nSANTANDER':'N.SANTANDER','NORTE DE SANTANDER':'N.SANTANDER'})        
            #
            NumeroEmisorasAgg=NumeroEmisoras.groupby(['CLASE DE EMISORA','BANDA'])['CODIGO EMISORA'].nunique().reset_index()
            NumeroEmisorasAgg=NumeroEmisorasAgg.rename(columns={'CODIGO EMISORA':'Número emisoras'})
            NumeroEmisorasAgg.loc[NumeroEmisorasAgg['CLASE DE EMISORA']=='COMUNITARIA','BANDA']=None
            NumeroEmisorasAgg['CLASE DE EMISORA']=NumeroEmisorasAgg['CLASE DE EMISORA'].replace({'INTERÉS PÚBLICO':'INTERÉS<br>PÚBLICO'})
            #
            NumeroEmisorasDepComerciales=NumeroEmisoras[NumeroEmisoras['CLASE DE EMISORA']=='COMERCIAL'].groupby(['DEPARTAMENTO','BANDA'])['CODIGO EMISORA'].nunique().reset_index()
            NumeroEmisorasDepComerciales=NumeroEmisorasDepComerciales.rename(columns={'CODIGO EMISORA':'Número empresas'})
            NumeroEmisorasDepComunitarias=NumeroEmisoras[NumeroEmisoras['CLASE DE EMISORA']=='COMUNITARIA'].groupby(['DEPARTAMENTO','BANDA'])['CODIGO EMISORA'].nunique().reset_index()
            NumeroEmisorasDepComunitarias=NumeroEmisorasDepComunitarias.rename(columns={'CODIGO EMISORA':'Número empresas'})
            
            ServiciosRadio=st.selectbox('Escoja el servicio de radio',['Ingresos','Número de emisoras'])
            
            if ServiciosRadio=='Ingresos':
                st.markdown("""<center><p style="font-size:12px"><b>Nota:</b> Ingresos ajustados por inflación, usando el IPC total. Periodo base, diciembre 2022</p></center>""",unsafe_allow_html=True)
                st.plotly_chart(PlotlyBarrasEmp(IngresosRadio,'ingresos','Miles de Millones de pesos',1e6,'<b>Ingresos en radio por empresa</b>',['rgb(0,76,153)','rgb(255,153,51)',
                'rgb(0,204,102)','#f27234','rgb(188,143,143)','rgb(221,160,221)','rgb(123,104,238)','rgb(220,11,11)'],''),use_container_width=True)
       
      
            if ServiciosRadio=='Número de emisoras':
                st.markdown("""<p style="font-size:12px"><b>Nota:</b> Las emisoras comunitarias son aquellas que prestan "un servicio público participativo y pluralista, orientado a satisfacer necesidades de comunicación en el municipio o área objeto de cubrimiento, promueven el desarrollo social, la convivencia pacífica, los valores democráticos, la construcción de ciudadanía y el fortalecimiento de las identidades culturales y
                sociales". </p>""",unsafe_allow_html=True)
                st.markdown("""<p style="font-size:12px"><b>Nota:</b> Son ejemplo de emisoras de interés público la Radio Pública Nacional de Colombia, emisoras de la Fuerza Pública (ejército y policía nacional), emisoras territoriales, emisoras educativas, emisoras educativas universitarias, emisoras para atención y prevención de desastres.</p>""",unsafe_allow_html=True)
                st.markdown("""<p style="font-size:12px"><b>Nota:</b> Las emisoras comerciales son aquellas cuya programación está destinada a la satisfacción de los hábitos y gustos del oyente y el servicio se presta con ánimo de lucro.</p>""",unsafe_allow_html=True)

                col1,col2=st.columns(2)
                with col1:
                    ParticipacionNEmmisoras=st.button('Participación')
                with col2:
                    ClasedeEmisoraRadio=st.button('Clase de emisora')
                
                if ParticipacionNEmmisoras:
                    figPartNEmis =go.Figure(go.Sunburst(
                        ids=["COMERCIAL", "INTERÉS<br>PÚBLICO", "COMUNITARIA","FM","AM","FM2","AM2"],
                        labels=["COMERCIAL", "INTERÉS<br>PÚBLICO", "COMUNITARIA","FM","AM","FM","AM"],
                        parents=["","","","INTERÉS<br>PÚBLICO","INTERÉS<br>PÚBLICO","COMERCIAL","COMERCIAL"],
                        values=[ 620,328,770,311,17,309,311],
                        branchvalues="total",
                        marker=dict(colors=['rgb(0, 128, 255)','rgb(102, 204, 0)','rgb(122, 68, 242)']),
                    ))
                    figPartNEmis.update_layout(margin = dict(t=0, l=0, r=0, b=0))

                    figPartNEmis.update_layout(height=550,legend_title=None)
                    figPartNEmis.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20,
                    title={
                    'text':'<b>Participación en el número de emisoras por clase de emisora y banda<br>(2022)',
                    'y':0.9,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'})      
                    figPartNEmis.update_layout(
                        margin = dict(t=10, l=10, r=10, b=10))

                    st.plotly_chart(figPartNEmis,use_container_width=True)    
                    st.markdown("<center><p style='font-size:11px'><b>Fuente</b>: Elaboración CRC con base en estados financieros del Sistema Integrado de Reportes Financieros<br>SIRFIN de la Superintendencia de Sociedades</p></center>",unsafe_allow_html=True)
                    
                if ClasedeEmisoraRadio:
                    figDepComercial = px.bar(NumeroEmisorasDepComerciales, x="DEPARTAMENTO", y='Número empresas',color='BANDA',color_discrete_sequence=['rgb(122, 68, 242)','rgb(0, 128, 255)'])
                    figDepComercial.update_xaxes(tickangle=-45, tickfont=dict(family='Times', color='black', size=12),title_text=None,row=1, col=1,
                    zeroline=True,linecolor = "rgba(192, 192, 192, 0.8)",zerolinewidth=2)
                    figDepComercial.update_yaxes(tickfont=dict(family='Poppins', color='black', size=16),titlefont_size=18, title_text='', row=1, col=1)
                    figDepComercial.update_layout(height=550,legend_title=None)
                    figDepComercial.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20,
                    title={
                    'text': '<b>Número de emisoras comerciales por departamento y banda</b>',
                    'y':0.95,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'})        
                    figDepComercial.update_layout(legend=dict(orientation="h",y=1,xanchor='center',x=0.5,font_size=12),showlegend=True)
                    figDepComercial.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',yaxis_tickformat='d')
                    figDepComercial.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
                    figDepComercial.add_annotation(
                    showarrow=False,
                    text='<b>Fuente</b>: Elaboración CRC con base en estados financieros del Sistema Integrado de Reportes Financieros SIRFIN de la Superintendencia de Sociedades',
                    font=dict(size=11), xref='x domain',x=0.5,yref='y domain',y=-0.32)

                    st.plotly_chart(figDepComercial,use_container_width=True)
                    #
                    figDepComunitaria = px.bar(NumeroEmisorasDepComunitarias, x="DEPARTAMENTO", y='Número empresas',color='BANDA',color_discrete_sequence=['rgb(0, 128, 255)'])
                    figDepComunitaria.update_xaxes(tickangle=-45, tickfont=dict(family='Times', color='black', size=12),title_text=None,row=1, col=1,
                    zeroline=True,linecolor = "rgba(192, 192, 192, 0.8)",zerolinewidth=2)
                    figDepComunitaria.update_yaxes(tickfont=dict(family='Poppins', color='black', size=16),titlefont_size=18, title_text='', row=1, col=1)
                    figDepComunitaria.update_layout(height=550,legend_title=None)
                    figDepComunitaria.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20,
                    title={
                    'text': '<b>Número de emisoras comunitarias por departamento y banda</b>',
                    'y':0.95,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'})        
                    figDepComunitaria.update_layout(legend=dict(orientation="h",y=0.95,xanchor='center',x=0.5,font_size=12),showlegend=True)
                    figDepComunitaria.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',yaxis_tickformat='d')
                    figDepComunitaria.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
                    figDepComunitaria.add_annotation(
                    showarrow=False,
                    text='<b>Fuente</b>: Elaboración CRC con base en estados financieros del Sistema Integrado de Reportes Financieros SIRFIN de la Superintendencia de Sociedades',
                    font=dict(size=11), xref='x domain',x=0.5,yref='y domain',y=-0.28)
                    st.plotly_chart(figDepComunitaria,use_container_width=True)

        if ServiciosRadiodifusion=='TV abierta':
            col1,col2=st.columns(2)
            with col1:
                st.markdown(r"""<div class='IconoTitulo'><img height="200px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Iconos/tv%20abierta.png?raw=true'/><h4 style="text-align:left">TV abierta</h4></div>""",unsafe_allow_html=True)   
            with col2:             
                with st.expander("Datos relevantes de TV abierta"):
                    st.markdown(r"""<ul>
                    <li>Los ingresos por TV abierta alcanzaron 2.02 billones de pesos en 2022, presentando una reducción del 0,2% en términos constantes.</li>
                    <li>Por servicio, la TV abierta privada representa el 65.4% de los ingresos y creció un 1%</li>
                    <li>Los operadores de TV públicos (nacionales, regionales y local sin ánimo de lucro) obtienen ingresos principalmente por transferencias del gobierno nacional y local para su operación.</li>
                    </ul>""",unsafe_allow_html=True)
            st.markdown('') 
            
            IngresosTVabierta=st.selectbox('Escoja el servicio de TV abierta',['Ingresos por servicio','Ingresos TV pública'])
              
            ##Ingresos TV abierta
            TVabierta=TVabierta.dropna()
            TVabierta=TVabierta[TVabierta['ingresos']>0]
            IPCAnuTot2=IPCAnuTot.copy()
            IPCAnuTot2['anno']=IPCAnuTot2['anno'].astype('int64')
            TVabierta=TVabierta.merge(IPCAnuTot2,left_on=['anno'],right_on=['anno'])
            TVabierta['ingresos']=TVabierta['ingresos']/TVabierta['indice2022']
            TVabierta=TVabierta.rename(columns={'nit':'id_empresa','razon social':'empresa'})   
            TVabiertaNac=TVabierta.groupby(['anno','modalidad'])['ingresos'].sum().reset_index()
            #
            TVabiertaEmp=TVabierta.groupby(['anno','empresa','id_empresa'])['ingresos'].sum().reset_index()
            TVabiertaEmp=TVabiertaEmp[TVabiertaEmp['anno'].isin([2021,2022])]
            EmpTVAbierta=TVabiertaEmp[TVabiertaEmp['anno']==2022].sort_values(by='ingresos',ascending=False)['id_empresa'].to_list()[0:4]
            TVabiertaEmp=TVabiertaEmp[(TVabiertaEmp['id_empresa'].isin(EmpTVAbierta))]
            ##Ingresos TV Pública
            
            if IngresosTVabierta=='Ingresos por servicio':
                st.markdown("""<center><p style="font-size:12px"><b>Nota:</b> Ingresos ajustados por inflación, usando el IPC total. Periodo base, diciembre 2022</p></center>""",unsafe_allow_html=True)
                st.markdown('Escoja la dimensión del análisis')  
                col1,col2=st.columns(2)
                with col1:
                    ModalidadTVabierta=st.button('Evolución temporal')
                with col2:
                    OperadoresTVabierta=st.button('Información por operadores')

                if ModalidadTVabierta:
                    figTVabiertaMod=make_subplots(rows=1,cols=2)
                    Color_Modalidad={'TELEVISIÓN LOCAL CON ÁNIMO DE LUCRO':'rgb(122, 68, 242)','TELEVISIÓN LOCAL SIN ÁNIMO DE LUCRO':'rgb(0, 128, 255)',
                                    'TELEVISIÓN NACIONAL (Concesión)':'rgb(102,204,0)','TELEVISIÓN NACIONAL PRIVADA':'#ffbf00'}
                    for modalidad in ['TELEVISIÓN NACIONAL PRIVADA']:
                        df=TVabiertaNac[TVabiertaNac['modalidad']==modalidad]
                        figTVabiertaMod.add_trace(go.Bar(x=df['anno'],y=df['ingresos']/1e9,name=modalidad,marker_color=Color_Modalidad[modalidad]),row=1,col=2)
                        
                    for modalidad in ['TELEVISIÓN LOCAL CON ÁNIMO DE LUCRO','TELEVISIÓN LOCAL SIN ÁNIMO DE LUCRO','TELEVISIÓN NACIONAL (Concesión)']:
                        df=TVabiertaNac[TVabiertaNac['modalidad']==modalidad]
                        figTVabiertaMod.add_trace(go.Bar(x=df['anno'],y=df['ingresos']/1e6,name=modalidad,marker_color=Color_Modalidad[modalidad]),row=1,col=1)
                        
                    figTVabiertaMod.update_layout(barmode='group')
                    figTVabiertaMod.update_yaxes(title_text='Miles de Millones de pesos',row=1,col=2)
                    figTVabiertaMod.update_yaxes(title_text='Millones de pesos',row=1,col=1)
                    figTVabiertaMod.update_xaxes(tickangle=0, tickfont=dict(family='Poppins', color='black', size=16),title_text=None,
                    zeroline=True,linecolor = "rgba(192, 192, 192, 0.8)",zerolinewidth=2)
                    figTVabiertaMod.update_yaxes(tickfont=dict(family='Poppins', color='black', size=16),titlefont_size=18)
                    figTVabiertaMod.update_layout(height=550,legend_title=None)
                    figTVabiertaMod.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20,
                    title={
                    'text': '<b>Ingresos de televisión abierta por modalidad</b>',
                    'y':0.95,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'})        
                    figTVabiertaMod.update_layout(legend=dict(orientation="h",y=1.12,x=0.1,font_size=12),showlegend=True)
                    figTVabiertaMod.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',yaxis_tickformat='d')
                    figTVabiertaMod.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
                    figTVabiertaMod.add_annotation(
                    showarrow=False,
                    text='<b>Fuente</b>: Elaboración CRC con base en estados financieros Contaduría general de la Nación y liquidación de contribución FUTIC',
                    font=dict(size=11), xref='x domain',x=0.1,yref='y domain',y=-0.2)
                    st.plotly_chart(figTVabiertaMod,use_container_width=True)
                 
                if OperadoresTVabierta:
                    st.plotly_chart(PlotlyBarras(TVabiertaEmp,'ingresos','Miles de Millones de pesos',1e9,'<b>Ingresos anuales por empresa</b>','<b>Fuente</b>: Elaboración CRC con base en estados financieros Contaduría general de la Nación y liquidación de contribución FUTIC'),use_container_width=True)            
            
            if IngresosTVabierta=='Ingresos TV pública':    
                columnas_corregir = ['Oper_TV(%)', 'Otros_servicios(%)', 'Transferencias(%)']
                for column in columnas_corregir:
                    TVPublica[column] = TVPublica[column].str.replace(',', '.').astype(float)
                TVPublicaAgg=TVPublica.groupby(['anno','empresa']).agg({'Oper_TV(%)':'sum','Otros_servicios(%)':'sum','Transferencias(%)':'sum'}).reset_index()
                TVPublicaAgg[['Oper_TV(%)','Otros_servicios(%)','Transferencias(%)']]=TVPublicaAgg[['Oper_TV(%)','Otros_servicios(%)','Transferencias(%)']]*100
                TVPublicaAgg=TVPublicaAgg.rename(columns={'Oper_TV(%)':'Operativo TV','Otros_servicios(%)':'Otros servicios','Transferencias(%)':'Transferencias'})
                TVPublicaAgg2=pd.melt(TVPublicaAgg,id_vars=['anno','empresa'],value_vars=['Operativo TV','Otros servicios','Transferencias'],
                                     var_name='ambito',value_name='Porcentaje')
                TVPublicaAgg2=TVPublicaAgg2[TVPublicaAgg2['anno'].isin([2021,2022])]

                color_ambitoTVPu={'Operativo TV':'rgb(178,102,255)','Otros servicios':'rgb(102,255,102)',
                             'Transferencias':'rgb(102,178,255)'}
                figTVPublica = make_subplots(rows=1,cols=1)
                for ambito in TVPublicaAgg2['ambito'].unique().tolist():
                    df2=TVPublicaAgg2[TVPublicaAgg2['ambito']==ambito]    
                    X=[df2['empresa'].tolist(),df2['anno'].tolist()]
                    figTVPublica.add_trace(go.Bar(x=X,y=TVPublicaAgg2[TVPublicaAgg2['ambito']==ambito]['Porcentaje'],name=ambito,marker_color=color_ambitoTVPu[ambito]))
                figTVPublica.update_layout(barmode='stack')
                figTVPublica.update_xaxes(tickangle=0, tickfont=dict(family='Poppins', color='black', size=12),title_text=None,row=1, col=1,
                zeroline=True,linecolor = "rgba(192, 192, 192, 0.8)",zerolinewidth=2)
                figTVPublica.update_yaxes(tickfont=dict(family='Poppins', color='black', size=16),titlefont_size=18, title_text='Porcentaje', row=1, col=1)
                figTVPublica.update_layout(height=550,legend_title=None)
                figTVPublica.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20,
                title={
                'text': '<b>Composición de ingresos de los canales públicos nacionales, regionales y locales</b>',
                'y':0.92,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'})        
                figTVPublica.update_layout(legend=dict(orientation="h",y=1.05,xanchor='center',x=0.5,font_size=12),showlegend=True)
                figTVPublica.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',yaxis_tickformat='d')
                figTVPublica.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
                figTVPublica.add_annotation(
                showarrow=False,
                text='<b>Fuente</b>: Elaboración CRC con base en estados financieros Contaduría general de la Nación y liquidación de contribución FUTIC',
                font=dict(size=11), xref='x domain',x=0.5,yref='y domain',y=-0.2)
                st.plotly_chart(figTVPublica,use_container_width=True)        

    if select_secResumenDinTic == 'Comparación internacional':
        st.markdown(r"""<div class="titulo"><h3>Comparación internacional</h3></div>""",unsafe_allow_html=True)
        
        ServiciosInternacionales=st.radio('',['Telefonía fija','Telefonía móvil','Internet fijo','Internet móvil','TV por suscripción'],horizontal=True)
        st.markdown(r"""<hr>""",unsafe_allow_html=True) 

        GlobalData=pd.read_csv('https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria/main/Datos_Sin_API/GlobalData.csv',delimiter=';')
        GlobalData=GlobalData.iloc[:,:6]
        GlobalData=GlobalData.rename(columns={'Country':'País'})
        GlobalData['País']=GlobalData['País'].replace({'Brazil':'Brasil','Dominican Republic':'República Dominicana'})
        GlobalData2=pd.melt(GlobalData,id_vars=['País','Variable'],value_vars=['2018A','2019A','2020A','2021A'],var_name='Año',value_name='Accesos')
        GlobalData2['Año']=GlobalData2['Año'].replace('\D','',regex=True)
        GlobalData2['Accesos']=GlobalData2['Accesos'].str.replace(',','.').astype('float')
        GlobalData2=GlobalData2[GlobalData2['País'].isin(['Costa Rica','República Dominicana','El Salvador',
                                              'Guatemala','Honduras','Mexico','Nicaragua','Panama','Colombia'])==False]
        ColombiaInt=pd.read_csv('https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria/main/Datos_Sin_API/Colombia_Internacional.csv',delimiter=';',encoding='latin-1')
        ColombiaInt.columns=GlobalData2.columns
        ColombiaInt['Accesos']=ColombiaInt['Accesos']/1e3
        ColombiaInt['Variable']=ColombiaInt['Variable'].replace({'Internet fijo (Fibra Óptica) ':'Internet fijo (Fibra Óptica)'})
        ColombiaInt['Año']=ColombiaInt['Año'].astype('str')
        GlobalData2=pd.concat([GlobalData2,ColombiaInt])
        
        if ServiciosInternacionales == 'Telefonía fija':
            col1,col2=st.columns(2)
            with col1:
                st.markdown(r"""<div class='IconoTitulo'><img height="200px" src='https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria/main/Iconos/telefonia-fija.png'/><h4 style="text-align:left">Telefonía fija</h4></div>""",unsafe_allow_html=True)   
            with col2:
                with st.expander("Datos relevantes de Telefonía fija"):
                    st.markdown(r"""<ul>
                    <li>En 2021 Colombia registró un total de 7.55 Millones de líneas, y presentó una penetración del 44.71%, ubicandose en este indicador en la tercera posición en Suramérica.</li>
                    </ul>""",unsafe_allow_html=True)
                SelectTelFijaInt=st.selectbox('',['Evolución temporal','Penetraciones'])

            if SelectTelFijaInt=='Evolución temporal':
                TelFijaInt=GlobalData2[GlobalData2['Variable']=='Telefonía fija']            
                st.plotly_chart(PlotlylineatiempoInt(TelFijaInt,'Accesos','Millones de líneas',1e3,'<b>Líneas de telefonía fija en Suramérica</b>','<b>Fuente</b>:Elaboración CRC con datos para Colombia tomados en los reportes de información al sistema Colombia TIC.<br>La información de los demás paises es consultada a través de la plataforma Global Data.'),use_container_width=True)

            TelFijaInt2=GlobalData2[GlobalData2['Variable'].isin(['Telefonía fija','Hogares'])]
            TelFijaInt2=pd.pivot(TelFijaInt2,index=['País','Año'],columns='Variable',values='Accesos').reset_index()
            TelFijaInt2['Penetración']=round(100*TelFijaInt2['Telefonía fija']/TelFijaInt2['Hogares'],2)
            TelFijaInt2['País']=TelFijaInt2['País'].replace({'Brasil':'Brazil'})            
            gdf_GlobalDataTelFija=gdf_Int.merge(TelFijaInt2, left_on=['País'], right_on=['País'])  
            
            if SelectTelFijaInt=='Penetraciones':
                with col2:
                    BotonAño=st.selectbox('Escoja el año para visualizar la penetración',['2018','2019','2020','2021'],3)
                col1,col2=st.columns([1,1])
                
                with col2:
                    TelFijaInt2=TelFijaInt2[TelFijaInt2['Año']==BotonAño]
                    TelFijaInt2['País']=TelFijaInt2['País'].replace({'Brazil':'Brasil'}) 
                    TelFijaInt2['Cod_pais']=TelFijaInt2['País'].apply(lambda x: x[0:3].upper())
                    st.plotly_chart(PlotlyBarrasInt(TelFijaInt2,'Penetración','Porcentaje (%)',1,'<b>Penetración en suramérica-</b>'+BotonAño,'<b>Fuente</b>: Elaboración CRC con datos para Colombia tomados en los reportes de información<br>al sistema Colombia TIC. La información de los demás paises es consultada a través de la<br>plataforma Global Data.'),use_container_width=True)
                
                with col1:                    
                    gdf_GlobalDataTelFija=gdf_GlobalDataTelFija[gdf_GlobalDataTelFija['Año']==BotonAño]
                    st.markdown('')
                    suramerica_map = folium.Map(location=[-24, -60], zoom_start=3,tiles='cartodbpositron')
                    choropleth=folium.Choropleth(
                        geo_data=SURAMERICA,
                        data=gdf_GlobalDataTelFija,
                        columns=['País', 'Penetración'],
                        key_on='feature.properties.name',
                        bins=[10,20,30,40,50,60,70,80,90,100],
                        fill_color='Greens', 
                        fill_opacity=1, 
                        line_opacity=0.9,
                        reversescale=True,
                        legend_name='Penetración',
                        nan_fill_color = "black",
                        smooth_factor=0).add_to(suramerica_map)

                    #Adicionar valores velocidad
                    style_function = lambda x: {'fillColor': '#ffffff', 
                                                'color':'#000000', 
                                                'fillOpacity': 0.1, 
                                                'weight': 0.1}
                    highlight_function = lambda x: {'fillColor': '#000000', 
                                                    'color':'#000000', 
                                                    'fillOpacity': 0.50, 
                                                    'weight': 0.1}
                    NIL = folium.features.GeoJson(
                        data = gdf_GlobalDataTelFija,
                        style_function=style_function, 
                        control=False,
                        highlight_function=highlight_function, 
                        tooltip=folium.features.GeoJsonTooltip(
                            fields=['País','Penetración'],
                            aliases=['País','Penetración'],
                            style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;") 
                        )
                    )
                    suramerica_map.add_child(NIL)
                    suramerica_map.keep_in_front(NIL)                           
                    st.markdown("<b>Penetración de Telefonía fija en Suramerica</b>-"+BotonAño,
                    unsafe_allow_html=True)
                    #Quitar barra de colores
                    for key in choropleth._children:
                        if key.startswith('color_map'):
                            del(choropleth._children[key])
                    folium_static(suramerica_map,width=400,height=500)     
                        
                with col1:    
                    st.markdown("<p style='font-size:10px'><b>Fuente</b>: Elaboración CRC con datos para Colombia tomados en los reportes de información<br>al sistema Colombia TIC. La información de los demás paises es consultada a través de la<br>plataforma Global Data.",unsafe_allow_html=True)    
                                                
        if ServiciosInternacionales == 'Telefonía móvil':
            col1,col2=st.columns(2)
            with col1:
                st.markdown(r"""<div class='IconoTitulo'><img height="200px" src='https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria/main/Iconos/telefonia-movil.png'/><h4 style="text-align:left">Telefonía móvil</h4></div>""",unsafe_allow_html=True)   
            with col2:
                with st.expander("Datos relevantes de Telefonía móvil"):
                    st.markdown(r"""<ul>
                    <li>En 2021 Colombia registró un total de 75.06 Millones de líneas, y presentó una penetración del 147%, ubicandose en este indicador en la primera posición en Suramérica.</li>
                    </ul>""",unsafe_allow_html=True)
                SelectTelMovilInt=st.selectbox('',['Evolución temporal','Penetraciones'])
            
            if SelectTelMovilInt=='Evolución temporal':
                TelMovilInt=GlobalData2[GlobalData2['Variable']=='Telefonía móvil']
                st.plotly_chart(PlotlylineatiempoInt(TelMovilInt,'Accesos','Millones de líneas',1e3,'<b>Líneas de telefonía móvil en Suramérica</b>','<b>Fuente</b>: Elaboración CRC con datos para Colombia tomados en los reportes de información<br>al sistema Colombia TIC. La información de los demás paises es consultada a través de la<br>plataforma Global Data.'),use_container_width=True)                        

            TelMovilInt2=GlobalData2[GlobalData2['Variable'].isin(['Telefonía móvil','Población'])]
            TelMovilInt2=pd.pivot(TelMovilInt2,index=['País','Año'],columns='Variable',values='Accesos').reset_index()
            TelMovilInt2['Penetración']=round(100*TelMovilInt2['Telefonía móvil']/TelMovilInt2['Población'],2)
            TelMovilInt2['País']=TelMovilInt2['País'].replace({'Brasil':'Brazil'})
            gdf_GlobalDataTelMovil=gdf_Int.merge(TelMovilInt2, left_on=['País'], right_on=['País']) 

            if SelectTelMovilInt=='Penetraciones':
                with col2:
                    BotonAño=st.selectbox('Escoja el año para visualizar la penetración',['2018','2019','2020','2021'],3)
                col1,col2=st.columns([1,1])
                
                with col2:
                    TelMovilInt2=TelMovilInt2[TelMovilInt2['Año']==BotonAño]
                    TelMovilInt2['País']=TelMovilInt2['País'].replace({'Brazil':'Brasil'}) 
                    TelMovilInt2['Cod_pais']=TelMovilInt2['País'].apply(lambda x: x[0:3].upper())
                    st.plotly_chart(PlotlyBarrasInt(TelMovilInt2,'Penetración','Porcentaje (%)',1,'<b>Penetración en suramérica-</b>'+BotonAño,'<b>Fuente</b>: Elaboración CRC con datos para Colombia tomados en los reportes de información<br>al sistema Colombia TIC. La información de los demás paises es consultada a través de la<br>plataforma Global Data.'),use_container_width=True)
                
                with col1:
                    gdf_GlobalDataTelMovil=gdf_GlobalDataTelMovil[gdf_GlobalDataTelMovil['Año']==BotonAño]
                
                    suramerica_map = folium.Map(location=[-24, -60], zoom_start=3,tiles='cartodbpositron')
                    choropleth=folium.Choropleth(
                        geo_data=SURAMERICA,
                        data=gdf_GlobalDataTelMovil,
                        columns=['País', 'Penetración'],
                        key_on='feature.properties.name',
                        #bins=[10,20,30,40,50,60,70,80,90,100],
                        fill_color='Greens', 
                        fill_opacity=1, 
                        line_opacity=0.9,
                        reversescale=True,
                        legend_name='Penetración',
                        nan_fill_color = "black",
                        smooth_factor=0).add_to(suramerica_map)

                    #Adicionar valores velocidad
                    style_function = lambda x: {'fillColor': '#ffffff', 
                                                'color':'#000000', 
                                                'fillOpacity': 0.1, 
                                                'weight': 0.1}
                    highlight_function = lambda x: {'fillColor': '#000000', 
                                                    'color':'#000000', 
                                                    'fillOpacity': 0.50, 
                                                    'weight': 0.1}
                    NIL = folium.features.GeoJson(
                        data = gdf_GlobalDataTelMovil,
                        style_function=style_function, 
                        control=False,
                        highlight_function=highlight_function, 
                        tooltip=folium.features.GeoJsonTooltip(
                            fields=['País','Penetración'],
                            aliases=['País','Penetración'],
                            style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;") 
                        )
                    )
                    suramerica_map.add_child(NIL)
                    suramerica_map.keep_in_front(NIL)                           
                    st.markdown("<b>Penetración de Telefonía móvil en Suramerica -</b>"+BotonAño,
                    unsafe_allow_html=True)
                    #Quitar barra de colores
                    for key in choropleth._children:
                        if key.startswith('color_map'):
                            del(choropleth._children[key])
                    folium_static(suramerica_map,width=400,height=500)   

                with col1:    
                    st.markdown("<p style='font-size:10px'><b>Fuente</b>: Elaboración CRC con datos para Colombia tomados en los reportes de información<br>al sistema Colombia TIC. La información de los demás paises es consultada a través de la<br>plataforma Global Data.",unsafe_allow_html=True)    
            
        if ServiciosInternacionales == 'Internet móvil':
            col1,col2=st.columns(2)
            with col1:
                st.markdown(r"""<div class='IconoTitulo'><img height="200px" src='https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria/main/Iconos/internet-movil.png'/><h4>Internet móvil</h4></div>""",unsafe_allow_html=True) 
            with col2:
                with st.expander("Datos relevantes de Internet móvil"):
                    st.markdown(r"""<ul>
                    <li>En 2021 Colombia registró un total de 37.96 Millones de accesos, y presentó una penetración del 74.4%, ubicandose en este indicador en la quinta posición en Suramérica.</li>
                    </ul>""",unsafe_allow_html=True)
                SelectIntMovilInt=st.selectbox('',['Evolución temporal','Penetraciones'])
            
            if SelectIntMovilInt=='Evolución temporal':
                IntMovilInt=GlobalData2[GlobalData2['Variable']=='Internet móvil']
                st.plotly_chart(PlotlylineatiempoInt(IntMovilInt,'Accesos','Millones de accesos',1e3,'<b>Accesos de Internet móvil en Suramérica</b>','<b>Fuente</b>: Elaboración CRC con datos para Colombia tomados en los reportes de información<br>al sistema Colombia TIC. La información de los demás paises es consultada a través de la<br>plataforma Global Data.'),use_container_width=True)

            IntMovilInt2=GlobalData2[GlobalData2['Variable'].isin(['Internet móvil','Población'])]
            IntMovilInt2=pd.pivot(IntMovilInt2,index=['País','Año'],columns='Variable',values='Accesos').reset_index()
            IntMovilInt2['Penetración']=round(100*IntMovilInt2['Internet móvil']/IntMovilInt2['Población'],2)
            IntMovilInt2['País']=IntMovilInt2['País'].replace({'Brasil':'Brazil'})
            gdf_GlobalDataIntMovil=gdf_Int.merge(IntMovilInt2, left_on=['País'], right_on=['País']) 

            if SelectIntMovilInt=='Penetraciones':
                with col2:
                    BotonAño=st.selectbox('Escoja el año para visualizar la penetración',['2018','2019','2020','2021'],3)
                col1,col2=st.columns([1,1])

                with col2:
                    IntMovilInt2=IntMovilInt2[IntMovilInt2['Año']==BotonAño]
                    IntMovilInt2['País']=IntMovilInt2['País'].replace({'Brazil':'Brasil'})
                    IntMovilInt2['Cod_pais']=IntMovilInt2['País'].apply(lambda x: x[0:3].upper())                    
                    st.plotly_chart(PlotlyBarrasInt(IntMovilInt2,'Penetración','Porcentaje (%)',1,'<b>Penetración en suramérica-</b>'+BotonAño,'<b>Fuente</b>: Elaboración CRC con datos para Colombia tomados en los reportes de información<br>al sistema Colombia TIC. La información de los demás paises es consultada a través de la<br>plataforma Global Data.'),use_container_width=True)

                with col1:
                    gdf_GlobalDataIntMovil=gdf_GlobalDataIntMovil[gdf_GlobalDataIntMovil['Año']==BotonAño]
                
                    suramerica_map = folium.Map(location=[-24, -60], zoom_start=3,tiles='cartodbpositron')
                    choropleth=folium.Choropleth(
                        geo_data=SURAMERICA,
                        data=gdf_GlobalDataIntMovil,
                        columns=['País', 'Penetración'],
                        key_on='feature.properties.name',
                        #bins=[10,20,30,40,50,60,70,80,90,100],
                        fill_color='Greens', 
                        fill_opacity=1, 
                        line_opacity=0.9,
                        reversescale=True,
                        legend_name='Penetración',
                        nan_fill_color = "black",
                        smooth_factor=0).add_to(suramerica_map)

                    #Adicionar valores velocidad
                    style_function = lambda x: {'fillColor': '#ffffff', 
                                                'color':'#000000', 
                                                'fillOpacity': 0.1, 
                                                'weight': 0.1}
                    highlight_function = lambda x: {'fillColor': '#000000', 
                                                    'color':'#000000', 
                                                    'fillOpacity': 0.50, 
                                                    'weight': 0.1}
                    NIL = folium.features.GeoJson(
                        data = gdf_GlobalDataIntMovil,
                        style_function=style_function, 
                        control=False,
                        highlight_function=highlight_function, 
                        tooltip=folium.features.GeoJsonTooltip(
                            fields=['País','Penetración'],
                            aliases=['País','Penetración'],
                            style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;") 
                        )
                    )
                    suramerica_map.add_child(NIL)
                    suramerica_map.keep_in_front(NIL)                           
                    st.markdown("<b>Penetración de Internet móvil en Suramerica -</b>"+BotonAño,
                    unsafe_allow_html=True)
                    #Quitar barra de colores
                    for key in choropleth._children:
                        if key.startswith('color_map'):
                            del(choropleth._children[key])
                    folium_static(suramerica_map,width=400,height=500)   

                with col1:    
                    st.markdown("<p style='font-size:10px'><b>Fuente</b>: Elaboración CRC con datos para Colombia tomados en los reportes de información<br>al sistema Colombia TIC. La información de los demás paises es consultada a través de la<br>plataforma Global Data.",unsafe_allow_html=True)    

        if ServiciosInternacionales == 'Internet fijo':
            col1,col2=st.columns(2)
            with col1:
                st.markdown(r"""<div class='IconoTitulo'><img height="200px" src='https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria/main/Iconos/internet-fijo.png'/><h4 style="text-align:left">Internet fijo</h4></div>""",unsafe_allow_html=True)   
            with col2:
                with st.expander("Datos relevantes de Internet fijo"):
                    st.markdown(r"""<ul>
                    <li>En 2021 Colombia registró un total de 8.43 Millones de accesos, y presentó una penetración del 49.9%, ubicandose en este indicador en la sexta posición en Suramérica.</li>
                    </ul>""",unsafe_allow_html=True)
                SelectIntFijoInt=st.selectbox('',['Evolución temporal','Penetraciones'])
            
            if SelectIntFijoInt=='Evolución temporal':    
                IntMovilfijo=GlobalData2[GlobalData2['Variable'].isin(['Internet fijo','Internet fijo (Fibra Óptica)'])]
                IntMovilfijo=pd.pivot(IntMovilfijo,index=['País','Año'],columns='Variable',values='Accesos').reset_index()
                IntMovilfijo['Fibra óptica(%)']=round(100*IntMovilfijo['Internet fijo (Fibra Óptica)']/IntMovilfijo['Internet fijo'],2)
                st.plotly_chart(PlotlylineatiempoInt(IntMovilfijo,'Internet fijo','Millones de accesos',1e3,'<b>Accesos de Internet fijo en Suramérica</b>','<b>Fuente</b>: Elaboración CRC con datos para Colombia tomados en los reportes de información<br>al sistema Colombia TIC. La información de los demás paises es consultada a través de la plataforma<br>Global Data.'),use_container_width=True)
                st.plotly_chart(PlotlylineatiempoInt(IntMovilfijo,'Fibra óptica(%)','Porcentaje (%)',1,'<b>Evolución porcentaje Fibra óptica de Internet fijo en Suramérica</b>','<b>Fuente</b>: Elaboración CRC con datos para Colombia tomados en los reportes de información<br>al sistema Colombia TIC. La información de los demás paises es consultada a través de la plataforma<br>Global Data.'),use_container_width=True)

            IntFijoInt2=GlobalData2[GlobalData2['Variable'].isin(['Internet fijo','Hogares'])]
            IntFijoInt2=pd.pivot(IntFijoInt2,index=['País','Año'],columns='Variable',values='Accesos').reset_index()
            IntFijoInt2['Penetración']=round(100*IntFijoInt2['Internet fijo']/IntFijoInt2['Hogares'],2)
            IntFijoInt2['País']=IntFijoInt2['País'].replace({'Brasil':'Brazil'})
            gdf_GlobalDataIntFijo=gdf_Int.merge(IntFijoInt2, left_on=['País'], right_on=['País']) 

            if SelectIntFijoInt=='Penetraciones':
                with col2:
                    BotonAño=st.selectbox('Escoja el año para visualizar la penetración',['2018','2019','2020','2021'],3)

                col1,col2=st.columns([1,1])

                with col2:
                    IntFijoInt2=IntFijoInt2[IntFijoInt2['Año']==BotonAño]
                    IntFijoInt2['País']=IntFijoInt2['País'].replace({'Brazil':'Brasil'}) 
                    IntFijoInt2['Cod_pais']=IntFijoInt2['País'].apply(lambda x: x[0:3].upper())
                    st.plotly_chart(PlotlyBarrasInt(IntFijoInt2,'Penetración','Porcentaje (%)',1,'<b>Penetración en suramérica-<b>'+BotonAño,'<b>Fuente</b>: Elaboración CRC con datos para Colombia tomados en los reportes de información<br>al sistema Colombia TIC. La información de los demás paises es consultada a través de la<br>plataforma Global Data.'),use_container_width=True)

                with col1:                    
                    gdf_GlobalDataIntFijo=gdf_GlobalDataIntFijo[gdf_GlobalDataIntFijo['Año']==BotonAño]
                    st.markdown('')
                    suramerica_map = folium.Map(location=[-24, -60], zoom_start=3,tiles='cartodbpositron')
                    choropleth=folium.Choropleth(
                        geo_data=SURAMERICA,
                        data=gdf_GlobalDataIntFijo,
                        columns=['País', 'Penetración'],
                        key_on='feature.properties.name',
                        bins=[10,20,30,40,50,60,70,80,90,100],
                        fill_color='Greens', 
                        fill_opacity=1, 
                        line_opacity=0.9,
                        reversescale=True,
                        legend_name='Penetración',
                        nan_fill_color = "black",
                        smooth_factor=0).add_to(suramerica_map)

                    #Adicionar valores velocidad
                    style_function = lambda x: {'fillColor': '#ffffff', 
                                                'color':'#000000', 
                                                'fillOpacity': 0.1, 
                                                'weight': 0.1}
                    highlight_function = lambda x: {'fillColor': '#000000', 
                                                    'color':'#000000', 
                                                    'fillOpacity': 0.50, 
                                                    'weight': 0.1}
                    NIL = folium.features.GeoJson(
                        data = gdf_GlobalDataIntFijo,
                        style_function=style_function, 
                        control=False,
                        highlight_function=highlight_function, 
                        tooltip=folium.features.GeoJsonTooltip(
                            fields=['País','Penetración'],
                            aliases=['País','Penetración'],
                            style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;") 
                        )
                    )
                    suramerica_map.add_child(NIL)
                    suramerica_map.keep_in_front(NIL)                           
                    st.markdown("<b>Penetración de Internet fijo en Suramerica -</b>"+BotonAño,
                    unsafe_allow_html=True)
                    #Quitar barra de colores
                    for key in choropleth._children:
                        if key.startswith('color_map'):
                            del(choropleth._children[key])
                    folium_static(suramerica_map,width=400,height=500)      

                with col1:    
                    st.markdown("<p style='font-size:10px'><b>Fuente</b>: Elaboración CRC con datos para Colombia tomados en los reportes de información<br>al sistema Colombia TIC. La información de los demás paises es consultada a través de la<br>plataforma Global Data.",unsafe_allow_html=True)    

        if ServiciosInternacionales == 'TV por suscripción':
            col1,col2=st.columns(2)
            with col1:
                st.markdown(r"""<div class='IconoTitulo'><img height="200px" src='https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria/main/Iconos/tv-por-suscripcion.png'/><h4 style="text-align:left">TV por suscripción</h4></div>""",unsafe_allow_html=True)   
            with col2:
                with st.expander("Datos relevantes de TV por suscripción"):
                    st.markdown(r"""<ul>
                    <li>En 2021 Colombia registró un total de 6.17 Millones de suscriptores, y presentó una penetración del 36.5%, ubicandose en este indicador en la cuarta posición en Suramérica.</li>
                    </ul>""",unsafe_allow_html=True)
                SelectTVSusInt=st.selectbox('',['Evolución temporal','Penetraciones'])
            
            if SelectTVSusInt =='Evolución temporal':
                TVSusInt=GlobalData2[GlobalData2['Variable']=='TV por suscripción']
                st.plotly_chart(PlotlylineatiempoInt(TVSusInt,'Accesos','Millones de accesos',1e3,'<b>Accesos de TV por suscripción en Suramérica</b>','<b>Fuente</b>: Elaboración CRC con datos para Colombia tomados en los reportes de información<br>al sistema Colombia TIC. La información de los demás paises es consultada a través de la<br>plataforma Global Data.'),use_container_width=True)

            TVSusInt2=GlobalData2[GlobalData2['Variable'].isin(['TV por suscripción','Hogares'])]
            TVSusInt2=pd.pivot(TVSusInt2,index=['País','Año'],columns='Variable',values='Accesos').reset_index()
            TVSusInt2['Penetración']=round(100*TVSusInt2['TV por suscripción']/TVSusInt2['Hogares'],2)
            TVSusInt2['País']=TVSusInt2['País'].replace({'Brasil':'Brazil'})
            gdf_GlobalDataTVSus=gdf_Int.merge(TVSusInt2, left_on=['País'], right_on=['País']) 

            if SelectTVSusInt=='Penetraciones':
                with col2:
                    BotonAño=st.selectbox('Escoja el año para visualizar la penetración',['2018','2019','2020','2021'],3)
                col1,col2=st.columns([1,1])

                with col2:
                    TVSusInt2=TVSusInt2[TVSusInt2['Año']==BotonAño]
                    TVSusInt2['País']=TVSusInt2['País'].replace({'Brazil':'Brasil'})
                    TVSusInt2['Cod_pais']=TVSusInt2['País'].apply(lambda x: x[0:3].upper())                    
                    st.plotly_chart(PlotlyBarrasInt(TVSusInt2,'Penetración','Porcentaje (%)',1,'<b>Penetración en suramérica-</b>'+BotonAño,'<b>Fuente</b>: Elaboración CRC con datos para Colombia tomados en los reportes de información<br>al sistema Colombia TIC. La información de los demás paises es consultada a través de la<br>plataforma Global Data.'),use_container_width=True)

                with col1:                    
                    gdf_GlobalDataTVSus=gdf_GlobalDataTVSus[gdf_GlobalDataTVSus['Año']==BotonAño]
                    st.markdown('')
                    suramerica_map = folium.Map(location=[-24, -60], zoom_start=3,tiles='cartodbpositron')
                    choropleth=folium.Choropleth(
                        geo_data=SURAMERICA,
                        data=gdf_GlobalDataTVSus,
                        columns=['País', 'Penetración'],
                        key_on='feature.properties.name',
                        bins=[10,20,30,40,50,60,70,80,90,100],
                        fill_color='Greens', 
                        fill_opacity=1, 
                        line_opacity=0.9,
                        reversescale=True,
                        legend_name='Penetración',
                        nan_fill_color = "black",
                        smooth_factor=0).add_to(suramerica_map)

                    #Adicionar valores velocidad
                    style_function = lambda x: {'fillColor': '#ffffff', 
                                                'color':'#000000', 
                                                'fillOpacity': 0.1, 
                                                'weight': 0.1}
                    highlight_function = lambda x: {'fillColor': '#000000', 
                                                    'color':'#000000', 
                                                    'fillOpacity': 0.50, 
                                                    'weight': 0.1}
                    NIL = folium.features.GeoJson(
                        data = gdf_GlobalDataTVSus,
                        style_function=style_function, 
                        control=False,
                        highlight_function=highlight_function, 
                        tooltip=folium.features.GeoJsonTooltip(
                            fields=['País','Penetración'],
                            aliases=['País','Penetración'],
                            style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;") 
                        )
                    )
                    suramerica_map.add_child(NIL)
                    suramerica_map.keep_in_front(NIL)                           
                    st.markdown("<b>Penetración de TV por suscripción en Suramerica -</b>"+BotonAño,
                    unsafe_allow_html=True)
                    #Quitar barra de colores
                    for key in choropleth._children:
                        if key.startswith('color_map'):
                            del(choropleth._children[key])
                    folium_static(suramerica_map,width=400,height=500)      

                with col1:    
                    st.markdown("<p style='font-size:10px'><b>Fuente</b>: Elaboración CRC con datos para Colombia tomados en los reportes de información<br>al sistema Colombia TIC. La información de los demás paises es consultada a través de la<br>plataforma Global Data.",unsafe_allow_html=True)    
                
if select_seccion =='Postal':
    st.title("Sector Postal")

    select_secResumenPos = st.sidebar.selectbox('Seleccione la información a consultar',['Información general',
    'Servicios postales'])

    if select_secResumenPos=='Información general':

        st.markdown(r"""<div class="titulo"><h3>Información general</h3></div>""",unsafe_allow_html=True)
        col1, col2, col3,col4 = st.columns(4)
        with col1:
            st.markdown("<h2>Envíos por servicio</h2>",unsafe_allow_html=True)
        with col2:
            st.markdown(r"""<div><img height="100px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Iconos/correo.png?raw=true'/></div>""",unsafe_allow_html=True) 
        with col3:
            st.markdown(r"""<div><img height="100px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Iconos/mensajeria%20expresa.png?raw=true'/></div>""",unsafe_allow_html=True) 
        with col4:
            st.markdown(r"""<div><img height="100px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Iconos/giros.png?raw=true'/></div>""",unsafe_allow_html=True) 

        col2.metric("Correo", "45,6 M", "-46,9%")
        col3.metric("Mensajería expresa", "279,2 M", "0,81%")
        col4.metric("Giros", "106,1 M", "-5,3%")      
        st.markdown("<p style='font-size:12px'><b>Nota:</b> Variación porcentual calculada respecto al número de envíos registrados en 2021 </p>",unsafe_allow_html=True)
        st.markdown('')
        st.markdown('<hr>',unsafe_allow_html=True)
        st.markdown(r"""<h2>Panorama del sector</h2>""",unsafe_allow_html=True)
        st.markdown("")    
        col1,col2=st.columns(2)
        with col1:
            st.markdown("<p style='text-align:justify'>En 2022, los operadores de servicios postales tuvieron ingresos por 2,4 billones de pesos, equivalente a una reducción de 6,2% en términos reales frente a 2021. Así mismo, se realizaron más de 495,1 millones de transacciones, de las cuales el 56,9% correspondió a envíos de mensajería expresa, 25,8% a giros y el 17,3% de envíos de correo realizados por el Operador Postal Oficial.</p>",unsafe_allow_html=True)
        with col2:
            st.image('https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Imagenes_adicionales/Ingresos_servicio_postales2022.png?raw=true')
            st.markdown("<p style='font-size:10px'><b>Fuente:</b> Elaboración CRC con base en los reportes de información al sistema Colombia TIC", unsafe_allow_html=True)

        col1,col2=st.columns(2)
        with col1:
            st.markdown("<p style='text-align:justify'>Para la prestación de los servicios postales Operador Postal Oficial dispuso 1.315 puntos físicos, de los cuales el 84,8% de estos tuvieron presencia fuera de las capitales de departamento. Por el contrario, mensajería expresa tuvo una mayor proporción de puntos de atención en las ciudades capitales en las que se concentró el 61,8% de sus puntos. Finalmente, los operadores postales de pago pusieron a disposición más de 46 mil puntos de atención ubicados en el territorio nacional con presencia en las 32 capitales y 795 municipios más. Sólo en 142 puntos es posible la realización de envíos o entregas de giros internacionales. </p>",unsafe_allow_html=True)
        with col2:
            st.image('https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Imagenes_adicionales/Num_puntosfisicos_servpost.png?raw=true')
            st.markdown("<p style='font-size:10px'><b>Fuente:</b> Elaboración CRC con base en los reportes de información al sistema Colombia TIC", unsafe_allow_html=True)

    if select_secResumenPos=='Servicios postales':
        st.markdown(r"""<div class="titulo"><h3>Servicios postales</h3></div>""",unsafe_allow_html=True)
        st.markdown("<center>Para continuar, por favor seleccione el botón con el servicio del cual desea conocer la información</center>",unsafe_allow_html=True)
        select_DinPos = st.radio('',['Correo',
        'Mensajería expresa','Giros'],horizontal=True)      
        st.markdown(r"""<hr>""",unsafe_allow_html=True)

        if select_DinPos=='Correo':
            col1,col2=st.columns(2)
            with col1:
                st.markdown(r"""<div class='IconoTitulo'><img height="200px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Iconos/correo.png?raw=true'/><h4>Correo</h4></div>""",unsafe_allow_html=True)
            with col2:             
                with st.expander("Datos relevantes de Correo"):
                    st.markdown(r"""<ul>
                    <li>En 2022 se contabilizaron 45.6 millones de envíos, representando una reducción de 46.9% frente a 2021. Por tipo de envío, los masivos se redujeron 50.7%, lo que corresponde al 77.5% del total de envíos en 2022.</li>
                    <li>Los ingresos de correo en 2022 fueron de 83,7 mil millones de pesos, representando 19% menos que en 2021. Discriminando por tipo de envío, los ingresos de los envíos indivuales decrecieron un 15,1% en términos reales. Por su parte, los ingresos en envíos masivos se redujeron 29,6% en términos reales respecto de 2021.</li>
                    </ul>""",unsafe_allow_html=True)

            ServiciosCorreo=st.selectbox('Escoja el ámbito de Correo',['Número de envíos','Ingresos'])
            ##Número de envíos e ingresos
            IngresosyEnviosCorreo=IngresosyEnviosCorreo.merge(IPCTrimTot, left_on=['anno','trimestre','periodo'],right_on=['anno','trimestre','periodo'])
            IngresosyEnviosCorreo['Ingresos']=IngresosyEnviosCorreo['Ingresos']/IngresosyEnviosCorreo['indice2022']
            IngresosyEnviosCorreoNac=IngresosyEnviosCorreo.groupby(['anno','ambito','tipo_envio']).agg({'Envíos':'sum','Ingresos':'sum'}).reset_index()
            if ServiciosCorreo=='Número de envíos':
                st.plotly_chart(PlotyMultiIndexBarra(IngresosyEnviosCorreoNac,'Envíos','Millones','<b>Número de envíos por tipo de envío y ámbito</b>',1e6,'<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)
            
            if ServiciosCorreo=='Ingresos':
                st.markdown("""<center><p style="font-size:12px"><b>Nota:</b> Ingresos ajustados por inflación, usando el IPC total. Periodo base, diciembre 2022</p></center>""",unsafe_allow_html=True)
                st.plotly_chart(PlotyMultiIndexBarra(IngresosyEnviosCorreoNac,'Ingresos','Miles de Millones de pesos','<b>Ingresos por tipo de envío y ámbito</b>',1e9,'<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)

        if select_DinPos=='Mensajería expresa':

            col1,col2=st.columns(2)
            with col1:
                st.markdown(r"""<div class='IconoTitulo'><img height="200px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Iconos/mensajeria%20expresa.png?raw=true'/><h4>Mensajería expresa</h4></div>""",unsafe_allow_html=True)
            with col2:             
                with st.expander("Datos relevantes de Mensajería expresa"):
                    st.markdown(r"""<ul>
                    <li>En 2022, a través del servicio de mensajería expresa se realizaron 279,2 millones de envíos, 0,8% menos que en el año 2021. El 53.2% correspondieron a envíos masivos y el 46.8% restante a envíos individuales.</li>
                    <li>En materia de ingresos, en 2022 la prestación de este servicio percibió 1.74 billones de pesos, 4,9% más que en 2021 en términos reales. Discriminando por tipo de envío, los envíos individuales acumularon un total de 1.59 mil millones de pesos, aumentando un 7,1% frente a 2021 en términos constantes. Por ámbito, los envíos nacionales representaron el 74,3% de los ingresos, seguido del ámbito local en 13,7%.</li>
                    </ul>""",unsafe_allow_html=True)

            ServiciosCorreo=st.selectbox('Escoja el ámbito de Correo',['Número de envíos','Ingresos'])
            ##Número de envíos e ingresos
            IngresosyEnviosMExpresa=IngresosyEnviosMExpresa.merge(IPCTrimTot, left_on=['anno','trimestre','periodo'],right_on=['anno','trimestre','periodo'])
            IngresosyEnviosMExpresa['Ingresos']=IngresosyEnviosMExpresa['Ingresos']/IngresosyEnviosMExpresa['indice2022']
            IngresosyEnviosMexpresaNac=IngresosyEnviosMExpresa.groupby(['anno','ambito','tipo_envio']).agg({'Envíos':'sum','Ingresos':'sum'}).reset_index()
            IngresosyEnviosMexpresaEMp=IngresosyEnviosMExpresa.groupby(['anno','id_empresa','empresa']).agg({'Envíos':'sum','Ingresos':'sum'}).reset_index()    
            EmpMensExpNumEnv=IngresosyEnviosMexpresaEMp[IngresosyEnviosMexpresaEMp['anno']=='2022'].sort_values(by='Envíos',ascending=False)['id_empresa'].to_list()[0:4]
            EmpMensExpIng=IngresosyEnviosMexpresaEMp[IngresosyEnviosMexpresaEMp['anno']=='2022'].sort_values(by='Ingresos',ascending=False)['id_empresa'].to_list()[0:4]
            IngresosyEnviosMexpresaEMpEnv=IngresosyEnviosMexpresaEMp[(IngresosyEnviosMexpresaEMp['id_empresa'].isin(EmpMensExpNumEnv))&(IngresosyEnviosMexpresaEMp['anno'].isin(['2021','2022']))]
            IngresosyEnviosMexpresaEMpIng=IngresosyEnviosMexpresaEMp[(IngresosyEnviosMexpresaEMp['id_empresa'].isin(EmpMensExpIng))&(IngresosyEnviosMexpresaEMp['anno'].isin(['2021','2022']))]
            IngresosMenExpEmp=IngresosyEnviosMExpresa[IngresosyEnviosMExpresa['anno']=='2022'].groupby(['tipo_envio','id_empresa','empresa']).agg({'Ingresos':'sum'}).reset_index()   
            #
            IngresosMenExpEmpInd=IngresosMenExpEmp[IngresosMenExpEmp['tipo_envio']=='Individuales']
            IngresosMenExpEmpInd['participacion']=round(100*IngresosMenExpEmpInd['Ingresos']/IngresosMenExpEmpInd['Ingresos'].sum(),1)
            IngresosMenExpEmpInd.loc[IngresosMenExpEmpInd['participacion']<=5,'empresa']='Otros'
            IngresosMenExpEmpInd['empresa']=IngresosMenExpEmpInd['empresa'].replace(nombresComerciales)
            IngresosMenExpEmpMas=IngresosMenExpEmp[IngresosMenExpEmp['tipo_envio']=='Masivos']
            IngresosMenExpEmpMas['participacion']=round(100*IngresosMenExpEmpMas['Ingresos']/IngresosMenExpEmpMas['Ingresos'].sum(),1)
            IngresosMenExpEmpMas.loc[IngresosMenExpEmpMas['participacion']<=5,'empresa']='Otros'
            IngresosMenExpEmpMas['empresa']=IngresosMenExpEmpMas['empresa'].replace(nombresComerciales)
            
            if ServiciosCorreo=='Número de envíos':
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoEnviosMenExpresa=st.button('Evolución temporal')
                with col2:
                    BarrasEnviosMenExpresa=st.button('Información por operadores')
                
                if LineaTiempoEnviosMenExpresa:
                    st.plotly_chart(PlotyMultiIndexBarra(IngresosyEnviosMexpresaNac,'Envíos','Millones','<b>Número de envíos por tipo de envío y ámbito</b>',1e6,'<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)
                
                if BarrasEnviosMenExpresa:
                   st.plotly_chart(PlotlyBarras(IngresosyEnviosMexpresaEMpEnv,'Envíos','Millones',1e6,'<b>Envíos anuales por empresa</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True) 
                    
            if ServiciosCorreo=='Ingresos':
                st.markdown("""<center><p style="font-size:12px"><b>Nota:</b> Ingresos ajustados por inflación, usando el IPC total. Periodo base, diciembre 2022</p></center>""",unsafe_allow_html=True)
                col1,col2,col3=st.columns(3)
                with col1:
                    LineaTiempoIngresosMenExpresa=st.button('Evolución temporal')
                with col2:
                    BarrasIngresosMenExpresa=st.button('Información por operadores')  
                with col3:
                    PieIngresosMenExpresa=st.button('Participaciones')
                
                if LineaTiempoIngresosMenExpresa:    
                    st.plotly_chart(PlotyMultiIndexBarra(IngresosyEnviosMexpresaNac,'Ingresos','Miles de Millones de pesos','<b>Ingresos por tipo de envío y ámbito</b>',1e9,'<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)
                if BarrasIngresosMenExpresa:
                    st.plotly_chart(PlotlyBarras(IngresosyEnviosMexpresaEMpIng,'Ingresos','Millones',1e6,'<b>Ingresos anuales por empresa</b>','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True) 
                if PieIngresosMenExpresa:
                    col1,col2=st.columns(2)
                    figPieMenExpInd = px.pie(IngresosMenExpEmpInd, values='Ingresos', names='empresa', color='empresa',
                                 color_discrete_map=Colores_pie3, title='<b>Participación en ingresos de<br>mensajería expresa individual (2022)')
                    figPieMenExpInd.update_traces(textposition='inside',textinfo='percent',hoverinfo='label+percent',textfont_color='black')
                    figPieMenExpInd.update_layout(uniformtext_minsize=18,uniformtext_mode='hide',showlegend=True,legend=dict(x=0.2,y=-0.1,orientation='h'),title_x=0.5)
                    figPieMenExpInd.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20)
                    with col1:
                        st.plotly_chart(figPieMenExpInd,use_container_width=True)

                    figPieMenExpMas = px.pie(IngresosMenExpEmpMas, values='Ingresos', names='empresa', color='empresa',
                                 color_discrete_map=Colores_pie3, title='<b>Participación en ingresos de<br>mensajería expresa masivos (2022)')
                    figPieMenExpMas.update_traces(textposition='inside',textinfo='percent',hoverinfo='label+percent',textfont_color='black')
                    figPieMenExpMas.update_layout(uniformtext_minsize=18,uniformtext_mode='hide',showlegend=True,legend=dict(x=0.1,y=-0.1,orientation='h'),title_x=0.5)
                    figPieMenExpMas.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20)
                    with col2:
                        st.plotly_chart(figPieMenExpMas,use_container_width=True)  
                    st.markdown("<center><p style='font-size:11px'><b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC</p></center>",unsafe_allow_html=True)            

        if select_DinPos=='Giros':
            

            col1,col2=st.columns(2)
            with col1:
                st.markdown(r"""<div class='IconoTitulo'><img height="200px" src='https://github.com/postdatacrc/Reporte-de-industria/blob/main/2023/Iconos/giros.png?raw=true'/><h4>Giros</h4></div>""",unsafe_allow_html=True)  
            with col2:             
                with st.expander("Datos relevantes de Giros"):
                    st.markdown(r"""<ul>
                    <li>Los operadores de los servicios postales de pago movilizaron un total de 18,3 billones de pesos en 2022 en 106,1 millones de giros. El valor de los giros así como el número de envíos redujeron anualmente a tasas (real) de 19,8% y 5,3% respectivamente</li>
                    <li>Por la prestación de este servicio, los operadores recibieron ingresos de 572,1 mil millones, 27,72% menos que en 2021 en términos reales. Los giros nacionales representaron el 99,3% del total de ingresos.</li>
                    <li>En 2022, en promedio por cada giro lo operadores tuvieron ingresos de $5.450, siendo menores en 2,8% a los obtenidos en 2021.</li>
                    </ul>""",unsafe_allow_html=True)
            
            ServiciosGiros=st.selectbox('Escoja el ámbito de Giros',['Ingresos','Número de giros','Ingresos por número de giros'])
            
            IngresosGiros=IngresosGiros.rename(columns={'sum_numero_giros':'Giros'})
            IngresosGiros=IngresosGiros.merge(IPCTrimTot, left_on=['anno','trimestre','periodo'],right_on=['anno','trimestre','periodo'])
            IngresosGiros['Ingresos']=IngresosGiros['Ingresos']/IngresosGiros['indice2022']            
            ##Ingresos
            IngresosGirosNac=IngresosGiros.groupby(['anno','ambito','tipo_giro']).agg({'Ingresos':'sum','Valor total giros':'sum'}).reset_index()
            IngresosGirosNac=IngresosGirosNac.rename(columns={'tipo_giro':'tipo_envio'})
            #
            IngresosGirosEmp=IngresosGiros.groupby(['anno','empresa','id_empresa']).agg({'Ingresos':'sum'}).reset_index()
            EmpGirosIng=IngresosGirosEmp[IngresosGirosEmp['anno']=='2022'].sort_values(by='Ingresos',ascending=False)['id_empresa'].to_list()[0:4]
            IngresosGirosEmp=IngresosGirosEmp[(IngresosGirosEmp['anno'].isin(['2021','2022']))&(IngresosGirosEmp['id_empresa'].isin(EmpGirosIng))]
            #
            IngresosGirosPie=IngresosGiros[(IngresosGiros['tipo_giro']=='Nacionales')&(IngresosGiros['anno']=='2022')].groupby(['id_empresa','empresa']).agg({'Ingresos':'sum','Valor total giros':'sum'}).reset_index()
            IngresosGirosPie['participacion']=round(100*IngresosGirosPie['Ingresos']/IngresosGirosPie['Ingresos'].sum(),3)
            IngresosGirosPie['participacion_2']=round(100*IngresosGirosPie['Valor total giros']/IngresosGirosPie['Valor total giros'].sum(),3)
            IngresosGirosPie['empresa']=IngresosGirosPie['empresa'].replace(nombresComerciales) 
            #Ingresos por valor de giro
            IngresosPorValorGiroEmp=IngresosGiros[IngresosGiros['ambito']=='Nacional'].groupby(['periodo','empresa','id_empresa']).agg({'Ingresos':'sum','Valor total giros':'sum'}).reset_index()
            IngresosPorValorGiroEmp['Tasa media de comisión']=round(100*IngresosPorValorGiroEmp['Ingresos']/IngresosPorValorGiroEmp['Valor total giros'],3)
            ##Giros
            NumeroGirosNac=IngresosGiros.groupby(['anno','ambito','tipo_giro']).agg({'Giros':'sum'}).reset_index()
            NumeroGirosNac=NumeroGirosNac.rename(columns={'tipo_giro':'tipo_envio'})
            #
            NumeroGirosEmp=IngresosGiros.groupby(['anno','empresa','id_empresa']).agg({'Giros':'sum'}).reset_index()
            EmpGirosNum=NumeroGirosEmp[NumeroGirosEmp['anno']=='2022'].sort_values(by='Giros',ascending=False)['id_empresa'].to_list()[0:4]
            NumeroGirosEmp=NumeroGirosEmp[(NumeroGirosEmp['anno'].isin(['2021','2022']))&(NumeroGirosEmp['id_empresa'].isin(EmpGirosNum))]
            #
            NumeroGirosPie=IngresosGiros[(IngresosGiros['tipo_giro']=='Nacionales')&(IngresosGiros['anno']=='2022')].groupby(['id_empresa','empresa']).agg({'Giros':'sum'}).reset_index()
            NumeroGirosPie['participacion']=round(100*NumeroGirosPie['Giros']/NumeroGirosPie['Giros'].sum(),3)
            NumeroGirosPie['empresa']=NumeroGirosPie['empresa'].replace(nombresComerciales)         

            #Ingresos por número de giros 
            IngresosGiros2=IngresosGiros.groupby(['anno','ambito','tipo_giro']).agg({'Ingresos':'sum','Valor total giros':'sum'}).reset_index()
            
            if ServiciosGiros=='Ingresos':
                st.markdown("""<center><p style="font-size:12px"><b>Nota:</b> Ingresos ajustados por inflación, usando el IPC total. Periodo base, diciembre 2022</p></center>""",unsafe_allow_html=True)
                st.markdown('')
                col1,col2,col3=st.columns(3)
                with col1:
                    LineaTiempoIngresosGiros=st.button('Evolución temporal')
                with col2:
                    BarrasIngresosGiros=st.button('Información por operadores')  
                with col3:
                    PieIngresosGiros=st.button('Participaciones')
                    
                if LineaTiempoIngresosGiros:
                    col1,col2=st.columns(2)                               
                    with col1:
                        st.plotly_chart(PlotlyBarras2(IngresosGirosNac[IngresosGirosNac['tipo_envio']=='Nacionales'],'Ingresos','ambito','Miles de Millones de pesos',1e9,'<b>Ingresos de giros nacionales</b>',['rgb(122, 68, 242)'],''),use_container_width=True)
                    with col2:    
                        st.plotly_chart(PlotlyBarras2(IngresosGirosNac[IngresosGirosNac['tipo_envio']=='Internacionales'],'Ingresos','ambito','Millones de pesos',1e6,'<b>Ingresos de giros internacionales<br>por ámbito</b>',['rgb(0, 128, 255)','rgb(102,204,0)'],''),use_container_width=True)
                    
                    st.markdown("<center><p style='font-size:11px'><b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC</p></center>",unsafe_allow_html=True)            

                if BarrasIngresosGiros:
                    st.plotly_chart(PlotlyBarras(IngresosGirosEmp,'Ingresos','Miles de Millones de pesos',1e9,'Ingresos anuales por empresa','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)
                    IngresosPorValorGiroEmp['periodo_formato']=IngresosPorValorGiroEmp['periodo'].apply(periodoformato)
                    #st.plotly_chart(PlotlylineatiempoEmp(IngresosPorValorGiroEmp,'Tasa media de comisión','Porcentaje',['rgb(255,213,30)','rgb(153,255,51)','rgb(255,0,127)','rgb(0,0,255)','rgb(0,102,204)'],'Tasa media de comisión de ámbito nacional','<b>Fuente</b>:Elaboración CRC con base en los reportes de información al sistema Colombia TIC'), use_container_width=True)
                
                if PieIngresosGiros:
                    figPieGirIng = px.pie(IngresosGirosPie, values='Ingresos', names='empresa', color='empresa',
                                 color_discrete_map=Colores_pie3, title='<b>Participación en ingresos de giros<br>(2022)')
                    figPieGirIng.update_traces(textposition='inside',textinfo='percent',hoverinfo='label+percent',textfont_color='black')
                    figPieGirIng.update_layout(uniformtext_minsize=18,uniformtext_mode='hide',showlegend=True,legend=dict(xanchor='center',x=0.5,y=-0.1,orientation='h'),title_x=0.5)
                    figPieGirIng.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20)
                    #
                    figPieGirValorGiro = px.pie(IngresosGirosPie, values='Valor total giros', names='empresa', color='empresa',
                     color_discrete_map=Colores_pie3, title='<b>Participación en el valor<br>total de giros (2022)')
                    figPieGirValorGiro.update_traces(textposition='inside',textinfo='percent',hoverinfo='label+percent',textfont_color='black')
                    figPieGirValorGiro.update_layout(uniformtext_minsize=18,uniformtext_mode='hide',showlegend=True,legend=dict(xanchor='center',x=0.5,y=-0.1,orientation='h'),title_x=0.5)
                    figPieGirValorGiro.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20)
                    col1,col2=st.columns(2)
                    with col1:
                        st.plotly_chart(figPieGirIng,use_container_width=True) 
                    with col2:
                        st.plotly_chart(figPieGirValorGiro,use_container_width=True)                  
                    st.markdown("<center><p style='font-size:11px'><b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC</p></center>",unsafe_allow_html=True)            
                        
            if ServiciosGiros=='Número de giros':
                st.markdown('')
                col1,col2,col3=st.columns(3)
                with col1:
                    LineaTiempoNGiros=st.button('Evolución temporal')
                with col2:
                    BarrasNGiros=st.button('Información por operadores')  
                with col3:
                    PieNGiros=st.button('Participaciones')                    
                    
                if LineaTiempoNGiros:
                    col1,col2=st.columns(2)                               
                    with col1:
                        st.plotly_chart(PlotlyBarras2(NumeroGirosNac[NumeroGirosNac['tipo_envio']=='Nacionales'],'Giros','ambito','Millones',1e6,'<b>Número de giros nacionales</b>',['rgb(122, 68, 242)'],''),use_container_width=True)
                    with col2:    
                        st.plotly_chart(PlotlyBarras2(NumeroGirosNac[NumeroGirosNac['tipo_envio']=='Internacionales'],'Giros','ambito','Miles',1e3,'<b>Número de giros internacionales<br>por ámbito</b>',['rgb(0, 128, 255)','rgb(102,204,0)'],''),use_container_width=True)
                    st.markdown("<center><p style='font-size:11px'><b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC</p></center>",unsafe_allow_html=True)            

                if BarrasNGiros:
                    st.plotly_chart(PlotlyBarras(NumeroGirosEmp,'Giros','Millones',1e6,'Número de giros anuales por empresa','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)

                if PieNGiros:
                    figPieGirNum = px.pie(NumeroGirosPie, values='Giros', names='empresa', color='empresa',
                     color_discrete_map=Colores_pie3, title='<b>Participación en número de giros<br>(2022)')
                    figPieGirNum.update_traces(textposition='inside',textinfo='percent',hoverinfo='label+percent',textfont_color='black')
                    figPieGirNum.update_layout(uniformtext_minsize=18,uniformtext_mode='hide',showlegend=True,legend=dict(xanchor='center',x=0.5,y=-0.1,orientation='h'),title_x=0.5)
                    figPieGirNum.update_layout(font_color="Black",font_family="Poppins",title_font_color="Black",titlefont_size=20)
                    st.plotly_chart(figPieGirNum,use_container_width=True)
                    st.markdown("<center><p style='font-size:11px'><b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC</p></center>",unsafe_allow_html=True)            
                    
            if ServiciosGiros=='Ingresos por número de giros':
                st.markdown("""<center><p style="font-size:12px"><b>Nota:</b> Ingresos ajustados por inflación, usando el IPC total. Periodo base, diciembre 2022</p></center>""",unsafe_allow_html=True)
                IngresosPorNGirosNac=IngresosGirosNac.merge(NumeroGirosNac,left_on=['anno','ambito','tipo_envio'],right_on=['anno','ambito','tipo_envio'])
                IngresosPorNGirosNac['Ingresos/Giros']=round(IngresosPorNGirosNac['Ingresos']/IngresosPorNGirosNac['Giros'],3)
                IngresosporGirosEmp=IngresosGiros[IngresosGiros['periodo'].isin(['2021-T4','2022-T4'])]
                IngresosporGirosEmp=IngresosporGirosEmp.groupby(['periodo','empresa','id_empresa']).agg({'Ingresos':'sum','Giros':'sum'}).reset_index()
                IngresosporGirosEmp['Ingresos/Giros']=round(IngresosporGirosEmp['Ingresos']/IngresosporGirosEmp['Giros'],3)
                IngresosporGirosEmp=IngresosporGirosEmp.rename(columns={'periodo':'anno'})
                
                
                col1,col2=st.columns(2)
                with col1:
                    LineaTiempoIngNGiros=st.button('Evolución temporal')
                with col2:
                    BarrasIngNGiros=st.button('Información por operadores')  
                
                if LineaTiempoIngNGiros:
                    col1,col2=st.columns(2)                               
                    with col1:
                        st.plotly_chart(PlotlyBarras2(IngresosPorNGirosNac[IngresosPorNGirosNac['tipo_envio']=='Nacionales'],'Ingresos/Giros','ambito','Pesos',1,'<b>Ingresos por giros (nacionales)</b>',['rgb(122, 68, 242)'],''),use_container_width=True)
                    with col2:    
                        st.plotly_chart(PlotlyBarras2(IngresosPorNGirosNac[IngresosPorNGirosNac['tipo_envio']=='Internacionales'],'Ingresos/Giros','ambito','Pesos',1,'<b>Ingresos por giros (internacionales)<br>por ámbito</b>',['rgb(0, 128, 255)','rgb(102,204,0)'],''),use_container_width=True)
                    st.markdown("<center><p style='font-size:11px'><b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC</p></center>",unsafe_allow_html=True)            

                if BarrasIngNGiros:
                    st.plotly_chart(PlotlyBarras(IngresosporGirosEmp,'Ingresos/Giros','Pesos',1,'Ingresos por giros por empresa','<b>Fuente</b>: Elaboración CRC con base en los reportes de información al sistema Colombia TIC'),use_container_width=True)