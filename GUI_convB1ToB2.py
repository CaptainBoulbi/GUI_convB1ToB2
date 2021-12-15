from tkinter import *

def convB1ToB2 (strr, base, baseOut, carac = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","²","*","/","+","-","∞"]):
##					       0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  42

	strr = strr.upper()
	if base <= 1 or baseOut <= 1 :
		return "Error : base cannot be less than 1"
	if base == baseOut :
		return strr

	nb = 0
	nbOut = ""
	indice = 0

	for i in range(0,len(strr)):

		indice -= 1
		for i in range(0, len(carac)):
			if strr[indice] == carac[i] or carac[i] == carac[base-1]:
				nb += i*(base**((indice+1)*-1))
				break

	if baseOut == 10 :
		return nb

	indice = 0
	while nb // baseOut**indice >= baseOut :
		indice += 1

	while indice != -1 :
		if nb//baseOut**indice <= baseOut :
			nbOut += str(carac[nb//baseOut**indice])
			nb -= baseOut**indice*(nb//baseOut**indice)
		else :
			nbOut += "0"
		indice -= 1

	return nbOut

def conv():

	nbb = str(Val.get())
	basee = 0
	baseeOut = 0

	if base.get() == 1:
		basee = 10
	elif base.get() == 2:
		basee = 16
	elif base.get() == 3:
		basee = 2
	elif base.get() == 4:
		basee = int(perso.get())

	if baseOut.get() == 1:
		baseeOut = 10
	elif baseOut.get() == 2:
		baseeOut = 16
	elif baseOut.get() == 3:
		baseeOut = 2
	elif baseOut.get() == 4:
		baseeOut = int(toPerso.get())

	convertit.set(str(convB1ToB2(nbb, basee, baseeOut)))

base = 0
baseOut = 0

fenetre=Tk()
fenetre.geometry('425x250')


lTitle=Label(fenetre, text="Convertisseur valeur X)b1 vers Y)b2\nBase max : 42").pack()
bExit=Button(text="QUITTER", command=fenetre.destroy).pack(side=BOTTOM)
bConv=Button(text="Convertir", command=conv).pack(side=BOTTOM)


fBase=Frame(fenetre)
fToBase=Frame(fenetre)
fVal=Frame(fenetre)

base=IntVar()
perso=StringVar()
lInfo=Label(fBase,text="Base de la valeur").pack(anchor=W)
bDec=Radiobutton(fBase, text="Decimal", variable = base, value = 1, indicatoron=0,width=15).pack(anchor=W)
bHexa=Radiobutton(fBase, text="Hexadecimal", variable = base, value = 2, indicatoron=0,width=15).pack(anchor=W)
bBin=Radiobutton(fBase, text="Binaire", variable = base, value = 3, indicatoron=0,width=15).pack(anchor=W)
lSpace=Label(fBase, text="").pack(anchor=W)
bPerso=Radiobutton(fBase, text="Personnalisé", variable = base, value = 4, indicatoron=0,width=15).pack(anchor=W)
ePerso=Entry(fBase, textvariable=perso).pack(anchor=W)
fBase.pack(side=LEFT)

baseOut=IntVar()
toPerso=StringVar()
lToInfo=Label(fToBase,text="Convertion vers base").pack(anchor=W)
bToDec=Radiobutton(fToBase, text="Decimal", variable = baseOut, value = 1, indicatoron=0,width=15).pack(anchor=W)
bToHexa=Radiobutton(fToBase, text="Hexadecimal", variable = baseOut, value = 2, indicatoron=0,width=15).pack(anchor=W)
bToBin=Radiobutton(fToBase, text="Binaire", variable = baseOut, value = 3, indicatoron=0,width=15).pack(anchor=W)
lSpace=Label(fToBase, text="").pack(anchor=W)
bToPerso=Radiobutton(fToBase, text="Personnalisé", variable = baseOut, value = 4, indicatoron=0,width=15).pack(anchor=W)
eToPerso=Entry(fToBase, textvariable=toPerso).pack(anchor=W)
fToBase.pack(side=RIGHT)

Val=StringVar()
convertit=IntVar()
lSpace=Label(fVal, text="").pack()
lCons=Label(fVal, text="Entrez la valeur a convertir :").pack()
eVal=Entry(fVal, textvariable=Val).pack()
lSpace=Label(fVal, text="").pack()
lResText=Label(fVal,text="Le resultat est :").pack()
lRes=Label(fVal,textvariable=convertit).pack()
lSpace=Label(fVal, text="").pack()
fVal.pack(side=BOTTOM)


fenetre.mainloop()
