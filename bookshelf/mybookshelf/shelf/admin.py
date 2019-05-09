from django.contrib import admin
from .models import Book, PublishingCompany, Author
# Register your models here.


admin.site.register(Book)
admin.site.register(PublishingCompany)
admin.site.register(Author)


