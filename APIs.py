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

########################################################### Mensajería Móvil

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

def ReadApiTelMovilTraficoCodigosCortos():
    resourceid = '7c2910ca-29d4-4ee3-99ae-4fc2f09eeb86'
    consulta='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid + ''\
             '&filters[anno]=' + '2018,2019,2020,2021' + ''\
             '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
             '&group_by=anno,trimestre,id_empresa,empresa'\
             '&sum[]=trafico_terminado&sum[]=trafico_originado' 
    response_base = urlopen(consulta + '&limit=10000000') 
    json_base = json.loads(response_base.read())
    VOZ_TRAF = pd.DataFrame(json_base['result']['records'])
    VOZ_TRAF.sum_trafico_terminado = VOZ_TRAF.sum_trafico_terminado.astype('int64')
    VOZ_TRAF.sum_trafico_originado = VOZ_TRAF.sum_trafico_originado.astype('int64')
    VOZ_TRAF = VOZ_TRAF.rename(columns={'sum_trafico_terminado':'trafico terminado','sum_trafico_originado':'trafico originado'})
    VOZ_TRAF['periodo']=VOZ_TRAF['anno']+'-T'+VOZ_TRAF['trimestre']
    return VOZ_TRAF
TraficoSMSCodigosCortos=ReadApiTelMovilTraficoCodigosCortos()

def ReadApiTelMovilIngresosCodigosCortos():
    resourceid = '2c9bba15-a735-41c0-9068-7bb8d280ee99'
    consulta='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid + ''\
             '&filters[anno]=' + '2018,2019,2020,2021' + ''\
             '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
             '&group_by=anno,trimestre,id_empresa,empresa'\
             '&sum[]=ingresos_sms' 
    response_base = urlopen(consulta + '&limit=10000000') 
    json_base = json.loads(response_base.read())
    VOZ_ING = pd.DataFrame(json_base['result']['records'])
    VOZ_ING.sum_ingresos_sms = VOZ_ING.sum_ingresos_sms.astype('int64')
    VOZ_ING = VOZ_ING.rename(columns={'sum_ingresos_sms':'ingresos'})
    VOZ_ING['periodo']=VOZ_ING['anno']+'-T'+VOZ_ING['trimestre']
    return VOZ_ING
