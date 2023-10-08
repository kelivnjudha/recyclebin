from django.shortcuts import render
from Arts.models import Upload, Info
from django.http import JsonResponse

# Create your views here.
def index(request):
    uploads = Upload.objects.all()
    info_objects = Info.objects.all()
    
    return render(request, 'core/index.html',{
        'uploads':uploads,
        'info_objects':info_objects,
    })

def update_likes(request, item_id):
    item = Info.objects.get(pk=item_id)
    item.likes += 1
    item.save()
    return JsonResponse({'likes': item.likes})
