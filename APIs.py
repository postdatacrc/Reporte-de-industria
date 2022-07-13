import pandas as pd
import numpy as np
import glob
import os
from urllib.request import urlopen
import json

####Telefonía Móvil

## Abonados
def ReadApiTelMovilAbonados():
    resourceid = '3a9c0304-3795-4c55-a78e-079362373b4d'
    consulta='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid + ''\
             '&filters[anno]=' + '2020,2021' + ''\
             '&fields[]=anno&fields[]=trimestre&fields[]=id_proveedor&fields[]=proveedor'\
             '&group_by=anno,trimestre,id_proveedor,proveedor'\
             '&sum=abonados' 
    response_base = urlopen(consulta + '&limit=10000000') 
    json_base = json.loads(response_base.read())
    VOZ_ABO = pd.DataFrame(json_base['result']['records'])
    VOZ_ABO.sum_abonados = VOZ_ABO.sum_abonados.astype('int64')
    VOZ_ABO = VOZ_ABO.rename(columns={'id_proveedor':'id_empresa','proveedor':'empresa','sum_abonados':'abonados'})
    return VOZ_ABO
AbonadosTelMovil=ReadApiTelMovilAbonados()

## Tráfico
def ReadApiTelMovilTrafico():
    resourceid = '1384a4d4-42d7-4930-b43c-bf9768c47ccb'
    consulta='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid + ''\
             '&filters[anno]=' + '2020,2021' + ''\
             '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
             '&group_by=anno,trimestre,id_empresa,empresa'\
             '&sum=trafico' 
    response_base = urlopen(consulta + '&limit=10000000') 
    json_base = json.loads(response_base.read())
    VOZ_TRAF = pd.DataFrame(json_base['result']['records'])
    VOZ_TRAF.sum_trafico = VOZ_TRAF.sum_trafico.astype('int64')
    VOZ_TRAF = VOZ_TRAF.rename(columns={'sum_trafico':'trafico'})
    return VOZ_TRAF
TraficoTelMovil=ReadApiTelMovilTrafico()

