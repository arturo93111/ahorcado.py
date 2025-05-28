import random

# Lista de palabras 
palabras = ["servidor", "red", "wifi", "automatas", "linux", "tecnologico"]

# Dibujo
dibujos = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

def jugar_ahorcado():
    palabra = random.choice(palabras)
    letras_adivinadas = []
    intentos = 0
    max_intentos = len(dibujos) - 1
    letras_usadas = []

    while True:
        # dibujo actual
        print(dibujos[intentos])

        # progreso de la palabra
        progreso = ""
        for letra in palabra:
            if letra in letras_adivinadas:
                progreso += letra
            else:
                progreso += "-"
        print("\nPalabra:", progreso)

        #  letras usadas
        print("Letras ya dichas:", " ".join(sorted(letras_usadas)))

        # checa si ganó
        if progreso == palabra:
            print("\n¡Ganaste! La palabra era:", palabra)
            break

        # checa si perdió
        if intentos == max_intentos:
            print("\nPerdiste...")
            print("La palabra era:", palabra)
            break

        # Pedir letra
        letra = input("\nIngresa una letra: ").lower()

        # Validar entrada
        if not letra.isalpha() or len(letra) != 1:
            print("Ingresa solo una letra válida.")
            continue
        if letra in letras_usadas:
            print("Ya usaste esa letra.")
            continue

        letras_usadas.append(letra)

        # Verificar si la letra está en la palabra
        if letra in palabra:
            letras_adivinadas.append(letra)
        else:
            intentos += 1

    # Preguntar si quiere jugar de nuevo
    otra = input("\n¿Jugar de nuevo? (s/n): ").lower()
    if otra == "s":
        jugar_ahorcado()

# Iniciar el juego
jugar_ahorcado()
