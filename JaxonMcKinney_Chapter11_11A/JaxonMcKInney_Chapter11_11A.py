## deck class and simulate playing five card draw (dont worry about actually scoring)
import random

class Deck:

    ## defines deck, including suits and ranks
    def __init__(self, n_decks = 1):
        self.card_list = [num + suit
                          for suit in '\u2665\u2666\u2663\u2660'
                          for num in 'A23456789TJQK'
                          for deck in range(n_decks)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)

    ## deals a card
    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print("Reshuffling...!!!")
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card

    ## deals a card without appending to hand (for other function reasons)
    def ex_deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print("Reshuffling...!!!")
        new_card = self.card_list.pop()
        return new_card

    ## clears the hand
    def new_hand(self):
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()

    ## discards a card and replaces it
    def discard_replace(self, discard):
        self.discards_list.append(self.cards_in_play_list[discard-1])
        self.cards_in_play_list.remove(self.cards_in_play_list[discard-1])
        self.cards_in_play_list.insert(discard-1, self.ex_deal())


def main():

    dk = Deck()

    while True:

        ## deals five cards
        for i in range(5):
            dk.deal()

        ## prints the hand
        for i in dk.cards_in_play_list:
            print(i, end=' ')

        ## gets which cards to discard
        discard = input('\nWhich cards would you like to discard? (Type the position of each number, '
                        'separate using a space) (0 keeps hand): ')

        ## splits the discarded cards and sets them to be replaced
        discard = discard.split(' ')
        for i in discard:
            dk.discard_replace(int(i))

        ## prints the new hand
        for i in dk.cards_in_play_list:
            print(i, end=' ')

        ## loop break
        inp = input("\nWould you like to play again? (y/n): ")
        if inp == "n":
            break

        dk.new_hand()

    print('Thanks for playing!')


if __name__ == "__main__":
    main()
