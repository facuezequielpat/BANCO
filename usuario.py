class Usuarios():
  
  def __init__(self,dni,nombre,apellido,deposito, retiro,accion):
    self.dni= dni
    self.nombre= nombre
    self.apellido= apellido
    self.deposito= deposito
    self.retiro= retiro
    self.saldo= deposito-retiro
    self.accion=accion
    self.historial= []

  def mostrarUsuario(self):
    print("Dni: {}, nombre: {}, apellido: {},saldo:{}".format(self.dni,self.nombre,self.apellido,self.saldo) )

  def editarSaldo(self,deposito,retiro):
    self.deposito+=deposito
    self.saldo+= deposito
    if self.saldo-retiro>=0:
      self.retiro+=retiro
      self.saldo-=retiro  
      print("Registro exitoso")
    else:
      print("No tienes suficiente saldo para realizar ese retiro")
  def editarTodo(self,nombre, apellido, deposito,retiro):
    self.nombre=nombre
    self.apellido=apellido
    self.deposito+=deposito
    self.saldo+= deposito
    if self.saldo-retiro>=0:
      self.retiro+=retiro
      self.saldo-=retiro
      print("Registro exitoso")
    else:
      print("No tienes suficiente saldo para realizar ese retiro")


  def modificacion(self, accion):
    return"{}, DNI: {}, Nombre: {}, Apellido: {}, Deposito: {}, Retiro: {}, Saldo: {} ".format(accion,self.dni,self.nombre,self.apellido,self.deposito,self.retiro, self.deposito-self.retiro)

  def mostrarHistorial(self):
    print("Dni: {}, Nombre {}, Apellido{}".format(self.dni,self.nombre, self.apellido))
    