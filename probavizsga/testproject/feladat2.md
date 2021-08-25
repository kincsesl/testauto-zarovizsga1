## 2 Feladat: Kártya

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a kártyakeverés app-ot az [https://wonderful-pond-0d96a8503.azurestaticapps.net/f2.html](https://wonderful-pond-0d96a8503.azurestaticapps.net/f2.html) oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a kártyakeverő app tesztelését.

Az alkalmazás akkor működik helyesen ha 52 gombnyomásból legalább van 4db 9-es szám. Ezt kell ellenőrizned.


Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!


### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `feladat2.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(
