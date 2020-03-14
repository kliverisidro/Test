import os

class Inicializar():
    #Directorio base
    basedir=os.path.abspath(os.path.join(__file__,"../.."))
    DateFormat='%d/%m/%Y'
    
    #JsonData
    Json=basedir+u'/pages'

    Environment='Dev'

    #BROWSER DE PRUEBAS
    NAVEGADOR=u'IExplorer'

    #DIRECTORIO DE EVIDENCIA
    Path_Evidencias=basedir+u'/data/capturas'

    #HOJA DE DATOS EXCEL
    Excel=basedir+u'/data/Data.xlsx'

    if Environment=='Dev':
        URL='https://www.google.com/'
        User='kliver'
        Pass='1234'
    if Environment=='Dev':
        URL='https://www.youtube.com/'
        User='kliver'
        Pass='1234'