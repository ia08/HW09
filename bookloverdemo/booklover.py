import pandas as pd 

class BookLover(): 
    def __init__(self,name, email,fav_genre):
        self.name= name 
        self.email= email 
        self.fav_genre= fav_genre
        self.num_books = 0 #initilize count
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]}) #create empty data frame with 2 columns
        
    def add_book(self, book_name, book_rating): #method 1
        
        new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [book_rating]})
        
        if (self.book_list['book_name']== book_name).any(): 
            print("This book already exists in the Book List!") 
            
        else: 
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1 
    
    def has_read(self, book_name): 
        if (self.book_list['book_name']== book_name).any(): 
            return True
        else:
            return False
    
    def num_books_read(self):
        
        return (self.num_books)
    
    def fav_books(self):
        return self.book_list[self.book_list.book_rating > 3]
    

if __name__ == '__main__':
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
