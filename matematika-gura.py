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


def Digit(X, Y):
    if is_empty(X) or is_empty(Y):
        return []
    else:
        if dimensi(X) > dimensi(Y):
            return Digit(X, konso(0, Y))
        elif dimensi(X) < dimensi(Y):
            return Digit(konso(0, X), Y)
        else:
            return [X] + Y


# fungsi BesarMana mngembalikan tanda dari bilangan antara positif atau negatif dan tanda mengeikuti bilangan yang paling besar antara X dan Y.


def BesarMana(X, Y, tandaX, tandaY):
    if is_empty(X):
        return []
    else:
        if first_elmt(X) > first_elmt(Y):
            if tandaX == "+":
                return []
            return [tandaX]
        elif first_elmt(Y) > first_elmt(X):
            if tandaY == "+":
                return []
            return [tandaY]
        else:
            return BesarMana(tail(X), tail(Y), tandaX, tandaY)


# fungsi BesarX mengembalikan boolean untuk mengetahui apakah X lebih dari Y agar pengurangan tidak ada yang menjadi negatif


def BesarX(X, Y):
    if is_empty(X):
        return False
    else:
        if first_elmt(X) > first_elmt(Y):
            return True
        elif first_elmt(Y) > first_elmt(X):
            return False
        else:
            return BesarX(tail(X), tail(Y))


# fungsi penghitung untuk menghitung X dan Y tergantung dari tanda X dan tanda Y. parameter b adalah boolean dari hasil BesarX(X,Y). parameter e berguna untuk carry menyimpan data sebelumnya.


def penghitung(X, Y, e, tandaX, tandaY, b):
    if is_empty(X):
        if e == 1:
            return [e]
        else:
            return []
    else:
        if tandaX == "-" and tandaY == "-" or (tandaX == "+" and tandaY == "+"):
            if last_elmt(X) + last_elmt(Y) + e > 9:
                return konsi(
                    penghitung(head(X), head(Y), 1, tandaX, tandaY, b),
                    last_elmt(X) + last_elmt(Y) + e - 10,
                )
            else:
                return konsi(
                    penghitung(head(X), head(Y), 0, tandaX, tandaY, b),
                    (last_elmt(X) + last_elmt(Y) + e),
                )
        elif tandaX == "-" and tandaY == "+" or (tandaX == "+" and tandaY == "-"):
            if b:
                if last_elmt(X) >= last_elmt(Y):
                    return konsi(
                        penghitung(head(X), head(Y), 0, tandaX, tandaY, b),
                        (last_elmt(X) - last_elmt(Y) + e) % 10,
                    )
                else:
                    return konsi(
                        penghitung(head(X), head(Y), -1, tandaX, tandaY, b),
                        10 + last_elmt(X) - last_elmt(Y) + e,
                    )

            else:
                if last_elmt(Y) >= last_elmt(X):
                    return konsi(
                        penghitung(head(X), head(Y), 0, tandaX, tandaY, b),
                        (last_elmt(Y) - last_elmt(X) + e) % 10,
                    )
                else:
                    return konsi(
                        penghitung(head(X), head(Y), -1, tandaX, tandaY, b),
                        10 + last_elmt(Y) - last_elmt(X) + e,
                    )


# fungsi hapus untuk menghapus angka 0 di awal list X. contoh [0,1,1] harusnya [1,1]


def hapus(X):
    if is_empty(X):
        return []
    elif first_elmt(X) != 0:
        return X
    else:
        if first_elmt(X) == 0 and is_empty(tail(X)):
            return X
        else:
            return hapus(tail(X))


def shrimp(X, Y):
    if is_empty(X) and is_empty(Y):
        return []
    elif is_empty(X) and not is_empty(Y):
        return Y
    elif is_empty(Y) and not is_empty(X):
        return X
    else:
        if first_elmt(X) == "-" and first_elmt(Y) == "-":
            return BesarMana(
                first_elmt(Digit(tail(X), tail(Y))),
                tail(Digit(tail(X), tail(Y))),
                "-",
                "-",
            ) + penghitung(
                first_elmt(Digit(tail(X), tail(Y))),
                tail(Digit(tail(X), tail(Y))),
                0,
                "-",
                "-",
                BesarX(
                    first_elmt(Digit(tail(X), tail(Y))), tail(Digit(tail(X), tail(Y)))
                ),
            )

        elif first_elmt(X) == "-" and first_elmt(Y) != "-":
            return BesarMana(
                first_elmt(Digit(tail(X), Y)), tail(Digit(tail(X), Y)), "-", "+"
            ) + hapus(
                penghitung(
                    first_elmt(Digit(tail(X), Y)),
                    tail(Digit(tail(X), Y)),
                    0,
                    "-",
                    "+",
                    BesarX(first_elmt(Digit(tail(X), Y)), tail(Digit(tail(X), Y))),
                )
            )

        elif first_elmt(X) != "-" and first_elmt(Y) == "-":
            return BesarMana(
                first_elmt(Digit(X, tail(Y))), tail(Digit(X, tail(Y))), "+", "-"
            ) + hapus(
                penghitung(
                    first_elmt(Digit(X, tail(Y))),
                    tail(Digit(X, tail(Y))),
                    0,
                    "+",
                    "-",
                    BesarX(first_elmt(Digit(X, tail(Y))), tail(Digit(X, tail(Y)))),
                )
            )

        else:
            return BesarMana(
                first_elmt(Digit(X, Y)), tail(Digit(X, Y)), "+", "+"
            ) + penghitung(
                first_elmt(Digit(X, Y)),
                tail(Digit(X, Y)),
                0,
                "+",
                "+",
                BesarX(first_elmt(Digit(X, Y)), tail(Digit(X, Y))),
            )


# APLIKASI
# print(shrimp([1, 2, 3], [9]))
# print(shrimp([4, 2, 3, 3, 1], [2, 3, 3, 4, 5, 9, 3, 1, 4]))
# print(shrimp([1, 2, 3], ["-", 9]))
# print(shrimp([1, 3], ["-", 1, 2]))
# print(shrimp([1, 3], ["-", 1, 2, 3]))
# print(shrimp([1, 0], ["-", 1, 2]))
print(shrimp([2], ["-", 1, 2]))
# print(eval(input()))