IngresosSMSCodigosCortos=ReadApiTelMovilIngresosCodigosCortos()

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
    IMCF_SUS['modalidad']='Cargo Fijo'
    IMCF_SUS.sum_cantidad_suscriptores = IMCF_SUS.sum_cantidad_suscriptores.astype('int64')
    IMCF_SUS=IMCF_SUS.rename(columns={'sum_cantidad_suscriptores':'accesos'})
    resourceid_dda = '3df620f6-deec-42a0-a6af-44ca23c2b73c'
    consulta_dda='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid_dda + ''\
                '&filters[anno]=' + '2017,2018,2019,2020,2021,2022,2023,2024,2025' + ''+'&filters[mes_del_trimestre]=3'\
                '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
                '&group_by=anno,trimestre,id_empresa,empresa'\
                '&sum=cantidad_abonados' 
    response_base_dda = urlopen(consulta_dda + '&limit=10000000') 
    json_base_dda = json.loads(response_base_dda.read())
    IMDDA_ABO = pd.DataFrame(json_base_dda['result']['records'])
    IMDDA_ABO.sum_cantidad_abonados = IMDDA_ABO.sum_cantidad_abonados.astype('int64')
    IMDDA_ABO['modalidad']='Demanda'
    IMDDA_ABO=IMDDA_ABO.rename(columns={'sum_cantidad_abonados':'accesos'})
    IM_ACCESOS=pd.concat([IMDDA_ABO,IMCF_SUS])
    IM_ACCESOS['periodo']=IM_ACCESOS['anno']+'-T'+IM_ACCESOS['trimestre']
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
    response_base_cf = urlopen(consulta_cf + '&limit=10000000000') 
    json_base_cf = json.loads(response_base_cf.read())
    IMCF_ING = pd.DataFrame(json_base_cf['result']['records'])
    IMCF_ING.sum_ingresos = IMCF_ING.sum_ingresos.astype('int64')
    IMCF_ING['modalidad']='Cargo Fijo'
    resourceid_dda = '60a55889-ba71-45ff-b68f-33b503da36f2'
    consulta_dda='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid_dda + ''\
                '&filters[anno]=' + '2018,2019,2020,2021' + ''\
                '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
                '&group_by=anno,trimestre,id_empresa,empresa'\
                '&sum=ingresos' 
    response_base_dda = urlopen(consulta_dda + '&limit=1000000000') 
    json_base_dda = json.loads(response_base_dda.read())
    IMDDA_ING = pd.DataFrame(json_base_dda['result']['records'])
    IMDDA_ING.sum_ingresos = IMDDA_ING.sum_ingresos.astype('int64')
    IMDDA_ING['modalidad']='Demanda'
    IM_ING=pd.concat([IMDDA_ING,IMCF_ING])
    IM_ING=IM_ING.rename(columns={'sum_ingresos':'ingresos'})
    IM_ING['periodo']=IM_ING['anno']+'-T'+IM_ING['trimestre']
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
    IMCF_TRAF['modalidad']='Cargo Fijo'
    IMCF_TRAF.sum_trafico = IMCF_TRAF.sum_trafico.astype('int64')
    resourceid_dda = 'c0be7034-29f8-4400-be54-c4aafe5df606'
    consulta_dda='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid_dda + ''\
                '&filters[anno]=' + '2018,2019,2020,2021' + ''\
                '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
                '&group_by=anno,trimestre,id_empresa,empresa'\
                '&sum=trafico' 
    response_base_dda = urlopen(consulta_dda + '&limit=10000000') 
    json_base_dda = json.loads(response_base_dda.read())
    IMDDA_TRAF = pd.DataFrame(json_base_dda['result']['records'])
    IMDDA_TRAF['modalidad']='Demanda'
    IMDDA_TRAF.sum_trafico = IMDDA_TRAF.sum_trafico.astype('int64')
    IM_TRAF=pd.concat([IMDDA_TRAF,IMCF_TRAF])
    IM_TRAF['periodo']=IM_TRAF['anno']+'-T'+IM_TRAF['trimestre']
    IM_TRAF=IM_TRAF.rename(columns={'sum_trafico':'trafico'})
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

########################################################### Telefonía fija
## Ingresos
def ReadAPILinTL():
    resourceid_tl_lineas = '967fbbd1-1c10-42b8-a6af-88b2376d43e7'
    consulta_anno='2018,2019,2020,2021'
    consulta_tl_lineas = 'https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid_tl_lineas + ''\
                        '&filters[anno]=' + consulta_anno + ''\
                        '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa&fields[]=empresa&fields[]=id_segmento'\
                        '&group_by=anno,trimestre,id_empresa,empresa,id_segmento'\
                        '&sum=lineas' 
    response_tl_lineas = urlopen(consulta_tl_lineas + '&limit=10000000') # Se obtiene solo un registro para obtener el total de registros en la respuesta
    json_tl_lineas = json.loads(response_tl_lineas.read())
    TL_LINEAS = pd.DataFrame(json_tl_lineas['result']['records'])
    TL_LINEAS.sum_lineas = TL_LINEAS.sum_lineas.astype('int64')
    TL_LINEAS['periodo']=TL_LINEAS['anno']+'-T'+TL_LINEAS['trimestre']
    TL_LINEAS = TL_LINEAS.rename(columns={'sum_lineas':'lineas'})
    return TL_LINEAS  
LineasTelefoníaLocal=ReadAPILinTL()

##Trafico
def ReadAPITrafTelefoniaLocal():
    resourceid_tl_traf = 'bb2b4afe-f098-4c5d-819a-cba76337c3a9'
    consulta_anno='2018,2019,2020,2021'
    consulta_tl_traf='https://postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid_tl_traf + ''\
                        '&filters[anno]=' + consulta_anno + ''\
                        '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa&fields[]=empresa'\
                        '&group_by=anno,trimestre,id_empresa,empresa'\
                        '&sum=trafico' 
    response_tl_traf = urlopen(consulta_tl_traf + '&limit=10000000') # Se obtiene solo un registro para obtener el total de registros en la respuesta
    json_tl_traf = json.loads(response_tl_traf.read())
    TL_TRAF = pd.DataFrame(json_tl_traf['result']['records'])
    TL_TRAF.sum_trafico = TL_TRAF.sum_trafico.astype('int64')
    TL_TRAF['modalidad']='Local'
    TL_TRAF['periodo']=TL_TRAF['anno']+'-T'+TL_TRAF['trimestre']
    TL_TRAF = TL_TRAF.rename(columns={'sum_trafico':'trafico'})
    return TL_TRAF
