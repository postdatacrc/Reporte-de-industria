import pandas as pd
import numpy as np
import glob
import os
from urllib.request import urlopen
import json

########################################################### Telefonía Móvil

## Abonados
def ReadApiTelMovilAbonados():
    resourceid = '3a9c0304-3795-4c55-a78e-079362373b4d'
    consulta='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid + ''\
             '&filters[anno]=' + '2018,2019,2020,2021' + ''\
             '&fields[]=anno&fields[]=trimestre&fields[]=id_proveedor&fields[]=proveedor&fields[]=modalidad'\
             '&group_by=anno,trimestre,modalidad,id_proveedor,proveedor'\
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
             '&filters[anno]=' + '2018,2019,2020,2021' + ''\
             '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa&fields[]=tipo_trafico'\
             '&group_by=anno,trimestre,tipo_trafico,id_empresa,empresa'\
             '&sum=trafico' 
    response_base = urlopen(consulta + '&limit=10000000') 
    json_base = json.loads(response_base.read())
    VOZ_TRAF = pd.DataFrame(json_base['result']['records'])
    VOZ_TRAF.sum_trafico = VOZ_TRAF.sum_trafico.astype('int64')
    VOZ_TRAF = VOZ_TRAF.rename(columns={'sum_trafico':'trafico'})
    return VOZ_TRAF
TraficoTelMovil=ReadApiTelMovilTrafico()

## Ingresos
def ReadApiTelMovilIngresos():
    resourceid = '43f0d3a9-cd5c-4f22-a996-74eae6cba9a3'
    consulta='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid + ''\
             '&filters[anno]=' + '2018,2019,2020,2021' + ''\
             '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
             '&group_by=anno,trimestre,id_empresa,empresa'\
             '&sum[]=ingresos_totales&sum[]=ingresos_prepago&sum[]=ingresos_pospago'
    response_base = urlopen(consulta + '&limit=10000000') 
    json_base = json.loads(response_base.read())
    VOZ_ING = pd.DataFrame(json_base['result']['records'])
    VOZ_ING.sum_ingresos_totales = VOZ_ING.sum_ingresos_totales.astype('int64')
    VOZ_ING = VOZ_ING.rename(columns={'sum_ingresos_totales':'ingresos_totales','sum_ingresos_pospago':'ingresos_pospago','sum_ingresos_prepago':'ingresos_prepago'})
    return VOZ_ING
IngresosTelMovil=ReadApiTelMovilIngresos()

## TraficoSMS
def ReadApiTelMovilTraficoSMS():
    resourceid = '8a0fcc94-a241-47ce-8245-569e54a22fd4'
    consulta='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid + ''\
             '&filters[anno]=' + '2018,2019,2020,2021' + ''\
             '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
             '&group_by=anno,trimestre,id_empresa,empresa'\
             '&sum=cantidad' 
    response_base = urlopen(consulta + '&limit=10000000') 
    json_base = json.loads(response_base.read())
    VOZ_TRAF = pd.DataFrame(json_base['result']['records'])
    VOZ_TRAF.sum_cantidad = VOZ_TRAF.sum_cantidad.astype('int64')
    VOZ_TRAF = VOZ_TRAF.rename(columns={'sum_cantidad':'cantidad'})
    return VOZ_TRAF
TraficoSMSTelMovil=ReadApiTelMovilTraficoSMS()

## IngresosSMS

def ReadApiTelMovilIngresosSMS():
    resourceid = 'aff5be3b-9a52-4777-956b-14094a265df2'
    consulta='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid + ''\
             '&filters[anno]=' + '2018,2019,2020,2021' + ''\
             '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
             '&group_by=anno,trimestre,id_empresa,empresa'\
             '&sum=ingresos' 
    response_base = urlopen(consulta + '&limit=10000000') 
    json_base = json.loads(response_base.read())
    VOZ_TRAF = pd.DataFrame(json_base['result']['records'])
    VOZ_TRAF.sum_ingresos = VOZ_TRAF.sum_ingresos.astype('int64')
    VOZ_TRAF = VOZ_TRAF.rename(columns={'sum_ingresos':'ingresos'})
    return VOZ_TRAF
IngresosSMSTelMovil=ReadApiTelMovilIngresosSMS()

########################################################### Internet móvil

