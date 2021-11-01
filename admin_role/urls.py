from django.urls import path
from .views import AdvisorView


urlpatterns = [
    path('admin/advisor/',AdvisorView.as_view()),
]