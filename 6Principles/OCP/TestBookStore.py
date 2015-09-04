#!/usr/bin/env python
#encoding: utf-8

import unittest

from BookStore import NovelBook, OffNovelBook

class TestBookStore(unittest.TestCase):
    '''
    Test class BookStore
    '''

    def test_NovelBook_getPrice(self):
        novelBook = NovelBook("Wei Chen", 4000, "Qian Zhongshu")
        self.assertEqual(4000, novelBook.getPrice())

    def test_OffNovelBook_getPriceBelow4000(self):
        offNovelBook = OffNovelBook("Wei Chen", 4000, "Qian Zhongshu")
        self.assertEqual(3200, offNovelBook.getPrice())

    def test_OffNovelBook_getPriceAbove4000(self):
        offNovelBook = OffNovelBook("Wei Chen", 4001, "Qian Zhongshu")
        self.assertEqual(3600, offNovelBook.getPrice())


if __name__ =='__main__':
    unittest.main()

