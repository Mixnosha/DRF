from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class WomenViewSet(viewsets.ModelViewSet): #ReadOnlyModelViewSet
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


    @action(method=['get'], detail=False)
    def category(self, request):
        cats = Category.objects.all()
        return Response({'cats': [c.name for c in cats]})


#class WomenAPIView(generics.ListAPIView):
#    queryset = Women.objects.all()
#    serializer_class = WomenSerializer
#
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer





# class WomenAPIView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "not pk"})
#         try:
#             w = Women.objects.get(pk=pk)
#             w.delete()
#         except:
#             return Response({"error": "Object does not exists"})
#
#         return Response({"post": "post delete" + str(pk)})
