lista_compras = []

while True:
  print("\nMenú de opciones:")
  print("1. Agregar artículo")
  print("2. Eliminar artículo")
  print("3. Mostrar lista")
  print("4. Salir")

  opcion = input("Ingrese una opción: ")

  if opcion == "1":
    articulo = input("Ingrese el artículo a agregar: ")
    lista_compras.append(articulo)
    print("Artículo agregado a la lista.")
  elif opcion == "2":
    if not lista_compras:
      print("La lista está vacía.")
    else:
      print("Lista de compras:")
      for i, articulo in enumerate(lista_compras):
        print(f"{i+1}. {articulo}")
      eliminar = int(input("Ingrese el número del artículo a eliminar: "))
      if 1 <= eliminar <= len(lista_compras):
        del lista_compras[eliminar - 1]
        print("Artículo eliminado.")
      else:
        print("Opción inválida.")
  elif opcion == "3":
    if not lista_compras:
      print("La lista está vacía.")
    else:
      print("Lista de compras:")
      for articulo in lista_compras:
        print(articulo)
  elif opcion == "4":
    print("Saliendo del programa...")
    break
  else:
    print("Opción inválida.")