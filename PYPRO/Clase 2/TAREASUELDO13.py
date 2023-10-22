numero =1
sueldo =0
total =0
while numero <=12:
 sueldo =int(input("Entre Sueldo :"))
 total = total + sueldo
 numero = numero + 1
print ("Total de Sueldos :", total)
print ("Sueldo 13: ", total / 12)