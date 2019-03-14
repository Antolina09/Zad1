m1 = [4,4,10,6,2]
m2 = [5,1,4,10,3]
zad = [0,1,2,3,4]

def permute(zad, low=0): #obliczanie permutacji
    if low + 1 >= len(zad):
        yield zad
    else:
        for p in permute(zad, low + 1):
            yield p        
        for i in range(low + 1, len(zad)):        
            zad[low], zad[i] = zad[i], zad[low]
            for p in permute(zad, low + 1):
                yield p        
            zad[low], zad[i] = zad[i], zad[low]

def liczenie_luk(m1,m2,p):
    luka = [0] #tablica zawierajace kolejne czasy oczekiwania maszyny 2 na mozliwosc wykonania zadania
    Cmax = 0
    for k in range(len(p)-1):
        if m1[p[k+1]] > m2[p[k]]: #jezeli czas wykonywania nastpenego zadania przez maszyne 1 jest dłuzszy niz poprzedniego przez druga
            b1 = 0 #biezacy czas wykonywania zadań przez maszynę 1
            b2 = 0 #biezacy czas wykonywania zadań przez maszynę 2
            for j in range(k+2):
                b1 += m1[p[j]] #obliczanie biezacego czasu wykonywania zadan
            for j in range(k+1):
                b2 += m2[p[j]]
            for q in range(len(luka)):
                l1 = 0
                l1 += luka[q]
            if b2 + l1 + m1[p[0]] < b1: #sprawdzenie czy wystapi luka
                for q in range(len(luka)):
                    l = 0
                    l += luka[q] #obliczanie czasu jaki maszyna 2 musi czekac na wykonanie nastepnego zadania
                luka.append(b1 - (b2 + m1[p[0]] + l)) #dodanie kolejnej wartosci luki do tablicy
    return luka

def liczenie_czasu(m1,m2,zad):
    cz1 = 0 #łączny czas wykonania zadań przez maszynę 1
    cz2 = 0 #łączny czas wykonania zadań przez maszynę 2
    for i in range(len(m1)): #obliczanie czasu wykonania zadań przez maszyny
        cz1 += m1[i]
    for i in range(len(m2)):
        cz2 += m2[i]

    for p in permute(zad):
        luka = liczenie_luk(m1,m2,p)
        Cmax = 0
        for i in range(len(luka)):
            l = 0
            l += luka[i]
        Cmax = cz1 + (cz2-cz1) + m1[p[0]] + l  #obliczanie lacznego czasu potrzbnego na wykonanie wszystkich zadan przez obie maszyny
        print("Permutacja:", p, "Cmax:", Cmax)
       
        
liczenie_czasu(m1,m2,zad) 
