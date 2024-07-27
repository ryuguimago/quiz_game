import random
Frage = ["Wie heißt die Hauptstadt von Italien? \n","Wer war der erste Mensch, der mit einem Raumschiff um die Erde flog? \n","Wie heißt die einflussreiche Kunstschule in Weimar? \n" ]
Antwort1 = ["Mailand", "Neil Armstrong", "Bauhof"]
Antwort2 = ["Madrid", "Lance Armstrong", "Baywa"]
AntwortRichtig = ["Rom", "Yuri Gagarin", "Bauhaus"]
z = 0
print("Los geht es mit der ersten Frage \n\n")
for AR in AntwortRichtig:
    print(Frage[z])
    antworten = [AntwortRichtig[z], Antwort1[z], Antwort2[z]]
    random.shuffle(antworten)
    print(f"A: {antworten[0]}")
    print(f"B: {antworten[1]}")
    print(f"C: {antworten[2]}")
    Lösung = input("ist die Antwort A B oder C\n")
    if  (Lösung.lower() == "a" and antworten[0] == AntwortRichtig[z]) or \
        (Lösung.lower() == "b" and antworten[1] == AntwortRichtig[z]) or \
        (Lösung.lower() == "c" and antworten[2] == AntwortRichtig[z]):
        print("RICHTIG")
    else:
        print(f"SCHADE, die richtige Antwort wäre {AntwortRichtig[z]} gewesen\n")
    z +=1 