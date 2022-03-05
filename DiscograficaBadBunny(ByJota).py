
                                    # BIENVENIDOS AL CATALOGO  DE.. #
                                              # BAD BUNNY #

    # CREADO POR @EL_JOTA # (FALTA MODO ALEATORIO) (SIGUIENTE/PAUSA/ANTERIOR) #
    # Alejandro Sanchez Serrano - 1º SMR #

    # DIA DE COMIENZO 04/03/22 #

print(" ")
nombre = input("Introduce tu nombre: ")
print("Hola " + nombre, "bienvenido al selector de canciones del Bad B, seleccione una opcion.")
print(" ")
#Nivel Fan
print(" -> Las opciones son: \n"
      " \n"
      "     - FANXMODA \n"
      "     - ENDTOUR \n"
      "     - LASQUENO \n"
      "     - YHLQMDLG \n"
      "     - OASIS \n"
      "     - X100PRE \n"
      "     - OG \n"
      "     - GOD \n"
      "     - LANUEVARELIGION \n")

opcionbad =  input(" -> Cual deseas? Introduce una opcion " "(Porfavor intente ser preciso escribiendo el nombre de la opcion): ")
opcionlower = opcionbad.lower()

#Opcion FANXMODA
if opcionlower == "fanxmoda":
    print(" ")
    print("Usted escogio: FANXMODA")
    print(" ")
    #Seleccion de cancion
    print("Las canciones alojadas en esta opcion: \n"
          " \n"
          "1. Lo Siento BB - Bad Bunny Ft. Julieta Venegas \n"
          "2. Volvi - Bad Bunny Ft. Aventura \n"
          "3. Volando Remix - Bad Bunny Ft. Sech, Mora \n"
          "4. De Museo - Bad Bunny \n"
          "5. AM Remix - Bad Bunny Ft. J Balvin, Nio Garcia \n"
          "6. Yonaguni - Bad Bunny \n"
          "7. 100 Millones - Bad Bunny \n")

    #Peticion de numero de cancion
    songfanxmoda = int(input("Inserte un numero entre 1-7 para seleccionar una cancion: "))

    #Cancion 1 = Lo Siento BB
    if songfanxmoda == 1:
        print(" ")

        letra1 = input("¿Deseas la letra? (y/n): ")
        letralower = letra1.lower()
        if letralower=="y":
            print(" ")
            print("Reproduciendo: Lo Siento BB - Bad Bunny Ft. Julieta Venegas")
            print("Letra:")
            print(" ")
            #Letra
            with open('C:\\Users\\usuario\\Desktop\\LETRAS\\letralosientobb.txt') as f:
                contents = f.read()
                print(contents)
        else:
                if letra1=="n":
                    print(" ")
                    print("Reproduciendo: Lo Siento BB - Bad Bunny Ft. Julieta Venegas")

                else:
                    print(" ")
                    print("Lo siento, no reconozco lo que dijiste")
                    print("Te reproduzco la cancion sin letra :D")

        #Este es el PlaySound
        from playsound import playsound
        playsound("C:\\Users\\usuario\\Music\\FANXMODA\\Lo_Siento_BB.mp3")

    else:

        #Cancion 2 = Volvi
        if songfanxmoda == 2:
            print(" ")

            letra1 = input("¿Deseas la letra? (y/n): ")
            letralower = letra1.lower()
            if letralower == "y":
                print(" ")
                print("Reproduciendo: Volvi - Bad Bunny Ft. Aventura")
                print("Letra:")
                print(" ")
                #Letra
                with open('C:\\Users\\usuario\\Desktop\\LETRAS\\letravolvi.txt') as f:
                    contents = f.read()
                    print(contents)

            else:
                if letra1 == "n":
                    print(" ")
                    print("Reproduciendo: Volvi - Bad Bunny Ft. Aventura")

                else:
                    print(" ")
                    print("Lo siento, no reconozco lo que dijiste")
                    print("Te reproduzco la cancion sin letra :D")

            #Este es el PlaySound
            from playsound import playsound
            playsound("C:\\Users\\usuario\\Music\\FANXMODA\\Volvi.mp3")

        else:

            #Cancion 3 = Volando Remix
            if songfanxmoda == 3:
                print(" ")

                letra1 = input("¿Deseas la letra? (y/n): ")
                letralower = letra1.lower()
                if letralower == "y":
                    print(" ")
                    print("Reproduciendo: Volando Remix - Bad Bunny Ft. Sech, Mora")
                    print("Letra:")
                    print(" ")
                    # Letra
                    with open('C:\\Users\\usuario\\Desktop\\LETRAS\\letravolando.txt') as f:
                        contents = f.read()
                        print(contents)

                else:
                    if letra1 == "n":
                        print(" ")
                        print("Reproduciendo: Volando Remix - Bad Bunny Ft. Sech, Mora")

                    else:
                        print(" ")
                        print("Lo siento, no reconozco lo que dijiste")
                        print("Te reproduzco la cancion sin letra :D")

                #Este es el PlaySound
                from playsound import playsound
                playsound("C:\\Users\\usuario\\Music\\FANXMODA\\Volando_Remix.mp3")

            else:

                #Cancion 4 = De Museo
                if songfanxmoda == 4:
                    print(" ")

                    letra1 = input("¿Deseas la letra? (y/n): ")
                    letralower = letra1.lower()
                    if letralower == "y":
                        print(" ")
                        print("Reproduciendo: De Museo - Bad Bunny")
                        print("Letra:")
                        print(" ")
                        # Letra
                        with open('C:\\Users\\usuario\\Desktop\\LETRAS\\letrademuseo.txt') as f:
                            contents = f.read()
                            print(contents)

                    else:
                        if letra1 == "n":
                            print(" ")
                            print("Reproduciendo: De Museo - Bad Bunny")

                        else:
                            print(" ")
                            print("Lo siento, no reconozco lo que dijiste")
                            print("Te reproduzco la cancion sin letra :D")

                    #Este es el PlaySound
                    from playsound import playsound
                    playsound("C:\\Users\\usuario\\Music\\FANXMODA\\De_Museo.mp3")

                else:

                    #Cancion 5 = AM Remix
                    if songfanxmoda == 5:
                        print(" ")

                        letra1 = input("¿Deseas la letra? (y/n): ")
                        letralower = letra1.lower()
                        if letralower == "y":
                            print(" ")
                            print("Reproduciendo: AM Remix - Bad Bunny Ft. J Balvin, Nio Garcia")
                            print("Letra:")
                            print(" ")
                            # Letra
                            with open('C:\\Users\\usuario\\Desktop\\LETRAS\\letraamremix.txt') as f:
                                contents = f.read()
                                print(contents)

                        else:
                            if letra1 == "n":
                                print(" ")
                                print("Reproduciendo: AM Remix - Bad Bunny Ft. J Balvin, Nio Garcia")

                            else:
                                print(" ")
                                print("Lo siento, no reconozco lo que dijiste")
                                print("Te reproduzco la cancion sin letra :D")

                        #Este es el PlaySound
                        from playsound import playsound
                        playsound("C:\\Users\\usuario\\Music\\FANXMODA\\AM_Remix.mp3")

                    else:

                        #Cancion 6 = Yonaguni
                        if songfanxmoda == 6:
                            print(" ")

                            letra1 = input("¿Deseas la letra? (y/n): ")
                            letralower = letra1.lower()
                            if letralower == "y":
                                print(" ")
                                print("Reproduciendo: Yonaguni - Bad Bunny")
                                print("Letra:")
                                print(" ")
                                #Letra
                                with open('C:\\Users\\usuario\\Desktop\\LETRAS\\letrayonaguni.txt') as f:
                                    contents = f.read()
                                    print(contents)

                            else:
                                if letra1 == "n":
                                    print(" ")
                                    print("Reproduciendo: Yonaguni - Bad Bunny")

                                else:
                                    print(" ")
                                    print("Lo siento, no reconozco lo que dijiste")
                                    print("Te reproduzco la cancion sin letra :D")

                            #Este es el PlaySound
                            from playsound import playsound
                            playsound("C:\\Users\\usuario\\Music\\FANXMODA\\Yonaguni.mp3")

                        else:

                            #Cancion 7 = Yonaguni
                            if songfanxmoda == 7:
                                print(" ")

                                letra1 = input("¿Deseas la letra? (y/n): ")
                                letralower = letra1.lower()
                                if letralower == "y":
                                    print(" ")
                                    print("Reproduciendo: 100 Millones - Bad Bunny")
                                    print("Letra:")
                                    print(" ")
                                    #Letra
                                    with open('C:\\Users\\usuario\\Desktop\\LETRAS\\letramillones.txt') as f:
                                        contents = f.read()
                                        print(contents)

                                else:
                                    if letra1 == "n":
                                        print(" ")
                                        print("Reproduciendo: 100 Millones - Bad Bunny")

                                    else:
                                        print(" ")
                                        print("Lo siento, no reconozco lo que dijiste")
                                        print("Te reproduzco la cancion sin letra :D")

                                #Este es el PlaySound
                                from playsound import playsound
                                playsound("C:\\Users\\usuario\\Music\\FANXMODA\\100_Millones.mp3")

