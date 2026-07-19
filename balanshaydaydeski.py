def przyrzuc(farma):
    tsilo=min(farma[:3])
    for i in range(3):
        k = farma[i] - tsilo - 1
        if k > 0:
            wolne_materialy[i] += k
            farma[i] = tsilo +1
    tbarn=min(farma[3:])
    for i in range(3, 6):
        k = farma[i] - tbarn - 1
        if k > 0:
            wolne_materialy[i] += k
            farma[i] = tbarn +1
            
            
def min_indeks_dol(farma):
    i=0
    for j in range(3):
                if farma[j]<farma[i]:
                    i=j
    return i   
    
def min_indeks_dol1(farma):
    i=1
    for j in range(1, 4):
                if farma[j%3]<farma[i]:
                    i=j%3
    return i      
    
def min_indeks_dol2(farma):
    i=2
    for j in range(2, 5):
                if farma[j%3]<farma[i]:
                    i=j%3
    return i             
  
      
def min_indeks_gora(farma):
    i=3
    for j in range(3, 6):
                if farma[j]<farma[i]:
                    i=j
    return i                
    
def min_indeks_gora1(farma):
    i=4
    for j in range(4, 7):
                if farma[j%3+3]<farma[i]:
                    i=j%3+3
    return i 
    
def min_indeks_gora2(farma):
    i=5
    for j in range(5, 8):
                if farma[j%3+3]<farma[i]:
                    i=j%3+3
    return i                                                              



liczba_farm = int(input("ile farm: "))
farmy= [[0, 0, 0, 0, 0, 0] for _ in range(liczba_farm)]
k=1
for farma in farmy:
    print("farma", k)
    farma[0]=int(input("ile gwozdzi: "))
    farma[1]=int(input("ile srubow: "))
    farma[2]=int(input("ile paneli: "))
    farma[3]=int(input("ile boltow: "))
    farma[4]=int(input("ile desek: "))
    farma[5]=int(input("ile tasiem: "))
    k +=1


wolne_materialy= [0 for _ in range(6)]

for i in range(liczba_farm):
    for j in range(i+1, liczba_farm):
        przyrzuc(farmy[j])
    
    indexdolny=min_indeks_dol(farmy[i])
    while wolne_materialy[indexdolny]:
        farmy[i][indexdolny] += 1
        wolne_materialy[indexdolny] -= 1
        indexdolny=min_indeks_dol(farmy[i]) 
        
    indexdolny=min_indeks_dol1(farmy[i])
    while wolne_materialy[indexdolny]:
        farmy[i][indexdolny] += 1
        wolne_materialy[indexdolny] -= 1
        indexdolny=min_indeks_dol1(farmy[i]) 
        
    indexdolny=min_indeks_dol2(farmy[i])
    while wolne_materialy[indexdolny]:
        farmy[i][indexdolny] += 1
        wolne_materialy[indexdolny] -= 1
        indexdolny=min_indeks_dol1(farmy[i]) 
        
    indexgorny=min_indeks_gora(farmy[i])
    while wolne_materialy[indexgorny]:
        farmy[i][indexgorny] += 1
        wolne_materialy[indexgorny] -= 1
        indexgorny=min_indeks_gora(farmy[i]) 
    
    indexgorny=min_indeks_gora1(farmy[i])
    while wolne_materialy[indexgorny]:
        farmy[i][indexgorny] += 1
        wolne_materialy[indexgorny] -= 1
        indexgorny=min_indeks_gora1(farmy[i]) 
    
    indexgorny=min_indeks_gora2(farmy[i])
    while wolne_materialy[indexgorny]:
        farmy[i][indexgorny] += 1
        wolne_materialy[indexgorny] -= 1
        indexgorny=min_indeks_gora2(farmy[i]) 
    przyrzuc(farmy[i])
    
print(farmy, "sprzedac: ", wolne_materialy)
