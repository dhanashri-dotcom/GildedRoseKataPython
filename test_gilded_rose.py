# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6)]
        gr = GildedRose(items)
    
        gr.update_quality()

        #assert gr.items == [Item(vest, 0, 1), Item(vest, 8, 18), Item(vest, 3, 5)]
        self.assertEqual(gr.items[0].name, vest)
        self.assertEqual(gr.items[0].sell_in, 0)
        self.assertEqual(gr.items[0].quality, 1)

        self.assertEqual(gr.items[1].name, vest)
        self.assertEqual(gr.items[1].sell_in, 8)
        self.assertEqual(gr.items[1].quality, 18)

        self.assertEqual(gr.items[2].name, vest)
        self.assertEqual(gr.items[2].sell_in, 3)
        self.assertEqual(gr.items[2].quality, 5)

    def test_conjured_item_should_degrade_twice_as_fast(self):
        conjured = "Conjured Mana Cake"
        items = [Item(conjured, 3, 6), Item(conjured, 2, 8)]
        gr = GildedRose(items)
        
        gr.update_quality()

        #assert gr.items == [Item(conjured, 2, 4), Item(conjured, 1, 6)]
        self.assertEqual(gr.items[0].name, conjured)
        self.assertEqual(gr.items[0].sell_in, 2)
        self.assertEqual(gr.items[0].quality, 4)

        self.assertEqual(gr.items[1].name, conjured)
        self.assertEqual(gr.items[1].sell_in, 1)
        self.assertEqual(gr.items[1].quality, 6)

    def test_aged_brie_should_increase_in_quality(self):
        brie = "Aged Brie"
        items = [Item(brie, 2, 0), Item(brie, 1, 48), Item(brie, 4, 48)]
        gr = GildedRose(items)
        
        gr.update_quality()

        #assert gr.items == [Item(brie, 1, 1), Item(brie, 0, 49), Item(brie, 3, 49)]
        #Commented this assertion as it requires me to add equals function to the Item class and Item Class specifically mentions not to change anything
        #Instead we rely on more granualr assetions as seen below. 
        #If we would not want to comment the object assertion above, we can uncomment the equals function in Item class and the test would pass for that case as well.
        self.assertEqual(gr.items[0].name, brie)
        self.assertEqual(gr.items[0].sell_in, 1)
        self.assertEqual(gr.items[0].quality, 1)

        self.assertEqual(gr.items[1].name, brie)
        self.assertEqual(gr.items[1].sell_in, 0)
        self.assertEqual(gr.items[1].quality, 49)

        self.assertEqual(gr.items[2].name, brie)
        self.assertEqual(gr.items[2].sell_in, 3)
        self.assertEqual(gr.items[2].quality, 49)

    def test_conjured_items_degrade_twice_as_fast_after_sellin_date(self):
        items = [Item("Conjured Mana Cake", 0, 6)]
        gr = GildedRose(items)
        
        gr.update_quality()
        
        self.assertEqual(gr.items[0].quality, 2)
        self.assertEqual(gr.items[0].sell_in, -1)

    def test_sulfuras_should_not_change(self):
        sulfuras = "Sulfuras, Hand of Ragnaros"
        items = [Item(sulfuras, 2, 30), Item(sulfuras, 3, 40)]
        gr = GildedRose(items)
        
        gr.update_quality()

        #assert gr.items == [Item(sulfuras, 2, 30), Item(sulfuras, 3, 40)]
        self.assertEqual(gr.items[0].name, sulfuras)
        self.assertEqual(gr.items[0].sell_in, 2)
        self.assertEqual(gr.items[0].quality, 30)

        self.assertEqual(gr.items[1].name, sulfuras)
        self.assertEqual(gr.items[1].sell_in, 3)
        self.assertEqual(gr.items[1].quality, 40)

    def test_quality_never_more_than_50(self):
        items = [Item("Aged Brie", 2, 50)]
        gr = GildedRose(items)
        
        gr.update_quality()
        
        self.assertEqual(gr.items[0].quality, 50)
        self.assertEqual(gr.items[0].sell_in, 1)

    def test_quality_never_negative(self):
        items = [Item("Elixir of the Mongoose", 5, 0)]
        gr = GildedRose(items)
        
        gr.update_quality()
        
        self.assertEqual(gr.items[0].quality, 0)
        self.assertEqual(gr.items[0].sell_in, 4)

    def test_backstage_passes_increase_by_2_when_sellin_date_less_than_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 9, 20)]
        gr = GildedRose(items)
        
        gr.update_quality()
        
        self.assertEqual(gr.items[0].quality, 22)
        self.assertEqual(gr.items[0].sell_in, 8)

    def test_backstage_passes_increase_by_3_when_sellin_date_less_than_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 20)]
        gr = GildedRose(items)
        
        gr.update_quality()
        
        self.assertEqual(gr.items[0].quality, 23)
        self.assertEqual(gr.items[0].sell_in, 3)

    def test_backstage_passes_drop_to_0_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gr = GildedRose(items)
        
        gr.update_quality()
        
        self.assertEqual(gr.items[0].quality, 0)
        self.assertEqual(gr.items[0].sell_in, -1)

    def test_normal_item_degrades_twice_as_fast_after_sellin_date(self):
        items = [Item("Elixir of the Mongoose", 0, 10)]
        gr = GildedRose(items)
        
        gr.update_quality()
        
        self.assertEqual(gr.items[0].quality, 8)
        self.assertEqual(gr.items[0].sell_in, -1)   

if __name__ == '__main__':
    unittest.main()
