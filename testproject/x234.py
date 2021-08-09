import lokatorok
import osztalyok

# Pedig szívesen teszteltem volna a véletlenszámaimmal is. :)
feladat01 = osztalyok.Test_feladat01()
log = True
for i in range(len(lokatorok.tesztlista01)):  # 3 adatsorral teszteli.
    log = log and feladat01.test_tesztel(lokatorok.tesztlista01[i][0], lokatorok.tesztlista01[i][1],
                                         lokatorok.tesztlista01[i][2])
assert log
feladat01.driver.close()
