from django.urls import path
from .views import ExpensesDetailAPIView, ExpensesListAPIView


urlpatterns = [
    path("", ExpensesListAPIView.as_view()),
    path("<int:id>", ExpensesDetailAPIView.as_view()),
]
