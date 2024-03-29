from django.db import models
from django.contrib.auth.models import User
from userprofile.models import Interest


class ArticleStatus(models.Model):
    label = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.label

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='articles')
    status = models.ForeignKey(ArticleStatus,on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)   
    published_date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=100)
    thumbnail = models.URLField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Interest,on_delete=models.PROTECT)
    summary = models.CharField(max_length=250,blank=True,null=True)
    current_reviewer = models.ForeignKey(User,on_delete=models.PROTECT,related_name='articles_reviewing')

    def __str__(self):
        return self.title


class ArticleComment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")
    content = models.CharField(max_length = 500)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    def __str__(self):
        return self.content


class ReviewRequestStatus(models.Model):
    label = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.label

class ReviewRequest(models.Model):
    reviewer =  models.ForeignKey(User,on_delete=models.CASCADE,related_name='review_request')
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    status = models.ForeignKey(ReviewRequestStatus,on_delete=models.PROTECT)
    declined_reason = models.CharField(max_length=500,blank=True,null=True)
    def __str__(self):
        return f"{self.article.title} : status {self.status}"


class Suggestion(models.Model):
    review_request= models.OneToOneField(ReviewRequest,on_delete=models.CASCADE,unique=True)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.title

    