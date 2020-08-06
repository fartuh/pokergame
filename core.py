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

        self.giveCards()
        
        print("Твои карты")
        for card in self.playercards:
            print(card[1])

        print("Карты твоего оппонента")
        for card in self.robotcards:
            print(card[1])

        self.findWinner()


    def giveCards(self):
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


    def getCards(self):
        self.dbcontroller = dbcontroller.DBController('db/cards.sqlite3')
        self.cards = self.dbcontroller.getAllCards()         

    def findWinner(self):
        winner = self.highest()
        pairs = self.pairs()
        if pairs != False:
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
            return 'У игрока старшая карта'
        elif r_s > p_s:
            return 'У соперника старшая карта'
        else:
            return 'Ничья'

    def pairs(self):

        # Strength of the highest player's pair

        player_pair = 0

        # Amount of pairs of the player

        p_amount = 0

        # Already used cards of the player

        p_paired = []

        # The same for Robot

        robot_pair = 0

        r_amount = 0

        r_paired = []

        
        for card in self.playercards:
            paired_check = False
            checkpass = False

            for i in range(5):
                if paired_check == True:
                    break

                if card[2] == self.playercards[i][2] and card[1] != self.playercards[i][1]:

                        for paired in p_paired:
                            if card[1] != paired and self.playercards[i][1] != paired:
                                checkpass = True
                            else:
                                checkpass = False
                                break
                        else:
                            checkpass = True

                        if checkpass != True:
                            break

                        if p_amount == 0:
                            p_amount += 1
                            player_pair = int(card[2])
                            p_paired.append(card[1])
                            p_paired.append(self.playercards[i][1])
                            
                            paired_check = True
                            break
                        elif p_amount == 1:
                            p_amount += 1
                            p_paired.append(card[1])
                            p_paired.append(self.playercards[i][1])

                            if card[2] > player_pair:
                                player_pair = int(card[2])
                                paired_check = True
                                break
                            else:
                                paired_check = True
                                break

        
            for card in self.robotcards:
                paired_check = False
                checkpass = False

                for i in range(5):
                    if paired_check == True:
                        break

                    if card[2] == self.robotcards[i][2] and card[1] != self.robotcards[i][1]:

                            for paired in r_paired:
                                if card[1] != paired and self.robotcards[i][1] != paired:
                                    checkpass = True
                                else:
                                    checkpass = False
                                    break
                            else:
                                checkpass = True

                            if checkpass != True:
                                break

                            if r_amount == 0:
                                r_amount += 1
                                robot_pair = int(card[2])
                                r_paired.append(card[1])
                                r_paired.append(self.playercards[i][1])
                                
                                paired_check = True
                                break
                            elif r_amount == 1:
                                r_amount += 1
                                r_paired.append(card[1])
                                r_paired.append(self.playercards[i][1])

                                if card[2] > robot_pair:
                                    robot_pair = int(card[2])
                                    paired_check = True
                                    break
                                else:
                                    paired_check = True
                                    break



        if p_amount > r_amount:
            return 'Игрок'
        elif r_amount > p_amount:
            return 'Соперник'
        elif r_amount == p_amount != 0:
            if player_pair > robot_pair and player_pair > 0:
                return 'Игрок'
            elif robot_pair > player_pair and robot_pair > 0:
                return 'Соперник'
            else:
                return 'Ничья'
        elif r_amount == p_amount == 0:
            return False

        
        




