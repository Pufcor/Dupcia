name = input("Podaj imię ")



print("Cześć " + name + " , to mój pierwszy program. Mam nadzieję, że przypadnie Ci do gustu!")

answer1 = input("wpisz start aby zacząć")
if answer1 == "start":
    pytanie2 = input("Co pijesz rano, kawa czy herbata?")
    print(pytanie2)
while answer1 not in "wpisz start aby zacząć":
    answer2 = input("Może jednak sprawdzisz mój program? Wpisz proszę start")
    print(answer2)
    if answer2 == "start":
        pytanie2 = input("Co pijesz rano, kawa czy herbata?")
        print(pytanie2)

if pytanie2 in ("kawa", "herbata"):
    odpowiedź1 = input("To świetnie! Picie gorących napojów do śniadanie pomaga w budowaniu porannego metabolizmu")














