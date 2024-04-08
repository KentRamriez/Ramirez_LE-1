import random
import sys

totWinning_amountC = 100_000
totWinning_amountM = 500_000
totWinning_amountE = 1_000_000 

num_choice = ""
color_choice = ""

assets = {
    "total_winnings" : 20_000, 
}

def check_winning_condition(difficulty_level):
    target_winnings = 0
    if difficulty_level == 'C':
        target_winnings = totWinning_amountC
    elif difficulty_level == 'M':
        target_winnings = totWinning_amountM
    elif difficulty_level == 'E':
        target_winnings = totWinning_amountE
    
    if assets["total_winnings"] >= target_winnings:
        print("\n------------------------------------------- Winner! -----------------------------------------------")
        print("\n      Congratulations! You have now become a bonafide gambling addict! Now it's time to stop!")
        print("\n------------------------------------------- Winner! -----------------------------------------------")
        sys.exit()

def check_game_over():
    if assets["total_winnings"] < 500:
        print("\n---------------------------------------------You -----------------------------------------------")
        print("\n     Game Over! You don't have enough funds to continue playing. The program will not exit...")
        print("\n-------------------------------------------Lost! -----------------------------------------------")
        sys.exit()

def check_game_over():
    if assets["total_winnings"] < 500:
        print("\n---------------------------------------------You -----------------------------------------------")
        print("\n     Game Over! You don't have enough funds to continue playing. The program will not exit...")
        print("\n-------------------------------------------Lost! -----------------------------------------------")
        sys.exit()

def select_gambling_game():
    print("-------------------------------------------------------------------------------------------------------")
    print("What gambling game would you take on? (Select from 1 to 3): ")
    print("1. Roll The Dice")
    print("2. Blackjack")
    print("3. Roulette")
    print("-------------------------------------------------------------------------------------------------------")

    select_game = input("I wanna play: ")
    while True:
        try:
            if select_game == "1":
                print("-------------------------------------------------------------------------------------------------------")
                print("                              ~---+---~ Welcome to Roll The Dice! ~---+---~")
                print("-------------------------------------------------------------------------------------------------------")
                return dice_roll()
            elif select_game == "2":
                print("-------------------------------------------------------------------------------------------------------")
                print("                                ~---+---~ Welcome to Blackjack! ~---+---~")
                print("-------------------------------------------------------------------------------------------------------")
                return blackjack()
            elif select_game == "3":
                print("-------------------------------------------------------------------------------------------------------")
                print("                           ~---+---~ Welcome to The Roulette! ~---+---~")
                print("-------------------------------------------------------------------------------------------------------")
                return roulette()
            else:
                print("\n---------------------------Invalid -----------------------------")
                print("         ^^^Please select from the available games displayed.")
                print("----------------------------Input-------------------------------")
                return select_gambling_game()
        except ValueError as e:
            print(e)
            return select_gambling_game()

