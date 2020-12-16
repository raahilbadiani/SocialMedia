This is social media website created in django
currently work under progress



1. terminal :
	django-admin startproject FRIENDS .
	python manage.py startapp posts
	python manage.py start uzrs
	mkdir static
	mkdir templates
	mkdir static/css
	python manage.py makemigrations uzrs
	python manage.py migrate
	python manage.py createsuperuzr
	python maange.py runserver


file changes:

2. settings.py 
	added 
	-static_dir
	-template_dir
	-login_url
	-login_redirect
	-email_backend
	-site_id=1
	-auth_user_model 
	-- installed apps :
		-django.contrib.sites
		-posts
		-uzrs
		-allauth
		-allauth.account
		-allauth.socialaccount
	-templates[0]['dirs] updated

3. uzrs/models.py 
	-added user class which inherits from predefined abstract user class

4. posts/views.py
	-added view on login simple http response

