'''
Ejercio academico - Universidad de Cundinamarca
Sistema de clientes y compras para la tienda de mascotas KANU PET

Desarrolladores
🤖Andrés Camilo Delgado Ramos
🤖Yensy Lorena Rueda Roa
🤖Jesús Andrés Infante Páez

-> El enunciado del ejercicio se encuentra en el documento adjunto.
'''

#Diccionario de los productos que ofrece la tienda
import json
import os



productosTienda = {
    'comida':
    {
            'galletas': 7000,
            'alimentoperro': 8000,
            'alimentogato': 10000,                                                                                 
            'snacks': 4500,
            'alpiste': 9000,
            'humedocarne': 4000,
            'humedopollo':5000,
            'hueso':3000,

        },
    'accesorios':
        {
            'collar': 12000,
            'camiseta': 9000,
            'correa': 8000,
            'Arnes': 60000,
            'cama': 40000,
            'bebedero': 10000,
            'arenero': 80000,
            'tapete':25000

        },
    'insumos':
        {
            'vitaminas': 80000,
            'desparasitante': 12000,
            'analgesico': 20000,
            'banioseco': 40000,
            'antibiotico': 60000,
            'jabon':6000,
            'colonia':15000,
            'shampoo':25000

        },
}

#Diccionario de los clientes actuales de la tienda.
clientes = {
    '1084343':
        {
            'nombre': 'Juan Torres',
            'email': 'juan@gmail.com',
            'numero': '312345242',
            'visitas': 0,
            'facturas': {}
        },
    '904234':
        {
            'nombre': 'Pedro Perez',
            'email': 'pedro@gmail.com',
            'numero': '312434242',
            'visitas':  0,
            'facturas': {}
        },
    '104366234':
        {
            'nombre': 'Maria Gonzales',
            'email': 'maria@gmail.com',
            'numero': '313435465',
            'visitas':  4,
            'facturas': {}
        },
}

archivo ="dictionaryClients.json"
if os.path.isfile(archivo):
    with open (archivo) as f:
        clientes =  json.load(f)
else:
    tf = open("dictionaryClients.json", "w")
    json.dump(clientes,tf)
    tf.close()
archivo = "dictionaryProducts.json"
if os.path.isfile(archivo):
    with open ("dictionaryProducts.json") as f:
        productosTienda= json.load(f)
#Tupla con información de la tienda
informacionTienda = ('Kaenu Pet', '320324322',
                     'Calle 5 # 7-23', 'kaenupet@gmail.com')

#Tupla para imprimir encabezados en las facturas (estructuras).
encabezadoTabla = ('Nombre Producto', 'Cantidad', 'Total')
idCliente = 0
print(f'\n----------------------------------------------------------------------------------\n'
      f'\t 🐶 Bienvenido al sistema de clientes de {informacionTienda[0]} 🐶\n')
opcion = 0

