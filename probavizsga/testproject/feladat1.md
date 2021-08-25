## 1 Feladat: Keressük a kör területét

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a kör területe app-ot az [https://wonderful-pond-0d96a8503.azurestaticapps.net/f1.html](https://wonderful-pond-0d96a8503.azurestaticapps.net/f1.html) oldalról.

Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a kör területe appban:

Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!

* Helyes kitöltés esete:
    * r: 10
    * Eredmény: 314

* Nem számokkal történő kitöltés:
    * r: kiscica
    * Eredmény: NaN

* Üres kitöltés:
    * r: <üres>
    * Eredmény: NaN   

### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `feladat1.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(
