from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.utils import timezone
from django.urls import reverse
from createPoll.models import Question,Choices,Voter
import datetime

def userProfile(request):
	try:
		sessUsername = request.session['sessUsername']
	except:
		return HttpResponseRedirect(reverse("user:user"))
	else:
		context = {'username':sessUsername}
		try:
			userPoll = Question.objects.filter(pollBy=sessUsername).order_by("-pub_date")
		except:
			pass
		else:
			context['userPoll'] = userPoll
			return render(request,"userProfile/user-profile.html",context)

def viewProfile(request,user):
	try:
		sessUsername = request.session['sessUsername']
	except:
		return HttpResponseRedirect(reverse("user:user"))
	else:
		if user != sessUsername:
			context = {}
			try:
				questions = Question.objects.filter(pollBy=user).order_by("-pub_date")
			except Question.DoesNotExist:
				pass
			else:
				context['questions'] = questions
				context['viewUser'] = user
				context['selfUser'] = sessUsername
				votedQuestions = Voter.objects.filter(votedBy=sessUsername)
				votedQuestionID = []
				for votedQuestion in votedQuestions:
					votedQuestionID.append(votedQuestion.question.id)
				context['votedQuestionID'] = votedQuestionID
				if "resultBtn" in request.GET:
					request.session['sessQID'] = request.GET.get('resultBtn');
					return HttpResponseRedirect(reverse("home:result"))
				return render(request,"userProfile/view-profile.html",context)
		return HttpResponseRedirect(reverse("userProfile:userProfile"))


def logout(request):
	if request.POST:
		del request.session['sessUsername']
	return HttpResponseRedirect(reverse("user:user"))