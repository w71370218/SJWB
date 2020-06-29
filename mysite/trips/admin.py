from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_filter = ('created_date',)

admin.site.register(Post, PostAdmin)

admin.site.site_url = 'http://127.0.0.1:8000/home'