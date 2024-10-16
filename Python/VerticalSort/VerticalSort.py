n,m = map(int,input().split())
lista = []
for i in range(m):
    lista.append(map(int,input().split()))

transpozycja = list(zip(*lista))

posortowanekolumny = [sorted(col) for col in transpozycja]

listaposortowana = list(zip(*posortowanekolumny))

for i in listaposortowana:
    print(*i)