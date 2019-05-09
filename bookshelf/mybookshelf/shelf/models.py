from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PublishingCompany(models.Model):
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    publishing_company = models.ForeignKey(PublishingCompany, on_delete=models.CASCADE, null=True)
    publication_date = models.DateField(null=True)
    cover_book = models.ImageField()
    pages = models.IntegerField(null=True)
    genre = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title




