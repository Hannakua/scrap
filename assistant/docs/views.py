from django.shortcuts import render, redirect
from .forms import UploadFileForm, RenameFileForm
from .models import File
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def user_files(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.user = request.user
            file_instance.category = File.determine_category(file_instance.file.name)
            file_instance.display_name = file_instance.get_display_filename()  # встановлення "відображуваного" імені
            file_instance.save()
            # Щоб не показувати форму після завантаження, редіректимо користувача
            return redirect('docs:user_files')
    
    files = File.objects.filter(user=request.user)
    # Отримуємо усі унікальні категорії, які належать користувачеві
    file_categories = files.values_list('category', flat=True).distinct()

    context = {
        'files': files,
        'file_categories': file_categories
    }

    return render(request, 'docs/user_files.html', context)


from .forms import RenameFileForm

def rename_file(request):
    if request.method == "POST":
        try:
            file_id = request.POST.get('file_id')
            new_name = request.POST.get('new_name')
            
            file_instance = File.objects.get(id=file_id)
            file_instance.display_name = new_name
            file_instance.save()

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def delete_file(request):
    if request.method == "POST":
        try:
            file_id = request.POST.get('file_id')
            file_instance = File.objects.get(id=file_id, user=request.user)
            file_instance.file.delete()  # це видалить файл з сервера
            file_instance.delete()  # це видалить запис з бази даних
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
