import objektum

def test_f05():
    f5 = objektum.Test_feladat05()
    log = f5.tesztel()
    f5.driver.close()
    assert log
