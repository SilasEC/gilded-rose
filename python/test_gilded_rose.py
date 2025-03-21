"""
Unit Tests for Gilded Rose Inventory Management

This script contains unit tests for the Gilded Rose inventory system, 
ensuring that different item types update their quality and sell-in 
values according to the specified rules.

Author: Silas Curtis
Date: 3.20.25
"""
import unittest

from gilded_rose import Item, GildedRose, Default, Aged, Ticket, Legendary, Conjured


class GildedRoseTest(unittest.TestCase):
    """Create all tests."""
    
    def test_default(self):
        items = [Default("cake", 20, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(39, items[0].quality)

    def test_default_after_sell_by(self):
        items = [Default("pie", -1, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(38, items[0].quality)

    def test_aged(self):
        items = [Aged("wine", 20, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(41, items[0].quality)
    
    def test_aged_ceiling(self):
        items = [Aged("vinegar", 20, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_ticket(self):
        items = [Ticket("sam smith concert", 20, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(41, items[0].quality)

    def test_ticket_five_or_less(self):
        items = [Ticket("tom mcdonald concert", 2, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(43, items[0].quality)

    def test_ticket_after_sell_by(self):
        items = [Ticket("jonas brothers concert", 0, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_conjured(self):
        items = [Conjured("pet genie", 8, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(38, items[0].quality)

    def test_legendary(self):
        items = [Legendary("big chungus body pillow", 20, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(40, items[0].quality)

if __name__ == '__main__':
    unittest.main()
