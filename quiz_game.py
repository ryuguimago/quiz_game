# this is a quiz game with multiple choice options 
x = 0
y = 0
print("<Hallo, hast du lust auf ein Quiz? ")
start = input("y/n \n") 
if start.lower() == "y":
    name = input("Super, wie heißt du? \n")
else:
    print("Schade")
    exit()
print("Hallo" +" " + name +", lass uns anfangen.\n")
print("Los geht es mir der ersten Frage \n\nWie heißt die Hauptstadt von Italien? \n")
y = y +1
Lösung = input("A: Mailand \nB: Rom \nC: Madrid\n")
if Lösung == "b" or Lösung == "B":
    print("RICHTIG")
    x = x + 1
else:
    print("SCHADE, die richtige Antwort wäre Rom gewesen.")
print("Nächste Frage: \n")
print("Wer war der erste Mensch, der mit einem Raumschiff um die Erde flog? \n")
y = y +1
Lösung = input("A: Neil Armstrong \nB: Lance Armstrong \nC: Yuri Gagarin\n")
if Lösung == "C" or Lösung == "c":
    print("RICHTIG")
    x = x + 1
else:
    print("SCHADE, die richtige Antwort wäre Yuri Gagarin gewesen.")
print("Nächste Frage: \n")
print("Wie heißt die einflussreiche Kunstschule in Weimar? \n")
y = y + 1
Lösung = input("A: Bauhof \nB: Baywa \nC: Bauhaus\n")
if Lösung == "C" or Lösung == "c":
    print("RICHTIG")
    x = x + 1
else:
    print("SCHADE, die richtige Antwort wäre Bauhaus gewesen.")
prozent = x / y * 100
if x == y:
    print("SUPER, du hast alle Fragen richtig beantwortet! \nDas sind", prozent , "%")
else:
    print("Du hast ", x, " von ", y, " Fragen richtig beantwortet\nDas sind", prozent , "%")
exit()