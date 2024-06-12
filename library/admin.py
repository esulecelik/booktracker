from django.contrib import admin

# Register your models here.
from .models import Category,Book,Writer,Quote


class BookAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register( Category )
admin.site.register( Book, BookAdmin )
admin.site.register( Writer )
admin.site.register( Quote)