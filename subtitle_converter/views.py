import chardet
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import SubtitleUploadForm
import os

from .models import BtnCounter

# Function to convert subtitle from windows-1256 to UTF-8
def convert_to_utf8(file_content):
    # Assuming file content is in windows-1256
    content = file_content.decode('windows-1256')
    return content.encode('utf-8')

# View for handling file uploads and conversion
def upload_subtitle(request):
    counter = 0
    try:
        obje, status_obje = BtnCounter.objects.get_or_create(counter_title="شمارنده ممد")
        counter = obje.visit_counter
    except Exception as error:
        print(error)
    
    if request.method == 'POST' and request.FILES['subtitle_file']:
        # Retrieve the uploaded file
        uploaded_file = request.FILES['subtitle_file']
        
        # Read the file as Windows-1256 encoded content
        file_content = uploaded_file.read()
        
        # Convert file content from Windows-1256 to UTF-8
        converted_content = convert_to_utf8(file_content)
        
        # Create a response with the converted content
        response = HttpResponse(converted_content, content_type='text/plain; charset=utf-8')
        response['Content-Disposition'] = f'attachment; filename="{uploaded_file.name}"'
        return response
    
    else:
        form = SubtitleUploadForm()
        context = {
            'form': form, 
            "conter": counter,
        }
        return render(request, 'index.html', context)


def counter(request):
    counter = 0
    try:
        obje, status_obje = BtnCounter.objects.get_or_create(counter_title="شمارنده ممد")
        obje.visit_counter += 1
        obje.save()
        counter = obje.visit_counter
    except Exception as error:
        print(error)
           
    output = {
        "counter":counter
    }
    return JsonResponse(output)