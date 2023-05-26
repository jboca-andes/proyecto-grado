import datetime
import logging
import pandas as pd 
import azure.functions as func
from azure.storage.blob import BlockBlobService
import pickle

# Función para convertir meses a días
def cambiar_a_dias(valor):
    return valor * 30

# Función principal que se ejecuta según el temporizador
def main(mytimer: func.TimerRequest) -> None:
    # Obtiene la marca de tiempo actual en formato UTC
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    # Lee el archivo CSV desde la URL especificada
    df = pd.read_csv('https://www.datos.gov.co/api/views/tb27-zmix/rows.csv?accessType=DOWNLOAD')
    
    # Selecciona columnas específicas del DataFrame
    df_seleccion = df[['ID del Proceso', 'Entidad', 'Descripción del Procedimiento', 'Duracion', 'Unidad de Duracion', 'Precio Base', 'Modalidad de Contratacion', 'Departamento Entidad', 'Ciudad Entidad', 'Fecha de Publicacion del Proceso', 'Departamento Proveedor',
        'Ciudad Proveedor', 'Valor Total Adjudicacion', 'Tipo de Contrato', 'Nombre del Proveedor Adjudicado',
        'NIT del Proveedor Adjudicado']][(df['Unidad de Duracion'] != 'ND')]

    # Convierte la duración de meses a días utilizando la función cambiar_a_dias
    df_seleccion['Duracion'] = df_seleccion['Duracion'][df_seleccion['Unidad de Duracion'] == 'Meses'].apply(cambiar_a_dias)

    # Elimina filas con valores nulos en el DataFrame
    df_seleccion = df_seleccion.dropna()

    # Modifica la unidad de duración a "Días" en todas las filas
    df_seleccion['Unidad de Duracion'] = 'Días'

    # Información de la cuenta de almacenamiento
    storageAccountName = "xxxxxxxxxxxxxx"
    storageKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    containerName = "xxxxxxxxxxxxxxxxxx"

    # Crea una instancia de BlockBlobService para interactuar con el servicio de almacenamiento de blobs
    blobService = BlockBlobService(account_name=storageAccountName, account_key=storageKey)

    #Cargar el pickle para la prediccion
    try:
        model = pickle.load(open('assets/modelo_andes.pkl', 'rb'))
        datos_prediccion = preparar(df_seleccion)
        df_salida = pd.DataFrame(model.predict(datos_prediccion), columns = ['ID del Proceso', 'Tipo de Contrato Esperado'])
        # Guarda el DataFrame seleccionado como un archivo CSV en el contenedor de almacenamiento de blobs
        blobService.create_blob_from_text(containerName, 'tb27-zmix-SUS-ML-CLASIFICACION.csv', df_salida.to_csv(index_label="idx", encoding="utf-8"))
    except:
        pass

    # Guarda el DataFrame seleccionado como un archivo CSV en el contenedor de almacenamiento de blobs
    blobService.create_blob_from_text(containerName, 'tb27-zmix.csv', df_seleccion.to_csv(index_label="idx", encoding="utf-8"))

    # Guarda una muestra del 30% del DataFrame como un archivo CSV en el contenedor de almacenamiento de blobs
    blobService.create_blob_from_text(containerName, 'sample-tb27-zmix.csv', df_seleccion.sample(frac=0.3).to_csv(index_label="idx", encoding="utf-8"))

    # Comprueba si el temporizador está atrasado y registra un mensaje si es así
    if mytimer.past_due:
        logging.info('The timer is past due!')

    # Registra un mensaje de información indicando que la función se ejecutó correctamente
    logging.info('Funcion ejecutada a %s', utc_timestamp)
