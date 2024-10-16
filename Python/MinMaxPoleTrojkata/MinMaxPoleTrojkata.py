from itertools import combinations

def P(p1,p2,p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2


def FC(N):
    najmniejsze = 10000000
    najwieksze = -11111111

    if N < 3 or N > 20:
        return 0

    tab = []

    # Wczytanie współrzędnych punktów
    for i in range(N):
        tab.append(list(map(int, input().split())))
        if tab[i][0] < -100 or tab[i][0] > 100 or tab[i][1] < -100 or tab[i][1] > 100:
            return 0

    # Generowanie wszystkich możliwych trójkątów
    triangles = combinations(tab, 3)
    for triangle in triangles:
        area = P(*triangle)
        if area > 0:
            najmniejsze = min(najmniejsze, area)
            najwieksze = max(najwieksze, area)

    return najmniejsze, najwieksze


N = int(input())
a, b = FC(N)
print(f"{a} {b}")


