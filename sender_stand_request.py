import configuration
import requests
import data

def post_new_client_kit(nombre):
    variableQueGuardaElToken = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=data.user_body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados
    response = variableQueGuardaElToken.json()["authToken"]
    return requests.post(configuration.URL_SERVICE + configuration.CREACION_DE_KIT,  # inserta la dirección URL completa
                         json=data.parametroJsonKitNombreCambiado(nombre),  # inserta el cuerpo de solicitud
                         headers=data.headersConToken(response))  # inserta los encabezados

