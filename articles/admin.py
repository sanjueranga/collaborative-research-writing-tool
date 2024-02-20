from django.contrib import admin
from .models import Article, ArticleComment, ReviewRequest, Suggestion, ArticleStatus, ReviewRequestStatus

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title", "created_date", "published_date")


class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "article", "content")


class ReviewRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "reviewer", "article", "status")


class SuggestionAdmin(admin.ModelAdmin):
    list_display = ("id", "review_request", "title")

admin.site.register(Suggestion, SuggestionAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ReviewRequest, ReviewRequestAdmin)
admin.site.register(ArticleComment, ArticleCommentAdmin)
admin.site.register(ArticleStatus)
admin.site.register(ReviewRequestStatus)
