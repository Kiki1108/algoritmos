


def buscar_elemento(elemento, arreglo):
    for i in arreglo:
        if elemento == i:
            return i


def letra_mayor(palabra):
    mayor = ""
    for i in palabra:
        if mayor < i:
            mayor = i
    return mayor


def repetido(elemento, arreglo):
    contador = 0
    for i in arreglo:
        if elemento == i:
            contador += 1
    return contador


def cifrado(key, mensaje):
    mensaje = mensaje.upper()
    key = key%26
    mensaje_cifrado = ""
    for i in mensaje:
        temp = ord(i) + key
        if (temp > 122 and temp < 90):
            mensaje_cifrado += chr(temp - 26)
        else:
            mensaje_cifrado += chr(temp)
    return mensaje_cifrado


def descifrado(key, mensaje_cifrado):
    key = key%26 
    mensaje = ""
    for i in mensaje_cifrado:
        temp = ord(i) - key
        if (temp < 65 and temp > 39):
            mensaje += chr(temp + 26)
        else:
            mensaje += chr(temp)
    return mensaje


def pre_letra_mayor():
    palabra = "AzTEROIDE"
    mayor = letra_mayor(palabra)

    print(f"\nPalabra: {palabra}")
    print(f"Letra mayor: {mayor}")


def pre_repetido():
    arreglo = [1,1,1,2,3,4,5,6,7,8,9]
    elemento = 1
    cantidad = repetido(elemento, arreglo)

    print(f"\nArreglo: {arreglo}")
    print(f"Elemento: {elemento}")
    print(f"Cantidad {cantidad}")


def pre_cifrado():
    key = 52
    mensaje = "Hola mundo"
    mensaje_cifrado = cifrado(key, mensaje)

    print(f"Key: {key}")
    print(f"Mensaje: {mensaje}")
    print(f"cifrado: {mensaje_cifrado}")
    return mensaje_cifrado


def pre_descrifrado(mensaje_cifrado):
    key = 52
    mensaje = descifrado(key, mensaje_cifrado)

    print(mensaje)


def pre_buscar_elemento():
    arreglo = [i for i in range(100)]
    elemento = -1
    indice = buscar_elemento(elemento, arreglo)
    
    print(f"\nArreglo: {arreglo}")
    print(f"Elemento: {elemento}")
    print(f"Indice: {indice}")


if __name__ == "__main__":
    """
    pre_buscar_elemento()
    print("Buscar elemento: T(5n) O(n)")

    pre_letra_mayor()
    print("Letra mayor: T(5n+3) O(n)")

    pre_repetido()
    print("Elemento repetido: T() O()")
    """
    mensaje_cifrado = pre_cifrado()
    pre_descrifrado(mensaje_cifrado)
