from django.urls import path
from . import views


app_name = 'polls'
# calling generic views
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results', views.ResultsView.as_view(), name='result'),
    path('<int:question_id>/vote', views.vote, name='vote')

]


# Hard-code way - calling function views
'''path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results', views.results, name='result'),
    path('<int:question_id>/vote', views.vote, name='vote')'''

