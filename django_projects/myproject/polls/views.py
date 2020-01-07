import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
	current_date_time = datetime.datetime.now()
	context = {'now_date': current_date_time}
	return render(request, 'abc.html',context)


from .forms import NameForm

def get_name(request):
    
    if request.method == 'POST':
        
        form = NameForm(request.POST)
 
        if form.is_valid():

            return HttpResponse('Form submitted successfully<br>Name:'+form.cleaned_data['your_name'])
    else:
        form = NameForm()
    return render(request, 'name.html', {'form': form})