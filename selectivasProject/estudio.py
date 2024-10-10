#definor variables
PRECIO_SENCILLA = 20000
PRECIO_DOBLE = 25000
PRECIO_TRIPLE = 28000
INPUESTO_TARJETA = 0.07

#FUNCION PARA CALCULAR EL PRECIO
def calcular_precio (tipo_hamburgesa, medio_pago, cantidad):
    #definir precio segun el tipo de hanburguesa
    if tipo_hamburgesa==1:
        precio= PRECIO_SENCILLA
        descripcion = "sencilla"
    elif tipo_hamburgesa==2:
        precio= PRECIO_DOBLE
        descripcion ="doble"
    elif tipo_hamburgesa==3:
        precio= PRECIO_TRIPLE
        descripcion = "triple"
        print("ingrese el numero de hamburgesas")
    else:
        return None # tipo de hanburgesa invalida


    #calcular el total sin cargos
    total_sin_cargo= precio*cantidad

    #aplicar inpuesto si el medio de pago es tarjeta

    if medio_pago ==1:
        inpuesto=round(total_sin_cargo* INPUESTO_TARJETA)
    else:
        inpuesto=0
    total =round(total_sin_cargo+inpuesto)
    #retornar datos elevantes
    return descripcion, precio, cantidad, inpuesto,total

#funcion para generer mensaje
def generar_mensaje(descripcion, precio, cantidad, inpuesto,total):
    return (f"tipo de hamburgesa: {descripcion}\n"
            f"precio: ${precio}\n"
            f"cantidad: {cantidad}\n"
            f"inpuesto: ${inpuesto}\n"
            f"total : ${total}")
#funcion para validar los datos

def validar_datos (tipo_hamburgesa, medio_pago, cantidad):
    if 1<= tipo_hamburgesa <=3 and 1<=medio_pago<=2 and cantidad >0:
        resultado = calcular_precio(tipo_hamburgesa, medio_pago, cantidad)
        #print("resultado: ", resultado)
        descripcion, precio, cantidad , inpuesto, total = resultado
        mensaje = generar_mensaje(descripcion, precio, cantidad , inpuesto, total)
        print("-------------------------------------------------\n"+ mensaje)
    else:
        print("verifique las opcciones ingresadas.")


# entardaas
tipo_hamburgesa = int(input("ingrese el tipo de hamburgesa \n1. sencilla \n2. doble \n3. triple\n "))
medio_pago= int(input("ingrese el medio de pago \n1. tarjeta \n2. otro \n"))
cantidad = int(input("ingree la cantidad: "))



#salidas
validar_datos(tipo_hamburgesa,medio_pago,cantidad)



























