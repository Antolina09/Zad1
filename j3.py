m1 = [4,4,8,6,2]
m2 = [5,1,4,8,3]
m3 = [4,4,10,6,2]

zad = [0,1,2,3,4]

def wczytywanie_z_pliku(plik):
    tablica=[]
    m1, m2, m3 = [], [], []
    text_file = open(plik, "r+")
    for line in text_file.readlines():
        tablica.extend(line.split())

    j,k,l = 2,3,4
    liczba_zadan = int(tablica[0])
    liczba_maszyn = int(tablica[1])

    for i in range(liczba_zadan):
        m1.append(int(tablica[j]))
        m2.append(int(tablica[k]))
        m3.append(int(tablica[l]))
        j += liczba_maszyn
        k += liczba_maszyn
        l += liczba_maszyn

    zadania = []
    for i in range(liczba_zadan):
        zadania.append(i)
    return m1, m2, m3, zadania


def takeSecond(elem): #funkcja zwracjaca drugi element w tablicy dwuwymiarowej (potrzebna do polaczenia zadan z czasem)
    return elem[1]

def liczenie_luk(m1,m2,p):
    luka = [0] #tablica zawierajace kolejne czasy oczekiwania maszyny 2 na mozliwosc wykonania zadania
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
            else:
                luka.append(0)
        else:
            luka.append(0)
    return luka

def liczenie_kolejnosci(m1,m2,m3,zad):
    t1, t2, tab1, tab2, kol, p1, p2, p3, p4 = [], [], [], [], [], [], [], [], []
    for i in range(len(zad)): #stworzenie dwoch pomocniczych tablic 
        t1.append(m1[i]+m2[i]) #pierwsza z suma odpowiednich czasów z maszyny 1 i 2
        t2.append(m2[i]+m3[i]) #druga z suma czasów z maszyny 2 i 3
    
    for i in range(len(zad)): 
        #sprawdzenie czasu zadan 
        #(jesli czas na maszynie 1 jest mniejszy od czasu na 2,
        #to to zadnaie jest dodawane do pierwszej tablicy, jak nie to do drugiej)
        if t1[i] <= t2[i]:
            tab1.append(zad[i])
        else:
            tab2.append(zad[i])

    for i in range(len(tab1)): #stworzenie pomocniczej tabeli z czasami dla zadan z t1
        p1.append(t1[tab1[i]])
    for i in range(len(tab2)): #stworzenie pomocniczej tabeli z czasami dla zadan z t2
        p2.append(t2[tab2[i]])

    for i in range(len(tab1)): #polaczenie tablic z zadaniami i czasami
        p3 = p3 + [[tab1[i],p1[i]]]
    for i in range(len(tab2)):
        p4 = p4 + [[tab2[i],p2[i]]]

    p3 = sorted(p3, key = takeSecond) #posortowanie tablicy wedlug czasu roznaco
    p4 = sorted(p4, key = takeSecond, reverse = True) #posortowanie tablicy wedlug czasu malejaco

    for i in range(len(tab1)): #stworzenie tablicy z odpowiednia kolejnościa zadan do wykonania 
        kol.append(p3[i][0])
    for i in range(len(tab2)):
        kol.append(p4[i][0])
    
    Cmax = 0
    luka1 = liczenie_luk(m1,m2,kol)

    p = []
    for i in range(len(luka1)):
        p.append(m2[kol[i]]+luka1[i])
    p[0] += (m1[kol[0]])      
    
    
    luka = [0]
    cz3 = 0
    for i in range(len(m3)):
        cz3 +=m3[i]
    
    luka2 = liczenie_luk(p,m3,kol)

    for q in range(len(luka2)):
        l2 = 0
        l2 += luka2[q]
    Cmax = cz3 + m1[kol[0]] + m2[kol[0]] + l2  #obliczanie lacznego czasu potrzbnego na wykonanie wszystkich zadan przez obie maszyny
    print("Cmax:", Cmax)


ma = [3,4,3,2,5]
mb = [2,2,1,1,2]
mc = [4,2,5,4,3]

d = [3,4,3,2,5]
e = [4,2,5,4,4]
f = [1,8,9,3,7]

liczenie_kolejnosci(d,e,f,zad)
liczenie_kolejnosci(ma,mb,mc,zad)
liczenie_kolejnosci(m1,m2,m3,zad)

zwrot = wczytywanie_z_pliku("ta000.txt")
masz1 = zwrot[0]
masz2 = zwrot[1]
masz3 = zwrot[2]
zadania = zwrot[3]

liczenie_kolejnosci(masz1,masz2,masz3,zadania)