else:
    #Opcion ENDTOUR
    if opcionlower == "endtour":
        print(" ")
        print("Usted escogio: ENDTOUR")
        print(" ")
        #Seleccion de cancion
        print("Las canciones alojadas en esta opcion: \n"
              " \n"
              "1. El Mundo Es Mio - Bad Bunny \n"
              "2. Te Mudaste - Bad Bunny \n"
              "3. Hoy Cobre - Bad Bunny \n"
              "4. Maldita Pobreza - Bad Bunny \n"
              "5. La Noche De Anoche - Bad Bunny Ft. Rosalia \n"
              "6. Te Deseo Lo Mejor - Bad Bunny \n"
              "7. Yo Visto Asi - Bad Bunny \n"
              "8. Haciendo Que Me Amas - Bad Bunny \n"
              "9. Booker T - Bad Bunny \n"
              "10. La Droga - Bad Bunny \n"
              "11. Dakiti - Bad Bunny Ft. Jhay Cortez \n"
              "12. Trellas - Bad Bunny \n"
              "13. Sorry Papi - Bad Bunny Ft. Abra \n"
              "14. 120 - Bad Bunny \n"
              "15. Antes Que Se Acabe - Bad Bunny \n"
              "16. Cantares De Navidad - Bad Bunny \n")

        #Peticion de numero de cancion
        songendtour = int(input("Inserte un numero entre 1-16 para seleccionar una cancion: "))

        #Cancion 1 = Lo Siento BB
        if songendtour == 1:
            print(" ")

            letra1 = input("¿Deseas la letra? (y/n): ")
            letralower = letra1.lower()
            if letralower == "y":
                print(" ")
                print("Reproduciendo: El Mundo Es Mio - Bad Bunny")
                print("Letra:")
                print(" ")
                #Letra
                with open('C:\\Users\\usuario\\Desktop\\LETRAS\\letraelmundomio.txt') as f:
                    contents = f.read()
                    print(contents)
            else:
                if letra1 == "n":
                    print(" ")
                    print("Reproduciendo: El Mundo Es Mio - Bad Bunny")

                else:
                    print(" ")
                    print("Lo siento, no reconozco lo que dijiste")
                    print("Te reproduzco la cancion sin letra :D")

            #Este es el PlaySound
            from playsound import playsound
            playsound("C:\\Users\\usuario\\Music\\ENDTOUR\\El_Mundo_Es_Mio.mp3")



