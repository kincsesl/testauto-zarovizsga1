import objektum

def test_f02():
    f2 = objektum.Test_feladat02()
    log = f2.tesztel()
    f2.driver.close()
    assert log
