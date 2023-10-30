#Se declara la sentencia Match

def http_error(status):
    match status:
        case 400:
            return "solicitud incorrecta"
        case 404:
            return "No encontrado"
        case 418:
            return "Soy una tetera"
        case _: #este valor se considera neutro
            return "Algo salio mal con el internet"

print(http_error(500))