from django.db import models

class Meeting(models.Model) :
    name = models.CharField(max_length=6)
    personnel = models.IntegerField()
    title = models.TextField()
    meetingdate = models.DateTimeField(null=True)

    def __str__(self):
        return self.name + ":" + str(self.personnel) + ":" +self.title + ":" + str(self.meetingdate)
