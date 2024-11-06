from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Path for login
    path(route='login', view=views.login_user, name='login'),
    
    # Path for logout
    path(route='logout', view=views.logout_user, name='logout'),
    
    # Path for registration
    path(route='register', view=views.registration, name='register'),
    
    # Path for getting dealers
path(route='get_dealers/', view=views.get_dealerships, name='get_dealers'),
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'), 
        path(route='dealer/<int:dealer_id>', view=views.get_dealer_details, name='dealer_details'),   
    # Uncomment the following paths if needed
    # path('login/', TemplateView.as_view(template_name="index.html")),
    
    # Path for dealer reviews view (uncomment and add the view if required)
    # path('dealer_reviews/', view=views.dealer_reviews, name='dealer_reviews'),
    path(route='add_review', view=views.add_review, name='add_review'),
    # Path for adding a review view (uncomment and add the view if required)
    # path('add_review/', view=views.add_review, name='add_review'),
        path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews, name='dealer_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
