from django.db import models
from django.contrib.auth.models import User
from users.models import Interest


class ArticleStatus(models.Model):
    label = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.label

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='articles')
    status = models.ForeignKey(ArticleStatus,on_delete=models.SET_NULL,blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)   
    published_date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=100)
    thumbnail_url = models.URLField(max_length=200)
    content = models.TextField(max_length=20000,blank=True,null=True)
    category = models.ForeignKey(Interest,on_delete=models.SET_NULL,blank=True,null=True)
    summary = models.TextField(max_length=500,blank=True,null=True)
    current_reviewer = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True,related_name='articles_reviewing')

    def __str__(self):
        return self.title


class ArticleComment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(max_length = 500, blank = True,null=True)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    def __str__(self):
        return self.content


class ReviewRequestStatus(models.Model):
    label = models.CharField(max_length=100)
    def __str__(self):
        return self.label

class ReviewRequest(models.Model):
    reviewer =  models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    status = models.ForeignKey(ReviewRequestStatus,on_delete=models.SET_NULL,blank=True,null=True)
    declined_reason = models.TextField(max_length=500,blank=True,null=True)
    def __str__(self):
        return f"{self.article.title} : status {self.status}"


class Suggestion(models.Model):
    review_request= models.ForeignKey(ReviewRequest,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000,blank=True,null=True)
    def __str__(self):
        return self.title

    