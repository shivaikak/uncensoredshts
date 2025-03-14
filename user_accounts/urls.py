from django.urls import path
from . import views
from .views import submit_ranking, get_rankings

urlpatterns = [
    path('submit/', submit_ranking, name='submit-ranking'),
    path('rankings/', get_rankings, name='get-rankings'),
    path('register/', views.register_view, name = 'register'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout')
]