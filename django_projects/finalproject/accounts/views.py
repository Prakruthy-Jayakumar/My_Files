from django.shortcuts import render
from .forms import SignupForm, LoginForm, pgForm, contactForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import redirect
from accounts.models import mysub, contact_info,Images,Notification,cities
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

def home(request): 
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def listpg(request):
    context = {'pg_details': mysub.objects.all()}
    return render(request,"listpg1.html",context)  





def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('acc_active_email.html', {
                'user':user,
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, 
                                 message,
                                  to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')

    else:
        form = SignupForm()

    return render(request, 'sign.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        # return HttpResponse(request, 'Thank you for your email confirmation. Now you can login your account.')
        #return HttpResponse()
        return HttpResponseRedirect('/login')
    else:
        return HttpResponse('Activation link is invalid!')


def login1(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('mysubmissions')
    
    else:   
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():

                email = login_form.cleaned_data['email']
                password = login_form.cleaned_data['password']

                user = authenticate(email=email, password=password)
                            
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

def forgot_password(request):
    form = SignupForm()
    return render(request, "forgot-your-password.html",{"form":form})
    



def logout1(request):
    logout(request)
    return HttpResponseRedirect('/')

def mysubmissions(request):
    properties = mysub.objects.filter(user=request.user)
    return render(request, 'mysubmissions.html', {'properties': properties})


def contact_pg(request):
    
    if request.method == 'POST':


        x = contactForm(request.POST)

        if x.is_valid():

            name_contact_user = x.cleaned_data['name'] 
            email_contact_user = x.cleaned_data['email'] 
            message_contact_user = x.cleaned_data['message']
          

            contact_object = contact_info(contact_name=name_contact_user, contact_email=email_contact_user, contact_message=message_contact_user)
            contact_object.save() # will save the data from the form to database
             
            return HttpResponseRedirect("/")

    else:
        x = contactForm(request.POST)
        return render(request, 'contact.html', {'form': x}) 


def add_pg(request):
    if request.method == 'POST':
        x = pgForm(request.POST,request.FILES)

        if x.is_valid():
            pg_name_user = x.cleaned_data['name'] 
            pg_city_user = request.POST['city']
            pg_dis_user = x.cleaned_data['district']
            pg_type_user=x.cleaned_data['pg_type']
            time_user=x.cleaned_data['time']
            status_user=x.cleaned_data['status']

            city=cities.objects.filter(id=pg_city_user)
            userInfo=request.user #this will add userid to mysub table

            pg_object = mysub(name=pg_name_user, district=pg_dis_user, pg_type=pg_type_user,time=time_user,status=status_user,city=city, user=userInfo)
            pg_object.save()



            #save image of corresponding pg
            instance = Images(image=request.FILES['image'],mysub=pg_object)
            instance.save()
            return HttpResponseRedirect("/mysubmissions")
    else:
        city=cities.objects.all()
        x = pgForm(request.POST)
        return render(request, 'add_pg.html', {'form': x,'city':city})  

def edit_pg(request,pg_id):
    if request.method == 'POST': #method is GET so else part is going to work

        x = pgForm(request.POST)
        if x.is_valid():
            pg_details = mysub.objects.get(id=pg_id)
            # this will select datafrom database 
            pg_details.name = x.cleaned_data['name']
            pg_details.city = x.cleaned_data['city']
            pg_details.district = x.cleaned_data['district']
            pg_details.pg_type = x.cleaned_data['pg_type']
            pg_details.time=x.cleaned_data['time']
            pg_details.status=x.cleaned_data['status']
            pg_details.save()
            return HttpResponseRedirect("/mysubmissions")

    else:

        pg_details = mysub.objects.get(id=pg_id) # this will select datafrom database 
        x = pgForm(initial={"name":pg_details.name,"city":pg_details.city,"disrict":pg_details.district,"pg_type":pg_details.pg_type,"time":pg_details.time,"status":pg_details.status}) # this will set initial values in the form from selected data

    return render(request, 'editedpg.html', {'form': x,'pg_id':pg_id,})  

def deleteDetails(request,pg_id):

    pg_details = mysub.objects.get(id=pg_id)  
    pg_details.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 


def viewcontact(request,pg_id):
    message="Clicked your pg details"
    userdetails=request.user
    not_object= Notification(message_not=message,mysub_id=pg_id,user=userdetails)
    not_object.save()
    
    return HttpResponse("Successfull")
    notification.send(recipients, 'new_comment', context)

def Notifications(request):
    context = {'not_details': Notification.objects.all()}
    return render(request,"notification.html",context) 

def search(request):
    if request.method == 'POST':
        location=request.POST['city']
        result=mysub.objects.filter(city=location)
        context = {'pg_details':result }
        return render(request,"listpg1.html",context) 

    else:
        city = cities.objects.all()
        return render(request, 'search.html', {'city': city})
