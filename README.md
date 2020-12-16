This is social media website created in django
currently work under progress



1. terminal :
-	1.1 django-admin startproject FRIENDS . 
-	1.2 python manage.py startapp posts	
-	1.3 python manage.py start uzrs
-	1.4 mkdir static
-	1.5 mkdir templates
-	1.6 mkdir static/css
-	1.7 python manage.py makemigrations uzrs
-	1.8 python manage.py migrate
-	1.9 python manage.py createsuperuzr
-	1.10 python maange.py runserver


file changes:

2. settings.py 
	added 
	- static_dir
	- template_dir
	- login_url
	- login_redirect
	- email_backend
	- site_id=1
	- auth_user_model 
	- - installed apps :
		- django.contrib.sites
		- posts
		- uzrs
		- allauth
		- allauth.account
		- allauth.socialaccount
	-templates[0]['dirs'] updated

3. uzrs/models.py 
	- added user class which inherits from predefined abstract user class

4. posts/views.py
	- added view on login simple http response

