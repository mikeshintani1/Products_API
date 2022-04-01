from django.urls import path
from . import views

urlpatterns = [
    path('review/<int:pk>/', views.review_list),
    path('<int:pk>', views.review_detail),

]