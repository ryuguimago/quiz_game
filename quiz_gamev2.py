# this is a quiz game with multiple choice options 
from time import sleep 
import random
#zähl variablen 
x = 0
y = 0
z = 0
#Frage variablen in listen
Frage = ["Wie heißt die Hauptstadt von Italien? \n","Wer war der erste Mensch, der mit einem Raumschiff um die Erde flog? \n","Wie heißt die einflussreiche Kunstschule in Weimar? \n" ]
Antwort1 = ["Mailand", "Neil Armstrong", "Bauhof"]
Antwort2 = ["Madrid", "Lance Armstrong", "Baywa"]
AntwortRichtig = ["Rom", "Yuri Gagarin", "Bauhaus"]
#Fragen und antworten müssen eig zusammen gehören shuffle möglich
print("<Hallo, hast du lust auf ein Quiz? ")
start = input("y/n \n") 
if start.lower() == "y":
    name = input("Super, wie heißt du? \n")
else:
    print("Schade")
    exit()
print(f"Hallo {name} lass uns anfangen.\n")
sleep(1)
#hier sowas wie eine for schleife einfügen mit zählerder automatisiert die fragen und antworten durch wechselt
print("Los geht es mit der ersten Frage \n\n")
sleep(1)
for AR in AntwortRichtig:
    y += 1
    print(Frage[z])
    sleep(1)
    antworten = [AntwortRichtig[z], Antwort1[z], Antwort2[z]]
    random.shuffle(antworten)
    print(f"A: {antworten[0]}")
    print(f"B: {antworten[1]}")
    print(f"C: {antworten[2]}")
    Lösung = input("Wie lautet die richtige Antwort?\n")
    if  (Lösung.lower() == "a" and antworten[0] == AntwortRichtig[z]) or \
        (Lösung.lower() == "b" and antworten[1] == AntwortRichtig[z]) or \
        (Lösung.lower() == "c" and antworten[2] == AntwortRichtig[z]):
        print("RICHTIG\n")
        x += 1
    else:
        print(f"SCHADE, die richtige Antwort wäre {AntwortRichtig[z]} gewesen\n")
    # print("Nächste Frage: \n")
    z +=1 
    sleep (1)
#ende des quiz
print("DAS WARS")
sleep(1)
prozent = x / y * 100
if x == y:
    print("SUPER, du hast alle Fragen richtig beantwortet! \nDas sind", round(prozent) , "%")
else:
    print("Du hast ", x," von ", y," Fragen richtig beantwortet\nDas sind", round(prozent) , "%")
exit()