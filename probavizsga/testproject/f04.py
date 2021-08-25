import objektum
import lokatorok

f4 = objektum.Test_feladat04()

log = f4.tesztel(lokatorok.helyesemil, lokatorok.helyesjelszo, "", "", "", "")
log = log and f4.tesztel(lokatorok.helyesemil, lokatorok.helytelenjelszo, "valid", "invalid", "valid", "invalid")

f4.driver.close()
assert log
