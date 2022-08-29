concert = "Backstage passes to a TAFKAL80ETC concert"
class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != concert:
                self.quality_less_zero(item)
            else:
                self.quality_less_fifty(item)
                if item.name == concert:
                    if item.sell_in < 11:
                        self.quality_less_fifty(item)
                    if item.sell_in < 6:
                        self.quality_less_fifty(item)
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                self.passed_sell_by(item)

    def passed_sell_by(self, item):
        if item.name != "Aged Brie":
            if item.name != concert:
                self.quality_less_zero(item)
            else:
                item.quality = 0
        else:
            self.quality_less_fifty(item)

    def quality_less_fifty(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
            
    def quality_less_zero(self, item):
        if item.quality > 0:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.quality = item.quality - 1