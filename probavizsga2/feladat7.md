## 7 Feladat: Stopper kihívás

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a Stopper kihívás app-ot az [https://witty-hill-0acfceb03.azurestaticapps.net/stopwatch.html](https://witty-hill-0acfceb03.azurestaticapps.net/stopwatch.html) oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Stopper kihívás app tesztelését.

TC01: iduláskor a stopper 00:00:00 értéket mutat

TC02: 6 másodperchez közel megállítás +-1 mp-en belül
 - Itt az a kihívás, hogy a start link megnyomása után pontosan 6 másodperc 
   után picivel nyomjuk meg a stop gombot és nézzük meg, hogy az óra 00:06:00 és 00:06:99 között állt meg

TC03: újrakezdés és stop után az óra kissebb értéket mutat, mint azelőtt, tehát újra indítható
 - Itt az a kihívás, hogy a restart nem egyszerűen leállítja az órát, hanem el is indítja a stoppert.
   Ezért egyből egy stop linket is kell nyomni, hogy megáljon és vizsgálhassuk a feltételt.

Az ellenőrzésekhez teszt keretrendszert kell használnod (pytest)!

### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `feladat5.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(
