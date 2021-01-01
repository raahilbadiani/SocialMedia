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
	userdp = models.ImageField(upload_to="profile",default="profile/dp_def_male.jpg")
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
	
class Comment(models.Model):
	post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
	name_of_commenter = models.CharField(max_length=255)
	comment_text = models.TextField()
	time_of_comment = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s -> %s \t %s' %  (self.post.get_user(),comment_text,name_of_commenter)