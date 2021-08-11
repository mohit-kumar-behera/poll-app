from django.db import models

class Question(models.Model):
	question_text = models.TextField()
	pollBy = models.CharField(max_length=20,default="anonymous")
	pub_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return "Poll@" + str(self.id) + str(self.question_text)

	class Meta:
		verbose_name_plural = "question"


class Choices(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	
	def __str__(self):
		return str(self.choice)

	def totalVotes(self,thisQuestion):
		tv = 0
		all_choices = thisQuestion.choices_set.all()
		for choice in all_choices:
			tv += choice.votes
		return tv

	def votePercentage(self):
		thisQuestion = Question.objects.get(id=self.question.id)
		vp = 0
		tv = self.totalVotes(thisQuestion)
		if tv == 0:
			return 0
		vp = round((self.votes/tv)*100,2)
		return vp

 
	class Meta:
		verbose_name_plural = "Choices"

class Voter(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	votedBy = models.CharField(max_length=20)

	def __str__(self):
		return self.votedBy + " voted " + str(self.question.question_text)

	class Meta:
		verbose_name_plural = "Voter"
