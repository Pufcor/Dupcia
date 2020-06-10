secret = 24


while True:


    guess = input("podaj liczbę ")
    answer = int(guess)

    if answer == secret:
        print("wygrałeś")
        break
    else:
        if answer > 19:
            print("za duża liczba ")
        if answer < 19:
            print("zby mała liczba")





# wykonywac ciagle:
# pobierz tekst od usera
# zamien tekst na liczbe
# sprawdz cz liczba jest rowna sekretowi
# jesli tak,to napisz userowi ze wygral gre i wyjdz z petli
# jesli nie, to napisz userowi czy jego liczba jest wieksza czy mniejsza