## Accesos
def ReadApiIMAccesos():
    resourceid_cf = '47d07e20-b257-4aaf-9309-1501c75a826c'
    consulta_cf='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid_cf + ''\
                '&filters[anno]=' + '2018,2019,2020,2021' + ''+'&filters[mes_del_trimestre]=3'\
                '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
                '&group_by=anno,trimestre,id_empresa,empresa'\
                '&sum=cantidad_suscriptores' 
    response_base_cf = urlopen(consulta_cf + '&limit=10000000') 
    json_base_cf = json.loads(response_base_cf.read())
    IMCF_SUS = pd.DataFrame(json_base_cf['result']['records'])
    IMCF_SUS.sum_cantidad_suscriptores = IMCF_SUS.sum_cantidad_suscriptores.astype('int64')
    resourceid_dda = '3df620f6-deec-42a0-a6af-44ca23c2b73c'
    consulta_dda='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid_dda + ''\
                '&filters[anno]=' + '2018,2019,2020,2021' + ''+'&filters[mes_del_trimestre]=3'\
                '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
                '&group_by=anno,trimestre,id_empresa,empresa'\
                '&sum=cantidad_abonados' 
    response_base_dda = urlopen(consulta_dda + '&limit=10000000') 
    json_base_dda = json.loads(response_base_dda.read())
    IMDDA_ABO = pd.DataFrame(json_base_dda['result']['records'])
    IMDDA_ABO.sum_cantidad_abonados = IMDDA_ABO.sum_cantidad_abonados.astype('int64')
    IM_ACCESOS=IMDDA_ABO.merge(IMCF_SUS, on=['anno','trimestre','id_empresa','empresa'])
    IM_ACCESOS['accesos']=IM_ACCESOS['sum_cantidad_suscriptores'].fillna(0)+IM_ACCESOS['sum_cantidad_abonados']
    #IM_ACCESOS.drop(columns=['sum_cantidad_suscriptores','sum_cantidad_abonados'], inplace=True)
    return IM_ACCESOS
AccesosInternetmovil=ReadApiIMAccesos()
##Ingresos

def ReadApiIMIng():
    resourceid_cf = '8366e39c-6a14-483a-80f4-7278ceb39f88'
    consulta_cf='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid_cf + ''\
                '&filters[anno]=' + '2018,2019,2020,2021' + ''\
                '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
                '&group_by=anno,trimestre,id_empresa,empresa'\
                '&sum=ingresos' 
    response_base_cf = urlopen(consulta_cf + '&limit=10000000') 
    json_base_cf = json.loads(response_base_cf.read())
    IMCF_ING = pd.DataFrame(json_base_cf['result']['records'])
    IMCF_ING.sum_ingresos = IMCF_ING.sum_ingresos.astype('int64')
    IMCF_ING=IMCF_ING.rename(columns={'sum_ingresos':'CARGO FIJO'})
    resourceid_dda = '60a55889-ba71-45ff-b68f-33b503da36f2'
    consulta_dda='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid_dda + ''\
                '&filters[anno]=' + '2018,2019,2020,2021' + ''\
                '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
                '&group_by=anno,trimestre,id_empresa,empresa'\
                '&sum=ingresos' 
    response_base_dda = urlopen(consulta_dda + '&limit=10000000') 
    json_base_dda = json.loads(response_base_dda.read())
    IMDDA_ING = pd.DataFrame(json_base_dda['result']['records'])
    IMDDA_ING.sum_ingresos = IMDDA_ING.sum_ingresos.astype('int64')
    IMDDA_ING=IMDDA_ING.rename(columns={'sum_ingresos':'DEMANDA'})
    IM_ING=IMDDA_ING.merge(IMCF_ING, on=['anno','trimestre','id_empresa','empresa'])
    IM_ING['ingresos']=IM_ING['CARGO FIJO'].fillna(0)+IM_ING['DEMANDA']
    #IM_ING.drop(columns=['sum_ingresos_y','sum_ingresos_x'], inplace=True)
    return IM_ING
IngresosInternetmovil=ReadApiIMIng()

##Tráfico

