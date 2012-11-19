#!/usr/bin/python

class book:
	
	def __init__(self, isbn, title, author, year, edition, publisher, rrp):
		self.isbn = isbn
		self.title = title
		self.author = author
		self.year = year
		self.edition = edition
		self.publisher = publisher
		self.rrp = rrp
		
	def __str__(self):
        return self.title+', '+self.author+', '+self.year+', '+self.edition+', '+self.publisher+', '+self.isbn+', '+self.rrp
