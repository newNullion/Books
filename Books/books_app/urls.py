from django.urls import path
from .views import MainView, CategoryView, BooksView, BookView



urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('category/<int:pk>/', CategoryView.as_view(), name='category'),
    path('author/<int:category_pk>/<int:author_pk>', BooksView.as_view(), name='author_books'),
    path('book/<int:pk>/', BookView.as_view(), name='book'),
]