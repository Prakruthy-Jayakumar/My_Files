from django.urls import path
from . import views
urlpatterns = [
		path('', views.home, name='home_page'),# view home page
		path('about',views.about,name='aboutus'),# view about us page
		path('portfolio',views.portfolio,name='portfolio'),# view gallery
		path('contact', views.contact, name='contactpage'),# view contact page

		path('register',views.register, name='registration'),# for registration     
		path('login',views.login1,name='loginpage'),# for login
		path('forgot',views.forgot,name='fogot-ur-password'),
		path('logout',views.logout1, name='logoutpage'),# for logout

		path('mysubmissions',views.mysubmissions,name='mypage'), #for viewing my submission page
		path('mypage',views.mypage,name='mysub1'), #for viewing profile pages, only

		path('listpg',views.listpg,name='show-pg'),# list the pg
		path('add_pg',views.add_pg,name='add-pg'),# for adding new pg
		path('editpg/<int:pg_id>',views.edit_pg,name='edit-pg'),# edit the pg details
		path('deletepg/<int:pg_id>',views.deleteDetails,name='delete-pg'),# delete the details
		path('viewpg/<int:pg_id>',views.showpgDetails,name='view-pg'),# view the all details

		
		

		  

]