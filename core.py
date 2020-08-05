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

                self.robotcards.append(picked) 
                self.cards.remove(picked)
            else:
                picked = random.choice(self.cards)
                picked_card = picked[1]

                self.playercards.append(picked) 
                self.cards.remove(picked)

        print("Твои карты")
        for card in self.playercards:
            print(card[1])

        print("Карты твоего оппонента")
        for card in self.robotcards:
            print(card[1])

        self.findWinner()


    def getCards(self):
        self.dbcontroller = dbcontroller.DBController('db/cards.sqlite3')
        self.cards = self.dbcontroller.getAllCards()         

    def findWinner(self):
        p_s_arr = []
        r_s_arr = []
        
        for arr in self.playercards:
            p_s_arr.append(arr[2]) 
        
        p_s = max(p_s_arr)

        for arr_r in self.robotcards:
            r_s_arr.append(arr_r[2]) 
            
        r_s = max(r_s_arr)

        if p_s > r_s:
            print('Ты победил')
        elif r_s > p_s:
            print('Ты проиграл')
        else:
            print('Ничья')
