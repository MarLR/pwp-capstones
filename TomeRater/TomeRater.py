class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.books={}

#create get_email method
    def get_email(self):
        return '{email}'.format(email=self.email)

#create method change_email
    def change_email(self, new_email):
      self.new_email=new_email
      print ('{old} has been changed to {new}'.format(old=self.email, new=self.new_email))
      self.email=new_email
      return self.email

#create representation method
    def __repr__(self):
        return 'User: {name}, email: {email}, books read:' \
               ' {books}:{list}'.format(name=self.name, email=self.email,
                          books=len(self.books), list=(self.books.keys()))

#create method eq that compares two users by name and email
    def __eq__(self, other):
        if self.name ==other and self.email==other:
            return True
        else:
            return False
#create method read_book that creates a dictionary of books and their ratings
    def read_book(self, book, rating=None):
        self.books[book]=rating
        return self.books

#create method which finds a user's average ratings
    def get_average_rating(self):
        total_ratings = 0
        num_of_ratings = 0
        for rating in self.books.values():
            if rating != None:
                total_ratings += rating
                num_of_ratings += 1
        average_rating = total_ratings/num_of_ratings
        return average_rating


class Book:
    def __init__(self, title, isbn, cost):
        self.title=title
        self.isbn=isbn
        self.cost=cost
        self.ratings=[]

    def __repr__(self):
        return ('{title}:{ISBN} costs ${cost}.').format(title=self.title,
                                                ISBN=self.isbn,
                                                cost=self.cost)

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn=new_isbn
        return 'The ISBN of this book has been updated to {}'.format(self.isbn)

    def get_cost(self):
        return self.cost

    def update_cost(self, new_cost):
        self.cost=new_cost
        return "The cost of this book has been updated to {cost}".format(cost=self.cost)

    def add_rating(self, rating):
        if rating >=0 and rating <=4:
            self.ratings.append(rating)
        else:
            return 'Invalid Rating'

    def __eq__ (self, other):
        if self.title==other and self.isbn==other and self.cost==other:
            return True
        else:
            return False
  #method that calculates the average rating of a particular book.
    def get_average_rating(self):
        total_ratings = 0
        num_of_ratings = 0
        for rating in self.ratings:
            total_ratings += rating
            num_of_ratings += 1
        if num_of_ratings >0:
            average_rating = total_ratings/num_of_ratings
        else:
            average_rating = 0
        return average_rating
#method to make class Book hashable
    def __hash__(self):
        return hash((self.title, self.isbn, self.cost))

#class Fiction defines all fiction books.  It is a sub-class of Book.
class Fiction (Book):
    def __init__(self,title, isbn, cost, author):
        super().__init__(title, isbn, cost)
        self.author=author

    def get_author(self):
        return self.author

    def __repr_(self):
        return '{book} by {author}'.format(book=self.book, author=self.author)

#class Non_Fiction defines all non-fiction books.  It is a sub-class of Book
class Non_Fiction(Book):
    def __init__(self, title, isbn, cost, subject, level):
        super().__init__(title, isbn, cost)
        self.subject = subject
        self.level=level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr_(self):
        return '{title} a {level} manual about {subject}'.format(self.title, self.level, self.subject)

class TomeRater:
    def __init__(self):
        self.users={} #maps users email to users
        self.books={} #maps books to # of users who have read the book

#Application Methods
    def create_book(self,title,isbn,cost):
        this_book = Book(title, isbn, cost)
        return this_book

    def create_novel(self,title, isbn, cost, author):
        this_fiction=Fiction(title, isbn, cost, author)
        return this_fiction

    def create_non_fiction(self,title, isbn, cost, subject, level):
        this_non_fiction=Non_Fiction(title, isbn, cost, subject, level)
        return this_non_fiction

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            if rating != None:
                book.add_rating(rating)

            if book in self.books.keys():
                self.books[book]+=1
            else:
                self.books[book]=1
        else:
            print ('No user with email '+email + '!')


    def add_user (self, name, email, user_books=None):
        if email in self.users.keys():
            print ("{email} already exists".format(email=email))
        else:
            if '@' in email:
                if '.com' in email or '.org' in email or '.edu' in email:
                    this_user = User(name, email)
                    self.users[email]=this_user
                    if user_books != None:
                        for book in user_books:
                            Tome_Rater.add_book_to_user(book, email, rating=None)

                else:
                    print('{email} is not a valid email address'.format(email=email))
            else:
                print('{email} is not a valid email address'.format(email=email))


