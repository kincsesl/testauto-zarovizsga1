import lokatorok
import osztalyok


feladat04 = osztalyok.Test_feladat04()

log = True
for elem in lokatorok.tesztlista04:
    print(feladat04.test_tesztel(elem[0], elem[1]))
assert log

feladat04.driver.close()
