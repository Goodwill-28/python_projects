import random 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
class Deck:
    
    def __init__(self):
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
class Player:
    
    def __init__(self,name):
        self.name = name
        # A new player has no cards
        self.all_cards = [] 
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            return self.all_cards.extend(new_cards)
        else:
            return self.all_cards.append(new_cards)
    
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
player_one = Player("One")
player_two = Player("Two")
new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on=True
game_round=0
while game_on:
    game_round+=1
    print(f'Player One cards: {len(player_one.all_cards)}')
    print(f'Player Two cards: {len(player_two.all_cards)}')
    print(f'Game round {game_round}')
    player_one_moves=[]
    player_two_moves=[]
    player_one_moves.append(player_one.remove_one())#ispe me galat likh rhi thi player_one list lo remove_one ke bracket me dal rhi thi 
    player_two_moves.append(player_two.remove_one())

    if len(player_one.all_cards) == 0: #yha pe bhi me direct player_one likh rhi thi jabki mujhe uske andar jake all cards ho gya ya remove_one ho gya ye sab explore karna chahiye
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break
    elif len(player_two.all_cards)==0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break
    at_war=True
    while at_war:
        if player_one_moves[-1].value<player_two_moves[-1].value:
            player_two.add_cards(player_one_moves)
            player_two.add_cards(player_two_moves)
            at_war=False
        elif player_one_moves[-1].value>player_two_moves[-1].value:
            player_one.add_cards(player_one_moves)
            player_one.add_cards(player_two_moves)
            at_war=False
        else:
            print('WAR SITUATION!')
            if len(player_one.all_cards)<1:
                print('player 1 has run out of cards')
                print('player 2 has won')
                game_on=False #honestly me yha pe confused thi ki kis while loop wale ko false kru...sahi strategy hai yarr
                break
            if len(player_two.all_cards)<1:
                print('player 2 has run out of cards')
                print('player 1 has won')
                game_on=False
                break
            else:
                 #here i felt ki mujhe for loop ki qn practice coding bat se krni chahiye
                    player_one_moves.append(player_one.remove_one())
                    player_two_moves.append(player_two.remove_one())
    