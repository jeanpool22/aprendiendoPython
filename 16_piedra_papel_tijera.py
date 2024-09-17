piedra = "piedra"
papel = "papel"
tijera = "tijera"

jugador_uno = input("Jugador uno ingrese piedra, papel o tijera:")
jugador_dos = input("Jugador dos ingrese piedra, papel o tijera:")

if jugador_uno == jugador_dos:
  print("Empate")
elif (jugador_uno == piedra and jugador_dos == papel) or \
     (jugador_uno == papel and jugador_dos == tijera) or \
     (jugador_uno == tijera and jugador_dos == piedra):
  print("Jugador dos gana con", jugador_dos)
elif (jugador_uno == piedra and jugador_dos == tijera) or \
     (jugador_uno == papel and jugador_dos == piedra) or \
     (jugador_uno == tijera and jugador_dos == papel):
  print("Jugador uno gana con", jugador_uno)
else:
  print("Opción invalida")