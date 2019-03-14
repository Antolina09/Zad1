m1 = [4,4,8,6,2]
m2 = [5,1,4,8,3]
m3 = [4,4,10,6,2]
m4 = [5,1,4,10,3]

zad = [0,1,2,3,4]

def wczytywanie_z_pliku(plik):
    tablica=[]
    m1, m2, m3 = [], [], []
    text_file = open(plik, "r+")
    for line in text_file.readlines():
        tablica.extend(line.split())

    j,k = 2,3
    l = 4
    liczba_zadan = int(tablica[0])
    liczba_maszyn = int(tablica[1])

    for i in range(liczba_zadan):
        m1.append(int(tablica[j]))
        m2.append(int(tablica[k]))
        m3.append(int(tablica[l]))
        j += liczba_maszyn
        k += liczba_maszyn
        #l += liczba_maszyn

    zadania = []
    for i in range(liczba_zadan):
        zadania.append(i)
    return m1, m2, zadania #,m3

def takeSecond(elem): #funkcja zwracjaca drugi element w tablicy dwuwymiarowej (potrzebna do polaczenia zadan z czasem)
    return elem[1]

def alg_Johnsona(m1,m2,zad):
    tab1, tab2, tab3, tab4, tab, tabx, tab32, tab42, tabx1, tab5, t1, t = [], [], [], [], [], [], [], [], [], [], [], []
    for i in range(len(zad)): 
        #sprawdzenie czasu zadan 
        #(jesli czas na maszynie 1 jest mniejszy od czasu na 2,
        #to to zadnaie jest dodawane do pierwszej tablicy, jak nie to do drugiej)
        if m1[i] <= m2[i]:
            tab1.append(zad[i])
        else:
            tab2.append(zad[i])
    
    if tab1 == [] or tab2 == []: #w przypadku gdy czasy wykonania zadan na ktorejs z maszyn sa zawsze wieksze od czasow drugiej
        cz1 = 0
        cz2 = 0
    
        for i in range(len(zad)): #obliczanie czasu wykonania zadań przez maszyny
            cz1 += m1[i]
        for i in range(len(zad)):
            cz2 += m2[i]
        luka = [0] #tablica zawierajace kolejne czasy oczekiwania maszyny 2 na mozliwosc wykonania zadania
        Cmax = 0
        for k in range(len(zad)-1):
            if m1[zad[k+1]] > m2[zad[k]]: #jezeli czas wykonywania nastpenego zadania przez maszyne 1 jest dłuzszy niz poprzedniego przez druga
                b1 = 0 #biezacy czas wykonywania zadań przez maszynę 1
                b2 = 0 #biezacy czas wykonywania zadań przez maszynę 2
                for j in range(k+2):
                    b1 += m1[zad[j]] #obliczanie biezacego czasu wykonywania zadan
                for j in range(k+1):
                    b2 += m2[zad[j]]
                for q in range(len(luka)):
                    l1 = 0
                    l1 += luka[q]
                if b2 + l1 + m1[zad[0]] < b1: #sprawdzenie czy wystapi luka
                    for q in range(len(luka)):
                        l = 0
                        l += luka[q] #obliczanie czasu jaki maszyna 2 musi czekac na wykonanie nastepnego zadania
                    luka.append(b1 - (b2 + m1[zad[0]] + l)) #dodanie kolejnej wartosci luki do tablicy
        Cmax = cz1 + (cz2-cz1) + m1[zad[0]] + l + luka[-1] #obliczanie lacznego czasu potrzbnego na wykonanie wszystkich zadan przez obie maszyny
        print("Cmax:", Cmax)
    else:       
        for i in range (len(tab1)): #stworzenie tablicy z czasami zadan podzielonych powyzej 
            tab3.append(m1[tab1[i]])
            tab32.append(m2[tab1[i]])
        print("tab3",tab3, "tab32", tab32)
        for i in range (len(tab2)):
            tab4.append(m1[tab2[i]])
            tab42.append(m2[tab2[i]])
    
        for j in range(len(tab1)): #przypisanie zadaniom czasu (z pierwszej tabeli)
            tab = tab + [[tab1[j],tab3[j]]] #dla pierwszej maszyny
            tabx = tabx + [[tab1[j],tab32[j]]] #dla drugiej
        for j in range(len(tab2)): #to samo tylko z drugiej
            tab5 = tab5 + [[tab2[j],tab4[j]]] 
            tabx1 = tabx1 + [[tab2[j],tab42[j]]]  


        tab = sorted(tab, key=takeSecond) #posortowanie czasu wykonywania zadan na 1 maszynie z maszyny 1 rosnaco 
        tabx1 = sorted(tabx1, key=takeSecond, reverse=True) #posortowanie czasu na 1 maszynie z maszyny 2 malejaco 
        tabx = sorted(tabx, key=takeSecond) #to samo tylko dla drugiej maszyny 
        tab5 = sorted(tab5, key=takeSecond, reverse=True) 

        t.extend(tab) #polaczenie czasow i zadan z pierwszej i drugiej tablicy w jedna (dla maszyny 1)
        t.extend(tab5)
        t1.extend(tabx) #to samo tylko dla drugiej
        t1.extend(tabx1)
        print(t1, t)
        cz1 = 0
        cz2 = 0
    
        for i in range(len(zad)): #obliczanie czasu wykonania zadań przez maszyny
            cz1 += m1[i]
        for i in range(len(zad)):
            cz2 += m2[i]

        luka = [0] #tablica zawierajace kolejne czasy oczekiwania maszyny 2 na mozliwosc wykonania zadania
        Cmax = 0
        for k in range(len(zad)-1):
            if t[k+1][1] > t1[k][1]: #jezeli czas wykonywania nastpenego zadania przez maszyne 1 jest dłuzszy niz poprzedniego przez druga
                b1 = 0 #biezacy czas wykonywania zadań przez maszynę 1
                b2 = 0 #biezacy czas wykonywania zadań przez maszynę 2
                for j in range(k+2):
                    b1 += t[j][1] #obliczanie biezacego czasu wykonywania zadan
                for j in range(k+1):
                    b2 += t1[j][1]
                for q in range(len(luka)):
                    l1 = 0
                    l1 += luka[q]
                if b2 + l1 + t[0][1] < b1: #sprawdzenie czy wystapi luka
                    for q in range(len(luka)):
                        l = 0
                        l += luka[q] 
                    luka.append(b1 - (b2 + t[0][1] + l)) #dodanie kolejnej wartosci luki do tablicy
                for q in range(len(luka)):
                        l = 0
                        l += luka[q] 
        Cmax = cz1 + (cz2-cz1) + t[0][1] + l #+ luka[-1] #obliczanie lacznego czasu potrzbnego na wykonanie wszystkich zadan przez obie maszyny
        print("Cmax:", Cmax)

#alg_Johnsona(m1,m2,zad)
#alg_Johnsona(m3,m4,zad)
ma = [3,4,3,2,5]
mb = [2,2,1,1,2]
#alg_Johnsona(ma,mb,zad)


zwrot = wczytywanie_z_pliku("ta000.txt")
masz1 = zwrot[0]
masz2 = zwrot[1]
zadania = zwrot[2]
print(masz1, masz2, zad)
alg_Johnsona(masz1,masz2,zadania)