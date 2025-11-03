# Lesson 11: Django File Uploads

## 📚 Darsning maqsadi
Django'da fayllar bilan ishlashni o'rganish - fayl yuklash, saqlash va ko'rsatish.

## 🎯 Topshiriqlar

### ✅ 1. Fayl yuklash formasini yaratish
Django'da fayl yuklash uchun forma shablon'ini tayyorlash. Forma maydonlari:
- **Nomi** (title)
- **Ta'rifi** (description)  
- **Fayli** (file)

### ✅ 2. Application modelini yaratish
Model maydonlari:
- `title` - CharField (max_length=200)
- `description` - TextField (blank=True)
- `file` - FileField (upload_to="applications/")
- `created_at` - DateTimeField (auto_now_add=True)

### ✅ 3. View va URL'larni yaratish
- Application'larni saqlaydigan view
- Application'larni ko'rsatadigan view
- URL pattern'lar

### ✅ 4. Index.html shablonini yaratish
- Yuklangan application'larni ko'rsatish
- Fayl yuklash formasi
- Fayllarni yuklab olish va ko'rish imkoniyati

## 🚀 Loyihani ishga tushirish

### 1. Virtual environment'ni aktivlashtirish
```bash
cd "d:\Universitet\JDU\Django\Lesson 10"
.\.venv\Scripts\Activate.ps1
cd "..\Lesson 11"
```

### 2. Migratsiyalarni qo'llash
```bash
python manage.py migrate
```

### 3. Development serverni ishga tushirish
```bash
python manage.py runserver
```

### 4. Brauzerda ochish
```
http://127.0.0.1:8000/
```

## 📁 Loyiha tuzilishi

```
Lesson 11/
├── config/
│   ├── __init__.py
│   ├── settings.py      # MEDIA_URL va MEDIA_ROOT konfiguratsiyasi
│   ├── urls.py          # Media fayllarni serve qilish
│   ├── wsgi.py
│   └── asgi.py
├── applications/
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── __init__.py
│   ├── admin.py         # Admin panel'da Application modelini ko'rsatish
│   ├── apps.py
│   ├── models.py        # Application modeli
│   ├── forms.py         # ApplicationForm (ModelForm)
│   ├── views.py         # application_list view
│   ├── urls.py          # URL pattern'lar
│   └── tests.py
├── templates/
│   └── applications/
│       └── index.html   # Asosiy sahifa - yuklash va ko'rsatish
├── media/               # Yuklangan fayllar shu yerda saqlanadi
│   └── applications/
├── manage.py
├── db.sqlite3
└── README.md
```

## 🔧 Asosiy komponentlar

### 1. Model (`applications/models.py`)
```python
class Application(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nomi")
    description = models.TextField(blank=True, verbose_name="Ta'rifi")
    file = models.FileField(upload_to="applications/", verbose_name="Fayli")
    created_at = models.DateTimeField(auto_now_add=True)
```

### 2. Form (`applications/forms.py`)
```python
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["title", "description", "file"]
```

### 3. View (`applications/views.py`)
```python
def application_list(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("application_list")
    else:
        form = ApplicationForm()
    
    applications = Application.objects.all()
    return render(request, "applications/index.html", {
        "form": form,
        "applications": applications,
    })
```

### 4. Settings konfiguratsiyasi
```python
# Media files (User uploads)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### 5. URL konfiguratsiyasi
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 💡 Muhim nuqtalar

1. **FileField** - Django'da fayllar bilan ishlash uchun
2. **upload_to** - Fayllarni qayerga saqlash kerakligini belgilaydi
3. **MEDIA_ROOT** - Fayllar saqlanadigan asosiy papka
4. **MEDIA_URL** - Fayllarga URL orqali murojaat qilish
5. **enctype="multipart/form-data"** - Formada fayllarni yuklash uchun zarur
6. **request.FILES** - View'da yuklangan fayllarni olish

## 🎨 Template xususiyatlari

- Bootstrap 5 styling
- Responsive dizayn
- Fayl yuklash formasi
- Yuklangan fayllar ro'yxati
- Fayllarni yuklab olish va ko'rish tugmalari
- Django messages frameworkidan foydalanish

## 🔐 Admin panel

Admin panelda Application modelini ko'rish va boshqarish:
```bash
python manage.py createsuperuser
```

Admin URL: `http://127.0.0.1:8000/admin/`

## 📝 Qo'shimcha imkoniyatlar

- Fayl hajmini cheklash
- Fayl turini validatsiya qilish
- Rasm fayllar uchun ImageField ishlatish
- Multiple file upload
- File compression
- Cloud storage (AWS S3, etc.) integratsiyasi

## 🎓 O'rganilgan Django kontseptsiyalari

✅ FileField va file uploads  
✅ MEDIA_URL va MEDIA_ROOT  
✅ ModelForm bilan ishlash  
✅ POST va FILES data handling  
✅ Template'larda file URL'larni ko'rsatish  
✅ Admin panel customization  
✅ Django messages framework
