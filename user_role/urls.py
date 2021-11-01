from django.urls import path
from .views import (RegisterView,LoginView,AdvisorListView,BookingView,BookedCallsView)

urlpatterns=[
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('<uuid:id>/advisor/',AdvisorListView.as_view()),
    path('<uuid:id>/advisor/<int:advisor_id>/',BookingView.as_view()),
    path('<uuid:id>/advisor/booking/',BookedCallsView.as_view()),
]