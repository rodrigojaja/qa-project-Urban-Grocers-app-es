import configuration
import requests
import data

def headersConToken(token):
    autorizacion = "Bearer " + token
    headersToken = {
        "Content-Type": "application/json", "Authorization": "\"" + autorizacion + "\""
    }
    return headersToken

def parametroJsonKitNombreCambiado(nombre):
    nombreCambiado = {
        "cardId": 1,
        "name": nombre
    }
    return nombreCambiado
def post_new_user():
    variableQueGuardaElToken = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                                             # inserta la dirección URL completa
                                             json=data.user_body,  # inserta el cuerpo de solicitud
                                             headers=data.headers)  # inserta los encabezados
    return variableQueGuardaElToken.json()["authToken"]

def post_new_client_kit(nombre):
    return requests.post(configuration.URL_SERVICE + configuration.CREACION_DE_KIT,  # inserta la dirección URL completa
                         json=parametroJsonKitNombreCambiado(nombre),  # inserta el cuerpo de solicitud
                         headers=headersConToken(post_new_user()))  # inserta los encabezados

