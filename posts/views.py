from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Post,Profile,Uzr,Like
from django.contrib import messages
import os
from django.conf import settings
from django.urls import path
# Create your views here.
BASR_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASR_DIR)

@login_required()
def homePage(request):
	print("homePage")
	posts = Post.objects.all().order_by('-pk')
	# profiles = Profile.objects.all()
	# profile_pics = {}
	# for i in profiles:
	# 	profile_pics[i.user] = i.userdp.url
	liked_posts = [i for i in posts if Like.objects.filter(post=i,user=request.user)]
	
	data = {
		'posts':posts,
		'liked_posts':liked_posts,	
		# 'profile_pictures':profile_pics,
	}
	return render(request,"posts/homepage.html",data)


@login_required()
def homePageOne(request):
	print("homePageOne")
	return redirect('posts/homepage')
	# data = {'posts':posts,'base_dir':BASR_DIR}
	# return render(request,"posts/homepage.html",data)


@login_required()
def post(request):
	print('post')	
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
	print('deletepost')
	post_ = Post.objects.filter(pk=postId)
	image_path = post_[0].img.url
	post_.delete()
	# os.remove(os.path.join(settings.BASE_DIR,image_path))
	return redirect("/")

@login_required()
def userProfile(request,username):
	print('userprofile')
	user_ = Uzr.objects.filter(username=username)
	print(user_)
	# print(user_.username)
	if user_ :
		print("yes!!")
		profile_ = Profile.objects.get(user=user_[0])
		print(profile_)
		bio = profile_.bio
		connecnt_with_me_ = profile_.connetWithMe
		friends = profile_.friends
		profile_pic = profile_.userdp
		post_obj_ = Post.objects.filter(user=user_[0])
		img_list_ = [post_obj_[i:i+3] for i in range(0,len(post_obj_),3)]
		# img_list_2 = [post_obj_[i:i+2] for i in range(0,len(post_obj_),3)]
		data = {'user_obj':user_[0],'profile_pic':profile_pic,'bio':bio,'friends':friends,'connecnt_with_me_':connecnt_with_me_,'img_list':img_list_}
		return render(request,'posts/userpage.html',data)
	else :
		return redirect("/")


def likePost(request,postId):
	print('likepost')
	print(postId)
	post = Post.objects.get(pk=postId)
	user = request.user
	like = Like.objects.filter(post=post,user=user)
	like_boolean = False
	if like : 
		print('disliking')
		Like.dislikeMethod(post,user)
	else :
		like_boolean = True
		print('liking')
		Like.likeMethod(post,user)
	
	return JsonResponse({'status':like_boolean})

def commentPost(request,postId):
	print('commenting..')
	return HttpResponse('commenttt')