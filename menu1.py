from ingreso import Ingreso
class Mostrar():
  def principal(self):
    ingreso = Ingreso()
    while True:
      print("""\n1- Registro de usuarios
  2- Mostrar usuarios
  3- Buscar usuario
  4- Editar saldo
  5- Editar todo
  6- Eliminar usuario
  7- Historial
  8- Salir \n""")
      opcion=int(input("Elija un numero: "))
      
      if opcion==1:
        ingreso.registroUsuarios()
      elif opcion==2:
        ingreso.listaUsuario()
      elif opcion==3:
        ingreso.buscar()
      elif opcion==4:
        ingreso.editar()
      elif opcion==5:
        ingreso.editar_todo()
      elif opcion==6:
        ingreso.eliminar()
      elif opcion==7:
        ingreso.historiales()
      elif opcion==8:
        ingreso.salir()
      
mostrar=Mostrar()  
mostrar.principal()      