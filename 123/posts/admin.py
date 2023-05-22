from django.contrib import admin
from posts.models import Post, Comment


# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "category", "status"]
    list_filter = ["status", "category"]
    list_editable = ["status", "category"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "username", "created"]
