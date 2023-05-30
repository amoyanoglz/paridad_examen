from bytes import bytes_a_comprobar

suma_par = int(0)

for i in bytes_a_comprobar:
    for x in i:
        if x == 1:
            suma_par = suma_par + 1

    if suma_par % 2 != 0:
        print(f"error en byte {bytes_a_comprobar.index(i) +  1} {i}")
    else:
        print(f"byte {bytes_a_comprobar.index(i) +  1} OK")
    suma_par = int(0)
