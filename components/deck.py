import random


class Deck:

    def __init__(self, card_list: list):
        self.card_list = card_list
        if len(card_list) > 1:
            random.shuffle(card_list)

    def deal(self):
        temp = self.card_list[0]
        list.remove(self.card_list[0])
        return temp
