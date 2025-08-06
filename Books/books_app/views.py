from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Category, Author, Book, Comment



class MainView(View):
    template_name = 'main.html'

    def get(self, request):
        context = {
            'categories': Category.objects.all()
        }
        return render(request=request, template_name=self.template_name, context=context)



class CategoryView(View):
    template_name = 'category.html'

    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)

        all_authors = Author.objects.all()
        authors = []

        for author in all_authors:
            books = Book.objects.filter(author=author, category=category)
            if books:
                authors.append(author)

        context = {
            'authors': authors,
            'category': category
        }

        return render(request=request, template_name=self.template_name, context=context)

class BooksView(View):
    template_name = 'books.html'

    def get(self, request, category_pk, author_pk):
        category = get_object_or_404(Category, pk=category_pk)
        author = get_object_or_404(Author, pk=author_pk)

        context = {
            'books': Book.objects.filter(author=author, category=category)
        }
        return render(request=request, template_name=self.template_name, context=context)


class BookView(View):
    template_name = 'book.html'

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)

        context = {
            'book': book,
            'comments': Comment.objects.filter(book=book),
        }
        return render(request=request, template_name=self.template_name, context=context)

    def post(self, request, pk):
        name = request.POST.get('name')
        text = request.POST.get('text')
        book = get_object_or_404(Book, pk=pk)
        if name and text:
            Comment.objects.create(name=name, book=book, text=text)
        return redirect('book', pk=book.pk)










