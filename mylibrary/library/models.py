from django.db import models

class Book(models.Model):
    book_title = models.CharField(max_length=50)
    book_author_name = models.CharField(max_length=50)
    author_surname = models.CharField(max_length=50,
                                      default=None)
    genre = models.TextField()
    publication_year = models.DateField()
    page_count = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.book_title} - {self.book_author_name} - {self.author_surname} - {self.publication_year} - {self.genre}"


class Reader(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name} - {self.surname} - {self.age}"


class BookRent(models.Model):
    book_title = models.CharField(max_length=50)
    return_date = models.DateField()
    rent_date = models.DateField()
    reader_surname = models.CharField(max_length=30,
                                      null=True)

    def __str__(self):
        return f"{self.book_title} was rent to {self.reader_surname}:{self.rent_date}  - {self.return_date}"


