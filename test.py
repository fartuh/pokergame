import core

game = core.Game()

game.cards = [[0, "2clubs", 2], [0, "2diamonds", 2], [0, "5spades", 5], [0, "5hearts", 5], [0, "5clubs", 5], [0, "5diamonds", 5], [0, "Aspades", 14], [0, "Ahearts", 14], [0, "Aclubs", 14], [0, "Adiamonds", 14]]

game.giveCards()

print(game.playercards)
print(game.robotcards)

print(game.pairs())
