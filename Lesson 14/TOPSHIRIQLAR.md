# 14-dars: Yakuniy Loyiha - Topshiriqlar

Bu faylda barcha topshiriqlar va ularning yechimlari batafsil keltirilgan.

## 📝 Topshiriq 1: Loyiha va ilova yaratish

### Vazifa
Django'da "final_project" loyihasini, unda profile ilovasini yarating va sozlamalarini amalga oshiring.

### Yechim

#### 1. Virtual environment yaratish
```powershell
# Yangi papka yaratish
mkdir "Lesson 14"
cd "Lesson 14"

# Virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### 2. Django o'rnatish
```powershell
pip install django pillow
```

#### 3. Loyiha yaratish
```powershell
django-admin startproject final_project .
```

#### 4. Ilovalar yaratish
```powershell
python manage.py startapp profiles
python manage.py startapp students
```

#### 5. Settings.py sozlash
```python
# final_project/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Local apps
    'profiles',
    'students',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        ...
    },
]

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'profile'
LOGOUT_REDIRECT_URL = 'login'
```

**Natija:** ✅ Loyiha va ilovalar yaratildi va sozlandi.

---

## 📝 Topshiriq 2: Admin template tanlash

### Vazifa
Yakuniy loyiha uchun template tanlash (berilgan admin template dan foydalansa ham bo'ladi).

### Yechim

#### Template Xususiyatlari
1. **Modern Gradient Dizayn**
   - Purple to Blue gradient
   - Clean va professional ko'rinish

2. **Bootstrap 5 Framework**
   - Responsive grid system
   - Pre-built components
   - Mobile-first approach

3. **Font Awesome Icons**
   - 6.4.0 versiyasi
   - 1000+ icons
   - Vector-based

4. **Custom Components**
   - Collapsible sidebar
   - Statistics cards
   - Animated elements
   - Toast notifications

#### Directory Structure
```
Lesson 14/
├── templates/
│   ├── base.html           # Asosiy layout
│   ├── login.html          # Login sahifasi
│   ├── register.html       # Register sahifasi
│   ├── profile.html        # Profile sahifasi
│   ├── students.html       # Students sahifasi
│   └── 404.html            # Error page
└── static/
    ├── css/
    │   ├── style.css       # Main styles
    │   └── auth.css        # Auth pages styles
    ├── js/
    │   └── script.js       # JavaScript
    └── img/
        └── default-avatar.png
```

#### base.html - Asosiy Template
```html
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Admin Panel{% endblock %}</title>
    {% load static %}
    
    <!-- Bootstrap 5 -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- Custom CSS -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <!-- Sidebar -->
    <div class="sidebar" id="sidebar">
        <div class="sidebar-brand">
            <h3><i class="fas fa-graduation-cap"></i> Admin Panel</h3>
        </div>
        <ul class="sidebar-menu">
            <li><a href="{% url 'profile' %}"><i class="fas fa-user"></i> Profile</a></li>
            <li><a href="{% url 'students' %}"><i class="fas fa-users"></i> Students</a></li>
            <li><a href="/admin/"><i class="fas fa-cog"></i> Django Admin</a></li>
            <li><a href="{% url 'logout' %}"><i class="fas fa-sign-out-alt"></i> Logout</a></li>
        </ul>
    </div>

    <!-- Main Content -->
    <div class="main-content">
        <nav class="navbar">...</nav>
        <div class="content-wrapper">
            {% block content %}{% endblock %}
        </div>
        <footer class="footer">...</footer>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="{% static 'js/script.js' %}"></script>
</body>
</html>
```

**Natija:** ✅ Modern, responsive admin template yaratildi.

---

## 📝 Topshiriq 3: Sahifalarni yaratish

### Vazifa
Loyihada login_page, registration_page, 404, students va profile sahifalarini yaratish.

### Yechim

#### 1. Login Page (templates/login.html)
```html
<!DOCTYPE html>
<html lang="uz">
<head>
    <title>Login - Admin Panel</title>
    {% load static %}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'css/auth.css' %}">
