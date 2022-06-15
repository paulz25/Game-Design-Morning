mport random, os
os.system('cls')
deck=[]
#next, let's start building list holders so we can place our cards in there:
def create_DECK():
    global deck
    numberCards = []
    suits = ["♥️","♦️", "♣️", "♠️"]
    royals = ["J", "Q", "K", "A"]
    

    #now, let's start using loops to add our content:
    for i in range(2,11):
        numberCards.append(str(i))
        #this adds numbers 2-10 and converts them to string data

    for j in range(4):
        numberCards.append(royals[j])
        #this will add the royal faces to the cardbase

    
    for k in range(4):
        for l in range(13):
            card = (numberCards[l] + " " + suits[k])
            #this makes each card, cycling through suits, but first through faces
            deck.append(card)
            #this adds the information to the "full deck" we want to make

    #now let's see the cards!
    counter=0
    for row in range(4):
        for col in range(13):
            # print(deck[counter], end=" ")
            counter +=1
        # print()
    #now let's shuffle our deck!
def playerCards():
    random.shuffle(deck)
    player1=[]
    player2=[]
    for l in range(52):
        if l%2==0:
            player1.append(deck[l])
        else:
            player2.append(deck[l])
    # print("player1 ",player1)
    # print()
    # print("player2 ",player2)
    #I also want to see what the deck looks like before shuffling. We should have
        #done that a while ago... oh well!
    return player1, player2    
create_DECK()

# Aidans code
decs = playerCards()
player1 = decs[0]
player2 = decs[1]

loopcount = 1
p1_listcount = 0
p2_listcount = 0
while loopcount < 50:
    if len(player1) == 0:
        print("player 1 loses")
        break
    if len(player2) == 0:
        print("player 2 loses")
        break
    if p1_listcount > len(player1)-1:
        p1_listcount = 0
    if p2_listcount > len(player2)-1:
        p2_listcount = 0

    player1_card = player1[p1_listcount]  
    player1_card = player1_card[0:len(player1_card)-3]  
    if player1_card == "J":
        player1_card = 11
    if player1_card == "Q":
        player1_card = 12
    if player1_card == "K":
        player1_card = 13
    if player1_card == "A":
        player1_card = 14        

    player2_card = player2[p2_listcount]  
    player2_card = player2_card[0:len(player2_card)-3]  
    if player2_card == "J":
        player2_card = 11
    if player2_card == "Q":
        player2_card = 12
    if player2_card == "K":
        player2_card = 13
    if player2_card == "A":
        player2_card = 14 

    if int(player1_card) > int(player2_card):  
        player1.append(player2[p2_listcount])
        player2.remove(player2[p2_listcount])

    elif int(player2_card) > int(player1_card):
        player2.append(player1[p1_listcount])
        player1.remove(player1[p1_listcount])

    if loopcount == 49:
        print("player 1 dec:",player1)
        print()
        print("player 2 deck:" , player2)
        print()
        if len(player1) > len(player2):
            print("player 1 wins")  
        elif len(player1) < len(player2):
            print("player 2 wins") 
        else:
            print("player 1 and player 2 tied")        
    
    p1_listcount +=1
    p2_listcount +=1
    loopcount +=1