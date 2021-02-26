from django.db import models

# Create your models here.
class QuestionPapers(models.Model):
    year = models.CharField(max_length=200, default="2018")
    name_of_subject = models.CharField(max_length=200)
    code_of_subject = models.CharField(max_length=200)
    semester = models.CharField(max_length=10, default=1)
    type_of_paper = models.CharField(max_length=200)
    question_paper_image = models.ImageField(upload_to='images/',blank=True,null=True)

    def __str__(self):
        return self.code_of_subject
