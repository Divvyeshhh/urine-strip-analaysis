from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .utils import process_image
import json

#Create your views here.

def index(request):
    return render(request, 'analysis/upload.html')

@api_view(['POST'])
def upload_image(request):
    image = request.FILES.get('image')
    if not image:
        return JsonResponse({'error': 'No image uploaded'}, status=400)
    
    colors = process_image(image)
    return JsonResponse({'colors': colors})