def ReadAPITrafTelefoniaLDN():
    resourceid_tl_traf = '786ced6d-5e4a-41d2-90f8-5f2a56fc50e1'
    consulta_anno='2018,2019,2020,2021'
    consulta_tl_traf='https://postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid_tl_traf + ''\
                        '&filters[anno]=' + consulta_anno + ''\
                        '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa&fields[]=empresa'\
                        '&group_by=anno,trimestre,id_empresa,empresa'\
                        '&sum=trafico' 
    response_tl_traf = urlopen(consulta_tl_traf + '&limit=10000000') # Se obtiene solo un registro para obtener el total de registros en la respuesta
    json_tl_traf = json.loads(response_tl_traf.read())
    TL_TRAF = pd.DataFrame(json_tl_traf['result']['records'])
    TL_TRAF.sum_trafico = TL_TRAF.sum_trafico.astype('int64')
    TL_TRAF['modalidad']='Larga distancia nacional'
    TL_TRAF['periodo']=TL_TRAF['anno']+'-T'+TL_TRAF['trimestre']
    TL_TRAF = TL_TRAF.rename(columns={'sum_trafico':'trafico'})
    return TL_TRAF
def ReadAPITrafTelefoniaLDI():
    resourceid_tl_traf = 'ae33862d-954e-493c-8a4a-37b3443ec1c6'
    consulta_anno='2018,2019,2020,2021'
    consulta_tl_traf='https://postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid_tl_traf + ''\
                        '&filters[anno]=' + consulta_anno + ''\
                        '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa&fields[]=empresa'\
                        '&group_by=anno,trimestre,id_empresa,empresa'\
                        '&sum=trafico' 
    response_tl_traf = urlopen(consulta_tl_traf + '&limit=10000000') # Se obtiene solo un registro para obtener el total de registros en la respuesta
    json_tl_traf = json.loads(response_tl_traf.read())
    TL_TRAF = pd.DataFrame(json_tl_traf['result']['records'])
    TL_TRAF.sum_trafico = TL_TRAF.sum_trafico.astype('int64')
    TL_TRAF['modalidad']='Larga distancia internacional'
    TL_TRAF['periodo']=TL_TRAF['anno']+'-T'+TL_TRAF['trimestre']
    TL_TRAF = TL_TRAF.rename(columns={'sum_trafico':'trafico'})
    return TL_TRAF
TraficoTelefoniaLocal=ReadAPITrafTelefoniaLocal()
TraficoTelefoniaLDN=ReadAPITrafTelefoniaLDN()
TraficoTelefoniaLDI=ReadAPITrafTelefoniaLDI()
TraficoTelefoniaFija=pd.concat([TraficoTelefoniaLocal,TraficoTelefoniaLDN,TraficoTelefoniaLDI]).sort_values(by=['periodo'])

##Ingresos
def ReadAPIIngTL():
    resourceid_tl_ing = 'f923f3bc-0628-44cc-beed-ca98b8bc3679'
    consulta_anno='2018,2019,2020,2021'
    consulta_tl_ing = 'https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid_tl_ing + ''\
                        '&filters[anno]=' + consulta_anno + ''\
                        '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
                        '&group_by=anno,trimestre,id_empresa,empresa'\
                        '&sum=ingresos' 
    response_tl_ing = urlopen(consulta_tl_ing + '&limit=10000000') # Se obtiene solo un registro para obtener el total de registros en la respuesta
    json_tl_ing = json.loads(response_tl_ing.read())
    TL_ING = pd.DataFrame(json_tl_ing['result']['records'])
    TL_ING.sum_ingresos = TL_ING.sum_ingresos.astype('int64')
    TL_ING = TL_ING.rename(columns={'sum_ingresos':'ingresos'})
    TL_ING['periodo']=TL_ING['anno']+'-T'+TL_ING['trimestre']
    TL_ING['modalidad']='Local'
    return TL_ING  
