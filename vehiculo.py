class Vehiculo():
    def __init__(self,id,nomCliente,marca,modelo,año,mantencion):
        self.id = id
        self.nomCliente = nomCliente
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.mantencion=mantencion

    def mostrarVehiculo(self):
        return  "ID:                "+str(self.id)+"\n"+\
                "Nombre Cliente:    "+self.nomCliente+"\n"+\
                "Marca:             "+self.marca+"\n"+\
                "Modelo:            "+self.modelo+"\n"+\
                "Año:               "+str(self.año)+"\n"+\
                "\nMantencion:"+self.mantencion.mostrarMantencion()+"\n"
    
    def agregarMantencion(self, nueva_mantencion):
        self.mantencion = nueva_mantencion
