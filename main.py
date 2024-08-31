import random  # Importing the random module for shuffling the deck

def create_deck():
    # Creates a deck of 52 cards, with face values for Blackjack.
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']  # Define the suits in a standard deck
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']  # Define card values
    deck = [f"{value} of {suit}" for suit in suits for value in values]  # Generate a deck of cards
    random.shuffle(deck)  # Shuffle the deck randomly
    return deck

def card_value(card):
    # Returns the value of a single card for Blackjack, adjusted for strings.
    value = card.split(' ')[0]  # Extract the value part from the card string
    if value in ['Jack', 'Queen', 'King']:  # Face cards have a value of 10
        return 10
    elif value == 'Ace':  # Ace can have a value of 1 or 11
        return 11  # We set it to 11 here for simplicity
    else:  # Other cards have their face value
        return int(value)

def hand_value(hand):
    # Calculates the total value of a hand of cards.
    value = sum(card_value(card) for card in hand)  # Sum up the values of all cards in the hand
    num_aces = sum(1 for card in hand if 'Ace' in card)  # Count the number of Aces in the hand
    while value > 21 and num_aces:  # Adjust the value if there are Aces and the total value exceeds 21
        value -= 10
        num_aces -= 1
    return value

def get_valid_bet(chips):
    # Prompts the user to place a bet and ensures it's a valid input.
    while True:
        try:
            bet = int(input("Place your bet: "))  # Prompt the user to enter their bet
            if bet <= 0:  # Ensure the bet is a positive number
                print("Please enter a positive bet.")
            elif bet > chips:  # Ensure the user has enough chips to place the bet
                print("You don't have enough chips!")
            else:
                return bet
        except ValueError:  # Handle invalid input (non-integer)
            print("Please enter a valid number for your bet.")

def get_valid_action():
    # Prompts the user to choose an action and ensures it's a valid input.
    while True:
        action = input("Do you want to (h)it or (s)tand? ").lower()  # Prompt the user to choose action
        if action in ['h', 's']:  # Check if the input is valid (hit or stand)
            return action
        else:
            print("Invalid input! Please enter 'h' to hit or 's' to stand.")

def play_game():
    chips = 10  # Initialize the player's chips
    while chips > 0:  # Continue playing as long as the player has chips
        print(f"You have {chips} chips.")

        bet = get_valid_bet(chips)  # Get the player's bet

        deck = create_deck()  # Create a shuffled deck of cards
        player_hand = [deck.pop(), deck.pop()]  # Deal two cards to the player
        dealer_hand = [deck.pop(), deck.pop()]  # Deal two cards to the dealer

        print(f"Your hand is a {' and a '.join(player_hand)} (with a total value of {hand_value(player_hand)})")
        print(f"Dealer's show card: {dealer_hand[0]}")

        # Player's turn
        while hand_value(player_hand) < 21:  # Allow the player to continue playing until they bust or stand
            action = get_valid_action()  # Prompt the player for action (hit or stand)
            if action == 'h':
                player_hand.append(deck.pop())  # Deal an additional card to the player
                print(f"Your hand is a {' and a '.join(player_hand)} (with a total value of {hand_value(player_hand)})")
            elif action == 's':
                break  # Player chooses to stand, exit the loop

        if hand_value(player_hand) > 21:
            print("Bust! You lose.")  # Player busts if their hand value exceeds 21
            chips -= bet  # Deduct the bet amount from the player's chips
            print(f"You lost {bet} chips.")
            if chips <= 0:
                print("You are out of chips! Run your code again to reset your chip count.")
                return  # Exit the game if the player is out of chips
            continue

        # Dealer's turn
        while hand_value(dealer_hand) < 17:  # Dealer must hit until their hand value is at least 17
            dealer_hand.append(deck.pop())  # Deal an additional card to the dealer
            print(f"Dealer's hand: {' and a '.join(dealer_hand)} (with a total value of {hand_value(dealer_hand)})")

        if hand_value(dealer_hand) > 21 or hand_value(player_hand) > hand_value(dealer_hand):
            print("You win!")  # Player wins if the dealer busts or their hand value is higher than the dealer's
            chips += bet  # Add the bet amount to the player's chips
            print(f"You won {bet} chips.")
        elif hand_value(player_hand) < hand_value(dealer_hand):
            print("Dealer wins.")  # Dealer wins if their hand value is higher than the player's
            chips -= bet  # Deduct the bet amount from the player's chips
            print(f"You lost {bet} chips.")
        else:
            print("It's a tie.")  # It's a tie if both player and dealer have the same hand value

        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()  # Ask the player if they want to play again
            if play_again in ['yes', 'no', 'y', 'n']:  # Check if the input is valid (yes or no)
                break
            else:
                print("Invalid input! Please enter 'yes' or 'no'.")

        if play_again in ['no', 'n']:
            print("Thank you for watching this code script!")  # Thank the player for playing
            return  # Exit the game if the player chooses not to play again

if __name__ == '__main__':
    play_game()  # Start the game
