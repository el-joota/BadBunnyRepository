
                                    # BIENVENIDOS AL CATALOGO  DE.. #
                                              # BAD BUNNY #

    # CREADO POR @EL_JOTA # (FALTA MODO ALEATORIO) (SIGUIENTE/PAUSA/ANTERIOR) #
    # Alejandro Sanchez Serrano - 1º SMR #

    # DIA DE COMIENZO 04/03/22 #

print(" ")
nombre = input("Introduce tu nombre: ")
print("Hola " + nombre, "bienvenido al selector de canciones del Bad B, seleccione una opcion.")
print(" ")
#Nivel Dificultad
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
print(" ")
opcionbad =  input(" -> Cual deseas? Introduce una opcion " "(Porfavor intente ser preciso escribiendo el nombre de la opcion): ")
opcionlower = opcionbad.lower()

#Opcion FanXModa
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
