class User:
    bookList = []

    def __init__(self, 
                 userid, 
                 email,
                 firstName, 
                 lastName, 
                 universityID, 
                 courseID, 
                 currentYear):
        self.id = userid
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.universityID = universityID
        self.courseID  = courseID
        self.currentYear = currentYear
        self.reputation = 0

    def increaseReputation(self):
        self.reputation += 1

    def decreaseReputation(self):
        self.reputation -= 1

    def addBook(self, book):
        self.bookList.append(book)

    def removeBook(self, book):
        self.bookList.remove(book)

    def listBooks(self):
        return '\n'.join(map(str, self.bookList))

    def __str__(self):
        return self.firstName+' '+self.lastName+' <'+self.email+'>'
