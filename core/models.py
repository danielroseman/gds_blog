from django.db import models

class Article(models.Model):
  title = models.CharField(max_length=100)
  body = models.TextField()
  author = models.ForeignKey('auth.User')
  created_at = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return self.title