def dice_roll():

    print(f"\nYour current winnings is ${assets['total_winnings']:,}. Good Luck!")

    dice_face_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}
    
    my_die_total = 0
    dealer_die_total = 0

    bet = None
    while True:
        bet = float(input(f"\nHow much will you bet? (You currently have ${assets['total_winnings']:,}, minimum bet is $500): "))
        try:
            if bet > assets["total_winnings"]:
                print("-----------------------------------------------Invalid -------------------------------------------------")
                print(f"           You can't bet an amount you don't have! Your current balance is ${assets['total_winnings']}")
                print("------------------------------------------------Input---------------------------------------------------")
                continue
            elif bet < 500:
                print("\n------------------------------------Invalid -------------------------------------")
                print("                             Minimum bet is $500      ")
                print("-------------------------------------Input---------------------------------------")
                return dice_roll()
            else:
                break
        except ValueError as e:
            print(e)
            return dice_roll()
        
    num_dice = None
    while True:
        num_dice = int(input("How many dice would you like to play? (Maximum of 4): "))
        try:
            if num_dice > 4:
                print("\n------------------------------------Invalid -------------------------------------")
                print("                             A maximum of 4 dice is allowed.      ")
                print("-------------------------------------Input---------------------------------------")
            elif num_dice <= 0:
                print("\n------------------------------------Invalid -------------------------------------")
                print("                             Must have atleast 1 die.      ")
                print("-------------------------------------Input---------------------------------------")
                continue
            else:
                break
        except ValueError as e:
            print(e)
            continue

    def player_rolls():
        my_dice = []
        my_die_total = 0

        for die in range(num_dice):
            my_dice.append(random.randint(1, 6))
        for line in range(5):
            for die in my_dice:
                print(dice_face_art.get(die)[line], end ="")
            print()

        for die in my_dice:
            my_die_total += die
        print(f"You rolled {my_die_total}")
        return my_die_total

    def dealer_rolls():
        dealer_dice = []
        dealer_die_total = 0

        for die in range(num_dice):
            dealer_dice.append(random.randint(1, 6))
        for line in range(5):
            for die in dealer_dice:
                print(dice_face_art.get(die)[line], end ="")
            print()

        for die in dealer_dice:
            dealer_die_total += die
        print(f"The dealer rolled {dealer_die_total}")
        return dealer_die_total

    my_die_total = player_rolls()
    dealer_die_total = dealer_rolls()

    def calc_payout():
        if my_die_total > dealer_die_total:
                payout = (my_die_total - dealer_die_total) * bet
                assets["total_winnings"] += payout
                print(f"You won! Here is your payout ${payout:,}. You now have ${assets['total_winnings']:,}.")
        elif my_die_total < dealer_die_total:
            payout = -bet
            assets["total_winnings"] += payout
            print(f"You lost! You lost ${bet:,}. You now have ${assets['total_winnings']:,}.")
        else:
            print(f"It's a tie! You get your bet back. You stil have ${assets['total_winnings']:,}.")
            
    calc_payout()

    check_winning_condition(difficulty)

    check_game_over(difficulty)

    def continue_playing():
        play_again = input("Would you like to play again? (y or n): ").lower()
        while True:
            try:
                if play_again == 'y':
                    return dice_roll()
                elif play_again == 'n':
                    return select_gambling_game()
                else:
                    print("\n------------------------------------Invalid -------------------------------------")
                    print("                            Please select a valid response. (y or n)      ")
                    print("-------------------------------------Input---------------------------------------")
                    return continue_playing()
            except ValueError as e:
                print(e)
                return continue_playing()

    continue_playing()

