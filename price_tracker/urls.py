from django.urls import path
from price_tracker import views

urlpatterns = [
    path('prices/', views.PriceTrackerViewSet.as_view()),
]