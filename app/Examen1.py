class Examen1:

    def box(self, entrada):
	stri = ''
        suma = 0
        cont = 0

        for x in range(1, int(entrada)):
            if x % 2 == 0 and x % 3 == 0:
                stri += str(x) + '\n'
                cont += 1
                suma += x
	
	stri += "Suma = " + str(suma) + '\n' + "Cantidad = " + str(cont) + '\n'
	print(stri)	
	stri
	return stri
