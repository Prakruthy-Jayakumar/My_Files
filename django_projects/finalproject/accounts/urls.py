from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
		path('', views.home, name='home_page'),# view home page
		path('about',views.about,name='aboutus'),# view about us page
		# path('portfolio',views.portfolio,name='portfolio'),# view gallery
		path('contact', views.contact_pg, name='contactpage'),# view contact page


		path('register',views.register, name='registration'),# for registration
		 url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),


		path('login',views.login1,name='loginpage'),# for login
		#path('forgot_your_password',views.forgot_password,name='forgot_your_password'),

		url(r'^reset/$', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt',
        ),
        name='password_reset'),
    url(r'^reset/done/$', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html',
        
    ),
        name='password_reset_done'),
    
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html',
      
    ),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html',
        
    ),
        name='password_reset_complete'),
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(
        template_name='password_change.html'
    ),
        name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'
    ),
        name='password_change_done'),



		path('viewcontact/<int:pg_id>',views.viewcontact,name='viewcontact'),
		path('search',views.search,name='search'),
        # path('search_view',views.search_view,name='search-view'),



		

		path('mysubmissions',views.mysubmissions,name='mypage'), #for viewing my submission page

		path('listpg',views.listpg,name='show-pg'),# list the pg
		path('notification',views.Notifications,name='show-notification'),
	

		path('add_pg',views.add_pg,name='add-pg'),# for adding new pg
		path('editpg/<int:pg_id>',views.edit_pg,name='edit-pg'),# edit the pg details
		path('deletepg/<int:pg_id>',views.deleteDetails,name='delete-pg'),# delete the details


		path('logout',views.logout1, name='logoutpage'),# for logout
]