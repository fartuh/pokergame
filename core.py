import random
import dbcontroller

class Game():
    cards = []
    playercards = []
    robotcards = []
    blocked = []
    dbcontroller = ""

    def __init__(self):
        print('Введи 1 чтобы начать игру')
        f = input()
        if(f == "1"):
            self.gameStart()

    def gameStart(self):
        self.getCards()
        for i in range(10):
            if i < 5:
                picked = random.choice(self.cards)
                picked_card = picked[1]

                self.robotcards.append(picked_card) 
                self.cards.remove(picked)
            else:
                picked = random.choice(self.cards)
                picked_card = picked[1]

                self.playercards.append(picked_card) 
                self.cards.remove(picked)

        print("Твои карты")
        print(self.playercards)
        print("Карты твоего оппонента")
        print(self.robotcards)


    def getCards(self):
        self.dbcontroller = dbcontroller.DBController('db/cards.sqlite3')
        self.cards = self.dbcontroller.getAllCards()         
