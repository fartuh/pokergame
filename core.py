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
        winner = self.highest()
        pairs = self.pair()
        if pairs != 0:
            winner = pairs

        print(winner)
        

    def highest(self):
        p_s_arr = []
        r_s_arr = []
        
        for arr in self.playercards:
            p_s_arr.append(arr[2]) 
        
        p_s = max(p_s_arr)

        for arr in self.robotcards:
            r_s_arr.append(arr[2]) 
            
        r_s = max(r_s_arr)

        if p_s > r_s:
            return 'player'
        elif r_s > p_s:
            return 'robot'
        else:
            return 'both'

    def pair(self):
        player_pair = 0
        robot_pair = 0

        for card in self.playercards:
            for i in range(5):
                if card[2] == self.playercards[i][2] and card[1] != self.playercards[i][1]:
                    if card[2] > player_pair:
                        player_pair = card[2]
                        break

        for card in self.robotcards:
            if robot_pair != 0:
                break
            for i in range(5):
                if card[2] == self.robotcards[i][2] and card[1] != self.robotcards[i][1]:
                    if card[2] > player_pair:
                        robot_pair = card[2]
                        break

        
        if player_pair > robot_pair and player_pair > 0:
            return 'player'
        if robot_pair > player_pair and robot_pair > 0:
            return 'robot'
        if robot_pair == player_pair and player_pair == 0:
            return 0
        else:
            return 'both'





