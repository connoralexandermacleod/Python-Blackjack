# Imports the random function used to shuffle the deck
import random;
import os;

# sets the status of the game as "pre", which prevents the game from showing the dealer's face down card until the proper time.
gameStatus = "pre";

# Creates the dealer variables. Dealer hand (empty list for cards in hand), dealer hand value and a pre-flop (the phase of the game where the dealer has a face-down card in their hand) total.
dealerHand = [];
dealerHandValue = 0;
dealerPreFlopHandValue = 0;

# Defines the Player class with properties for a player name, a blackjack hand, a value for the total of the hand, a bank to hold the player's money total, a split hand, and a split hand total value.
class Player(object):
    def __init__(self, playerLabel="Rick", hand=[], bank=100, handValue=0, splitHand=[], splitHandValue=0):
        self.playerLabel = playerLabel;
        self.hand = hand;
        self.bank = bank;
        self.handValue = handValue;
        self.splitHand = splitHand;
        self.splitHandValue = splitHandValue;

# Defines the Card class with properties for name and suit. Also has instance methods for printing the full name of a card, and for getting the point value for a card.
class Card(object):
    def __init__(self, name, suit):
        self.name = name;
        self.suit = suit;
    def __str__(self):
        return "%s of %s" %(self.name, self.suit);
    def getValue(self):
        if self.name == "2" or self.name == "3" or self.name == "4" or self.name == "5" or self.name == "6" or self.name == "7" or self.name == "8" or self.name == "9" or self.name == "10":
            return int(self.name);
        if self.name == "Ace":
            return 11;
        if self.name == "Jack" or self.name == "Queen" or self.name == "King":
            return 10;

# Deck Creation Function: Creates a deck of cards. First, an empty list called deck (global variable) is created.Then, 52 card objects, 13 for each suit. The point value for each card is calculated using the getValue() card class function. After each card is created, it is appended to a list (initially empty) called deck. The deck list is then shuffled using the random.shuffle function
def deckCreation():
    global deck;
    deck = [];
    suits = ["Clubs", "Hearts", "Spades", "Diamonds"];
    names = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"];
    for suit in suits:
        for name in names:
            card = Card(name=name, suit=suit);
            deck.append(card);
    random.shuffle(deck);

# deck check function: checks if the deck is empty. If it is, a new deck is created.
def deckCheck():
    if len(deck) <1:
        print "The deck is empty! A new deck is now in use.";
        deckCreation();

# initial deal function: Deals two cards to the dealer and players.
def initialDeal():
    deckCheck();
    player.hand.append(deck.pop());
    deckCheck();
    dealerHand.append(deck.pop());
    deckCheck();
    player.hand.append(deck.pop());
    deckCheck();
    dealerHand.append(deck.pop());

# The status function prints the contents of the player and
def status():
    os.system('cls');

    global gameStatus;
    global dealerHandValue;
    global dealerPreFlopHandValue;

    player.handValue = 0;
    player.splitHandValue = 0;
    dealerHandValue = 0;
    dealerPreFlopHandValue = dealerHand[1].getValue();

    for cards in dealerHand:
        dealerHandValue += cards.getValue();

    for cards in dealerHand:
        if dealerHandValue > 21 and cards.name == "Ace":
            dealerHandValue -= 10;

    for cards in player.hand:
        player.handValue += cards.getValue();

    for cards in player.hand:
        if player.handValue > 21 and cards.name == "Ace":
            player.handValue -= 10;

    if len(player.splitHand) > 0:
        for cards in player.splitHand:
            player.splitHandValue += cards.getValue();
        for cards in player.splitHand:
            if player.splitHandValue > 21 and cards.name == "Ace":
                player.splitHandValue -= 10;

    print "\nPlayer Hand:"
    for cards in player.hand:
        print cards;
    print "\nPlayer Hand Value:"
    print player.handValue;

    if len(player.splitHand) > 0:
        print "\n Player Split Hand:";
        for cards in player.splitHand:
            print cards;
        print "\n Player Split Hand Value:";
        print player.splitHandValue;

    if gameStatus == "pre":
        print "\nDealer Hand:";
        print "Face-down card";
        print dealerHand[1];
        print "\nDealer Hand Value:";
        print dealerPreFlopHandValue;

    if gameStatus == "post":
        print "\nDealer Hand:";
        for cards in dealerHand:
            print cards;
        print "\nDealer Hand Value:";
        print dealerHandValue;




