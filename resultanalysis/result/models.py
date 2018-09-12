from django.db import models

class student_info(models.Model):
    Name = models.CharField(max_length=250)
    Branch = models.CharField(max_length=500)
    Rollno = models.IntegerField()

    def __str__(self):
        return self.Name + ' - ' + self.Branch

class resultinfo(models.Model):
    studentkey = models.ForeignKey(student_info, on_delete=models.CASCADE)
    sub_1 = models.IntegerField()
    sub_2 = models.IntegerField()
    sub_3 = models.IntegerField()
    sub_4 = models.IntegerField()
    sub_5 = models.IntegerField()

    def __str__(self):
        return self.sub_1, self.sub_2, self.sub_3, self.sub_4, self.sub_5
