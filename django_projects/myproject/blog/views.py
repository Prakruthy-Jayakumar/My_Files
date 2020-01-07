from django.http import JsonResponse
import csv
from blog.models import Blog,Entry,Author,Images
from django.shortcuts import render
from .forms import BlogForm, SignupForm, LoginForm,UploadFileForm
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import get_template
from xhtml2pdf import pisa  #pisa is a html2pdf converter using the ReportLab Toolkit, the HTML5lib and pyPdf.
#xhtml2pdf is a python library, third-party module, used to generate pdf docs
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from blog.serializers import BlogSerializer

def insert_blog(request):
    if request.method == 'POST':

        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():

            blog_name_from_user = blog_form.cleaned_data['blog_name'] 
            blog_tagline_from_user = blog_form.cleaned_data['blog_tag_line'] 

            blog_object = Blog(name=blog_name_from_user, tagline=blog_tagline_from_user)
            blog_object.save() # will save the data from the form to database
            

            blog_object = Blog()
            blog_object.name = "Blog"
            blog_object.tagline =  "Lorem ipsum dolor sit amet"
            blog_object.save() # will save the data from the form to database table blog

            entry_object = Entry()
            entry_object.headline = "Lorum Ipsum"
            entry_object.body_text = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
            entry_object.pub_date = "2018-07-04"
            entry_object.mod_date = "2018-07-04"
            entry_object.n_comments = 0
            entry_object.n_pingbacks = 0
            entry_object.rating = 5
            entry_object.blog = blog_object # will insert the blog id into blog_entry
            entry_object.save()

            john = Author.objects.create(name="John") # will create new author in blog_authers table
            paul = Author.objects.create(name="Paul") # will create new author in blog_authers table
            george = Author.objects.create(name="George") # will create new author in blog_authers table

            entry_object.authors.add(john, paul, george) # will add data to blog_entry_authors
            return HttpResponse('Data Inserted successfully')

    else:
        blog_form = BlogForm(request.POST)  
        return render(request, 'blog-insert-form.html', {'form': blog_form})  



#@login_required
def showBlog(request,requested_blog_id):
    blog_details = Blog.objects.get(id=requested_blog_id)
    all_result = Blog.objects.all()
    context = {"blog":blog_details,"rslt":all_result}
    return render(request,"view-blog.html",context)   

#def showBlogDetails(request,requested_blog_id):
#    blog_details = Entry.objects.prefetch_related("blog").get(id=requested_blog_id)
#    context = {"blog_details":blog_details}
#    return render(request,"view-blog-details.html",context)   


 
def edit_blog(request,requested_blog_id):
    if request.method == 'POST': #method is GET so else part is going to work

        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():
            blog_details = Blog.objects.get(id=requested_blog_id) # this will select datafrom database 
            blog_details.name = blog_form.cleaned_data['blog_name']
            blog_details.tagline = blog_form.cleaned_data['blog_tag_line']
            blog_details.save()
                
            return HttpResponse('Data Edited successfully')

    else:

        blog_details = Blog.objects.get(id=requested_blog_id) # this will select datafrom database 
        blog_form = BlogForm(initial={"blog_name":blog_details.name,"blog_tag_line":blog_details.tagline}) # this will set initial values in the form from selected data

    return render(request, 'edit-blog.html', {'form': blog_form,'blog_id':requested_blog_id,})  

def delete_entry(request,requested_blog_id):

    blog_details = Blog.objects.get(id=requested_blog_id)  
    blog_details.delete()
    return HttpResponse('Data Deleted successfully')

def listBlogs(request):

    blogs_list = Blog.objects.all()
    paginator = Paginator(blogs_list, 1)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)

    return render(request, "list-blogs.html",{"blogs":blogs})




def signup(request):
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
                    return HttpResponse("Signup successfull")
    else:
        signup_form = SignupForm(request.POST)
    return render(request, 'signup.html',{"form":signup_form})                 
    

def loginAction(request):
    if request.user.is_authenticated:
        return HttpResponse('You Are already logged in')
    else:   
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():

                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']

                user = authenticate(username=username, password=password)
                            
                if user is not None:
                    if user.is_active:
                        login(request, user)  #in-built fn login != loginAction()  
                        #return HttpResponse('Login Successful')
                        messages.success(request,'Login successfully')
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

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a success page.ss 



def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Images(image=request.FILES['image'])
            instance.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully added')
            return HttpResponseRedirect('upload')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


    
def showImage(request):
    img = Images.objects.get(id=1)
    return render(request, 'image_preview.html', {"file":img})

def sendMailToUser(request):
    subject = "Subject here"            
    message = "hai how are you"
    sender = "whitebrickincpvtltd@gmail.com"
    recievers = ["prakruthyjkumar@gmail.com"]
    msg = EmailMessage(subject,message,sender,recievers)
    msg.content_subtype = "html"
    msg.send()  
    return HttpResponse("successfull")


def sample_view(request):
    return render(request,"ajax_template.html")

def sample_ajax_view(request):  
    data = {"name":"Prakruthy"}
    return JsonResponse(data)


def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response



def html_to_pdf_view(request):
    blog_objects = Blog.objects.all()


    template_path = 'pdf_template.html'
    context = {"blogs":blog_objects}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback="")
    # if error then show some funy view
    if pisaStatus.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))


def login_api(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)
@csrf_exempt
@api_view(["GET"])
def authenticatedapi(request):
    data = {"message":"Hello World"}
    return Response(data, status=HTTP_200_OK) 


@csrf_exempt
@api_view(["GET"])
def serializersample(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs,many=True)
    return Response(serializer.data)    


@csrf_exempt
@api_view(["PUT"])
def serializer_put(request,requested_blog_id):

    blog = Blog.objects.get(id=requested_blog_id)
    serializer = BlogSerializer(blog,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)       



@csrf_exempt
@api_view(["DELETE"])
def serializer_delete(request,requested_blog_id):

    blog = Blog.objects.get(id=requested_blog_id)
    blog.delete()
    return Response(status=HTTP_204_NO_CONTENT)     
