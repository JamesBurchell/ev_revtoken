from django.db import models

class Car(models.Model):
    license_plate = models.CharField(max_length=7)
    vin = models.CharField(max_length=17)
    year = models.CharField(max_length=4)
    def __str__(self):
        return self.license_plate
    
class Make(models.Model):
    make = models.CharField(max_length=200)
    def __str__(self):
        return self.make

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text