from random import randint


def erste_versuch():
    wuerfel_list = []
    for _ in range(1, 6):
        wuerfel_list.append(randint(1, 6))
    wuerfel_list = sorted(wuerfel_list)
    print(f"Wuerfeln von erste versuch: {wuerfel_list}\n")
    return [wuerfel_list, None]


def dritte_versuch(my_zweite_list):
    dritte_versuch_list = []
    if len(my_zweite_list) == 1:
        my_zweite_list.clear()
        new_wuerfeln = randint(1, 6)
        dritte_versuch_list.append(new_wuerfeln)
    else:
        altes_wuerfel = input("Geben Sie bitte ein, welche Wuerfel möchten Sie wechseln. "
                              "Trennen Sie durch Komma whenn mehrere: ").split(',')
        zweite_altes_wuerfel = [int(wuerfel_elem) for wuerfel_elem in altes_wuerfel]
        for wuerf in zweite_altes_wuerfel:
            if wuerf in my_zweite_list:
                my_zweite_list.remove(wuerf)
                new_wuerfeln = randint(1, 6)
                dritte_versuch_list.append(new_wuerfeln)
    print(f"\nWuerfeln Augen von dritte versuch: {sorted(dritte_versuch_list)}")
    my_dritte_list = my_zweite_list + dritte_versuch_list
    return my_dritte_list


def finale_wuerfel_list(my_list, list_zu_wechseln):
    zweite_versuch_list = []
    for wuerf in list_zu_wechseln:
        if wuerf in my_list:
            my_list.remove(wuerf)
            new_wuerfeln = randint(1, 6)
            zweite_versuch_list.append(new_wuerfeln)
    print(f"\nWuerfeln Augen von zweite versuch: {sorted(zweite_versuch_list)}")
    my_zweite_list = sorted(my_list + zweite_versuch_list)
    print(f"Wuerfeln von zweite versuch: {my_zweite_list}\n")
    laetzte_versuch = input(f"Möchten Sie der dritte Versuch von Augen Wuerfeln {sorted(zweite_versuch_list)} "
                            f"benutzen (ja / nein)? ").lower()
    if laetzte_versuch == "ja":
        dritte_versuch_list = dritte_versuch(zweite_versuch_list)
        my_final_list = sorted(my_list + dritte_versuch_list)
        print(f"Wuerfeln von dritte versuch: {my_final_list}\n")
    else:
        my_final_list = sorted(my_list + zweite_versuch_list)
    return [my_final_list, laetzte_versuch]


def wuerfel_waehlen(initial_wuerfel_list):
    zahl_wuerfel = int(input("Wie viele Wuerfeln moechten Sie werfen? "))
    altes_wuerfel_list = []
    for wuerfel_num in range(1, zahl_wuerfel + 1):
        altes_wuerfel = int(input(f"Geben Sie bitte {wuerfel_num}-er Wuerfel ein: "))
        altes_wuerfel_list.append(altes_wuerfel)
    wuerfel_list = finale_wuerfel_list(initial_wuerfel_list[0], altes_wuerfel_list)
    print(f"Meine finale liste aller Wuerfel ist: {wuerfel_list[0]}")
    return wuerfel_list
