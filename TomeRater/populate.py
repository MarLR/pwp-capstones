from TomeRater import *

Tome_Rater = TomeRater

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678, 12)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", 12345, 13, "Lewis Carroll")
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", 1929452, 36, "Python", "beginner")
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", 11111938, 36, "AI", "advanced")
novel2 = Tome_Rater.create_novel("The Diamond Age", 10101010, 19, "Neal Stephenson")
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", 10001000, 17, "Ray Bradbury")


#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)
#book2 = Tome_Rater.create_book("The Society of Mind", 12345678, 12)


#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.get_most_read_book())
print("List of most expensive books")
print (Tome_Rater.n_most_expensive_books(6))
print ("list of most prolific readers")
print (Tome_Rater.n_most_prolific_reader(3))
print ("Worth of user:")
print (Tome_Rater.get_worth_of_user("alan@turing.com"))
print ('List of most read books:')
print (Tome_Rater.n_most_read_books(6))