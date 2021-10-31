from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name="Home page"),
   path('handlelogin/',views.handlelogin,name="Login"),
   path('handlelogout/',views.handlelogout,name="Logout"),
   path('studentuser/',views.studentuser,name="User page"),
   path('register/',views.register,name="Register Page"),
   path('viewdetails/',views.viewdetails,name="Student Details")
]
