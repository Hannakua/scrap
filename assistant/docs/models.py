from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    CATEGORY_CHOICES = [
        ('image', 'Image'),
        ('document', 'Document'),
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('archive', 'Archive'),
        ('other', 'Other'),
    ]

    file = models.FileField(upload_to='files/')  # сам файл, який буде зберігатися
    upload_date = models.DateTimeField(auto_now_add=True)  # дата завантаження
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  # категорія файлу
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # користувач, який завантажив файл
    display_name = models.CharField(max_length=255, blank=True, null=True) # назва файлу, яка буде відображатися

    def __str__(self):
        return self.get_display_filename()

    def get_display_filename(self):
        if self.display_name:
            return self.display_name
        # Відсікаємо приставку та розширення файлу
        name_without_extension = self.file.name.rsplit('.', 1)[0]
        displayed_name = name_without_extension[:-7]  # Відсікаємо приставку "_хххххх"
        #return displayed_name or "Unnamed File"
        return name_without_extension or "Unnamed File"

    @staticmethod
    def determine_category(filename):
        # Визначення категорії на основі розширення файлу
        IMAGE_EXTENSIONS = ['jpg', 'jpeg', 'png', 'bmp', 'gif', 'svg', 'tiff', 'webp']
        DOCUMENT_EXTENSIONS = ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'odt', 'ods', 'txt']
        VIDEO_EXTENSIONS = ['mp4', 'mkv', 'flv', 'avi', 'mov', 'wmv']
        AUDIO_EXTENSIONS = ['mp3', 'wav', 'ogg', 'm4a', 'aac', 'flac']
        ARCHIVE_EXTENSIONS = ['zip', 'rar', '7z', 'tar', 'gz']

        extension = filename.split('.')[-1].lower()

        if extension in IMAGE_EXTENSIONS:
            return 'image'
        elif extension in DOCUMENT_EXTENSIONS:
            return 'document'
        elif extension in VIDEO_EXTENSIONS:
            return 'video'
        elif extension in AUDIO_EXTENSIONS:
            return 'audio'
        elif extension in ARCHIVE_EXTENSIONS:
            return 'archive'
        else:
            return 'other'
