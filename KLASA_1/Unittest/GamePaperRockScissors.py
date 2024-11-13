
# **********************************************
# nazwa funkcji: <GamePaperRockScissors>
# opis funkcji: <Gra w papier kamień i nożyczki>
# parametry: <napis - napis, element musi należeć do podanych elementów z tablicy>
# zwracany typ i opis: <string - zwraca zwyciężcę lub remis>
# autor: <Karyna Pomin>

#***********************************************

def GamePaperRockScissors(gamer_1, gamer_2):
    Choice = ["paper", "rock", "scissors"]

    if CzyWybor(Choice, gamer_1, gamer_2):
        if (gamer_1 == gamer_2):
                return "remis" 
        elif (gamer_1 == Choice[0]):
            if (gamer_2 == Choice[1]):
                return gamer_1 
            elif (gamer_2 == Choice[2]):
                return gamer_2 
        elif (gamer_1 == Choice[1]):
            if (gamer_2 == Choice[0]):
                return gamer_2 
            elif (gamer_2 == Choice[2]):
                return gamer_1 
        elif (gamer_1 == Choice[2]):
            if (gamer_2 == Choice[0]):
                return gamer_1 
            elif (gamer_2 == Choice[1]):
                return gamer_2 
    else:
        raise ValueError("Invalid choice!")        
    
                
def CzyWybor(Choice, gamer_1, gamer_2):
    if (gamer_1 in Choice and gamer_2 in Choice):
        return True
    return False
