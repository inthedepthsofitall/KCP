from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse

import logging

from .models import URL
from .serializers import URLSerializer


logger = logging.getLogger(__name__)

class URLListCreate(generics.ListCreateAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer

    # def create(self, request, *args, **kwargs):
    #     logger.info("Received data: %s", request.data)
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         self.perform_create(serializer)
    #         headers = self.get_success_headers(serializer.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #     else:
    #         logger.error("Errors: %s", serializer.errors)  # Log serializer errors
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        logger.info("Received data: %s", request.data)  # Log the incoming request data
        return super().post(request, *args, **kwargs)

class URLRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer


def home(request):
    return HttpResponse("Welcome to the backend server! SLim UrlZ")

def redirect_view(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    return redirect(url.original_url)

def my_view(request):
    if request.method == 'POST':
        try:
            return JsonResponse({'error': 'Validation failed'}, status=400)
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)}, status=400)

