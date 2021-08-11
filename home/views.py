from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.utils import timezone
from django.urls import reverse
from createPoll.models import Question,Choices,Voter
import datetime


def home(request):
	try:
		sessUsername = request.session['sessUsername']
	except:
		#print("Session has Expired")
		return HttpResponseRedirect(reverse("user:user"))
	else:
		context = {}
		try:
			questions = Question.objects.order_by("-pub_date")
		except Question.DoesNotExist: 
			pass
		else:
			context['questions'] = questions
			context['user'] = sessUsername
			votedQuestions = Voter.objects.filter(votedBy=sessUsername) #questions voted by session user
			votedQuestionID = []
			for votedQuestion in votedQuestions:
				votedQuestionID.append(votedQuestion.question.id)
			context['votedQuestionID'] = votedQuestionID

			if "resultBtn" in request.GET:
				request.session['sessQID'] = request.GET.get('resultBtn');
				return HttpResponseRedirect(reverse("home:result"))

			return render(request,'home/home.html',context)


# def vote(request):
# 	if request.GET:
# 		choice_id = request.GET.get('choice_id') #id of the choice selected
# 		vote_choice = Choices.objects.get(id=choice_id)
# 		vote_choice.votes += 1
# 		vote_choice.save()
# 		choice_question_id = vote_choice.question.id  #id of the question
# 		get_question = Question.objects.get(id=choice_question_id) #get the object query of the question of id = choice_question_id
# 		get_question.voter_set.create(votedBy=request.session['sessUsername']) #who voted the question
# 		data = {'successfull':True}
# 		return JsonResponse(data)
# 	else:
# 		data ={'successfull':False}
# 		return JsonResponse(data)

def vote(request):
	if request.GET:
		choice_id = request.GET.get('choice_id') #id of the choice selected
		vote_choice = Choices.objects.get(id=choice_id)
		choice_question_id = vote_choice.question.id  #id of the question
		get_question = Question.objects.get(id=choice_question_id) #get the object query of the question of id = choice_question_id
		data = {'successfull':True}
		try:
			get_question.voter_set.get(votedBy=request.session['sessUsername'])
		except:
			data['alreadyVoted'] = False
			vote_choice.votes += 1
			vote_choice.save()	
			get_question.voter_set.create(votedBy=request.session['sessUsername']) #who voted the question
		else:
			data['alreadyVoted'] = True
	else:
		data ={'successfull':False}
	return JsonResponse(data)

def result(request):
	try:
		question_id = request.session['sessQID'];
		question = Question.objects.get(id=question_id)
	except Question.DoesNotExist:
		return HttpResponse(reverse("home:home"))
	else:
		context = {'question':question}
		return render(request,"home/result.html",context)


