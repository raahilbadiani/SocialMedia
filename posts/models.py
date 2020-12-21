from django.db import models
from uzrs.models import Uzr
# Create your models here.
class Post(models.Model):
	user = models.ForeignKey(Uzr,on_delete=models.CASCADE)
	captions = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	img = models.ImageField(upload_to="posts")
	def __str__(self):
		return str(self.user.username+' '+str(self.date.date()))

	def get_user():
		return user