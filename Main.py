import random
from clases.Enemigo import Enemigo
from clases.Jugador import Jugador


def main():
    nombre_jugador = input("Bienvenido a esta nueva aventura en el reino de las sombras! Por favor, ingrese tu nombre: ")
    jugador = Jugador(nombre_jugador)

    enemigos = [Enemigo("0Esqueleto reanimado", 40, 10 ),
                Enemigo("Nigromante", 50, 15),
                Enemigo("Bestia sombria", 70, 20)
                 ]
    enemigos_derrotados = []
    print("Comienza la aventura!")

    while enemigos:
        enemigo_actual = random.choice(enemigos)
        if enemigo_actual in enemigos_derrotados:
            continue
        print(f"Te encuentras con un {enemigo_actual.nombre} en tu camino")

        while enemigo_actual.salud > 0:
            accion = input("Que deseas hacer? (atacar/huir)").lower()

            if accion == "atacar":
                dano_jugador = jugador.atacar()
                print(f"Has atacado al {enemigo_actual.nombre} y le has causado {dano_jugador} de daño")
                enemigo_actual.recibir_dano(dano_jugador)

                if enemigo_actual.salud > 0:
                    dano_enemigo = enemigo_actual.atacar()
                    print(f"El {enemigo_actual.nombre} te ataco y te causo {dano_enemigo} de dano")
                    jugador.recibir_dano(dano_enemigo)

            elif accion == "huir":
                print("Has decidido huir del combate!")
                break # Salir del While
        if jugador.salud <= 0:
            print("Has perdido la partida!")
            break
        if enemigo_actual.salud <= 0:
            enemigos_derrotados.append(enemigo_actual)
            enemigos.remove(enemigo_actual)

        jugador.ganar_experiencia(20)

        continuar = input("Quieres seguir explorando (Si/No)").lower()

        if continuar != "SI":
            print("Gracias, por haber jugado!")
    if not enemigos:
        print("Felicidades mataste a todos!!!!")

if __name__ == "__main__": #Solo podemos ejecutar este script dsesde el archivo principal
    main()