def ReadAPIIngTLDN():
    resourceid_tl_ing = '535bae3e-87d2-46df-b9f4-b73cdbc9fceb'
    consulta_anno='2018,2019,2020,2021'
    consulta_tl_ing = 'https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid_tl_ing + ''\
                        '&filters[anno]=' + consulta_anno + ''\
                        '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
                        '&group_by=anno,trimestre,id_empresa,empresa'\
                        '&sum=ingresos' 
    response_tl_ing = urlopen(consulta_tl_ing + '&limit=10000000') # Se obtiene solo un registro para obtener el total de registros en la respuesta
    json_tl_ing = json.loads(response_tl_ing.read())
    TL_ING = pd.DataFrame(json_tl_ing['result']['records'])
    TL_ING.sum_ingresos = TL_ING.sum_ingresos.astype('int64')
    TL_ING = TL_ING.rename(columns={'sum_ingresos':'ingresos'})
    TL_ING['periodo']=TL_ING['anno']+'-T'+TL_ING['trimestre']
    TL_ING['modalidad']='Larga distancia nacional'
    return TL_ING 
def ReadAPIIngTLDI():
    resourceid_tl_ing = '878678cb-89c8-4b55-a60d-316870c3e896'
    consulta_anno='2018,2019,2020,2021'
    consulta_tl_ing = 'https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid_tl_ing + ''\
                        '&filters[anno]=' + consulta_anno + ''\
                        '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa'\
                        '&group_by=anno,trimestre,id_empresa,empresa'\
                        '&sum=ingresos' 
    response_tl_ing = urlopen(consulta_tl_ing + '&limit=10000000') # Se obtiene solo un registro para obtener el total de registros en la respuesta
    json_tl_ing = json.loads(response_tl_ing.read())
    TL_ING = pd.DataFrame(json_tl_ing['result']['records'])
    TL_ING.sum_ingresos = TL_ING.sum_ingresos.astype('int64')
    TL_ING = TL_ING.rename(columns={'sum_ingresos':'ingresos'})
    TL_ING['periodo']=TL_ING['anno']+'-T'+TL_ING['trimestre']
    TL_ING['modalidad']='Larga distancia internacional'
    return TL_ING 
IngresosTelefoniaLocal=ReadAPIIngTL()
IngresosTelefoniaLDN=ReadAPIIngTLDN()
IngresosTelefoniaLDI=ReadAPIIngTLDI()
IngresosTelefoniaFija=pd.concat([IngresosTelefoniaLocal,IngresosTelefoniaLDN,IngresosTelefoniaLDI])

########################################################### TV por suscripción

##Suscriptores
def ReadApiTVSUSSus():
    resourceid = '0c4b69a7-734d-432c-9d9b-9dc600d50391'
    consulta_anno='2018,2019,2020,2021'
    consulta='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid + ''\
             '&filters[mes_del_trimestre]=3&filters[anno]=' + consulta_anno + ''\
             '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa&fields[]=id_tecnologia&fields[]=tecnologia'\
             '&group_by=anno,trimestre,id_empresa,empresa,id_tecnologia,tecnologia'\
             '&sum=suscriptores' 
    response_base = urlopen(consulta + '&limit=10000000') 
    json_base = json.loads(response_base.read())
    TV_SUS = pd.DataFrame(json_base['result']['records'])
    TV_SUS.sum_suscriptores = TV_SUS.sum_suscriptores.astype('int64')
    TV_SUS = TV_SUS.rename(columns={'sum_suscriptores':'suscriptores'})
    TV_SUS['periodo']=TV_SUS['anno']+'-T'+TV_SUS['trimestre']
    return TV_SUS 
