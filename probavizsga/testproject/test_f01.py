import objektum

def test_f01a():
    f1 = objektum.Test_feladat01()
    assert f1.tesztel("10", "314")
    f1.driver.close()

def test_f01b():
    f1 = objektum.Test_feladat01()
    assert f1.tesztel("kiscica", "NaN")
    f1.driver.close()

def test_f01c():
    f1 = objektum.Test_feladat01()
    assert f1.tesztel("", "NaN")
    f1.driver.close()
