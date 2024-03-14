from rest_framework import generics

from .models import Women
from .serializers import WomenSerializer


class WomenAPIList(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIRetrieve(generics.RetrieveAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPICrete(generics.CreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIDelete(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
