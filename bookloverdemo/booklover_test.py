

import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        
        test_booklover= BookLover('Isha', 'ia@gmail.com', 'Fiction')
        
        test_booklover.add_book('Testing Book', '4') #need book name and rating
        
        
        self.assertTrue(test_booklover.has_read('Testing Book'))
        

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        
        test_booklover= BookLover('Isha', 'ia@gmail.com', 'Fiction')
      
        test_booklover.add_book('Testing Book', '4') #add once
        test_booklover.add_book('Testing Book', '4') #add twice 
        
        total_once=1 
        actualval= len(test_booklover.book_list['book_name'] == 'Testing Book')
        
        self.assertEqual(total_once, actualval) 
        
        
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        
        test_booklover= BookLover('Isha', 'ia@gmail.com', 'Fiction')
        test_bookname= 'Testing' 
        test_rating= 4
        
        
        test_booklover.add_book(test_bookname, test_rating)
        self.assertTrue(test_booklover.has_read(test_bookname))
       
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        
        new_booklover= BookLover('Sam', 'sam@gmail.com', 'Fantasy')
        newtestbook= 'Educated' 
        new_rating= 5
                                 
        self.assertFalse(new_booklover.has_read(newtestbook))
        
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
       
       
        test_booklover= BookLover('Isha', 'ia@gmail.com', 'Fiction')
        testbooklist = [("Book1", 2), ("Book2", 3), ("Book3", 4), ("Book4", 5)]
        
        for book in testbooklist: 
            test_booklover.add_book(book[0],book[1])
        
        
        
        expected= len(testbooklist)
        actual= test_booklover.num_books
        
        self.assertEqual(expected, actual) 
        

        
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        
        test_booklover= BookLover('Isha', 'ia@gmail.com', 'Fiction')
        testbooklist = [("Book1", 2), ("Book2", 3), ("Book3", 4), ("Book4", 5)]
        
        for book in testbooklist: 
            test_booklover.add_book(book[0],book[1])
            
        returned_books= test_booklover.fav_books()
    
    
        checkval= [] #if the rating is over 3 then add it to the list
        for book,rating in testbooklist: 
            if rating > 3: 
                checkval.append(book)
        
        
        
        self.assertEqual(len(returned_books), len(checkval))
        
  
    
if __name__ == '__main__':
    
    unittest.main(verbosity=3)