from django.db import models

# Create your models here.

class Post(models.Model):
    #タイトル
    title = models.CharField(max_length=255)
    #投稿番号
    slug = models.SlugField()
    intro =models.TextField()
    body = models.TextField()
    #投稿日時
    posted_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    #外部キー
    post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)