def blackjack():
    playerIn = True
    dealerIn = True

    deck = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K']
    player_hand = []
    dealer_hand = []

    print(f"\nYour current winnings is ${assets['total_winnings']}. Good Luck!")

    bet = None
    while True:
        bet = float(input(f"\nHow much will you bet? (You currently have ${assets['total_winnings']:,}, minimum bet is $1,000): "))
        try:
            if bet > assets["total_winnings"]:
                print("-----------------------------------------------Invalid -------------------------------------------------")
                print(f"           You can't bet an amount you don't have! Your current balance is ${assets['total_winnings']}")
                print("------------------------------------------------Input---------------------------------------------------")
                continue
            elif bet < 1000:
                print("\n------------------------------------Invalid -------------------------------------")
                print("                             Minimum bet is $500      ")
                print("-------------------------------------Input---------------------------------------")
                return blackjack()
            else:
                break
        except ValueError as e:
            print(e)
            return blackjack()

    def deal_cards(turn):
        card = random.choice(deck)
        turn.append(card)
        deck.remove(card)

    def calc_total(turn):
        total = 0
        face_cards = ['J', 'Q', 'K']

        for card in turn:
            if card in range(1, 11):
                total += card
            elif card in face_cards:
                total += 10
            else:
                total += 11
        return total
    
    def dealer_hand_play():
        if len(dealer_hand) == 2:
            return dealer_hand[0]
        elif len(dealer_hand) > 2:
            return dealer_hand[0], dealer_hand[1]
        
    for _ in  range(2):
        deal_cards(dealer_hand)
        deal_cards(player_hand)

    while playerIn or dealerIn:
        print(f"The Dealer had {dealer_hand_play()} and X")
        print(f"You have {player_hand} for a total of {calc_total(player_hand)}")
        if playerIn:
            move = input("1. Stay\n2. Hit\nWhat would you like to do?: ")
        if calc_total(dealer_hand) > 16:
            dealerIn = False
        else:
            deal_cards(dealer_hand)
        
        if move == '1':
            playerIn = False
        else:
            deal_cards(player_hand)

        if calc_total(player_hand) >= 21:
            break
        elif calc_total(dealer_hand) >= 21:
            break

    if calc_total(player_hand) == 21:
        print(f"\nYou have {player_hand} for a total of {calc_total(player_hand)} and the dealer have {dealer_hand} for a total of {calc_total(dealer_hand)}.")
        print("BlackJack! You won the round!")
        assets["total_winnings"] += (bet * 1.5)
        print(f"Your current total winnings is {assets['total_winnings']:,}")
    elif calc_total(dealer_hand) == 21:
        print(f"\nYou have {player_hand} for a total of {calc_total(player_hand)} and the dealer have {dealer_hand} for a total of {calc_total(dealer_hand)}.")
        print("BlackJack! The dealer has won the round!")
        assets["total_winnings"] -= bet
        print(f"Your current total winnings is {assets['total_winnings']:,}")
    elif calc_total(player_hand) and calc_total(dealer_hand) == 21:
        print(f"\nYou have {player_hand} for a total of {calc_total(player_hand)} and the dealer have {dealer_hand} for a total of {calc_total(dealer_hand)}.")
        print("BlackJack! It's a draw!")
        assets["total_winnings"] == assets["total_winnings"]
        print(f"Your current total winnings is {assets['total_winnings']:,}")
    elif calc_total(player_hand) > 21:
        print(f"\nYou have {player_hand} for a total of {calc_total(player_hand)} and the dealer have {dealer_hand} for a total of {calc_total(dealer_hand)}.")
        print("You bust! The dealer has won the round!")
        assets["total_winnings"] -= bet
        print(f"Your current total winnings is {assets['total_winnings']:,}")
    elif calc_total(dealer_hand) > 21:
        print(f"\nYou have {player_hand} for a total of {calc_total(player_hand)} and the dealer have {dealer_hand} for a total of {calc_total(dealer_hand)}.")
        print("Dealer busts! You have won the round!")
        assets["total_winnings"] += (bet * 1.5)
        print(f"Your current total winnings is {assets['total_winnings']:,}")
    elif 21 - calc_total(dealer_hand) < 21 - calc_total(player_hand):
        print(f"\nYou have {player_hand} for a total of {calc_total(player_hand)} and the dealer have {dealer_hand} for a total of {calc_total(dealer_hand)}.")
        print("The dealer has won the round!")
        assets["total_winnings"] -= bet
        print(f"Your current total winnings is {assets['total_winnings']:,}")
    elif 21 - calc_total(dealer_hand) > 21 - calc_total(player_hand):
        print(f"\nYou have {player_hand} for a total of {calc_total(player_hand)} and the dealer have {dealer_hand} for a total of {calc_total(dealer_hand)}.")
        print("You have won the round!")
        assets["total_winnings"] += (bet * 1.5)
        print(f"Your current total winnings is {assets['total_winnings']:,}")

    check_winning_condition(difficulty)

    check_game_over(difficulty)

    def continue_playing():
        play_again = input("Would you like to play again? (y or n): ").lower()
        while True:
            try:
                if play_again == 'y':
                    return blackjack()
                elif play_again == 'n':
                    return select_gambling_game()
                else:
                    print("\n------------------------------------Invalid -------------------------------------")
                    print("                            Please select a valid response. (y or n)      ")
                    print("-------------------------------------Input---------------------------------------")
                    return continue_playing()
            except ValueError as e:
                print(e)
                return continue_playing()

    continue_playing()

