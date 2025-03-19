import numpy as np
import pandas as pd

class BookLover:
    def __init__(self,name:str,email:str,fav_genre:str):
        self.name=name
        self.email=email
        self.fav_genre=fav_genre
        self.book_list=pd.DataFrame({'book_name':[],'book_rating':[]})
    def add_book(self,book_name:str,book_rating:int):
        current_books=list(self.book_list['book_name'].values)
        if not (0 <= book_rating <= 5):
            print('Invalid rating, please add a rating between 0-5')
            return
        if book_name not in current_books:
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [book_rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        else:
            print('Book already present in list, please add different book.')     
    def has_read(self,book_name:str):
        current_books=list(self.book_list['book_name'].values)
        if book_name in self.book_list['book_name'].values:
            return True
        else:
            return False
    def num_books_read(self):
        return len(self.book_list)
    def fav_books(self):
        return self.book_list[self.book_list.book_rating > 3].sort_values(by='book_rating',ascending=False)