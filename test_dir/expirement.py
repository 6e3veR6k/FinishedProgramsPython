class Buildings:
    def __init__(self, item, color, countnumber):
        self.what = item
        self.color = color
        self.number = countnumber
        self.mwhere(countnumber)



    def incomingStock(self, numberofnewitems):
        self.number = self.number + numberofnewitems
        self.mwhere(self.number)

    def outputStock(self, numberofexistingitems):
        if self.number >= numberofexistingitems:
            self.number = self.number - numberofexistingitems
        else:
            self.number = 0

        self.mwhere(self.number)

    def mwhere(self, nnumber ):
        self.number = nnumber
        print self.number
        if self.number == 0:
            self.where = 'We have nothing'
        if 0 < self.number < 100:
            self.where = 'We have some in small stock room'
        else:
            self.where = 'You should look in warehouse'

#---------------------------------------------------------------------------

today = Buildings('planks', 'white', 30)
midday = Buildings('planks', 'red', 500)
evening = Buildings('bricks', 'white', 300)

print today.what, today.color, today.where
print midday.what, midday.color, midday.where
print evening.what, evening.color, evening.where

today.incomingStock(300)
print today.number, today.where

midday.outputStock(550)
print midday.number, midday.where

print midday.what, midday.where, midday.number, midday.color



