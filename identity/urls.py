from django.urls import path
from .views import login_view
from .views import signup_view
# from .views import logout





app_name = "identity"
urlpatterns = [
        path('login/', login_view, name="login"),    
        path('signup/', signup_view, name="signup"),
        # path("logout", logout, name="logout"),
        
        
       
]

