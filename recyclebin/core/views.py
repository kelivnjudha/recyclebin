from django.shortcuts import render
from Arts.models import Upload, info

# Create your views here.
def index(request):
    
    return render(request, 'core/index.html',{
        'upload':Upload,
        'info':info,
    })