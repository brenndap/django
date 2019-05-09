import re as r
import pandas as pd


class BooksData:

    def __init__(self, title, author, publisher, genre, pages):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.pages = pages

    def __str__(self):
        return '{}/{}/{}/{}/{}'.format(self.title, self.author, self.publisher, self.genre, self.pages)

    def __repr__(self):
        return '{}/{}/{}/{}/{} '.format(self.title, self.author, self.publisher, self.genre, self.pages)


def read_data_frame():

    file = pd.read_csv("books.csv")
    file_clean = file.fillna('-')
    count = 0
    data_frame = []

    while count < len(file_clean.index):
        data = list(file_clean.loc[[count][0]])
        count += 1
        data_frame.append(data)

    return data_frame


def books_rearrangement(data_frame):
    new_data_frame = []

    for book in data_frame:
        new_data_list = []

        for items in book:

            new_data = r.split(r'[,]', str(items))

            if len(new_data) > 1:
                new_data_list.append(''.join(new_data[1].strip()+' '+new_data[0]))
            elif len(new_data) == 1:
                new_data_list.append(new_data[0])

        new_data_frame.append(new_data_list)

    return new_data_frame


def main():

    books_file = read_data_frame()
    books_data_frame = books_rearrangement(books_file)
    books_data = []
    books_instances_list = []

    for book_list in books_data_frame:
        attributes = ['title', 'author', 'genre', 'pages', 'publisher']
        book_dict = dict(zip(attributes, book_list))
        books_data.append(book_dict)

    for book_dict in books_data:
        book = BooksData(title=book_dict['title'], author=book_dict['author'], genre=book_dict['genre'],
                         pages=book_dict['pages'], publisher=book_dict['publisher'])
        books_instances_list.append(book)

    return books_data


'''if __name__ == "__main__":
    main()'''