</head>
<body class="login-page">
    <div class="login-container">
        <div class="login-card">
            <div class="login-header">
                <i class="fas fa-graduation-cap fa-3x mb-3"></i>
                <h2>Admin Panel</h2>
            </div>
            
            <form method="post" class="login-form">
                {% csrf_token %}
                <div class="form-group mb-3">
                    <label><i class="fas fa-user"></i> Username</label>
                    <input type="text" name="username" class="form-control" required>
                </div>
                <div class="form-group mb-3">
                    <label><i class="fas fa-lock"></i> Password</label>
                    <input type="password" name="password" class="form-control" required>
                </div>
                <button type="submit" class="btn btn-primary w-100">
                    <i class="fas fa-sign-in-alt"></i> Kirish
                </button>
            </form>
        </div>
    </div>
</body>
</html>
```

#### 2. Register Page (templates/register.html)
```html
<form method="post" class="login-form">
    {% csrf_token %}
    <div class="row">
        <div class="col-md-6 mb-3">
            <label>Ism</label>
            <input type="text" name="first_name" class="form-control" required>
        </div>
        <div class="col-md-6 mb-3">
            <label>Familiya</label>
            <input type="text" name="last_name" class="form-control" required>
        </div>
    </div>
    <div class="mb-3">
        <label>Username</label>
        <input type="text" name="username" class="form-control" required>
    </div>
    <div class="mb-3">
        <label>Email</label>
        <input type="email" name="email" class="form-control" required>
    </div>
    <div class="mb-3">
        <label>Parol</label>
        <input type="password" name="password1" class="form-control" required>
    </div>
    <div class="mb-3">
        <label>Parolni tasdiqlash</label>
        <input type="password" name="password2" class="form-control" required>
    </div>
    <button type="submit" class="btn btn-success w-100">
        Ro'yxatdan o'tish
    </button>
</form>
```

#### 3. Profile Page (templates/profile.html)
```html
{% extends 'base.html' %}

{% block content %}
<div class="container-fluid">
    <h2><i class="fas fa-user"></i> My Profile</h2>
    
    <div class="row">
        <div class="col-md-4">
            <!-- Avatar and info -->
            <div class="card">
                <div class="card-body text-center">
                    <img src="{% static 'img/default-avatar.png' %}" 
                         class="rounded-circle" width="150">
                    <h4>{{ user.get_full_name }}</h4>
                    <p>@{{ user.username }}</p>
                </div>
            </div>
        </div>
        
        <div class="col-md-8">
            <!-- Edit form -->
            <div class="card">
                <div class="card-header">
                    <h5>Edit Profile</h5>
                </div>
                <div class="card-body">
                    <form method="post">
                        {% csrf_token %}
                        <!-- Form fields -->
                        <button type="submit" class="btn btn-primary">
                            Save Changes
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

#### 4. Students Page (templates/students.html)
```html
{% extends 'base.html' %}

{% block content %}
<div class="container-fluid">
    <h2><i class="fas fa-users"></i> Students</h2>
    
    <!-- Statistics Cards -->
    <div class="row mb-4">
        <div class="col-md-3">
            <div class="stat-card bg-primary">
                <div class="stat-icon"><i class="fas fa-users"></i></div>
                <div class="stat-content">
                    <h3>{{ students.count }}</h3>
                    <p>Total Students</p>
                </div>
            </div>
        </div>
        <!-- More stat cards -->
    </div>
    
    <!-- Students Table -->
    <div class="card">
        <div class="card-body">
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Course</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {% for student in students %}
                    <tr>
                        <td>{{ student.student_id }}</td>
                        <td>{{ student.get_full_name }}</td>
                        <td>{{ student.email }}</td>
                        <td>{{ student.course }}-kurs</td>
                        <td>
                            <button class="btn btn-sm btn-warning">Edit</button>
                            <button class="btn btn-sm btn-danger">Delete</button>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</div>
{% endblock %}
```

