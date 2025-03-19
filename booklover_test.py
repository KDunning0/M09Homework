import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self):
        Booklov1=BookLover('James','email@email.com','Comedy')
        Booklov1.add_book('Fried Egg',4)
        current_books=list(Booklov1.book_list['book_name'].values)
        self.assertTrue('Fried Egg' in current_books)
    def test_2_add_book(self):
        Booklov1=BookLover('James','email@email.com','Comedy')
        Booklov1.add_book('Fried Egg',4)
        Booklov1.add_book('Fried Egg',4)
        current_books=list(Booklov1.book_list['book_name'].values)
        self.assertEqual(current_books.count('Fried Egg'),1)
    def test_3_has_read(self):
        Booklov1=BookLover('James','email@email.com','Comedy')
        Booklov1.add_book('Fried Egg',4)
        self.assertTrue(Booklov1.has_read('Fried Egg'))
    def test_4_has_read(self):
        Booklov1=BookLover('James','email@email.com','Comedy')
        Booklov1.add_book('Fried Egg',4)
        self.assertFalse(Booklov1.has_read('Fried Bacon'))
    def test_5_num_books_read(self):
        Booklov1=BookLover('James','email@email.com','Comedy')
        Booklov1.add_book('Fried Egg',4)
        Booklov1.add_book('Pancakes',5)
        Booklov1.add_book('Grits',1)
        Booklov1.add_book('Jam',3)
        self.assertEqual(Booklov1.num_books_read(),4)
    def test_6_fav_books(self):
        Booklov1=BookLover('James','email@email.com','Comedy')
        Booklov1.add_book('Fried Egg',4)
        Booklov1.add_book('Pancakes',5)
        Booklov1.add_book('Grits',1)
        Booklov1.add_book('Jam',3)
        fav_ratings=list(Booklov1.fav_books().loc[:,'book_rating'])
        self.assertTrue(all(rating > 3 for rating in fav_ratings))
        
if __name__ == '__main__':
    unittest.main(verbosity=3)
        
        
        
        