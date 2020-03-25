# Practicing Classes

# Playing Card Class


class Card(object):
    '''Playing card'''
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.color = 'Not Known'
        if (self.suit == 'Diamonds') or (self.suit == 'Hearts'):
            self.color = 'Red'
        else:
            self.color = "Black"

    def __str__(self):
        my_card = str(self.value) + 'of' + str(self.suit)
        return my_card
