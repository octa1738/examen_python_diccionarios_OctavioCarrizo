tipienpedapa = {
        "accion": [
    "fortinaiti",
    "braulstars"
],
    "ciencia ficcion": [
    "amogus"
],
    "terror": [
    "roblocs"
]
}
biblioteca = {}
siguienteid = 1
while True:
    print("\n- - - - - - - - - - - - - -")
    print("|       ETec Station      |")
    print("|                         |")
    print("- - - - - - - - - - - - - -")
    print("1. meterse a la tienda")
    print("2. jugar a un juego")
    print("3. salir")
    opcion = input("elegí una opción: ")
    if opcion == "1":
        while True:
            print("\n--- TIENDA ---")
            print("1. comprar un juego")
            print("2. ingresar un juego")
            print("3. salir")
    opcion_tienda = input("elegí una opción: ")
    if opcion_tienda == "1":
                print("\nlos géneros disponibles son:")

                for genero in tipienpedapa.keys():
                    print("-", genero)
                genero = input("ingresá el género: ").lower().strip()
                if genero in tipienpedapa:
                    juegos = tipienpedapa[genero]
                    print("\nlos juegos disponibles son:")
                    for i in range(len(juegos)):
                        print(i, ".", juegos[i])
                    if len(juegos) > 0:
                        try:
                            numero = int(input("ingresá el número del juego: "))
                            if numero >= 0 and numero < len(juegos):
                                titulo = juegos[numero]
                                biblioteca[siguienteid] = titulo
                                siguienteid += 1
                                print("¡compraste:", titulo, "!")
                            else:
                                print("este número de juego es inválido")
                        except ValueError:
                            print("tenés que ingresar un número panchirulo")
                    else:
                        print("no hay juegos en este género papu")
    else:
            print("no se ha encontrado este genero, probá con otro")
    elif opcion_tienda == "2":
    genero = input("ingresá el género del juego: ").lower().strip()
    titulo = input("ingresá el título del juego: ").strip()    
    if genero != "" and titulo != "":
                    if genero not in tipienpedapa:
                        tipienpedapa[genero] = []
    tipienpedapa[genero].append(titulo)    
    print("este juego fue agregado a la tienda")
    else:
    print("el género y el título no pueden estar vacíos")
    elif opcion_tienda == "3":
    break
else:
print("opción inválida")        
elif opcion == "2":
if len(biblioteca) == 0:
        print("\naún no tenés juegos en tu biblioteca")
else:
        print("\n--- TU BIBLIOTECA ---")    
        for id_juego, titulo in biblioteca.items():
                    print(id_juego, ".", titulo)    
try:
                    id_elegido = int(input("ingresá el número del juego: "))    
                    if id_elegido in biblioteca:
                        titulo = biblioteca[id_elegido]    
                        print("\njugando a", titulo, "...")                       
                        input("presioná Enter para dejar de jugar...")
                        print("dejaste de jugar a", titulo)
                    else:
                        print("ese número no es de un juego de tu biblioteca")
except ValueError:
                 print("tenés que ingresar un número")        
elif opcion == "3":
print("¡gracias por usar ETec station!")
break