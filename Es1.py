def menu():
    print("Menu.\nNew task\nRemove\nSorted\nClose")
    scelta=input()
    return int(scelta)
def insert(lista):
    print("Inserire il task: ",end='')
    task=input()
    lista.append(task)
    return lista
def rimuovi(lista):
    print("Cosa devo rimuovere? ",end='')
    task=input()
    if (task in lista):
        print("Rimosso")
        lista.remove(task)
    else:
        print("Non trovato")
    return lista

val=0
txt = open("task_list.txt","r")
contenuto=txt.read()
txt.close()
lista = contenuto.split("\n")
while val!=4:
    val=menu()
    if val==1:
        lista=insert(lista)
    elif val==3:
        ordinata=sorted(lista)
        print(ordinata)
    elif val==2:
        lista = rimuovi(lista)
txt = open("task_list.txt","w")

aus=""
l=1
N=len(lista)
for elem in lista:
    aus = aus + elem
    if l!=N:
        aus = aus + "\n"
    l=l+1
txt.write(aus)
txt.close()