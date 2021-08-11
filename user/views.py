from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.utils import timezone
from django.urls import reverse
from . models import quickPollUser
import datetime

def user(request):
	try:
		sessUsername = request.session['sessUsername']
	except:
		context = {}
		if "create-account" in request.POST:
			print("Create Account")
			f_username = request.POST.get("username")
			try:
				userExist = quickPollUser.objects.filter(username = f_username)
			except:
				pass
			else:
				if not userExist.exists():
					userCreate = quickPollUser.objects.create(username = f_username)
					context['message'] = "Account is created successfully."
					context['redirect_home'] = True
					request.session['sessUsername'] = f_username
					return render(request,'user/user.html',context)
				context['message'] = "Account already Exists."
				return render(request,'user/user.html',context)
		if "login-account" in request.POST:
			print("Login Account")
			f_username = request.POST.get('username')
			try:
				userExist = quickPollUser.objects.get(username = f_username)
			except quickPollUser.DoesNotExist:
				context['message'] = "Sorry, this username is not in our database. Create a new username."
				return render(request,'user/user.html',context)
			else:
				request.session['sessUsername'] = f_username
				return HttpResponseRedirect(reverse("home:home")) 
		return render(request,'user/user.html')
	else:
		return HttpResponseRedirect(reverse("home:home"))

def usernameExist(request):
	if request.GET:
		data = {'successfull':True}
		_username = request.GET.get("_username")
		try:
			username_qs = quickPollUser.objects.filter(username=_username)
		except:
			pass
		else:
			if username_qs.exists():
				print("Username exists")
				data['can_be_taken'] = False
				return JsonResponse(data)
			print("username not exists")
			data['can_be_taken'] = True
			return JsonResponse(data) 
	else:
		data = {'successfull':False}
		return JsonResponse(data)
