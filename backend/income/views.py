from .serializers import IncomeSerializer
from .models import Income

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework import pagination


class IncomeListAPIView(ListCreateAPIView):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = pagination.BasePagination

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class IncomeDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = IncomeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Income.objects.all()
    lookup_field = "id"
    pagination_class = pagination.BasePagination

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
