# Nama : Muhamad Kemal Faza - 24060124120013
# Tanggal : 03/12/2024


def FirstElmt(L):
    return L[0]


def LastElmt(L):
    return L[-1]


def Head(L):
    return L[:-1]


def Tail(L):
    return L[1:]


def Konso(e, L):
    return [e] + L


def isEmpty(L):
    return L == []


def dimensi(L):  # atau NbElmt()
    if isEmpty(L):
        return 0
    else:
        return 1 + dimensi(Tail(L))


def DuelSihir(S, M):
    # Tulis algoritma di sini
    return PoinMenang(S, M, [], [])


def PoinMenang(S, M, lvlS, lvlM):
    if isEmpty(S) and isEmpty(M):
        if dimensi(lvlS) > dimensi(lvlM):
            return "Snape Menang"
        elif dimensi(lvlS) < dimensi(lvlM):
            return "McGonagall Menang"
        else:
            return "Keduanya Seri"
    elif FirstElmt(S) == FirstElmt(M):
        return PoinMenang(Tail(S), Tail(M), lvlS, lvlM)
    elif FirstElmt(S) > FirstElmt(M):
        return PoinMenang(Tail(S), Tail(M), Konso(1, lvlS), lvlM)
    elif FirstElmt(S) < FirstElmt(M):
        return PoinMenang(Tail(S), Tail(M), lvlS, Konso(1, lvlM))


# PRINT
# print(eval(input()))
print(DuelSihir([10, 20], [15, 10]))
print(DuelSihir([50, 40, 30], [20, 30, 40]))
print(
    DuelSihir(
        [100, 20, 30, 40, 50, 60, 70, 80, 90, 10],
        [10, 90, 80, 70, 60, 50, 40, 30, 20, 100],
    )
)

# Selamat Menikmati
