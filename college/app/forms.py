from django import forms
from .models import QuestionPapers

class QuestionPaperSubmit(forms.ModelForm):
    class Meta:
        model = QuestionPapers
        fields = '__all__'

