from django.db.models.signals import post_save
from django.dispatch import receiver
from uzrs.models import Uzr
from posts.models import Profile


@receiver(post_save,sender=Uzr)
def create_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)
		print('profile_created!!')




"""
Signals

Receiver function takes a sender argument along with wildcard keyword arguments(**kwargs). It can be a function or a method
def receiver_function(sneder,request,user,**kwargs)
2 ways :-
-------------------------------

1. Manual Connect Route
using Signal.connect(rec_func,sender,weak,dispatch_uid)
rec_func : callback function that will be connected to signal
sender : specifies a particular sender to receive signals from
weak : Django stores signal handlers as weak references by default
dispatch_uid : unique identifier for a signal receiver in cases where duplicate signals may be sent


2. Decorator
from django.dispatch import receiver
@receiver(signal or list of signal, sender)
---------------------------------
Builtin signals

from django.contrib.auth.signals import xyz
1. **Login & logout signals**
- user_logged_in(sender,request,user)
- user_logged_out(sender,request,user)	
	sender - the class of user that just logged in.
	request - the current HttpRequest instance
	user - The user instance that just logged in
- user_login_failed(sender,credentials,request)

2.Model Signals
django.db.models.signals

1. pre_init(sender,args,kwargs) : sent on instantiation of model or we can say before __init__ method of model
2. post_init(sender,instance)
3. pre_save(sender,instance,raw,using,updating_fields)
4. post_save(sender,instance,created,raw,using,update_fiels) created tells if record is created or modified
5. pre_delete(sender,instance,using)
6. post_delete(sender,instance,using)
7. m2m_changed(sender)
8. class_prepared(sender) : snet when a model class has been prepard






"""