def ReadApiIMTraf():
    resourceid_cf = 'd40c5e75-db56-4ec1-a441-0314c47bd71d'
    consulta_cf='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid_cf + ''\
                '&filters[anno]=' + '2018,2019,2020,2021' + ''\
                '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
                '&group_by=anno,trimestre,id_empresa,empresa'\
                '&sum=trafico' 
    response_base_cf = urlopen(consulta_cf + '&limit=10000000') 
    json_base_cf = json.loads(response_base_cf.read())
    IMCF_TRAF = pd.DataFrame(json_base_cf['result']['records'])
    IMCF_TRAF.sum_trafico = IMCF_TRAF.sum_trafico.astype('int64')
    IMCF_TRAF=IMCF_TRAF.rename(columns={'sum_trafico':'trafico cargo fijo'})
    resourceid_dda = 'c0be7034-29f8-4400-be54-c4aafe5df606'
    consulta_dda='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid_dda + ''\
                '&filters[anno]=' + '2018,2019,2020,2021' + ''\
                '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
                '&group_by=anno,trimestre,id_empresa,empresa'\
                '&sum=trafico' 
    response_base_dda = urlopen(consulta_dda + '&limit=10000000') 
    json_base_dda = json.loads(response_base_dda.read())
    IMDDA_TRAF = pd.DataFrame(json_base_dda['result']['records'])
    IMDDA_TRAF.sum_trafico = IMDDA_TRAF.sum_trafico.astype('int64')
    IMDDA_TRAF=IMDDA_TRAF.rename(columns={'sum_trafico':'trafico demanda'})
    IM_TRAF=IMDDA_TRAF.merge(IMCF_TRAF, on=['anno','trimestre','id_empresa','empresa'])
    IM_TRAF['trafico']=IM_TRAF['trafico cargo fijo'].fillna(0)+IM_TRAF['trafico demanda']
    #IM_TRAF.drop(columns=['sum_trafico_y','sum_trafico_x'], inplace=True)
    return IM_TRAF
TraficoInternetMovil=ReadApiIMTraf()

########################################################### Internet fijo

## Accesos Corporativos
def ReadApiINTFAccesosCorp():
    consulta_anno='2018','2019','2020','2021'
    resourceid = '540ea080-bf16-4d63-911f-3b4814e8e4f1'
    INTF_ACCESOS = pd.DataFrame()
    for anno in consulta_anno:
        consulta='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid + ''\
                 '&filters[id_segmento]=107,108&filters[anno]=' + anno + ''\
                 '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa&fields[]=id_tecnologia&fields[]=tecnologia'\
                 '&group_by=anno,trimestre,id_empresa,empresa,id_tecnologia,tecnologia'\
                 '&sum=accesos' 
        response_base = urlopen(consulta + '&limit=10000000') 
        json_base = json.loads(response_base.read())
        ACCESOS = pd.DataFrame(json_base['result']['records'])
        INTF_ACCESOS = INTF_ACCESOS.append(ACCESOS)
    INTF_ACCESOS.sum_accesos = INTF_ACCESOS.sum_accesos.astype('int64')
    INTF_ACCESOS = INTF_ACCESOS.rename(columns={'sum_accesos':'accesos'})
    return INTF_ACCESOS
AccesosCorpIntFijo=ReadApiINTFAccesosCorp()
## Accesos Residenciales
def ReadApiINTFAccesosRes():
    consulta_anno='2018','2019','2020','2021'
    resourceid = '540ea080-bf16-4d63-911f-3b4814e8e4f1'
    INTF_ACCESOS = pd.DataFrame()
    for anno in consulta_anno:
        consulta='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid + ''\
                 '&filters[id_segmento]=101,102,103,104,105,106&filters[anno]=' + anno + ''\
                 '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa&fields[]=id_tecnologia&fields[]=tecnologia'\
                 '&group_by=anno,trimestre,id_empresa,empresa,id_tecnologia,tecnologia'\
                 '&sum=accesos' 
        response_base = urlopen(consulta + '&limit=10000000') 
        json_base = json.loads(response_base.read())
        ACCESOS = pd.DataFrame(json_base['result']['records'])
        INTF_ACCESOS = INTF_ACCESOS.append(ACCESOS)
    INTF_ACCESOS.sum_accesos = INTF_ACCESOS.sum_accesos.astype('int64')
    INTF_ACCESOS = INTF_ACCESOS.rename(columns={'sum_accesos':'accesos'})
    return INTF_ACCESOS
AccesosResIntFijo=ReadApiINTFAccesosRes()    
## Ingresos
def ReadApiINTFIng():
    resourceid = 'd917a68d-9cb9-4257-82f1-74115a4cf629'
    consulta_anno='2018,2019,2020,2021'
    consulta='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid + ''\
             '&filters[anno]=' + consulta_anno + ''\
             '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
             '&group_by=anno,trimestre,id_empresa,empresa'\
             '&sum=ingresos' 
    response_base = urlopen(consulta + '&limit=10000000') 
    json_base = json.loads(response_base.read())
    INTF_ING = pd.DataFrame(json_base['result']['records'])
    INTF_ING.sum_ingresos = INTF_ING.sum_ingresos.astype('int64')
    INTF_ING = INTF_ING.rename(columns={'sum_ingresos':'ingresos'})
    return INTF_ING
IngresosInternetFijo=ReadApiINTFIng()