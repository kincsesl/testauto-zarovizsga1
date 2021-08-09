# Jó lett volna meghatározni a specifikációban a lehetséges műveleteket.

import osztalyok

feladat03 = osztalyok.Test_feladat03() #Nem bírtam ki, hogy ne szabadítsak rá egy ciklust. :)

for i in range(20):
    assert feladat03.test_tesztel()
    feladat03.driver.refresh()
