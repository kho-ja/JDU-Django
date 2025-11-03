# Lesson 14: Yakuniy Loyiha - Admin Panel

Bu yakuniy loyiha bo'lib, Django'da to'liq admin panel interfeysi yaratilgan.

## 📋 Loyiha Haqida

**Final Project** - Django asosida yaratilgan admin panel interfeysi:
- Foydalanuvchilar tizimi (login/register)
- Profile sahifasi
- Students CRUD operatsiyalari
- Modern responsive dizayn
- Bootstrap 5 va Font Awesome

## 🎯 Topshiriqlar

### ✅ 1-topshiriq: Loyiha va ilova yaratish
- `final_project` loyihasi yaratildi
- `profiles` ilovasi yaratildi
- `students` ilovasi yaratildi
- Settings.py sozlandi

### ✅ 2-topshiriq: Admin template tanlash
- Modern gradient dizayn
- Bootstrap 5 framework
- Font Awesome icons
- Responsive sidebar
- Professional UI/UX

### ✅ 3-topshiriq: Sahifalarni yaratish
- **login.html** - Login sahifasi
- **register.html** - Ro'yxatdan o'tish sahifasi
- **profile.html** - Profil sahifasi
- **students.html** - Talabalar ro'yxati
- **404.html** - Xatolik sahifasi
- **base.html** - Asosiy template

### ✅ 4-topshiriq: URL va View funksiyalari
- Authentication views (login, register, logout)
- Profile view (CRUD operations)
- Students view (list, add)
- Custom 404 handler

### ✅ 5-topshiriq: Static fayllar sozlamasi
- CSS fayllar (style.css, auth.css)
- JavaScript (script.js)
- Images (avatars)
- Static files sozlamasi

## 🏗️ Loyiha Strukturasi

```
Lesson 14/
├── manage.py
├── db.sqlite3
├── final_project/
│   ├── __init__.py
│   ├── settings.py          # Asosiy sozlamalar
│   ├── urls.py              # URL routing
│   ├── asgi.py
│   └── wsgi.py
├── profiles/
│   ├── models.py            # Profile modeli
│   ├── views.py             # Auth va profile views
│   ├── admin.py             # Admin registration
│   └── migrations/
├── students/
│   ├── models.py            # Student modeli
│   ├── views.py             # Students CRUD views
│   ├── admin.py             # Admin registration
│   └── migrations/
├── templates/
│   ├── base.html            # Base template
│   ├── login.html           # Login sahifasi
│   ├── register.html        # Register sahifasi
│   ├── profile.html         # Profile sahifasi
│   ├── students.html        # Students sahifasi
│   └── 404.html             # 404 error page
└── static/
    ├── css/
    │   ├── style.css        # Asosiy CSS
    │   └── auth.css         # Auth pages CSS
    ├── js/
    │   └── script.js        # JavaScript
    └── img/
        └── default-avatar.png
```

## 🚀 O'rnatish va Ishga Tushirish

### 1. Virtual Environment
```powershell
# Yaratish
python -m venv .venv

# Aktivlashtirish
.\.venv\Scripts\Activate.ps1
```

### 2. Paketlarni o'rnatish
```powershell
pip install django pillow
```

### 3. Migratsiyalarni bajarish
```powershell
python manage.py makemigrations
python manage.py migrate
```

### 4. Superuser yaratish
```powershell
python manage.py createsuperuser
# Username: admin
# Email: admin@example.com
# Password: admin123
```

### 5. Serverni ishga tushirish
```powershell
python manage.py runserver
```

### 6. Brauzerda ochish
```
http://127.0.0.1:8000/
```

## 🔐 Foydalanuvchi Ma'lumotlari

### Superuser
- **Username:** admin
- **Password:** admin123

### Sample Student Data
- ID: 2024001 - Ali Valiyev
- ID: 2024002 - Dilnoza Karimova
- ID: 2024003 - Bobur Tursunov

## 📱 Sahifalar

### 1. Login Page (`/login/`)
- Username va password bilan kirish
- "Remember me" checkbox
- Register sahifasiga havola
- Gradient background dizayni

### 2. Register Page (`/register/`)
- Yangi akkaunt yaratish
- First name, Last name
- Username, Email
- Password validation
- Login sahifasiga havola

### 3. Profile Page (`/profile/`)
- Foydalanuvchi ma'lumotlarini ko'rish
- Profile tahrirlash
- Avatar yuklab olish
- Parolni o'zgartirish
- **Login talab qilinadi**

### 4. Students Page (`/students/`)
- Barcha talabalarni ko'rish
- Yangi talaba qo'shish
- Statistika kartochkalari
- Table bilan ro'yxat
- **Login talab qilinadi**

### 5. 404 Page
- Custom error page
- Animated design
- Home page link