#Analysis Methods
    def print_catalog(self):
        for book in self.books.keys():
            print (book.title +', $'+ str(book.cost))

    def print_users(self):
        for user in self.users.values():
            print (user)

    def get_most_read_book (self):
        largest_reader_value = float("-inf")
        for book in self.books.keys():
            if self.books[book] > largest_reader_value:
                largest_reader_value = self.books[book]
                largest_book_name = book.title
        return '"{largest_book}" has been read the most:' \
               ' {largest_value} times'.format\
            (largest_book=largest_book_name, largest_value=largest_reader_value)


    def highest_rated_book(self):
        highest_rating = 0
        for book in self.books.keys():
            if book.get_average_rating()>highest_rating:
                highest_rated_book = book.title
                highest_rating = book.get_average_rating()
        return '"{book}" is highest rated book at a rating of {rating}'.format\
            (book=highest_rated_book, rating=highest_rating)

    def most_positive_user(self):
        most_positive_ratings = 0
        for user in self.users.values():
            rating = user.get_average_rating()
            if rating > most_positive_ratings:
                most_positive_user= user.name
                most_positive_ratings=rating
        return'{user} is most positive user with an average rating of {rating}'.format\
            (user=most_positive_user, rating=most_positive_ratings)

    def n_most_prolific_reader(self,n):
        #make a list of lists [user name, number of books read]
        make_list = []

        for user in self.users.values():
            make_list.append([user.name, len(user.books)])

        #sort list based on number of books read
        for i in range(0,len(make_list)):
            for j in range (0, len(make_list)-i-1):
                if make_list[j][1]>make_list[j+1][1]:
                    temp=make_list[j]
                    make_list[j]=make_list[j+1]
                    make_list[j+1]=temp
        #choose top n readers
        if len(make_list) < n:
            return 'There are only ' + str(len(make_list)) + ' readers; not ' +str(n)+'.'
        else:
            index = 1
            while index <= n:
                    if index+1 <= len(make_list) and make_list[-index - 1][1] == make_list[-index][1]:
                        print("ranking at #" + str(index) + ":")
                        while index+1 <= len(make_list) and index <= n and make_list[-index - 1][1] == make_list[-index][1]:
                            print('     ' + make_list[-index][0])
                            index += 1
                            n += 1
                            if make_list[-index - 1][1] != make_list[-index][1]:
                                print('     {reader}'.format(reader=make_list[-index][0]))
                                n -= 1
                                index += 1
                    else:
                        print('Ranking at #' + str(index) + ' reader: ' + str(make_list[-index][0]))
                        index += 1
    def n_most_read_books(self,n):
        #make a list of lists [book title, number of readers]
        make_list = []
        for book in self.books.keys():
            readers = self.books[book]
            make_list.append([book.title, readers])
        # sort the list based on number of readers
        for i in range(0, len(make_list)):
            for j in range(0, len(make_list) - i - 1):
                 if make_list[j][1] > make_list[j + 1][1]:
                     temp = make_list[j]
                     make_list[j] = make_list[j + 1]
                     make_list[j + 1] = temp
        #choose the top n books
        if len(make_list) < n:
            return 'There are only ' + str(len(make_list)) + \
                   ' books;' \
                   ' not ' +str(n)+'.'
        else:
            index = 1
            while index <= n:
                while index+1 <= len(make_list)and make_list[-index-1][1] == make_list [-index][1]:
                    print ("ranking at #"+ str(index)+":")
                    while index <=n and index+1 <= len(make_list) and make_list [-index-1][1] == make_list [-index][1]:
                        print('     '+make_list[-index][0])
                        index += 1
                        n += 1
                    if index+1 <= len(make_list) and make_list[-index - 1][1] != make_list[-index][1]:
                        print('     '+ make_list[-index][0])
                        index += 1
                        n -= 1
                if index <= len(make_list):
                    print ('Ranking at #'+str(index)+ ': ' +str(make_list[-index][0]))
                    index += 1
                else:
                    break

    def n_most_expensive_books(self,n):
        #make a list of lists [book title, book cost]
        make_list = []
        for book in self.books.keys():
            make_list.append([book.title, book.cost])
        #sort the list based on cost
        for i in range(0,len(make_list)):
            for j in range (0, len(make_list)-i-1):
                if make_list[j][1]>make_list[j+1][1]:
                    temp=make_list[j]
                    make_list[j]=make_list[j+1]
                    make_list[j+1]=temp
        #choose the top n books
        if len(make_list) < n:
            return 'There are only ' + str(len(make_list)) + \
                   ' books;' \
                   ' not ' +str(n)+'.'
        else:
            index = 1
            while index <= n:
                if index+1 <= len(make_list) and make_list[-index - 1][1] == make_list[-index][1]:
                    print("ranking at #" + str(index) + ":")
                    while index <= n and index+1 <= len(make_list) and make_list[-index - 1][1] == make_list[-index][1]:
                        print('     ' + make_list[-index][0])
                        index += 1
                        n += 1
                        if make_list[-index - 1][1] != make_list[-index][1]:
                            print('     {book}'.format(book=make_list[-index][0]))
                            n -= 1
                            index += 1


                else:
                    print('Ranking at #' + str(index) + ' most expensive book: ' + str(make_list[-index][0]))
                    index += 1
    def get_worth_of_user(self, email):
        user= self.users[email]
        make_list=[]
        total_worth=0
        if email in self.users.keys():
            for book in user.books:
                make_list.append([book.title, book.cost])
            for i in range(0,len(make_list)):
                total_worth += make_list[i][1]
            return '{name} has read ${cost} worth of books'.format(name=user.name, cost=total_worth)
        else:
            return "{name} does not exist".format(name=user_email)
