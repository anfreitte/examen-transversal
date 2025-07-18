productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

precio=[]
p_min=[]
p_max=[]
modelo=[]

def stock_marca(marca):
    marca=marca.lower()
    total=0
    for modelo, datos in productos.items():
       if datos[0].lower()==marca:
        total+=stock[modelo][1]
    print(f"stock total de productos marca {marca}: {total}")

def busqueda_precio(p_min,p_max):
    while True:
     try:
        p_min=int(p_min)
        p_max=int(p_max)
        break
     except:
        print("debe ingresar valores enteros!!")

resultados=[]
for modelo(precio,stock) in productos.items():
   if p_min <= precio <= p_max and stock >0:
      marca=productos[modelo][1]
      resultados.append(f"{marca}--{modelo}")

if resultados:
   for res in (resultados):
      print(f"los notebooks entre los precios consultas son: {res}")
else:
   print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo,p):
 while True:
    modelo=input("ingrese modelo a actualizar: ").upper()
    if modelo in stock:
       try:
          nuevo_precio=int(input("ingrese nuevo precio: "))
          stock=[modelo][0]=nuevo_precio
          print("precio actualizado!!")
       except:
          print("debe ingresar un numero valido")
    else:
       print("El modelo no existe!!")
     
    continuar=input("desea actualizar otro precio? (si/no): ").strip().lower()
    if continuar !="si":
        print("hola ")
        break
   
    else:
        print("no se puedo actualzar el precio")

while True:
 print("***MENU PRINCIPAL***")
 print("1) stock marca")
 print("2) Búsqueda de precio")
 print("3) Atualizar precio")
 print("4) Salir")

 opcion=(input("ingrese opción: "))

 if opcion=="1":
    marca=input("ingrese marca a consultar: ")
    stock_marca(marca)
 elif opcion=="2":
    busqueda_precio()
 elif opcion=="3":
    actualizar_precio()
 elif opcion=="4":
    print("programa finalizado")
    break
 else:
    print("Debe seleccionar una opción válida!!")