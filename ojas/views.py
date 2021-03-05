from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from ojas.models import FileUploadData
from .forms import *

def uploadfile(request):
    alert_message = False
    if request.method == 'POST': 
        submitted_form = FileUploadForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            submitted_form.save()
            alert_message = {
                'status': True,
                'message': 'Successfully saved the image'
            }
        else:
            alert_message = {
                'status': False,
                'message': 'Form data is invalid. Please check if your image / title is repeated'
            }
    
    form = FileUploadForm()
    context = {
        'alert_data': alert_message,
        'form': form,
        'images': FileUploadData.objects.all
    }
    return render(request, 'index.html', context=context)