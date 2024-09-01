from django.db import models

# Create your models here.


class Questions(models.Model):
    question_choices = (("Text", "Text"), ("BigText", "BigText"), ("Radio", "Radio"), ("Checkbox", "Checkbox"))
    questions = models.CharField(max_length=100)
    question_type = models.CharField(choices= question_choices, max_length=50, default="text")

    def __str__(self) -> str:
        return f"{self.questions} {self.question_type}"

class Options(models.Model):
    question = models.ForeignKey(Questions, related_name= "options", on_delete=models.CASCADE)
    option_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.option_name} {self.question.questions}"

class CustomerFeedback(models.Model):
    question = models.ManyToManyField(Questions)

class CustomerResponse(models.Model):
    feedback = models.ForeignKey(CustomerFeedback, on_delete = models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    response_text = models.TextField(null=True, blank=True)
    selected_options = models.ManyToManyField(Options, blank=True)
