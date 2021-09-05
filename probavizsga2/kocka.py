import random

n = 30  # Ennyi kockával dobok.
minta = 1000  # Ennyiszer.


def darabkocka_darabhatos(a):  # a db kockával dobok, visszaadja, hány 6-ost kaptam.
    darabhatos = 0
    for _ in range(a):  # Mivel i-t nem használom a cikluson belül, lehet _-lel helyettesíteni a változót.
        if random.randint(1, 6) == 6:
            darabhatos += 1
    return darabhatos


def hanylepes(db):  # Addig dob, míg el nem fogynak a kockák (eredetileg n db).
    lepesszam = 0
    while db > 0:
        lepesszam += 1
        db = db - darabkocka_darabhatos(db)  # Kiszedi a 6-osokat.
    return lepesszam


szum = 0
for _ in range(minta):
    szum += hanylepes(n)

print(szum / minta)
