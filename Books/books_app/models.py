from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Book(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
















