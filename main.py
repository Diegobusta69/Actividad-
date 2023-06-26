from actividadprueba import *
import os
os.system("cls")
import time

sw = True
try:
    while sw:
        print("Bienvenido a contiuacion elija una opcion")
        opcion = int (input("1).Calcular IVA\n2).Calcular descuento\n3).Calcular IMC\n4).Salir\n"))
        if opcion==1:
            valor = float(input("Ingrese un valor: " ))
            IVA = calcularIVA(valor)
            print(f"este es el valor de su iva {IVA}")
#----------------------------------------------------------------------------------------            
        elif opcion==2:
            valor = int(input("Ingrese un valor para hacer descuento: " ))
            descuento = float(input("Ingrese su descuento:  " ))
            dsc = descuento(valor,descuento)
            print(f"el valor de su descuento es {descuento},el valor es {valor} es de {dsc}")
#--------------------------------------------------------------------------------------------        
        elif opcion==3:
            estatura = float (input("Ingrese su estatura: " ))
            masa = float (input("Ingrese su peso en kg: " ))
            imc = IMC (estatura,masa)
            if imc <18.5:
                print("usted esta bajo peso")
            elif imc > 18.5 and 24.9:
                print("su peso esta adecuado")
            elif imc >= 25.0 and imc <= 29.9:
                print(f"usted esta con sobrepeso su imc es {round(imc,2)}")
            elif imc >=30.0 and imc <= 34.9:
                print(f"usted tiene obesidad grado 1 {round(imc,2)}")
            elif imc >= 35.0 and imc <= 39.9:
                print(f"su imc es {round(imc,2)}, usted tiene obesidad grado 2")
            elif imc>40:
                print(f"su imc es {round(imc,2)}, usted tiene tiene obesidad grado 3")
#-----------------------------------------------------------------------------------------        
        elif opcion==4:
            print("no vuelva")
        time.sleep(2)
        sw = False
        os.system("cls")
        
except:
    print("error intentelo nuevamente")
        
        
        
        
