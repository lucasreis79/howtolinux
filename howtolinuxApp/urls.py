from django.urls import path
from . import views


app_name = 'howtolinuxApp'

urlpatterns = [
    path('', views.TemplateView.as_view()),
    path('blog/', views.PostListView.as_view(), name='list'),
    path('blog/<slug:slug>/', views.PostDetailView.as_view(), name='detail'),
]