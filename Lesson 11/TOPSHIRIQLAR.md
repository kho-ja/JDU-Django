# TOPSHIRIQLAR - Lesson 11: Django File Uploads

## 📋 Dars topshiriqlari

### ✅ Topshiriq 1: Forma shablo'nini tayyorlash
**Talablar:**
- Django'da fayl yuklashni amalga oshirish uchun forma yaratish
- Forma maydonlari:
  - **Nomi** (CharField)
  - **Ta'rifi** (TextField)
  - **Fayli** (FileField)

**Bajarilgan:**
- `applications/forms.py` da `ApplicationForm` yaratildi
- Bootstrap 5 bilan stilizatsiya qilindi
- Form validation va error handling qo'shildi

---

### ✅ Topshiriq 2: Application modelini yaratish
**Talablar:**
- Django modeli yaratish
- Maydonlar:
  - `title` - application nomi
  - `description` - application ta'rifi
  - `file` - yuklangan fayl

**Bajarilgan:**
- `applications/models.py` da `Application` modeli yaratildi
- Qo'shimcha maydonlar:
  - `created_at` - yaratilgan sanani avtomatik saqlash uchun
- Model Meta class qo'shildi:
  - `ordering` - yangilaridan eskigaroq tartibda
  - `verbose_name` - admin panelda ko'rsatish uchun
- `__str__` metodi qo'shildi

---

### ✅ Topshiriq 3: View va URL'larni yaratish
**Talablar:**
- Application'larni saqlaydigan view yaratish
- Application'larni ko'rsatadigan view yaratish
- URL pattern'larni sozlash

**Bajarilgan:**
- `applications/views.py` da `application_list` view yaratildi:
  - GET request: forma va ro'yxatni ko'rsatadi
  - POST request: yangi application saqlaydi
  - Django messages bilan foydalanuvchiga xabar beradi
- `applications/urls.py` yaratildi
- `config/urls.py` yangilandi:
  - applications app URL'lari qo'shildi
  - Media fayllarni serve qilish sozlandi (DEBUG mode)

---

### ✅ Topshiriq 4: index.html shablonini yaratish
**Talablar:**
- Yaratilgan application'larni ko'rsatish
- Fayl yuklash formasi
- Fayllarni yuklab olish imkoniyati

**Bajarilgan:**
- `templates/applications/index.html` yaratildi
- **Xususiyatlar:**
  - 📤 Fayl yuklash formasi (title, description, file)
  - 📋 Yuklangan application'lar ro'yxati
  - ⬇️ Fayllarni yuklab olish tugmasi
  - 👁️ Fayllarni brauzerda ko'rish tugmasi
  - 📅 Yaratilgan sanani ko'rsatish
  - Bootstrap 5 dizayni
  - Responsive layout
  - Django messages uchun alert'lar
  - Emoji ikonlar

---

## 🎯 Qo'shimcha bajarilanlar

### Admin Panel Integration
- `applications/admin.py` da `ApplicationAdmin` yaratildi
- List display: title, created_at, file
- Search fields: title, description
- Filter options: created_at
- Readonly field: created_at

### Settings Configuration
- `INSTALLED_APPS` ga `applications` qo'shildi
- `MEDIA_URL` va `MEDIA_ROOT` sozlandi
- `TEMPLATES` `DIRS` yangilandi

### Database Migration
- Migration fayllar yaratildi va qo'llandi
- Database schema yaratildi

---

## 🚀 Loyihani test qilish

### 1. Serverni ishga tushirish
```bash
cd "d:\Universitet\JDU\Django\Lesson 10"
.\.venv\Scripts\Activate.ps1
cd "..\Lesson 11"
python manage.py runserver
```

### 2. Brauzerda ochish
```
http://127.0.0.1:8000/
```

### 3. Test qilish
1. ✅ Formani to'ldiring (nomi, ta'rifi, fayl)
2. ✅ "Yuklash" tugmasini bosing
3. ✅ Yuklangan application ro'yxatda paydo bo'ladi
4. ✅ "Yuklab olish" tugmasini bosib faylni yuklab oling
5. ✅ "Ko'rish" tugmasini bosib faylni brauzerda oching

---

## 📊 Natijalar

### Yaratilgan fayllar:
```
Lesson 11/
├── applications/
│   ├── admin.py          ✅ Admin panel konfiguratsiyasi
│   ├── forms.py          ✅ ApplicationForm (ModelForm)
│   ├── models.py         ✅ Application modeli
│   ├── views.py          ✅ application_list view
│   ├── urls.py           ✅ URL patterns
│   └── migrations/
│       └── 0001_initial.py ✅ Database migration
├── templates/
│   └── applications/
│       └── index.html    ✅ Main template
├── config/
│   ├── settings.py       ✅ MEDIA konfiguratsiyasi
│   └── urls.py           ✅ URL routing va media serving
├── media/                ✅ Fayl saqlash uchun
└── README.md             ✅ Dokumentatsiya
```

### Ishlatilgan Django kontseptsiyalari:
- ✅ FileField for file uploads
- ✅ ModelForm for form handling
- ✅ MEDIA_URL and MEDIA_ROOT configuration
- ✅ request.FILES handling in views
- ✅ Django messages framework
- ✅ Admin panel customization
- ✅ URL routing and include()
- ✅ Template rendering with context
- ✅ Static file serving in DEBUG mode

---

## 🎓 O'rganilganlar

1. **Django File Uploads**: Fayllarni qanday yuklash va saqlash
2. **FileField**: Model'da fayllar uchun maydon turi
3. **ModelForm**: Model asosida forma yaratish
4. **request.FILES**: View'da yuklangan fayllarni olish
5. **MEDIA settings**: Yuklangan fayllarni boshqarish
6. **Template file URLs**: Template'da fayl URL'larini ko'rsatish
7. **Admin integration**: Admin panelda file field'larni boshqarish

---

## 💻 Kod misollari

### Model Example
```python
class Application(models.Model):
    file = models.FileField(upload_to="applications/")
```

### Form Example
```python
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["title", "description", "file"]
```

### View Example
```python
def application_list(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
```

### Template Example
```html
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Yuklash</button>
</form>

<a href="{{ application.file.url }}">Yuklab olish</a>
```

---

## ✨ Barcha topshiriqlar muvaffaqiyatli bajarildi!
