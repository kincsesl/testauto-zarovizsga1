## 4 Feladat: Password mező

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a Password mező app-ot az [https://wonderful-pond-0d96a8503.azurestaticapps.net/f4.html](https://wonderful-pond-0d96a8503.azurestaticapps.net/f4.html) oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a password mező app tesztelését.

A cél az password validáció tesztelése:

* Helyes kitöltés esete:
    * email: teszt@elek.hu
    * jelszó: Kiscica1234
    * A Submit gomb megnyomása után átnavigál egy oldalra ahol a "404 Not Found" hibaüzenet látható. Ezt kell assertezned.

* Helytelen:
    * email: teszt@elek.hu
    * jelszó: a1
    * Megjelenik egy üzenet ami megmondja, mit kell tartalmazni a jelszónak. Ellenőrizd le, hogy:
      * number ellnőrzés valid jelzés ad
      * letter ellnőrzés valid jelzés ad
      * capital ellnőrzés invalid jelzés ad
      * length ellnőrzés invalid jelzés ad


Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!

### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `feladat4.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(