SuscriptoresTVSus=ReadApiTVSUSSus()    
##Ingresos
def ReadApiTVSUSIng():
    resourceid = '1033b0f2-8107-4e04-ae33-8b12882b762d'
    consulta_anno='2018,2019,2020,2021'
    consulta='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid + ''\
             '&filters[anno]=' + consulta_anno + ''\
             '&fields[]=anno&fields[]=trimestre&fields[]=id_empresa&fields[]=empresa&fields[]=id_concepto&fields[]=concepto'\
             '&group_by=anno,trimestre,id_empresa,empresa'\
             '&sum=ingresos' 
    response_base = urlopen(consulta + '&limit=10000000') 
    json_base = json.loads(response_base.read())
    TVSUS_ING = pd.DataFrame(json_base['result']['records'])
    TVSUS_ING.sum_ingresos = TVSUS_ING.sum_ingresos.astype('float').astype('int64')
    TVSUS_ING = TVSUS_ING.rename(columns={'sum_ingresos':'ingresos'})
    TVSUS_ING['periodo']=TVSUS_ING['anno']+'-T'+TVSUS_ING['trimestre']
    return TVSUS_ING
IngresosTVSus=ReadApiTVSUSIng()

########################################################### TV Comunitaria
##Asociados
def ReadApiTVComunitariaAsociados():
    resourceid = '6a80e055-0a5c-427e-a6d8-fcb3526dbcd5'
    consulta_anno='2019,2020,2021'
    consulta='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid + ''\
             '&filters[mes]=3&filters[anno]=' + consulta_anno + ''\
             '&fields[]=anno&fields[]=trimestre&fields[]=id_operador&fields[]=operador&fields[]=id_departamento&fields[]=departamento'\
             '&group_by=anno,trimestre,id_operador,operador,id_departamento,departamento'\
             '&sum=total_asociados' 
    response_base = urlopen(consulta + '&limit=10000000') 
    json_base = json.loads(response_base.read())
    TV_COM = pd.DataFrame(json_base['result']['records'])
    TV_COM.sum_total_asociados = TV_COM.sum_total_asociados.astype('int64')
    TV_COM = TV_COM.rename(columns={'id_operador':'id_empresa','operador':'empresa','sum_total_asociados':'asociados'})
    return TV_COM  
AsociadosTVComunitaria=ReadApiTVComunitariaAsociados()

##Ingresos
def ReadApiTVComunitariaIngresos():
    resourceid = '359d8eff-6891-4b4d-b04d-0948b002a651'
    consulta_anno='2019,2020,2021'
    consulta='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid + ''\
             '&filters[anno]=' + consulta_anno + ''\
             '&fields[]=anno&fields[]=trimestre&fields[]=mes_del_trimestre&fields[]=id_empresa&fields[]=desc_empresa'\
             '&group_by=anno,trimestre,mes_del_trimestre,id_empresa,desc_empresa'\
             '&sum[]=ingresos_totales&sum[]=ingr_brutos_pauta_publicitaria&sum[]=ingresos_brutos_operacionales' 
    response_base = urlopen(consulta + '&limit=10000000') 
    json_base = json.loads(response_base.read())
    TV_COM = pd.DataFrame(json_base['result']['records'])
    TV_COM['periodo']=TV_COM['anno']+'-T'+TV_COM['trimestre']
    TV_COM.sum_ingresos_totales = TV_COM.sum_ingresos_totales.astype('int64')
    TV_COM.sum_ingr_brutos_pauta_publicitaria = TV_COM.sum_ingr_brutos_pauta_publicitaria.astype('int64')
    TV_COM.sum_ingresos_brutos_operacionales = TV_COM.sum_ingresos_brutos_operacionales.astype('int64')
    TV_COM.trimestre=TV_COM.trimestre.astype('int64')
    TV_COM.mes_del_trimestre=TV_COM.mes_del_trimestre.astype('int64')
    TV_COM = TV_COM.rename(columns={'desc_empresa':'empresa','sum_ingresos_totales':'Ing Total',
                                   'sum_ingr_brutos_pauta_publicitaria':'Ing Pauta publicitaria',
                                   'sum_ingresos_brutos_operacionales':'Ing Brutos operacionales'})
    return TV_COM  
IngresosTVComunitariaIng=ReadApiTVComunitariaIngresos()

