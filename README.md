### Wykonane

- **(done)** Dodanie zmiany gracza dopiero po ruchu, a nie w dowolnym momencie.
- **(done)** Dodanie funkcjonalności, że jeśli jest ostatni index patha przed kotwiczeniem (kwadracik o jasnym kolorze), to może się poruszyć do bazy o danym rzucie kostki.
- **(done)** Dodanie kilku pionków w grze.
- **(done)** Dopisanie funkcji, która sprawdza, czy koniec gry, czyli czy gracz zakotwiczył 4 pionki.
- **(done)** Naprawienie działania licznika ruchów.
- **(done)** Zastanowienie się, czy potrzebne jest rysowanie poprawionego matrixa po zakończeniu pierwszej pętli.
- **(done)** Wybór ilości graczy.
- **(done)** Jeżeli pionki różnego koloru najdą na siebie, to wracają do bazy.
- **(done)** Wybór ruchu pionka, jeżeli jest ich kilka na mapie.
- **(done)** Pytanie, czy dodać nowego pionka, jeżeli jeszcze można, oraz pytanie, którego pionka użyć.
- **(done ecebc4c)** Nie można odmówić postawienia pionka, jeżeli ma się 0 na planszy.
- **(done 33e79c5)** Zbugowane klikanie ruchem pionka - jeśli klikniemy kilka klawiszy ruchu, to buguje się (zmieniona kolejność w kodzie `for event in pygame.event.get()`).
- **(done eeee7be)** Jeżeli pionki tego samego koloru najdą na siebie, to stakują się (jest różnica między 1 pionkiem a kilkoma na jednej pozycji).
- **(done 51fa50f)** Zrobienie oznaczenia szachownicy takie jak w szachach (A-F 1-8) i dodanie efektów pociachania planszy jak w szachach.
- **(done - rare event 697e63b)** Jeżeli na 2. miejscu stoją 4 pionki, i jeden z nich ukończy, a na 2. miejscu pozostaną 3 pionki, to zostaną one usunięte, ale nie będzie 
  można postawić nowych pionków. Kolor ten nigdy nie skończy gry. (Obejrzeć gameplay)
- **(done 3783cc5)** dziwne spalnienie sie w zlych miejscach pionkow (nie dawanie kolorow dla tkineter **(XDDDDDDDDDDDDDDDDDDDDDDDDDDD)**)
- **(done ee14adf)** Przy wyborze ilosci graczy wyjasnic co to znaczy ze cyfra 2 jest na pionku(2 stackowane pionki) oraz sterowanie  graczy ze zawsze dobor koloru staly dla 
  klawisza czyli wsad gdzie 2 graczy to zielony i czerwony 3 graczy to zielony czerwony zolty itp
- **(done 698b57a)** Po wyrzuceniu 6 drugi raz, jeśli wyrzucimy 6 w drugim rzucie, to ban na ruch.
 
### Możliwe do wykonania

- **(may be done)** jezeli ktos wyrzuci 6 i nie mozna zrobic ruchu to nie powinno byc sytuacji ze ma sie kolejny ruch(dac ileszostek na 3 w miejscach gdzie opisane sa sytuacje gdzie nie powinno byc ruchu)
- **(may be done)** Zmiana na klasowość, aby używać socketów.
- **(may be done)** Dodanie socketów do gry.
- **(may be done)** Po zakończeniu, umieszczenie na Dysku Google.
  


