import objektum

def test_f03():
    f3 = objektum.Test_feladat03()
    log = f3.tesztel()
    f3.driver.close()
    assert log