def roulette():
    global num_choice, color_choice

    roulette_table = {
        "0" : "green",
        "1" : "black",
        "2" : "red",
        "3" : "black",
        "4" : "red",
        "5" : "black",
        "6" : "red",
        "7" : "black",
        "8" : "red",
        "9" : "black",
        "10" : "red",
        "11" : "black",
        "12" : "red",
        "13" : "black",
        "14" : "red",
        "15" : "black",
        "16" : "red",
        "17" : "black",
        "18" : "red",
        "19" : "black",
        "20" : "red",
        "21" : "black",
        "22" : "red",
        "23" : "black",
        "24" : "red",
        "25" : "black",
        "26" : "red",
        "27" : "black",
        "28" : "red",
        "29" : "black",
        "30" : "red",
        "31" : "black",
        "32" : "red",
        "33" : "black",
        "34" : "red",
        "35" : "black",
        "36" : "red"
    }

    print("-------------------------------------------------------------------------------------------------------------------")
    print("                                       Here lies the roulette table: ")
    print("Green (Zero): ")
    for key, value in roulette_table.items():
        if value == "green":
            print(f"{key}, ", end ="")
    print("\nBlack (Odds): ")
    for key, value in roulette_table.items():
        if value == "black":
            print(f"{key}, ", end ="")
    print("\nRed (Evens): ")
    for key, value in roulette_table.items():
        if value == "red":
            print(f"{key}, ", end ="")
    print("\n-------------------------------------------------------------------------------------------------------------------")
    print(f"Your current winnings is ${assets['total_winnings']}. Good Luck!")

    def bet_money():
        bet = None
        while True:
            bet = float(input(f"\nHow much will you bet? (You currently have ${assets['total_winnings']:,}, minimum bet is $1,500): "))
            if bet > assets["total_winnings"]:
                print("-----------------------------------------------Invalid -------------------------------------------------")
                print(f"           You can't bet an amount you don't have! Your current balance is ${assets['total_winnings']}")
                print("------------------------------------------------Input---------------------------------------------------")
                return bet_money()
            elif bet < 1500:
                print("\n------------------------------------Invalid -------------------------------------")
                print("                             Minimum bet is $1,500      ")
                print("-------------------------------------Input---------------------------------------")
                return bet_money()
            else:
                return bet

    def place_bet():
        print("-------------------------------------------------------------------------------------------------------------------")
        print("                                     It's time to place your bet!")
        print("\n1. Luck is on my side. (I'll place bet on a number!)")
        print("2. Skeptical luck. (I'll place bet on colors for now.)")

        def choose_luck():
            global num_choice, color_choice

            choice = input("\nHow lucky are you feeling right now? (1 or 2): ")
            while True:
                try:
                    if choice == "1":
                        input_num_choice = int(input("Choose your lucky number (1 to 36): "))
                        if 1 <= input_num_choice <= 36:
                            num_choice = input_num_choice
                            return num_choice
                        else:
                            print("\n--------------------------------------------Invalid ---------------------------------------------")
                            print("                            Please select a valid response. (Select number from 1 to 36)      ")
                            print("-----------------------------------------------Input-----------------------------------------------")             
                    elif choice == "2":
                        input_color_choice = input("Choose a color (Red or Black): ").lower()
                        if input_color_choice == "red" or input_color_choice == "black":
                            color_choice = input_color_choice
                            return color_choice
                        else:
                            print("\n------------------------------------Invalid -------------------------------------")
                            print("                            Please select a valid response. (Red or Black)      ")
                            print("-------------------------------------Input---------------------------------------")                            
                    else:
                        print("\n------------------------------------Invalid -------------------------------------")
                        print("                            Please select a valid response. (1 or 2)      ")
                        print("-------------------------------------Input---------------------------------------")
                        return choose_luck()
                except ValueError as e:
                    print(e)
                    return choose_luck()
        
        choose_luck()

    place_bet()

    def roll_roulette():
        global num_choice, color_choice
        bet = bet_money()
        rollables = list(roulette_table.keys())
        rolled = random.choice(rollables)
        if rolled in roulette_table:
            color = roulette_table[rolled]
        print(f"\nYour bet was {num_choice}{color_choice}. Meanwhile, the roulette has rolled {rolled} which has the color {color}.")

        if num_choice == str(rolled):
            assets["total_winnings"] += (35 * bet)
            print(f"\nYou won by the number!! Congrats! You now have ${assets['total_winnings']:,}.")
        elif color_choice == color:
            assets["total_winnings"] += (17.5 * bet)
            print(f"\nYou won by the color! You now have ${assets['total_winnings']:,}.")
        else:
            assets["total_winnings"] -= bet
            print(f"\nYou have lost the money you had bet. You now have ${assets['total_winnings']:,}.")

    check_winning_condition(difficulty)

    check_game_over(difficulty)

    roll_roulette()

    def continue_playing():
        play_again = input("Would you like to play again? (y or n): ").lower()
        while True:
            try:
                if play_again == 'y':
                    return roulette()
                elif play_again == 'n':
                    return select_gambling_game()
                else:
                    print("\n------------------------------------Invalid -------------------------------------")
                    print("                            Please select a valid response. (y or n)      ")
                    print("-------------------------------------Input---------------------------------------")
                    return continue_playing()
            except ValueError as e:
                print(e)
                return continue_playing()

    continue_playing()

