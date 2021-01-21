from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    OPTIONS = (
        ('d','draft'),
        ('p','published')
    )
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    image = models.URLField(max_length=400,default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.webmasterpro.de%2Fcoding%2Farticle%2Fframework-django-konventionen.html&psig=AOvVaw1M9yqS3Ssaxns61eMMQpUh&ust=1611224927907000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJjyzOWmqu4CFQAAAAAdAAAAABAD')
    status = models.CharField(max_length=10,choices=OPTIONS,default='d')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def _str_(self):
        return self.title
    
    def comment_count(self):
        return self.comment_set.all().count()
    
    def view_count(self):
        return self.view_set.all().count()
    
    def like_count(self):
        return self.like_set.all().count()
    
    def comments(self):
        return self.comment_set.all()
    

    
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.TextField()
    time =models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.user.username
class Like(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     post = models.ForeignKey(Post,on_delete=models.CASCADE)
     
     def _str_(self):
        return self.user.username
    
class View(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.user.username