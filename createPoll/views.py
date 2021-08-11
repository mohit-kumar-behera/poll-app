from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.utils import timezone
from django.urls import reverse
from .models import Question,Choices
import datetime


def createPoll(request):
	try:
		sessUsername = request.session['sessUsername']
	except:
		#print("Session has Expired")
		return HttpResponseRedirect(reverse("user:user"))
	else:
		if "submitPoll" in request.POST:
			question = (request.POST.get('question')).strip();
			question_db = Question.objects.create(question_text = question, pollBy = sessUsername);
			question_db_id = question_db.id 
			question_db_query = Question.objects.get(id = question_db_id) 

			post_elems = request.POST
			for post_elem,value in post_elems.items():
				if post_elem.startswith("choice") and value != '':
					question_db_query.choices_set.create(choice = value.strip())

			return HttpResponseRedirect(reverse("home:home"))
		return render(request,'createPoll/createPoll.html',{})