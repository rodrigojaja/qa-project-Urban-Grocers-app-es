import sender_stand_request
import data

def positive_assert(nombre):
    validacion = sender_stand_request.post_new_client_kit(nombre)

    assert validacion.status_code == 201
    assert validacion.json()['name'] == nombre

def negative_assert(nombre):
    validacion = sender_stand_request.post_new_client_kit(nombre)

    assert validacion.status_code == 400
def test_create_kit_1_letra():
    positive_assert("Aa")
def test_create_kit_501_letra():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdab"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
def test_create_kit_0_letras():
    negative_assert("")
def test_create_kit_512_letras():
    negative_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabC")
def test_create_kit_con_caracter_especial():
    positive_assert('"№%@"')

def test_create_kit_con_espacios():
    positive_assert(" A Aaa ")


def test_create_kit_con_numeros():
    positive_assert("123")

def test_create_kit_sin_parametro():
    negative_assert(None)

def test_create_kit_dado_difernete():
    negative_assert(123)





