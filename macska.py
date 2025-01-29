szam=-3
if szam > 0:
    print(szam , "nagyobb mint 0")
if szam ==6:
    print(szam , "megegyezik 0 -al")

else:
    print(szam , "kisebb mint 0")
bekeres=input("mi a neved ? ")
if bekeres == "béla":
   print(bekeres,"szia")
else:
    print(bekeres, "szia valaki")
    
könyvek=[1,2,10,12,34,2.3,True,"macska6",7]
print(type(könyvek))
print(könyvek)
könyvek_1=könyvek[-3]
print(könyvek_1)
for elem in könyvek:
    print(elem)
    if elem=="macska":
        print("szia cirmi")