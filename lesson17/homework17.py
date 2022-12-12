# ######Task1
# class Animal:
#     def talk(self):
#         pass
#
# class Dog(Animal):
#     def talk(self):
#         print('woof woof')
#
# class Cat(Animal):
#     def talk(self):
#         print('meow')
#
# def make_animal_talk(animal):
#     animal.talk()
#
# dog = Dog()
# cat = Cat()
# make_animal_talk(dog)
# make_animal_talk(cat)
##Task2
# class Library:
#     def init(self, name):
#         self.name = name
#         self.books = []
#         self.authors = []
#
#     def add_book(self, book):
#         self.books.append(book)
#
#     def add_author(self, author):
#         self.authors.append(author)
#
# class Book:
#     def init(self, name, year, author):
#         self.name = name
#         self.year = year
#         self.author = author
#
# class Author:
#     def init(self, name, country, birthday):
#         self.name = name
#         self.country = country
#         self.birthday = birthday
#         self.books = []
#
#     def add_book(self, book):
#         self.books.append(book)
#
#     def new_book(self, name, year, author):
#         book = Book(name, year, author)
#         self.add_book(book)
#         return book
#
#     def group_by_author(self, author):
#         return [book for book in self.books if book.author == author]
#
#     def group_by_year(self, year):
#         return [book for book in self.books if book.year == year]
#
#     def str(self):
#         return f"Library: {self.name}, Books: {len(self.books)}, Authors: {len(self.authors)}"
#
#     def repr(self):
#         return self.str()
#
# class Book:
#     count = 0
#
#     def init(self, name, year, author):
#         self.name = name
#         self.year = year
#         self.author = author
#         Book.count += 1
#
#     def str(self):
#         return f"Book: {self.name}, Year: {self.year}, Author: {self.author.name}"
#
#     def repr(self):
#         return self.str()
#Task3
class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError('Denominator cannot be 0')
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return '{0}/{1}'.format(self.numerator, self.denominator)

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError('Cannot add a Fraction to a non-Fraction')

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError('Cannot subtract a Fraction from a non-Fraction')

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError('Cannot multiply a Fraction with a non-Fraction')

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError('Cannot divide a Fraction by a non-Fraction')

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator == other.numerator * self.denominator
        else:
            raise TypeError('Cannot compare a Fraction to a non-Fraction')

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator < other.numerator * self.denominator
        else:
            raise TypeError('Cannot compare a Fraction to a non-Fraction')

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator > other.numerator * self.denominator
        else:
            raise TypeError('Cannot compare a Fraction to a non-Fraction')
    def __ge__(self, other):
        # Compare two fractions
        return self.numerator * other.denominator >= other.numerator * self.denominator

