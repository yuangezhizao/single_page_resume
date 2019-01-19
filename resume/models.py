from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='姓名')
    content = models.CharField(max_length=1024, verbose_name='详情')

    def __str__(self):
        return self.name


class Message(models.Model):
    username=models.CharField(max_length=50)
    content=models.TextField(max_length=256)
    time=models.DateTimeField()

    def __str__(self):
        tpl = '<Message:[username={username}, content={content}, time={time}]>'
        return tpl.format(username=self.username, content=self.content, time=self.time)
