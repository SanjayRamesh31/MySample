from django.shortcuts import render, redirect
from django.conf import settings
from .forms import DocumentForm
from .models import Document
import firebase_admin
from firebase_admin import storage
import os

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()

            try:
                file_path = document.file.path
                bucket = storage.bucket()
                blob = bucket.blob(f'documents/{os.path.basename(file_path)}')

                blob.upload_from_filename(file_path)

                document.file_url = blob.public_url
                document.save()

                return redirect('document_list')
            except Exception as e:
                print(f"Error uploading file to Firebase: {e}")
                document.delete()
                return render(request, 'upload.html', {'form': form, 'error': 'Failed to upload to Firebase'})
        else:
            return render(request, 'upload.html', {'form': form, 'error': 'Invalid form submission'})
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'document_list.html', {'documents': documents})

def home(request):
    return redirect('document_list')
