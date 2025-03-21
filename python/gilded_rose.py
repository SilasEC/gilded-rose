"""
Gilded Rose Refactored

This script implements an object-oriented solution for managing 
inventory items in the Gilded Rose system. Different item types 
depreciate or appreciate in quality based on specific rules.

Classes:
- GildedRose: Handles bulk updates of item quality.
- Item: Base class for all items.
- Default: Standard items that degrade over time.
- Aged: Items that improve in quality over time.
- Legendary: Items that do not change in quality.
- Ticket: Items that increase in quality until expiration.
- Conjured: Items that degrade in quality at an accelerated rate.

Author: Silas Curtis
Date: 3.20.25
"""

class GildedRose(object):
    """Creates a class for the store, and when called will update all items in the store for the next day."""

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_date()
            item.update_quality()

class Item:
    """Create parent class for all items to be sold."""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Default (Item):
    """Create class for default items, which depreciate over time, and faster after sell by date."""

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_date(self):
        self.sell_in = self.sell_in-1
    
    def update_quality(self):
        if self.sell_in > 0:
            self.quality = max(self.quality-1, 0)
        else:
            self.quality = max(self.quality-2, 0)
        

class Aged (Item):
    """Create class for aged items, which appreciate over time."""

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_date(self):
        self.sell_in = self.sell_in - 1
    
    def update_quality(self):
        self.quality = min(self.quality+1, 50)


class Legendary (Item):
    """Create class for legendary items, which effectively have no sell by date and do not change in quality."""

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_date(self):
        self.sell_in = self.sell_in
    
    def update_quality(self):
        self.quality = self.quality

class Ticket (Item):
    """Create class for tickets, whose quality changes at different rates."""

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_date(self):
        self.sell_in = self.sell_in-1
    
    def update_quality(self):

        if self.sell_in < 0:
            self.quality = 0

        elif self.sell_in <= 5:
            self.quality = min(self.quality + 3, 50)

        elif self.sell_in <=10:
            self.quality = min(self.quality+2,50)

        else:
            self.quality = min(self.quality + 1, 50)
        

class Conjured (Item):
    """Create class for conjured items, which depreciate quickly."""

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_date(self):
        self.sell_in = self.sell_in-1

    def update_quality(self):
        self.quality = max(self.quality-2, 0)