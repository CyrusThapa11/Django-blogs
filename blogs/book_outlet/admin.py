from django.contrib import admin

# Register your models here.
from .models import Book

# admin.site.register(Book)
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",) # here we are saying that it should not be editable hence it will throw error !
    # because of this we dont need save() method to be overridden
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating",)
    list_display = ("title", "author",)


admin.site.register(Book, BookAdmin)
