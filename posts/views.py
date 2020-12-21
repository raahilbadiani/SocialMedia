from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post
from django.contrib import messages
import os
from django.conf import settings
from django.urls import path
# Create your views here.

@login_required()
def homePage(request):
	posts = Post.objects.all().order_by('-pk')
	data = {'posts':posts}
	return render(request,"posts/homepage.html",data)

@login_required()
def post(request):
	print('hiii')
	messages.success(request,"successfully posted")
	if request.method == "POST" :
		post_image_ = request.FILES['post_image']
		post_text_ = request.POST.get('post_text')
		post_user_ = request.user
		post_object = Post(user=post_user_,captions=post_text_,img=post_image_)
		post_object.save()
		return redirect("/")
	else :
		print('else')
		return redirect("/")

@login_required()
def deletePost(request,postId):
	post_ = Post.objects.filter(pk=postId)
	image_path = post_[0].img.url
	post_.delete()
	# os.remove(os.path.join(settings.BASE_DIR,image_path))
	return redirect("/")

# @login_required()
# def userProfile(request,username):
# 	return render()