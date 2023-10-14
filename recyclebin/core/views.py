from django.shortcuts import render
from Arts.models import Upload, Info
from django.http import JsonResponse
from .utils import format_likes_count
import random
# Create your views here.
def index(request):
    uploads = Upload.objects.all()
    info_objects = Info.objects.all().order_by('?')
    return render(request, 'core/index.html',{
        'uploads':uploads,
        'info_objects':info_objects,
    })

def like_view(request, info_object_id):
    if request.method == "POST":
        info_object = Info.objects.get(id=info_object_id)
        info_object.likes += 1
        info_object.save()
        return JsonResponse({'like_count': info_object.likes})