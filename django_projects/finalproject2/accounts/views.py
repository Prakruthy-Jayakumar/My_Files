from django.shortcuts import render
from .forms import SignupForm, LoginForm, pgForm, UploadFileForm, contactForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import redirect
from accounts.models import mysub, contact,Images
from django.contrib import messages
from django.http import JsonResponse

def home(request): 
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def forgot(request):
    return render(request, 'forgot.html')

def contact(request):
    return render(request, 'contact.html')
    if request.method == 'POST':


        x = contactForm(request.POST)

        if x.is_valid():

            name_user = x.cleaned_data['name'] 
            email_user = x.cleaned_data['email'] 
            message_user = x.cleaned_data['message']
           

            contact_pg = mysub(name=name_user, email=email_user, message=message_user)
            contact_pg.save() # will save the data from the form to database
                
            return HttpResponseRedirect("/")

    else:
        x = contactForm(request.POST)
        return render(request, 'contact.html', {'form': x}) 

def listpg(request):
    context = {'pg_details': mysub.objects.all()}
    return render(request,"listpg1.html",context)  


def register(request): 
    if request.method == 'POST':
            signup_form = SignupForm(request.POST)
            if signup_form.is_valid():
                username = signup_form.cleaned_data['username'] 
                email = signup_form.cleaned_data['email']   
                password = signup_form.cleaned_data['password'] 
                if  User.objects.filter(username=username).exists():
                    return HttpResponse("Username/Email Already Exists")
                else:   
                
                    user = User.objects.create_user(username, email, password)
                    user.save()
                    return HttpResponseRedirect("login")
    else:
    	signup_form = SignupForm(request.POST)
    return render(request, 'signup.html',{"form":signup_form})


def login1(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('mysubmissions')
    
    else:   
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():

                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']

                user = authenticate(username=username, password=password)
                            
                if user is not None:
                    if user.is_active:
                        login(request, user)    
                        return HttpResponseRedirect('mysubmissions')
                    else:
                        return HttpResponse('Your account is not active')
                        

                else:
                    return HttpResponse('The Account does not exists')
                   
            else:
                login_form = LoginForm()
                return render(request, "login.html",{"form":login_form})
        else:
            login_form = LoginForm()
        return render(request, "login.html",{"form":login_form})

def logout1(request):
    logout(request)
    return HttpResponseRedirect('/')

def mysubmissions(request):
    return render(request, 'mysubmissions.html')




def add_pg(request):
    if request.method == 'POST':


        x = pgForm(request.POST)

        if x.is_valid():

            pg_name_user = x.cleaned_data['name'] 
            pg_place_user =x.cleaned_data['place'] 
            pg_contact=x.cleaned_data['contact']
            userInfo=request.user #this will add userid to mysub table

            pg_object = mysub(name=pg_name_user, place=pg_place_user, contact=pg_contact,user=userInfo)
            pg_object.save() # will save the data from the form to database
                
            return HttpResponseRedirect("mysubmissions")

    else:
        x = pgForm(request.POST)
        return render(request, 'add_pg.html', {'form': x})  


def mypage(request):
    #if user.is_active
    properties = mysub.objects.filter(user=request.user)
    return render(request, 'mypage.html', {'properties': properties})



def edit_pg(request,pg_id):
    if request.method == 'POST': #method is GET so else part is going to work

        x = pgForm(request.POST)
        if x.is_valid():
            pg_details = mysub.objects.get(id=pg_id)
            # this will select datafrom database 
            pg_details.name = x.cleaned_data['name']
            pg_details.place = x.cleaned_data['place']
            pg_details.contact = x.cleaned_data['contact']
            pg_details.save()
            return HttpResponseRedirect("/mysubmissions")


                

    else:

        pg_details = mysub.objects.get(id=pg_id) # this will select datafrom database 
        x = pgForm(initial={"name":pg_details.name,"place":pg_details.place,"contact":pg_details.contact}) # this will set initial values in the form from selected data

    return render(request, 'editedpg.html', {'form': x,'pg_id':pg_id,})  

def deleteDetails(request,pg_id):

    pg_details = mysub.objects.get(id=pg_id)  
    pg_details.delete()
    #return HttpResponse('Deleted successfully')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 

def showpgDetails(request,pg_id):
    pg_details= mysub.objects.get(id=pg_id) 
    context = {"pg_details":pg_details}
    return render(request,"view_pg.html",context) 