#### 5. 404 Page (templates/404.html)
```html
<!DOCTYPE html>
<html>
<head>
    <title>404 - Page Not Found</title>
    <style>
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
        }
        .error-code {
            font-size: 150px;
            font-weight: bold;
            animation: bounce 2s infinite;
        }
    </style>
</head>
<body>
    <div class="error-container text-center">
        <div class="error-icon">
            <i class="fas fa-exclamation-triangle fa-5x"></i>
        </div>
        <h1 class="error-code">404</h1>
        <h2>Sahifa topilmadi!</h2>
        <a href="{% url 'profile' %}" class="btn btn-light btn-lg">
            Bosh sahifaga qaytish
        </a>
    </div>
</body>
</html>
```

**Natija:** ✅ 5 ta sahifa yaratildi va dizayn qilindi.

---

## 📝 Topshiriq 4: URL va View funksiyalari

### Vazifa
Sahifalarni ko'rsatib berish uchun url va view funksiyalarini yaratish.

### Yechim

#### 1. Views yaratish (profiles/views.py)
```python
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile


def login_page(request):
    """Login page view"""
    if request.user.is_authenticated:
        return redirect('profile')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid credentials!')
    
    return render(request, 'login.html')


def register_page(request):
    """Registration page view"""
    if request.user.is_authenticated:
        return redirect('profile')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return render(request, 'register.html')
        
        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password1
        )
        Profile.objects.create(user=user)
        
        messages.success(request, 'Registration successful!')
        return redirect('login')
    
    return render(request, 'register.html')


def logout_view(request):
    """Logout view"""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')


@login_required
def profile_page(request):
    """Profile page view"""
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email = request.POST.get('email', '')
        request.user.save()
        
        profile.bio = request.POST.get('bio', '')
        profile.phone = request.POST.get('phone', '')
        profile.address = request.POST.get('address', '')
        profile.save()
        
        messages.success(request, 'Profile updated!')
        return redirect('profile')
    
    return render(request, 'profile.html', {'profile': profile})


def custom_404(request, exception):
    """Custom 404 view"""
    return render(request, '404.html', status=404)
```

#### 2. Students Views (students/views.py)
```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student


@login_required
def students_page(request):
    """Students page view"""
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        course = request.POST.get('course')
        
        if Student.objects.filter(student_id=student_id).exists():
            messages.error(request, 'Student ID already exists!')
        else:
            Student.objects.create(
                student_id=student_id,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                course=course
            )
            messages.success(request, 'Student added successfully!')
        
        return redirect('students')
    
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})
```

#### 3. URLs yaratish (final_project/urls.py)
```python
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from profiles.views import (
    login_page, register_page, logout_view, 
    profile_page
)
from students.views import students_page

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentication
    path('', login_page, name='login'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_view, name='logout'),
    
    # Pages
    path('profile/', profile_page, name='profile'),
    path('students/', students_page, name='students'),
]

# Static files
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, 
                         document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, 
                         document_root=settings.MEDIA_ROOT)

# 404 handler
handler404 = 'profiles.views.custom_404'
```

**Natija:** ✅ Barcha views va URLs yaratildi.

---

## 📝 Topshiriq 5: Static fayllar sozlamasi

### Vazifa
Admin template'dagi static fayllar sozlamalarini amalga oshiring va sahiflarda ishlashini ta'minlang.

### Yechim

#### 1. CSS - style.css
```css
/* Sidebar Styles */
.sidebar {
    position: fixed;
    left: 0;
    top: 0;
    height: 100vh;
    width: 250px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    transition: all 0.3s;
}

.sidebar.collapsed {
    width: 70px;
}

.sidebar-menu li a {
    display: flex;
    align-items: center;
    padding: 15px 20px;
    color: white;
    text-decoration: none;
    transition: all 0.3s;
}

.sidebar-menu li a:hover {
    background-color: rgba(255, 255, 255, 0.1);
    padding-left: 30px;
}

/* Statistics Cards */
.stat-card {
    padding: 20px;
    border-radius: 10px;
    color: white;
    display: flex;
    align-items: center;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s;
}

.stat-card:hover {
    transform: translateY(-5px);
}

.stat-icon {
    font-size: 48px;
    margin-right: 20px;
    opacity: 0.8;
}
```

