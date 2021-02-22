from django.shortcuts import render
from .forms import QuestionPaperSubmit
from .models import QuestionPapers
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    template_name = "home.html"
    context = {}
    return render(request, template_name, context)

def newpaper(request):
    form = QuestionPaperSubmit()
    if request.method == "POST":
        form = QuestionPaperSubmit(request.POST or None, request.FILES or None)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    form = QuestionPaperSubmit()
    template_name = "newpaper.html"
    context = {"form":form}
    return render(request, template_name, context)

def allpapers(request):
    questions = QuestionPapers.objects.all()
    template_name = "list.html"
    context = {"papers":questions}
    return render(request, template_name, context)

def contact(request):
    template_name = "contact.html"
    context = {}
    return render(request, template_name, context)

@csrf_exempt
def search(request):
    template_name = "list.html"
    context = {}
    if request.method == "POST":
        code = request.POST["search"]
        questions = QuestionPapers.objects.filter(code_of_subject__icontains=code)
        context = {"papers":questions,"found":len(questions)}
        return render(request, template_name, context)
    return render(request, template_name, context)