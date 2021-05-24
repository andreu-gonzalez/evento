from evento import evento
from eventocontroller import eventocontroller

con = eventocontroller()

while True:
    print("***MENUS***")
    print("1-AGREGAR EVENTO")
    print("2-AGREGAR PARTICIPANTES")
    print("3-LISTAR EVENTOS (SIN PARTICIPANTES)")
    print("4-LISTAR EVENTOS (CON PARTICIPANTES)")
    print("5-LISTAR EVENTOS ACABADOS")
    print("6-FINALIZAR EVENTO")
    print("7-SALIR")
    
    while True:
        try:
            op=int(input("Introduce Opción: "))

            if op<=6 and op>=1:
                break

            else:
                print("Introduce un numero del 1 al 6")

        except ValueError:
            print("Introduce un numero!")

    
    if op==7:
        print("Adiós!")
        break


    if op == 1:
        print("Registrando evento")
        nombre=input("Nombre del evento: ")
        fecha=input("Fecha del evento: ")
        localidad=input("Localidad del evento: ")
        provincia=input("Provincia del evento: ")
        precio=input("Precio de inscripción del evento: ")

        evento = evento(nombre,fecha,localidad,provincia,precio)

        if con.addevento(evento):
            print("Evento añadido correctamente!")
        else:
            print("Error al añadir el evento!")
    if op ==2:
        print("Registrando participante")
        while True:
            nombre = input("Introduce el nombre")
            
            if con.existe(nombre):
                print("el nombre existe")
            elif nombre=="fin":
                break
            else:
                print("El nombre no existe")     
            print()
            dni = input("Dime la dni")
            nombres =input("Dime el nombre del participante")
            edad = int(input("Dime la edad"))
            if con.registrarparticipante(nombre,dni,nombres,edad):
                print("se ha registado")
            else:
                print("No se ha registrado")
    if op==3:
        print("Listar sin partircipantes")
        lista = con.listar()
        for i in lista:
                print("Nombre ",lista[i].getNombre())
                print("Fecha",lista[i].getFecha())
                print("Localidad",lista[i].getLocalidad())
                print("Provincia",lista[i].getProvincia())
                print("Precio",lista[i].getPrecio())
                print("Total",lista[i].getTotal())
                print("Finalizado",lista[i].getFinalizado())
    if op==4:
        print("Listar  con paticipantes")
        for i in lista:
                print("Nombre ",lista[i].getNombre())
                print("Fecha",lista[i].getFecha())
                print("Localidad",lista[i].getLocalidad())
                print("Provincia",lista[i].getProvincia())
                print("Precio",lista[i].getPrecio())
                print("Total",lista[i].getTotal())
                print("Finalizado",lista[i].getFinalizado())
                print("Participantes",lista[i].mostrarParticipantes())
    if op==5:
        print("Listar  con podio")
        finalizado= True
        for i in lista:
                if finalizado == lista[i].getFinalizado():
                    print("Nombre ",lista[i].getNombre())
                    print("Fecha",lista[i].getFecha())
                    print("Localidad",lista[i].getLocalidad())
                    print("Provincia",lista[i].getProvincia())
                    print("Precio",lista[i].getPrecio())
                    print("Total",lista[i].getTotal())
                    print("Finalizado",lista[i].getFinalizado())
                    print("Participantes",lista[i].mostrarParticipantes()) 
                    print("Podio",lista[i].mostrarPodo())                
    if op == 6:
        nombre=input("¿Que evento quieres finalizar? ")

        if con.finalizar(nombre):
            print("Evento finalizado con exito!")

        else:
            print("Error al finalizar evento!")




  

