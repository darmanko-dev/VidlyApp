from django.contrib import admin
from .models import Genres, Movie

# Register your models here.

class GenresAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
    
class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('title', 'release_year', 'number_in_stock', 'daily_rate')



admin.site.register(Genres, GenresAdmin)
admin.site.register(Movie, MovieAdmin)