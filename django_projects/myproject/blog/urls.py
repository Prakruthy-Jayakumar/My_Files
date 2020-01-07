from django.urls import path
from . import views
urlpatterns = [
path('insert-data', views.insert_blog, name='insert_blog'),
path('<int:requested_blog_id>', views.showBlog, name='show_blog'),
#path('details/<int:requested_blog_id>', views.showBlogDetails, name='show_blog_details'),
path('edit/<int:requested_blog_id>',views.edit_blog,name='editblog'),
path('delete/<int:requested_blog_id>',views.delete_entry,name='dltblog'),
path('listblogs',views.listBlogs,name='list'),
path('signup',views.signup,name='signup'),
path('login',views.loginAction,name='login'),
path('logout',views.logout_view,name='logout'),
path('upload',views.upload_file,name='upload'),
path('showimage',views.showImage,name='image'),
path('email',views.sendMailToUser,name='email'),
path('sample',views.sample_view,name='sample'),
path('test_ajax',views.sample_ajax_view,name='sample'),
path('someview',views.some_view,name='someview'),
path('pdf',views.html_to_pdf_view,name='pdf'),
path('api/login',views.login_api,name='api'),
path('api/authenticated',views.authenticatedapi,name='serializer-sample'),
path('api/serializersample',views.serializersample,name='serializer'),
path('api/serializer-put/<int:requested_blog_id>',views.serializer_put,name='put'),
path('api/serializer-delete/<int:requested_blog_id>',views.serializer_delete,name='delete')
]