# Creates the initial deck for use during the game.
deckCreation();



# # This while loop asks the player what their name is.
# while True:
#     try:
#         playerLabel = raw_input("Player, what is your name?");
#     except:
#         print "Something messed up!";
#     else:
#         player = Player(playerLabel=playerLabel);
#         break;

player = Player();

os.system('cls');
raw_input("Hello, friend. Welcome to Exciting Text Blackjack.\nYour goal is to amass $1000. You need it to purchase hamburgers.\nPress Enter to start.");
os.system('cls');
while True:
    while True:
        try:
            wager = int(raw_input("Please enter a wager.\nYou currently have %s dollars in your bank\n" %(player.bank)));
            if wager > player.bank:
                print "You can't wager more than you have.";
                continue;
        except:
            print "You are doing something wrong. Try again.";
        else:
            player.bank -= wager;
            break;

    initialDeal();

    status();

    while True:
        try:
            if player.handValue > 21:
                raw_input("You have busted! Press enter to continue");
                gameStatus = "post";
                break;
            if player.handValue == 21:
                raw_input("You have blackjack! Press enter to continue");
                gameStatus = "post";
                break;
            print "\nYour choices are:\nHit: press h\nStand: press s";
            if len(player.hand) == 2:
                print "Double Down: press d";
            choice = raw_input("If you would like to hit, submit h. If you would like to stand, submit s.\n");
        except:
            print "Something has gone terribly wrong! Try again.";
            continue;
        if choice == "h":
            deckCheck();
            player.hand.append(deck.pop());
            status();
            continue;
        if choice == "s":
            gameStatus = "post";
            break;
        if choice == "d" and len(player.hand) == 2:
            if player.bank - wager > 0:
                player.bank -= wager;
                wager = wager * 2;
                deckCheck();
                player.hand.append(deck.pop());
                gameStatus = "post";
                break;
            if player.bank - wager < 1:
                print "You can't afford to double down right now!";
                continue;
        else:
            print "You have not chosen properly. Try again.";
            continue;

    # Post-flop
    status();

    while True:
        if dealerHandValue >16:
            break;
        if dealerHandValue < 17:
            deckCheck();
            dealerHand.append(deck.pop());
            status();
            raw_input();
            continue;

    while True:
        if player.handValue == 21 and dealerHandValue < 21:
            print "Blackjack! You win.";
            player.bank += wager*2;
            break;
        if player.handValue > 21:
            print "You have busted. You lose.";
            break;
        if dealerHandValue == 21:
            print "The Dealer has blackjack. You lose.";
            break;
        if player.handValue < 22 and dealerHandValue < 22 and dealerHandValue > player.handValue:
            print "The dealer is closer to 21. You lose.";
            break;
        if dealerHandValue > 21:
            print "The dealer has busted. You win.";
            player.bank += wager*2;
            break;
        if player.handValue < 21 and dealerHandValue < player.handValue:
            print "You are closer to 21! You win.";
            player.bank += wager*2;
            break;
        if player.handValue == dealerHandValue:
            print "Tie! You lose.";
            break;
    player.handValue = 0;
    dealerHandValue = 0;
    player.hand = [];
    dealerHand = [];
    raw_input();
    if player.bank == 0:
        print "You have run out of money. Game over.";
        break;
    if player.bank >= 1000:
        print "You have won $%s. Four large goons approach the table. They drag you away, and you are never seen again. Game over." %(player.bank);
        break;
    if player.bank > 0 and player.bank < 1000:
        continuePlaying = raw_input("Your current balance is $%s.\nWould you like to continue playing?\nIf yes, press enter.\nIf no, type quit and submit\n" %(player.bank));
    if continuePlaying != "quit":
        continuePlaying = "";
        gameStatus = "pre";
        continue;
    if continuePlaying == "quit" or continuePlaying == "q":
        continuePlaying = "";
        print "Goodbye!";
        break;
