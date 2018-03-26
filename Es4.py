def init(rit):
    fin = open("dictionary.txt","r")
    lettura = fin.read()
    fin.close()
    rit = {}
    rows = lettura.split("\n")
    for riga in rows:
        i=riga.find("{")
        sub=riga[i+1:len(riga)-1]    #le stringhe sono immutabili tanto
        pezzi=sub.split("\', \'")
        task = pezzi[0]
        urgenza = pezzi[1]
        #qui faccio la parte di task
        pezzi=task.split("\': \'")
        task=pezzi[1]
        #qui faccio urgenza
        pezzi=urgenza.split("\': ")
        urgenza=pezzi[1]
     #   print(task,urgenza)
        rit[task]=urgenza
    return rit

#main
dizionario = {}
dizionario = init(dizionario)
finale = {}
for key in dizionario:
    val=dizionario[key]
    if val=="True":
        finale[key] = val

print(finale)