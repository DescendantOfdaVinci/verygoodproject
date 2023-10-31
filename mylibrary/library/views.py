from django.shortcuts import render
from library.models import *


def show_start_page(request):
    return render(request, "index.html")


def show_showbooks_page(request):
    if request.method == "GET":
        context = {"books": Book.objects.all()}
        return render(request, "showBooks.html", context=context)

def show_showreaders_page(request):
    if request.method == "GET":
        context = {"readers": Reader.objects.all()}
        return render(request, 'showReaders.html', context=context)


def show_addbook_page(request):
    if request.method == "POST":
        book_title = request.POST.get("book_title")
        book_author_name = request.POST.get("book_author_name")
        author_surname = request.POST.get("author_surname")
        genre = request.POST.get("genre")
        publication_year = request.POST.get("publication_year")
        page_count = request.POST.get("page_count")
        description = request.POST.get("description")

        Book.objects.create(book_title=book_title,
                            book_author_name=book_author_name,
                            author_surname=author_surname,
                            genre=genre,
                            publication_year=publication_year,
                            page_count=page_count,
                            description=description)

    return render(request, "addBook.html")


def show_addreader_page(request):
    if request.method == "POST":
        reader_name = request.POST.get("reader_name")
        reader_surname = request.POST.get("reader_surname")
        reader_age = request.POST.get("reader_age")
        reader_address = request.POST.get("reader_address")

        Reader.objects.create(name=reader_name,
                              surname=reader_surname,
                              age=reader_age,
                              address=reader_address)

    return render(request, "addReader.html")


def show_addrent_page(request):
    if request.method == "POST":
        title = request.POST.get("book_title")
        reader_surname = request.POST.get("reader_surname")
        rent_date = request.POST.get("rent_date")
        return_data = request.POST.get("return_data")

        BookRent.objects.create(book_title=title,
                                reader_surname=reader_surname,
                                rent_date=rent_date,
                                return_data=return_data)

    return render(request, "addRent.html")

