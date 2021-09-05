## 6 Feladat: Caesar rejtjelező

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a Caesar rejtjelező app-ot az [https://witty-hill-0acfceb03.azurestaticapps.net/caesar.html](https://witty-hill-0acfceb03.azurestaticapps.net/caesar.html) oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Caesar rejtjelező app tesztelését.

TC01: helybenhagyás
 * Szöveg: abcd
 * Eltolás: 26
 * Titkosított szöveg: abcd

TC02: titokítás
 * Szöveg: abcd
 * Eltolás: 2
 * Titkosított szöveg: cdef

TC03: dekódolás
 * Szöveg: cdef
 * Eltolás: -2
 * Titkosított szöveg: abcd

Az ellenőrzésekhez teszt keretrendszert kell használnod (pytest)!

### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `feladat5.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(
