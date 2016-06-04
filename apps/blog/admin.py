from django.contrib import admin
from .models import Post, Email
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'date')
	search_fields = ('title',)

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
	list_display = ('name', 'email')
	search_fields = ('name', 'email')