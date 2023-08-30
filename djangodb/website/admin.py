from django.contrib import admin
from .models import *

# costimaze admin page to show data on each itme
class publisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'email')

# costimaze admin page to show publisher data sort by it 
# note : publisher must be  foringkey in  that model (FK in movies_info or any one you add to   ) 
class MovieAdmin(admin.ModelAdmin):
    list_filter = ('publisher',)


# Register your models here.
admin.site.register(Members)
admin.site.register(Publisher , publisherAdmin)
admin.site.register(movies_info , MovieAdmin)
admin.site.register(MovieMembers)
admin.site.register(Review)
