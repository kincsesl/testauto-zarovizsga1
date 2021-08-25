import objektum

f1 = objektum.Test_feladat01()

log = True

log = log and f1.tesztel("10", "314")
log = log and f1.tesztel("kiscica", "NaN")
log = log and f1.tesztel("", "NaN")
f1.driver.close()
assert log

