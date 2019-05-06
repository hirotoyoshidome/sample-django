from django.urls import path

from . import views

app_name = 'hello'

urlpatterns = [
    path('', views.HelloView.as_view(), name='hello'),
    # path('', views.hello, name='hello'),
    path('specifics/<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('specifics/<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