### 6. Django Admin (`/admin/`)
- Django default admin panel
- Student va Profile modellari
- Superuser bilan kirish

## 🎨 Dizayn Xususiyatlari

### Color Scheme
- **Primary:** Gradient (Purple to Blue)
  ```css
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  ```
- **Success:** Green (#28a745)
- **Warning:** Yellow (#ffc107)
- **Danger:** Red (#dc3545)

### Typography
- Font Family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
- Headings: Bold, Modern
- Body: Regular, Readable

### Components
- **Sidebar:** Fixed, collapsible
- **Cards:** Shadow, rounded corners
- **Buttons:** Gradient, hover effects
- **Tables:** Hover effects, responsive
- **Forms:** Clean, validated

### Animations
- Fade in effects
- Slide up animations
- Hover transitions
- Smooth scrolling

## 💻 Texnologiyalar

### Backend
- **Django:** 5.2.7
- **Python:** 3.11.3
- **Database:** SQLite3
- **Pillow:** 12.0.0 (Image processing)

### Frontend
- **Bootstrap:** 5.3.0 (CSS Framework)
- **Font Awesome:** 6.4.0 (Icons)
- **JavaScript:** Vanilla JS
- **CSS3:** Custom styles

## 📝 Models

### Profile Model
```python
class Profile(models.Model):
    user = OneToOneField(User)
    bio = TextField()
    avatar = ImageField()
    phone = CharField()
    address = TextField()
    birth_date = DateField()
    created_at = DateTimeField()
    updated_at = DateTimeField()
```

### Student Model
```python
class Student(models.Model):
    first_name = CharField()
    last_name = CharField()
    email = EmailField()
    phone = CharField()
    student_id = CharField()
    course = IntegerField()
    created_at = DateTimeField()
    updated_at = DateTimeField()
```

## 🔧 Settings Sozlamalari

### Installed Apps
```python
INSTALLED_APPS = [
    ...
    'profiles',
    'students',
]
```

### Templates
```python
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],
        ...
    }
]
```

### Static Files
```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Auth URLs
```python
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'profile'
LOGOUT_REDIRECT_URL = 'login'
```

## 🎯 Features

### ✅ Authentication
- User login/logout
- User registration
- Password validation
- Login required decorator
- Session management

### ✅ Profile Management
- View profile info
- Edit profile
- Update user data
- Change password
- Avatar upload (ready)

### ✅ Students Management
- List all students
- Add new student
- Student ID validation
- Email validation
- Course selection

### ✅ UI/UX
- Responsive design
- Mobile friendly
- Smooth animations
- Toast notifications
- Form validation
- Loading states

### ✅ Admin Panel
- Django admin integration
- Custom admin classes
- Search functionality
- Filters
- List display

## 🚦 URL Patterns

```python
/                   # Login page
/login/             # Login page
/register/          # Register page
/logout/            # Logout view
/profile/           # Profile page (auth required)
/students/          # Students page (auth required)
/admin/             # Django admin panel
```

## 📚 Qo'shimcha Ma'lumotlar

### Messages Framework
```python
from django.contrib import messages

messages.success(request, 'Success message')
messages.error(request, 'Error message')
messages.warning(request, 'Warning message')
messages.info(request, 'Info message')
```

### Login Required
```python
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    pass
```

### Custom 404 Handler
```python
# urls.py
handler404 = 'profiles.views.custom_404'

# views.py
def custom_404(request, exception):
    return render(request, '404.html', status=404)
```

## 🎓 O'rganilgan Mavzular

1. ✅ Django project va app yaratish
2. ✅ Models va migrations
3. ✅ Templates va static files
4. ✅ Authentication system
5. ✅ Forms va validation
6. ✅ CRUD operations
7. ✅ Admin customization
8. ✅ URL routing
9. ✅ Messages framework
10. ✅ Custom error pages

## 🔍 Keyingi Qadamlar

- [ ] Profile avatar upload functionality
- [ ] Student update va delete operations
- [ ] Pagination for students list
- [ ] Search functionality
- [ ] Export to Excel/PDF
- [ ] Email notifications
- [ ] Password reset functionality
- [ ] Profile picture cropping
- [ ] Advanced filters
- [ ] Charts and statistics

## 🎉 Xulosa

Bu yakuniy loyiha Django'ning asosiy konseptlarini to'liq qamrab oladi:
- Authentication va Authorization
- Models va Database
- Templates va Static Files
- CRUD Operations
- Admin Customization
- Modern UI/UX

**Barcha topshiriqlar muvaffaqiyatli bajarildi!** ✨

---

**Muallif:** Django Course  
**Sana:** 2025  
**Versiya:** 1.0  
**Status:** ✅ Completed
