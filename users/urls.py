
from django.urls    import path
from users.views    import SignupView, LoginView, EmailView

urlpatterns = [
    path('/signup', SignupView.as_view()),
    path('/email', EmailView.as_view()),
    path('/login', LoginView.as_view())
]
