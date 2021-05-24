from evento import evento
class eventocontroller:
    def __init__(self) :
        self.listaeventos={}
    def addevento(self,factura):
        if factura.getNombre() not in self.listaeventos:
            self.listaeventos[factura.getNombre()] = factura
            return True
        return False

    def registrarparticipante(self,nombre,dni,nombres,edad):
        if nombre in self.listaeventos:
                self.listaeventos[nombre].addparticipante(dni,nombres,edad)
                return True
        return False

    def existe(self,nombre):
        if nombre in self.listaeventos:
            return True
        return False           
    def finalizar(self,nombres):
        if nombres in self.listaeventos:
            self.listaeventos[nombres].finalizar()
            return True
        return False  
    def listar(self):
        return self.listaeventos       