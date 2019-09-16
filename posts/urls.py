from django.urls import path
from .views import HomePostView,DetailPostsView
urlpatterns =[
              path('',HomePostView.as_view(),name ='home'),
              path('detail/',DetailPostsView.as_view(),name ='detail'),
              ]