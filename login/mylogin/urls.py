from django.urls import path
from . import views

app_name = "mylogin"

urlpatterns = [
    path("",views.index,name="index"),
    path("signin",views.signin,name="signin"),
    path("signup",views.signup,name="signup"),
    path("mypage",views.userpage,name="userpage"),
    path("logout",views.logout_views,name="logout_views")
]