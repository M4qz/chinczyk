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
- **(done)** Nie można odmówić postawienia pionka, jeżeli ma się 0 na planszy.
- **(done)** Zbugowane klikanie ruchem pionka - jeśli klikniemy kilka klawiszy ruchu, to buguje się (zmieniona kolejność w kodzie `for event in pygame.event.get()`).
- **(done)** Jeżeli pionki tego samego koloru najdą na siebie, to stakują się (jest różnica między 1 pionkiem a kilkoma na jednej pozycji).
- **(done)** Zrobienie oznaczenia szachownicy takie jak w szachach (A-F 1-8) i dodanie efektów pociachania planszy jak w szachach.

### Do zrobienia

- **(to be done)** Wyjasnienie sterowania przy wyborze ilosci graczy ze zawsze dobor koloru staly dla klawisza czyli wsad gdzie 2 graczy to zielony i czerwony 3 graczy to zielony czerwony zolty itp
- **(to be done)** Po wyrzuceniu 6 drugi raz, jeśli wyrzucimy 6 w drugim rzucie, to ban na ruch.
- **(to be done - rare event)** Jeżeli na 2. miejscu stoją 4 pionki, i jeden z nich ukończy, a na 2. miejscu pozostaną 3 pionki, to zostaną one usunięte, ale nie będzie można postawić nowych pionków. Kolor ten nigdy nie skończy gry. (Obejrzeć gameplay)
  
### Możliwe do wykonania

- **(may be done)** Zmiana na klasowość, aby używać socketów.
- **(may be done)** Dodanie socketów do gry.
- **(may be done)** Po zakończeniu, umieszczenie na Dysku Google.


