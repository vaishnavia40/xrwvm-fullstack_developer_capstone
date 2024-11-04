# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration

    # path for login
    path(route='login', view=views.login_user, name='login'),
        path('logout', views.logout_user, name='logout'),  # Logout path
    path('register', views.registration, name='register'),  # Registration path

    # path('login/', TemplateView.as_view(template_name="index.html")),
    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
