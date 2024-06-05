def headersConToken(token):
    autorizacion = "Bearer " + token
    headersToken = {
        "Content-Type": "application/json", "Authorization": "\"" + autorizacion + "\""
    }
    return headersToken


user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

headers = {
    "Content-Type": "application/json"
}


def parametroJsonKitNombreCambiado(nombre):
    nombreCambiado = {
        "cardId": 1,
        "name": nombre
    }
    return nombreCambiado
