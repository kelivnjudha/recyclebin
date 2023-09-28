from django.shortcuts import render
from Arts.models import Upload, Info

# Create your views here.
def index(request):
    uploads = Upload.objects.all()
    info_objects = Info.objects.all()
    
    return render(request, 'core/index.html',{
        'uploads':uploads,
        'info_objects':info_objects,
    })