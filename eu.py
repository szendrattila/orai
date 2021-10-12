#Ausztria;1995.01.01
f = open("EUcsatlakozas.txt", "r", encoding="ISO8859-2")
lista = []
for i in f:
    print(i)
    lista.append(i.strip().split(";"))
    
f.close()
#3. feladat EU tagállamainak száma : ? db
print(f"3. feladat EU tagállamainak száma : {len(lista)} db")

#4. feladat: 2007-ben ? ország csatlakozott
szamlalo = 0
for i in lista:
    if i[1][0:4] == "2007":
        szamlalo += 1
print(f"4. feladat: 2007-ben {szamlalo} ország csatlakozott")

#5. feladat Magyarország csatlakozásának dátuma: ?
for i in lista:
    if i[0] == "Magyarország":
        print(f"5. feladat Magyarország csatlakozásának dátuma: {i[1]}")
#6. feladat Májusban ? csatlakozás!
volt_csatlakozas = False
for i in lista:
    if i[1][5:7] == "05":
        volt_csatlakozas = True
        
if volt_csatlakozas:
    print("6. feladat Májusban volt csatlakozás!")
else:
    print("6. feladat Májusban nem volt csatlakozás!")
#7. feladat: Legutoljára csatlakozott ország: ?
utoljara = ""
for i in lista:
    if i[1] > utoljara:
        utoljara = i[1]
        orszag = i[0]
print(f"7. feladat: Legutoljára csatlakozott ország: {orszag}")
