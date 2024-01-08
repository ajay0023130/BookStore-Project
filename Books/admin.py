from django.contrib import admin

# Register your models here.
from .models import Book,Review
from django.contrib.admin import AdminSite

@admin.register(Book)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'pages','publisher',"author") 
    list_filter = ('title', 'pages','publisher',"author")
    search_fields = ('title', 'publisher',"author")  # for ssarching
    date_hierarchy = 'published'  # Enable date-based hierarchical navigation

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('date', 'book', 'review') 
    list_filter = ('date', 'book',)
    search_fields = ('review', 'book__title')  # for ssarching
    date_hierarchy = 'date'  # Enable date-based hierarchical navigation




# class CustomAdminSite(AdminSite):
#     # Set the name and title for the admin site
#     site_title = 'Book Store Admin Site'
#     site_header = 'Book Store Admin Site'

# # Register your custom admin site
# custom_admin_site = CustomAdminSite(name='HavenBookhjgjhgjhg')

# # Use your custom admin site instead of the default
# admin.site = custom_admin_site'''abs

admin.site.site_header = 'Haven Book Store Admin Panel'
#Add the below line
admin.site.index_title = 'Book Store Admin Panel'