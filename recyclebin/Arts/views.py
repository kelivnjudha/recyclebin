from django.shortcuts import render
from django.http import JsonResponse
from .models import Info

def like_slide(request, slide_id):
    slide = Info.objects.get(pk=slide_id)
    slide.likes += 1
    slide.save()
    return JsonResponse({'like_count': slide.likes})

def get_like_count(request, slide_id):
    slide = Info.objects.get(pk=slide_id)
    return JsonResponse({'like_count': slide.likes})

# Create your views here.
