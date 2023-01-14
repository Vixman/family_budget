from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ExpensesSerializer
from .models import Expenses

from rest_framework import permissions
from rest_framework import pagination


class ExpensesListAPIView(ListCreateAPIView):
    serializer_class = ExpensesSerializer
    queryset = Expenses.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = pagination.BasePagination

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class ExpensesDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpensesSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Expenses.objects.all()
    lookup_field = "id"
    pagination_class = pagination.BasePagination

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
