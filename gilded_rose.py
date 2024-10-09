from abc import ABC, abstractmethod

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
    # def __eq__(self, other):
    #     if isinstance(other, Item):
    #         return self.name == other.name and self.sell_in == other.sell_in and self.quality == other.quality
    #     return False

class UpdateStrategy(ABC):
    """Abstract base class representing a strategy for updating items."""
    
    @abstractmethod
    def update(self, item: Item):
        pass


class NormalItemStrategy(UpdateStrategy):
    def update(self, item: Item):
        if item.quality > 0:
            item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1

class AgedBrieStrategy(UpdateStrategy):
    def update(self, item: Item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1


class SulfurasStrategy(UpdateStrategy):
    def update(self, item: Item):
        # Sulfuras does not change in quality or sell_in
        pass


class BackstagePassesStrategy(UpdateStrategy):
    def update(self, item: Item):
        if item.sell_in > 10:
            item.quality += 1
        elif 5 < item.sell_in <= 10:
            item.quality += 2
        elif 0 < item.sell_in <= 5:
            item.quality += 3
        else:
            item.quality = 0

        if item.quality > 50:
            item.quality = 50

        item.sell_in -= 1


class ConjuredItemStrategy(UpdateStrategy):
    def update(self, item: Item):
        if item.quality > 0:
            item.quality -= 2
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 2
        if item.quality < 0:
            item.quality = 0


class GildedRose:
    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items
        # Mapping item names to their corresponding strategies
        self.strategies = {
            "Aged Brie": AgedBrieStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassesStrategy(),
            "Conjured Mana Cake": ConjuredItemStrategy(),
        }

    def update_quality(self):
        for item in self.items:
            # Select the appropriate strategy based on the item name
            strategy = self.strategies.get(item.name, NormalItemStrategy())
            # Delegate the update logic to the selected strategy
            strategy.update(item)