#### 2. CSS - auth.css
```css
body.login-page {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}

.login-card {
    background: white;
    border-radius: 15px;
    padding: 40px;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
    animation: slideUp 0.5s ease-in-out;
}

@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(50px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.login-form .form-control:focus {
    border-color: #667eea;
    box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.25);
}

.login-form .btn-primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border: none;
}

.login-form .btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 15px rgba(102, 126, 234, 0.4);
}
```

#### 3. JavaScript - script.js
```javascript
// Sidebar Toggle
document.addEventListener('DOMContentLoaded', function() {
    const sidebarToggle = document.getElementById('sidebarToggle');
    const sidebar = document.getElementById('sidebar');
    
    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener('click', function() {
            sidebar.classList.toggle('collapsed');
        });
    }

    // Auto-hide alerts
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Confirm delete
    const deleteButtons = document.querySelectorAll('[data-action="delete"]');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure?')) {
                e.preventDefault();
            }
        });
    });
});

// Table search
function searchTable(inputId, tableId) {
    const input = document.getElementById(inputId);
    const table = document.getElementById(tableId);
    const tr = table.getElementsByTagName('tr');

    input.addEventListener('keyup', function() {
        const filter = input.value.toUpperCase();
        
        for (let i = 1; i < tr.length; i++) {
            let found = false;
            const td = tr[i].getElementsByTagName('td');
            
            for (let j = 0; j < td.length; j++) {
                if (td[j]) {
                    const txtValue = td[j].textContent || td[j].innerText;
                    if (txtValue.toUpperCase().indexOf(filter) > -1) {
                        found = true;
                        break;
                    }
                }
            }
            
            tr[i].style.display = found ? '' : 'none';
        }
    });
}
```

#### 4. Settings.py - Static Configuration
```python
# Static files
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

#### 5. URLs.py - Static in Development
```python
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, 
                         document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, 
                         document_root=settings.MEDIA_ROOT)
```

#### 6. Template'larda ishlatish
```html
{% load static %}

<!-- CSS -->
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<link rel="stylesheet" href="{% static 'css/auth.css' %}">

<!-- JavaScript -->
<script src="{% static 'js/script.js' %}"></script>

<!-- Images -->
<img src="{% static 'img/default-avatar.png' %}" alt="Avatar">
```

**Natija:** ✅ Static files sozlandi va ishlayapti.

---

## 🎯 Barcha Topshiriqlar Yakunlandi!

### ✅ Checklist
- [x] Loyiha va ilovalar yaratildi
- [x] Admin template tanlandi va sozlandi
- [x] 5 ta sahifa yaratildi (login, register, profile, students, 404)
- [x] Views va URLs yaratildi
- [x] Static files sozlandi

### 📊 Natijalar
- **Models:** 2 (Profile, Student)
- **Views:** 6 (login, register, logout, profile, students, 404)
- **Templates:** 6 (base, login, register, profile, students, 404)
- **Static Files:** 5 (2 CSS, 1 JS, 2 img)
- **URLs:** 7 patterns

### 🚀 Ishga Tushirish
```powershell
# Migratsiyalar
python manage.py makemigrations
python manage.py migrate

# Superuser
python manage.py createsuperuser

# Server
python manage.py runserver
```

### 🌐 Test Qilish
1. http://127.0.0.1:8000/ - Login page
2. http://127.0.0.1:8000/register/ - Register page
3. http://127.0.0.1:8000/profile/ - Profile page (login required)
4. http://127.0.0.1:8000/students/ - Students page (login required)
5. http://127.0.0.1:8000/admin/ - Django admin
6. http://127.0.0.1:8000/404/ - 404 page

### 🎉 Muvaffaqiyat!

Barcha topshiriqlar muvaffaqiyatli bajarildi! Admin panel to'liq tayyor! ✨

---

**Yakuniy Loyiha**  
**Status:** ✅ Completed  
**Versiya:** 1.0  
**Sana:** 2025
