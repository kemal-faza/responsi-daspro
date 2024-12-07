# Nama File: matematika_gura.py
# Pembuat: Muhamad Kemal Faza - 24060124120013
# Tanggal: 03/12/2024
# Deskripsi: Mengembalikan list hasil tambah-tambah dua buah list sebagai representasi integer.

# DEFINISI DAN SPESIFIKASI
# shrimp --> list: integer
# shrimp(X, Y) mengembalikan list hasil tambah-tambah dua buah list sebagai representasi integer.


# REALISASI


def konso(e, L):
    return [e] + L


def konsi(L, e):
    return L + [e]


def first_elmt(L):
    return L[0]


def last_elmt(L):
    return L[-1]


def head(L):
    return L[:-1]


def tail(L):
    return L[1:]


def is_empty(L):
    return len(L) == 0


def dimensi(L):  # atau NbElmt()
    if is_empty(L):
        return 0
    else:
        return 1 + dimensi(tail(L))


def tambah(X, Y, carry):
    plus = lambda a, b, cry: a + b + cry
    isCarry = lambda plus: 1 if plus > 9 else 0
    sisa = lambda plus: plus % 10

    if is_empty(X) and is_empty(Y):
        return []
    elif is_empty(X):
        return konsi(
            tambah(X, head(Y), isCarry(plus(0, last_elmt(Y), carry))),
            sisa(plus(0, last_elmt(Y), carry)),
        )
    elif is_empty(Y):
        return konsi(
            tambah(head(X), Y, isCarry(plus(last_elmt(X), 0, carry))),
            sisa(plus(last_elmt(X), 0, carry)),
        )
    else:
        return konsi(
            tambah(head(X), head(Y), isCarry(plus(last_elmt(X), last_elmt(Y), carry))),
            sisa(plus(last_elmt(X), last_elmt(Y), carry)),
        )


def kurang(X, Y, carry):
    minus = lambda a, b, cry: a - b - cry
    isCarry = lambda minus: 1 if minus < 0 else 0
    sisa = lambda minus: minus + 10 if minus < 0 else minus

    if is_empty(X) and is_empty(Y):
        return []
    elif dimensi(X) < dimensi(Y) - 1:
        return [X, Y]
    # [2] ['-', 1, 2]

    # elif last_elmt(Y) == "-":
    #     if is_empty(X):
    #         return []
    #     else:
    #         if sisa(minus(last_elmt(X), 0, carry)) == 0:
    #             return []
    #         else:
    #             return konsi(
    #                 kurang(head(X), Y, isCarry(minus(last_elmt(X), 0, carry))),
    #                 sisa(minus(last_elmt(X), 0, carry)),
    #             )
    else:
        if (is_empty(head(X)) or is_empty(head(Y))) and sisa(
            minus(last_elmt(X), last_elmt(Y), carry)
        ) == 0:
            return []
        else:
            return konsi(
                kurang(
                    head(X), head(Y), isCarry(minus(last_elmt(X), last_elmt(Y), carry))
                ),
                sisa(minus(last_elmt(X), last_elmt(Y), carry)),
            )


def shrimp(X, Y):
    if first_elmt(X) != "-" and first_elmt(Y) != "-":
        return tambah(X, Y, 0)
    elif first_elmt(X) != "-" and first_elmt(Y) == "-":
        # if dimensi(X) < dimensi(Y) - 1:
        #     return konso("-", kurang(tail(Y), konso("-", X), 0))
        # else:
        return kurang(X, Y, 0)
    elif first_elmt(X) == "-" and first_elmt(Y) != "-":
        if dimensi(X) - 1 > dimensi(Y):
            return konso("-", kurang(tail(Y), konso("-", X), 0))
        else:
            print(tail(X), konso("-", Y), 0)
            return kurang(tail(X), konso("-", Y), 0)


def skalaKePixel(skala):
    return (skala / 5) * 570


print(skalaKePixel(4.33))

# APLIKASI
# print(shrimp([1, 2, 3], [9]))
# print(shrimp([4, 2, 3, 3, 1], [2, 3, 3, 4, 5, 9, 3, 1, 4]))
# print(shrimp([1, 2, 3], ["-", 9]))
# print(shrimp([1, 3], ["-", 1, 2]))
# print(shrimp([1, 3], ["-", 1, 2, 3]))
# print(shrimp([1, 0], ["-", 1, 2]))
# print(shrimp([2], ["-", 1, 2]))
# print(eval(input()))