#Menu de opciones controlando la salida de usuario con un ciclo while
while opcion != 5:
    print('----------------------------------------------------------------------------------\n'
          '\t\t\t Menú principal\n\n'
          '\t\t1. -> Agregar nuevo cliente\n'
          '\t\t2. -> Buscar Cliente\n'
          '\t\t3. -> Registrar compra\n'
          '\t\t4. -> Consultar historial de compras\n'
          '\t\t5. -> Salir\n'
          '----------------------------------------------------------------------------------')

    opcion = int(input('Digite una opción\n👉  '))
    print('----------------------------------------------------------------------------------')

    #Agregar cliente: Se verifica que este no exista a 
    # partir de su identificación y posteriormente se solicitan los demás datos
    if (opcion == 1):
        print('\n\t👨 Agregar nuevo cliente 👨\n'
              "\nIngrese el numero de identificación del cliente")
        idCliente = input('👉  ')
        if (idCliente in clientes) == False:
            nombreCliente = input('Ingrese el nombre del cliente'
                                  '\n👉  ')
            email = input("Ingresa su correo electronico"
                          '\n👉  ')
            numeroTelefono = input("Ingresa un número de teléfono válido"
                                   '\n👉  ')
            clientes[str(idCliente)] = {
                'nombre': nombreCliente,
                'email': email,
                'numero': numeroTelefono,
                'visitas': 0,
                'facturas': {}
            }
            print(
                f"\n\t¡¡¡El cliente {nombreCliente} fue agregado con exito!!!\n")
        else:
            print("\n\t¡¡¡El cliente ya existe en la lista!!!\n")

    #Busqueda de cliente: El cliente es buscado a partir de la identificación registrada como clave 
    # en el diccionario, despues se imprime la información registrada de este
    elif (opcion == 2):
        flag = True
        print('\n\t🔎 Buscar Cliente 🔍\n'
              "\nIngrese el numero de identificación del cliente")
        idCliente = input('👉  ')
        for clave in clientes:
            if (clave == idCliente):
                print("\n\t¡¡¡Cliente encontrado!!!\n"
                      f"\nIdentificación:{clave}\n"
                      f"Nombre: {clientes[clave]['nombre']}"
                      f"\nCorreo Electrónico:{clientes[clave]['email']}"
                      f"\nTeléfono:{clientes[clave]['numero']}"
                      f"\nvisitas:{clientes[clave]['visitas']}\n")
                flag=True
                break
            else:
                flag = False
        if flag==False: print("\n\t¡¡¡Cliente No encontrado!!!\n")
        
    #Registro de compra: Se solicita la identificación del cliente que compra, posteriormente se solicitan 
    #los productos y la cantidad que compraron para que finalmente se pueda totalizar todo e imprimir la factura del cliente.
    elif (opcion == 3):
        print('\n\t🛒 Registrar compra 🛒\n'
              "\nIngrese el numero de identificación del cliente")
        idCliente = input('👉  ')
        suma = 0
        opcion = 0
        fechaCompra = input('Ingrese la fecha de hoy (DD/MM/AAAA)\n'
                            '👉  ')
        factura = {
            fechaCompra: []
        }
        while opcion != 2:
            contador = 0
            total = 0
            nombreProducto = input('\nDigite el nombre del producto\n'
                                   '👉  ').lower()
            cantidad = int(input('Digite la cantidad del producto\n'
                                 '👉  '))
            for i in productosTienda:
                for j in productosTienda[i]:
                    if (j == nombreProducto):
                        total = cantidad * (productosTienda[i][j])
                        contador += 1
            if (contador == 0):
                print("\n\t¡¡¡El producto no esta disponible!!!")
            else:
                factura[fechaCompra].append([nombreProducto, cantidad, total])
                # factura.append([nombreProducto, cantidad, total])
                opcion = int(input('\n\t¿Desea agregar otro producto a la compra?\n\n'
                                   '1. -> Agregar\n'
                                   '2. -> Salir\n'
                                   '👉  '))

        #print(factura)
        clientes[idCliente]['visitas'] += 1
        print("\n----------------------------------------------------------------------------------"
            "\n\t\t\tFACTURA DE COMPRA"
            "\n----------------------------------------------------------------------------------\n")
        for i in range(0, len(informacionTienda)):
            print(f"{informacionTienda[i]}",end=' -- ')
        lista = list(clientes[idCliente])
        print('\n')
        for i in range(len(lista)-1):
            print(f"{lista[i]}: {clientes[idCliente][lista[i]]}")
        print(f"\n{encabezadoTabla[0]} ---- {encabezadoTabla[1]} ---- {encabezadoTabla[2]}")
        for j in factura[fechaCompra]:
            nombre = j[0]
            for i in range(len(nombre), 15):
                nombre += " "
            cantidad = str(j[1])
            for i in range(len(cantidad), 5):
                cantidad += " "
            print(f"{nombre } ----    {cantidad} ---- {j[2]}")
            suma += j[2]
        if (clientes[idCliente]['visitas'] == 5):
            suma *= 0.9
            print('¡¡¡\n\t!!!Obtuvo un descuento de 10 por ciento en su compra!!!')
            clientes[idCliente]['visitas'] = 0
        print(f"\nTotal compra --------------------- {suma}\n"
              "\n\t\t\t🐶 ¡¡¡Vuelva pronto!!! 🐶")
        factura[fechaCompra].append(suma)
        clientes[idCliente]['facturas'].update(factura)
        # print(clientes[idCliente]['facturas'])
    
    #Historial de compras: A partir del registro en el subdiccionario "facturas" en clientes.
    elif (opcion == 4):
        totalComprado = 0
        print('\n\t📃 Historial de compras 📃\n'
              "\nIngrese el numero de identificación del cliente")
        idCliente = input('👉  ')
        print('\n----------------------------------------------------------------------------------\n')
        print(f'\nIdentificación: {idCliente}'
                  f"\nCliente: {clientes[idCliente]['nombre']}")
        for clave, valor in clientes[idCliente]['facturas'].items():
            print(f"\n\tFecha de compra: {clave}")
            for i in range(len(valor)-1):
                for j in range(len(valor[i])):
                    print(f"{encabezadoTabla[j]}: {valor[i][j]}")
            
            totalComprado += valor[-1]
            print(f"Total de compra: {valor[-1]}")
        print(f"\nEl Total de compras del cliente es: {totalComprado}")
        print('\n----------------------------------------------------------------------------------\n')
        
    #Salida del sistema
    elif(opcion ==5):
        tf = open("dictionaryClients.json", "w")
        json.dump(clientes,tf)
        tf.close()
        tf = open("dictionaryProducts.json", "w")
        json.dump(productosTienda,tf)
        tf.close()
        print("\t\t\t¡¡GRACIAS POR USAR NUESTRO SISTEMA!!"
              '\n----------------------------------------------------------------------------------\n')       
    else:
        print("Opción incorrecta, intentelo nuevamente") 