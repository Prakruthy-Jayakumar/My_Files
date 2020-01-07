from django.urls import path
from . import views
urlpatterns =[
path('add_books',views.add_books,name='books'),
path('listbook', views.listBooks, name='details'),
path('view/<int:requested_book_id>', views.showBookDetails, name='details'),
path('edit/<int:requested_book_id>',views.editDetails, name='edited'),
path('delete/<int:requested_book_id>',views.deleteDetails, name='deleted'),
path('signup',views.signup,name='signup'),
path('login',views.loginAction,name='login'),
path('logout',views.logout_view,name='logout')
]