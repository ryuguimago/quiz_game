# this is a quiz game with multiple choice options 
from time import sleep 
import random
#zähl variablen 
x = 0
y = 0
#Fragen
quiz = [
    {
        "frage": "Wie heißt die Hauptstadt von Italien?\n",
        "antworten": ["Rom", "Mailand", "Madrid"],
        "richtig": "Rom"
    },
    {
        "frage": "Wer war der erste Mensch, der mit einem Raumschiff um die Erde flog?\n",
        "antworten": ["Yuri Gagarin", "Neil Armstrong", "Lance Armstrong"],
        "richtig": "Yuri Gagarin"
    },
    {
        "frage": "Wie heißt die einflussreiche Kunstschule in Weimar?\n",
        "antworten": ["Bauhaus", "Bauhof", "Baywa"],
        "richtig": "Bauhaus"
    },
    {
        "frage": "Welches ist der größte Ozean der Welt?\n",
        "antworten": ["Nordsee", "Atlantischer Ozean", "Pazifischer Ozean"],
        "richtig": "Pazifischer Ozean"
    },
    {
        "frage": "Welches Tier hat grün gefärbtes Fett?\n",
        "antworten": ["Faultier", "Schlange", "Krokodil"],
        "richtig": "Krokodil"
    }
]
print("<Hallo, hast du lust auf ein Quiz? ")
start = input("y/n \n") 
if start.lower() == "y":
    name = input("Super, wie heißt du? \n")
else:
    print("Schade")
    exit()
print(f"Hallo {name} lass uns anfangen.\n")
sleep(1)
print("Los geht es mit der ersten Frage \n\n")
sleep(1)
for q in quiz:
    y += 1
    print(q["frage"])
    sleep(1)
    #Antworten mischen
    antworten = q["antworten"]
    random.shuffle(antworten)
    print(f"A: {antworten[0]}")
    print(f"B: {antworten[1]}")
    print(f"C: {antworten[2]}")
    Lösung = input("Wie lautet die richtige Antwort?\n")
    if  (Lösung.lower() == "a" and antworten[0] == q["richtig"] )or \
        (Lösung.lower() == "b" and antworten[1] == q["richtig"]) or \
        (Lösung.lower() == "c" and antworten[2] == q["richtig"]):
        print("RICHTIG\n")
        x += 1
    else:
        print(f"SCHADE, die richtige Antwort wäre {q["richtig"]} gewesen\n")
    # print("Nächste Frage: \n")
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