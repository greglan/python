#Indique si un changement de signe à lieu dans une liste

def changement_signe(var) :
    s=0;
    for x in range(0, len(var)-1):
        if var[x] == 0:
            print("Terme "+str(x)+" nul");
            current = 1;
            second = 1;
        elif var[x+1] == 0:
            print("Terme "+str(x+1)+" nul");
            print("Test de changement de signe entre le terme "+str(x)+" et le terme "+str(x+2));
            if abs(var[x]) == var[x] :
                current = 1;
            else :
                current = -1;
            if abs(var[x+2]) == var[x+2] :
                second = 1;
            else :
                second = -1;
        else :
            if abs(var[x]) == var[x] :
                current = 1;
            else :
                current = -1;
            if abs(var[x+1]) == var[x+1] :
                second = 1;
            else :
                second = -1;
        if current*second < 0:
            print("Changement de signe: Terme "+str(x+1)+" et le terme "+str(x+2));
            s = s + 1;
    print(str(s)+" changement de signe détectés");