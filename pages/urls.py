from django.urls import path # path is used for routing URLs to the appropriate view functions within a Django application using the URL dispatcher.
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [  # make sure the spelling is right. the hello.urls will look into this list as urlpatterns to look for the patter of pages.urls
    #path('', views.index, name='index'),
    path('', views.index, {'pagename': ''}, name='home'),
    path('contact', views.contact, name = 'contact'),
    path('<str:pagename>', views.index, name='index'), # capturing group : everything inside the angle brackets will be captured and sent to the view as parameter
    # <str:pagename> : capture everything after the domain name and send it to the view as the string parameter pagename.
    ]