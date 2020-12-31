from django.db import models
from uzrs.models import Uzr
# Create your models here.
class Post(models.Model):
	user = models.ForeignKey(Uzr,on_delete=models.CASCADE)
	captions = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	img = models.ImageField(upload_to="posts",blank=False)
	def __str__(self):
		return str(self.user.username+' '+str(self.date.date()))

	def get_user():
		return user

class Profile(models.Model):
	user = models.ForeignKey(Uzr,on_delete=models.CASCADE)
	userdp = models.ImageField(upload_to="profile")
	bio = models.CharField(max_length=500,blank=True)
	connetWithMe = models.URLField(max_length=100,blank=True)
	friends = models.IntegerField(default=0)
	def __str__(self):
		return str(self.user)


class Like(models.Model):
	user = models.ManyToManyField(Uzr)
	post = models.OneToOneField(Post,on_delete=models.CASCADE)
	
	@classmethod
	def likeMethod(cls,post,user) :
		obj,create = cls.objects.get_or_create(post=post)
		obj.user.add(user)
		
	@classmethod
	def dislikeMethod(cls,post,user):
		obj,create = cls.objects.get_or_create(post=post)
		obj.user.remove(user)
	
	def __str__(self):
		return str(self.post)