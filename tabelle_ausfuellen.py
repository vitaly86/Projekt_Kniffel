from menu import display_menu
from punkte_rechnen import final_results
from display_table import table_print


namen_list, new_header, data, spiel_extract, spielen_list, keys_runden, values_runden = display_menu()


def insert_punkte_in_tabelle(nam):
    try:
        anzahl_punkte = final_results(spiel_extract[nam][0])
        table_print(spiel_extract=spiel_extract[nam][0],
                    spiel=anzahl_punkte[0][0],
                    data=data,
                    spielen_list=spielen_list,
                    name=nam,
                    punkte=anzahl_punkte[0][3],
                    headers=new_header)
    except ValueError:
        spiel_streichen = input("Welche Spiel willst du in der Tabele streichen? ").strip()
        spiel_streichen = spiel_streichen if spiel_streichen in [f"{index}er" for index in range(1, 7)] \
            else spiel_streichen.title()
        table_print(spiel_extract=spiel_extract[nam][0],
                    spiel=spiel_streichen,
                    data=data,
                    spielen_list=spielen_list,
                    name=nam,
                    punkte=0,
                    headers=new_header)
    finally:
        print(spiel_extract[nam][0])
    return



