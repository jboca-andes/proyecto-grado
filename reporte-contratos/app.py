from flask import Flask, render_template, send_from_directory, session, request, redirect, url_for, jsonify
from azure.storage.blob import AppendBlobService
import config as cfg

# Crea una instancia de la aplicación Flask
app = Flask(__name__)
# Configura la aplicación Flask utilizando la clase BaseConfig del módulo config
app.config.from_object('config.BaseConfig')
# Configuración adicional para trabajar detrás de un proxy
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Ruta de la aplicación para reportar un proceso dado un ID de proceso
@app.route('/reportar/<idproceso>', methods=['GET'])
def reportar(idproceso):
    try:
        # Crea una instancia de AppendBlobService utilizando la información de la cuenta de almacenamiento
        service = AppendBlobService(account_name=cfg.getConfigValue("account_name"), account_key=cfg.getConfigValue("account_key", True))

        # Intenta agregar el ID del proceso al blob existente
        try:
            service.append_blob_from_text(container_name=cfg.getConfigValue("container_name"), blob_name=cfg.getConfigValue("blob_name"), text=f'{idproceso}\n')
        except:
            # Si el blob no existe, crea uno nuevo y agrega el ID del proceso
            service.create_blob(container_name=cfg.getConfigValue("container_name"), blob_name=cfg.getConfigValue("blob_name"))
            service.append_blob_from_text(container_name=cfg.getConfigValue("container_name"), blob_name=cfg.getConfigValue("blob_name"), text=f'{idproceso}\n')

        # Prepara una respuesta de éxito
        response = {
            'status': 'success',
            'message': 'Operación completada correctamente',
            'result': 'Reportado'
        }
        return render_template('gracias.html')
    except Exception as e:
        # En caso de excepción, retornar una respuesta de error
        response = {
            'status': 'error',
            'message': str(e)
        }
        return jsonify(response), 500

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