########################################################### Correo
##Ingresos y envíos
def ReadApiCorreoEnviosIngresos():
    resourceid = '3709bd6a-ee6b-4bc7-b711-9ebc64a89898'
    consulta_anno='2018,2019,2020,2021'
    consulta='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid + ''\
             '&filters[anno]=' + consulta_anno + ''\
             '&fields[]=anno&fields[]=trimestre&fields[]=ambito&fields[]=tipo_envio'\
             '&group_by=anno,trimestre,ambito,tipo_envio'\
             '&sum[]=ingresos&sum[]=numero_total_envios' 
    response_base = urlopen(consulta + '&limit=10000000') 
    json_base = json.loads(response_base.read())
    Correo = pd.DataFrame(json_base['result']['records'])
    Correo['periodo']=Correo['anno']+'-T'+Correo['trimestre']
    Correo.sum_ingresos = Correo.sum_ingresos.astype('int64')
    Correo.sum_numero_total_envios = Correo.sum_numero_total_envios.astype('int64')
    Correo = Correo.rename(columns={'sum_numero_total_envios':'Envíos','sum_ingresos':'Ingresos'})
    Correo['tipo_envio']=Correo['tipo_envio'].replace({'Envíos Individuales':'Individuales','Envíos Masivos':'Masivos'})
    return Correo  
IngresosyEnviosCorreo=ReadApiCorreoEnviosIngresos()

########################################################### M Expresa
##Ingresos y envíos
def ReadApiMExpresaEnviosIngresos():
    resourceid = '8b901e29-4fcd-465f-b006-fd73bd01215f'
    consulta_anno='2018,2019,2020,2021'
    consulta='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid + ''\
             '&filters[anno]=' + consulta_anno + ''\
             '&fields[]=anno&fields[]=trimestre&fields[]=ambito&fields[]=tipo_envio&fields[]=id_empresa&fields[]=empresa'\
             '&group_by=anno,trimestre,ambito,tipo_envio,id_empresa,empresa'\
             '&sum[]=ingresos&sum[]=numero_total_envios' 
    response_base = urlopen(consulta + '&limit=10000000') 
    json_base = json.loads(response_base.read())
    MExpresa = pd.DataFrame(json_base['result']['records'])
    MExpresa['periodo']=MExpresa['anno']+'-T'+MExpresa['trimestre']
    MExpresa.sum_ingresos = MExpresa.sum_ingresos.astype('int64')
    MExpresa.sum_numero_total_envios = MExpresa.sum_numero_total_envios.astype('int64')
    MExpresa = MExpresa.rename(columns={'sum_numero_total_envios':'Envíos','sum_ingresos':'Ingresos'})
    MExpresa['tipo_envio']=MExpresa['tipo_envio'].replace({'Envíos Individuales':'Individuales','Envíos Masivos':'Masivos'})
    return MExpresa  
IngresosyEnviosMExpresa=ReadApiMExpresaEnviosIngresos()

########################################################### Giros
##Ingresos 
def ReadApiGirosIngresos():
    resourceid = 'cbb58f7a-0d33-4667-a8df-8f7a707d0893'
    consulta_anno='2018,2019,2020,2021'
    consulta='https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resourceid + ''\
             '&filters[anno]=' + consulta_anno + ''\
             '&fields[]=anno&fields[]=trimestre&fields[]=ambito&fields[]=tipo_giro&fields[]=id_empresa&fields[]=empresa'\
             '&group_by=anno,trimestre,ambito,tipo_giro,id_empresa,empresa'\
             '&sum[]=ingresos&sum[]=valor_total_giros&sum[]=numero_giros' 
    response_base = urlopen(consulta + '&limit=10000000') 
    json_base = json.loads(response_base.read())
    Giros = pd.DataFrame(json_base['result']['records'])
    Giros['periodo']=Giros['anno']+'-T'+Giros['trimestre']
    Giros.sum_ingresos = Giros.sum_ingresos.astype('int64')
    Giros.sum_valor_total_giros = Giros.sum_valor_total_giros.astype('int64')
    Giros.sum_numero_giros = Giros.sum_numero_giros.astype('int64')
    Giros = Giros.rename(columns={'sum_valor_total_giros':'Valor total giros','sum_ingresos':'Ingresos'})
    Giros['tipo_giro']=Giros['tipo_giro'].replace({'Giros Nacionales':'Nacionales','Giros Internacionales':'Internacionales'})
    Giros=Giros.rename(columns={'sum_numero_giros':'Giros'})
    return Giros  
IngresosGiros=ReadApiGirosIngresos()
