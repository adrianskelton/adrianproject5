from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='post/', default='')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    text = models.TextField(default='')
    pub_date = models.DateTimeField('date commented', default=None)  

    def __str__(self):
        return f"{self.author} on {self.post.title}"
