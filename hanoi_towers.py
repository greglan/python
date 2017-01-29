def hanoi(n,t1,t2,t3): #t1 à déplacer, t2 temp, t3 cible
    # if n==1:
    #     t3.append(t1.pop())
    if n>1:
        hanoi(n-1, t1, t3, t2)
        hanoi(n-1, t2, t1, t3)

# t1 = [3,2,1];t2=[];t3=[];n=3

def hanoi_pile(n,t1,t2,t3):
    p = [[n,t1,t2,t3]]
    
    while p != []:
        i = p.pop()
        if i[0]>1:
            p.append(i[0]-1,i[1],i[3],i[2])
            # print
            p.append(i[0]-1,i[2],i[1],i[3])