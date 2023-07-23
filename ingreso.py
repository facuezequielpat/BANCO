from usuario import Usuarios
listaUsuarios=[]
class Ingreso():
  def registroUsuarios(self):
    print("\nRegistro de usuarios")
    dniCorrecto=False
    
    while (not dniCorrecto):
      dni= input("Dni: ")
      
      if dni.isnumeric():
        if len(dni)==8:
          if len(listaUsuarios)>0:
            for Obj in listaUsuarios:
              if dni!=Obj.dni:
                dniCorrecto= True
              else:
                print("El usuario ya exisiste")
          else:
            dniCorrecto= True
        else:
          print("El dni debe tener 8 digitos")
      elif dni.isalnum():
        print("No debe ser alfanumerico")
      else:
        print("ingrese Dni valido, no es numerico")
        
    nombre=str(input('nombre: '))
    apellido= str(input("Apellido: "))
    deposito= float(input("Deposito: "))
    retiro=float(input("Retiro: "))
    x=True
    while x:
      if retiro <= deposito:
        x=False
      else:
        print("El retiro debe ser menor que el deposito")
        retiro=float(input("Retiro: "))
    accion='Registro de usuario'
    usuarioObj=Usuarios(dni,nombre,apellido,deposito,retiro,accion)
    listaUsuarios.append(usuarioObj)
    for Obj in listaUsuarios:
      if dni==Obj.dni:
        mensaje=Obj.modificacion(accion)
        Obj.historial.append(mensaje)
    print("Se registro al usuario")

  def listaUsuario(self):
    if len(listaUsuarios)>0:
      for Obj in listaUsuarios:
        Obj.mostrarUsuario()
    else:
      print("No se registraron usuarios")

  def buscar(self):
    seleccion=input("Dime el dni del objeto a buscar ")
    for Obj in listaUsuarios:
      if seleccion==Obj.dni:
        Obj.mostrarUsuario()
      else:
        print("Usuario inexistente")
  def salir(self):
    print("Programa finalizado")
    exit()

  def editar(self):
    print("Editar saldo")
    dni=input("Ingrese el dni a buscar ")
    for Obj in listaUsuarios:
      if dni==Obj.dni:
        deposito= float(input("Deposito: "))
        retiro=float(input("Retiro: "))
        accion="Editar saldo"
        Obj.editarSaldo(deposito,retiro)
        mensaje=Obj.modificacion(accion)
        Obj.historial.append(mensaje)
        
      else:
        print("DNI invalido")

        
  def editar_todo(self):
    print("Editar todo")
    dni=input("Ingrese el dni a buscar ")
    for Obj in listaUsuarios:
      if dni==Obj.dni:
        nombre=str(input("Nombre: "))
        apellido=str(input("Apellido: "))
        deposito=int(input("Deposito: "))
        retiro=int(input("Retiro: "))
        accion="Editar todo"
        Obj.editarTodo(nombre,apellido,deposito, retiro)
        mensaje=Obj.modificacion(accion)
        Obj.historial.append(mensaje)
      else:
        print("DNI invalido")

  def eliminar(self):
    dni= input("Dime el DNI del usuario que quieres eliminar ")
    for Obj in listaUsuarios:
        if dni == Obj.dni:
          listaUsuarios.remove(Obj)
          print('Usuario eliminado')
        else:
          ("DNI invalido")
        
  def historiales(self):
    print("Historial")
    if len(listaUsuarios)!=0:
      dni=input("Ingrese el dni a buscar ")
      for Obj in listaUsuarios:
        if dni==Obj.dni:
          for mensaje in Obj.historial:
            print("Evento: {}".format(mensaje))
        else:
          print("Dni NO registrado")
    else:
      print("No hay registros hechos")
            
      