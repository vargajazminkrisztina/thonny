

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, 88, 299]

#/

#//

#%

# == --> megegyezés

# != --> tagadás



for szam in lista:
    if szam % 2 == 0:
        print(f"A szám osztható kettövel: {szam}")
    if szam % 3 == 0:
        print(f"A szám osztható hárommal: {szam}")
    if szam % 3 != 0 or szam % 2 != 0:
        print(f"egyikkel sem osztható: {szam}")
    

     
     
     
     
     
     
     #else:
        #print(f"A szám SE kettövel SE hárommal oztható {szam}")
        
        
        

        