def difficulty():
    print("\n--------------------------------------------------------------")
    print("~---+---~ Welcome to your gambling addiction ~---+---~")
    print("Please select how addicted you are to gambling (C, M, E): ")
    print("C - Casual (Must accumulate $100,000)")
    print("M - Moderate (Must accumulate $500,000)")
    print("E - Extreme (Must accumulate $1,000,000)")
    print("---------------------------------------------------------------")

    diff_choice = input("\nThrough self diagnosis, my gambling addiction fits that of: ").upper()
    while True:
        try:
            if diff_choice == "C":
                print("-----------------------------------------------------------------------------------------------------------------------------")
                print(f"            Your goal is to accumulate a total winnings of ${totWinning_amountC:,}. Right now you have ${assets['total_winnings']:,}.")
                print("-----------------------------------------------------------------------------------------------------------------------------")
                return select_gambling_game()
            elif diff_choice == "M":
                print("-----------------------------------------------------------------------------------------------------------------------------")
                print(f"            Your goal is to accumulate a total winnings of ${totWinning_amountM:,}. Right now you have ${assets['total_winnings']:,}.")
                print("-----------------------------------------------------------------------------------------------------------------------------")
                return select_gambling_game()
            elif diff_choice == "E":
                print("-----------------------------------------------------------------------------------------------------------------------------")
                print(f"            Your goal is to accumulate a total winnings of ${totWinning_amountE:,}. Right now you have ${assets['total_winnings']:,}.")
                print("-----------------------------------------------------------------------------------------------------------------------------")
                return select_gambling_game()
            else:
                print("\n--------------------------------------Invalid-------------------------------------------------")
                print("         ^^^Please select from the three stages of gambling addiction displayed (C, M, E)")
                print("---------------------------------------Input---------------------------------------------------")
                return difficulty()
        except ValueError as e:
            print(e)
            return difficulty()

def intro():

    print("\n-------------------------------------------------------------------------")
    print("\n          This program is a simulation of gambling addiction")
    print("\n-------------------------------------------------------------------------")
    difficulty()

intro()