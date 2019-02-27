from django.db import models

class hindu(models.Model):
    Title = models.CharField(max_length=250)
    Place_of_study = models.TextField()
    Prin_invest = models.CharField(max_length=250)
    Name = models.CharField(max_length=250)
    Desig = models.CharField(max_length=250)
    NAme_of_research_fellow = models.CharField(max_length=250)
    Invitation_paragraph = models.TextField()
    Intro = models.TextField()
    Why_am_i = models.TextField()
    Duration = models.TextField()
    How_many = models.TextField()
    IS_my_part = models.TextField()
    Can_i_withdraw = models.TextField()
    What_will_be_done = models.TextField()
    What_are_my_responsibility = models.TextField()
    What_are_risk = models.TextField()
    Confidentiality = models.TextField()
    Whom_contact = models.TextField()


class comment(models.Model):
    post = models.ForeignKey(hindu, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

