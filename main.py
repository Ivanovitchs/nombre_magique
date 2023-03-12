import random;
def nbre_magic(min,max):
    nbr_int=0
    while nbr_int==0:
        try:
            nbre_str=input("entrer le nombre magic compris entre " + str(min) + " et " + str(max) + " ? " ) 
            nbr_int=int(nbre_str)
        except ValueError:
            print("veillez entre un nombre correcte ")
        else:
            if nbr_int>max or nbr_int<min:
                print("Attention veillez entre un nombre entre " + str(min) + " et " + str(max))
                nbr_int=0

    return nbr_int

        

NBRE_MIN=5
NBRE_MAX=20
nbr=random.randint(NBRE_MIN,NBRE_MAX)
nbrvie=3
vie=nbrvie
nbres_magic=0
while not nbres_magic==nbr and vie>0:
    print("il vous reste" + vie + "vie" )
    nbres_magic=nbre_magic(NBRE_MIN,NBRE_MAX)
    if nbres_magic > nbr:
        print("le nombre recherché est plus petit que celui entré")
        vie -= 1
    elif nbres_magic < nbr:
        print("le nombre magique est plus grand que celui que vous avez saisis")
        vie -= 1
    else:
        print("Bravo vous avez gagnés")

if vie<=0:
    print("vous avez perdu le nombre de vie etait de " + str(nbrvie) )


