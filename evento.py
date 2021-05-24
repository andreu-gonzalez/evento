class evento:
    def __init__(self,nombre,fecha,localidad,provincia,precio):
        self.nombre=nombre
        self.fecha=fecha
        self.localidad=localidad
        self.provincia=provincia
        self.precio=precio
        self.total=0
        self.finalizado=False
        self.participantes=[]
        self.podio={"PRIMERO":0,
                    "SEGUNDO":0,
                    "TERCERO":0}

    def getNombre(self):
        return self.nombre
    def getFecha(self):
        return self.fecha
    def getLocalidad(self):
        return self.localidad
    def getProvincia(self):
        return self.provincia
    def getPrecio(self):
        return self.precio
    def getTotal(self):
        return self.total
    def getFinalizado(self):
        return self.finalizado            

    def addparticipante(self,dni,nombres,edad):
        self.participantes.append((dni,nombres,edad))                       

    def mostrarParticipantes(self):
        lista=""
        for i in self.participantes:
            lista+="\tDni: "+str(i[0])+"\tNombre: "+str(i[1])+"\tEdad: "+str(i[2])+"\n\t\t\t"

        return lista


    def mostrarPodo(self):
        lista=""
        for clave,valor in self.podio.items():
            lista+="\t"+clave+": "+valor+"\n\t\t\t"

        return lista


    def finalizar(self):
        self.finalizado=True    