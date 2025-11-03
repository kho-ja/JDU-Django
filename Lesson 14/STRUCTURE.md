# 📁 Lesson 14 - Project Structure

## 🎯 Yakuniy Loyiha (Final Project) - Admin Panel

```
Lesson 14/
│
├── 📄 manage.py                    # Django boshqaruv skripti
├── 📄 db.sqlite3                   # SQLite ma'lumotlar bazasi
├── 📄 requirements.txt             # Python dependencies
├── 📄 README.md                    # Asosiy hujjat
├── 📄 TOPSHIRIQLAR.md             # Topshiriqlar yechimi
├── 📄 SUMMARY.md                   # Loyiha xulosasi
├── 📄 STRUCTURE.md                 # Bu fayl
│
├── 📂 final_project/               # Asosiy loyiha konfiguratsiyasi
│   ├── __init__.py
│   ├── asgi.py                    # ASGI konfiguratsiya
│   ├── wsgi.py                    # WSGI konfiguratsiya
│   ├── settings.py                # Django sozlamalari
│   └── urls.py                    # Asosiy URL marshrutlar
│
├── 📂 profiles/                    # Foydalanuvchi profillari app
│   ├── __init__.py
│   ├── admin.py                   # Admin panel sozlamalari
│   ├── apps.py                    # App konfiguratsiyasi
│   ├── models.py                  # Profile modeli
│   ├── views.py                   # 6 ta view funksiya
│   ├── tests.py                   # Test fayllar
│   └── migrations/                # Ma'lumotlar bazasi migratsiyalar
│       └── 0001_initial.py
│
├── 📂 students/                    # Talabalar boshqaruvi app
│   ├── __init__.py
│   ├── admin.py                   # Admin panel sozlamalari
│   ├── apps.py                    # App konfiguratsiyasi
│   ├── models.py                  # Student modeli
│   ├── views.py                   # CRUD operatsiyalar
│   ├── tests.py                   # Test fayllar
│   └── migrations/                # Ma'lumotlar bazasi migratsiyalar
│       └── 0001_initial.py
│
├── 📂 templates/                   # HTML shablonlar
│   ├── base.html                  # Asosiy shablon (sidebar + navbar)
│   ├── login.html                 # Login sahifasi
│   ├── register.html              # Ro'yxatdan o'tish
│   ├── profile.html               # Profil sahifasi
│   ├── students.html              # Talabalar ro'yxati
│   └── 404.html                   # Xato sahifasi
│
├── 📂 static/                      # Statik fayllar
│   ├── css/
│   │   ├── style.css              # Asosiy CSS (3.7KB)
│   │   └── auth.css               # Login/Register CSS (2.2KB)
│   ├── js/
│   │   └── script.js              # JavaScript (3.5KB)
│   └── img/
│       └── default-avatar.png     # Standart avatar
│
├── 📂 media/                       # Foydalanuvchi yuklagan fayllar
│   └── avatars/                   # Profil rasmlari
│
└── 📂 .venv/                       # Virtual environment
    ├── Lib/
    │   └── site-packages/         # O'rnatilgan paketlar
    └── Scripts/
        └── python.exe             # Python interpretator
```

## 🔧 Komponentlar Tafsiloti

### 1. **final_project/** - Asosiy Sozlamalar
| Fayl | Vazifasi | Asosiy Sozlamalar |
|------|----------|------------------|
| `settings.py` | Django konfiguratsiyasi | Apps, Templates, Static, Media, Database |
| `urls.py` | URL marshrutlash | 7 ta URL pattern + 404 handler |

### 2. **profiles/** - Autentifikatsiya & Profillar
| Fayl | Vazifasi | Funktsiyalar |
|------|----------|--------------|
| `models.py` | Ma'lumotlar strukturasi | Profile(user, bio, avatar, phone, address, birth_date) |
| `views.py` | Business logika | login_page, register_page, logout_view, profile_page, custom_404 |
| `admin.py` | Admin panel | ProfileAdmin (list_display, search_fields) |

### 3. **students/** - Talabalar Boshqaruvi
| Fayl | Vazifasi | Funktsiyalar |
|------|----------|--------------|
| `models.py` | Ma'lumotlar strukturasi | Student(first_name, last_name, email, phone, student_id, course) |
| `views.py` | CRUD operatsiyalar | students_page (list + create) |
| `admin.py` | Admin panel | StudentAdmin (filters, search, list_display) |

### 4. **templates/** - Frontend Sahifalar
| Shablon | Turi | Maqsadi |
|---------|------|---------|
| `base.html` | Layout | Sidebar + Navbar + Content area |
| `login.html` | Standalone | Autentifikatsiya |
| `register.html` | Standalone | Ro'yxatdan o'tish |
| `profile.html` | Extends base | Profil ko'rish/tahrirlash |
| `students.html` | Extends base | Talabalar ro'yxati + CRUD |
| `404.html` | Standalone | Xato sahifasi |

### 5. **static/** - Frontend Resurslari
| Fayl | Hajmi | Maqsadi |
|------|-------|---------|
| `style.css` | 3.7KB | Asosiy dizayn (sidebar, cards, tables) |
| `auth.css` | 2.2KB | Login/Register gradient dizayn |
| `script.js` | 3.5KB | Sidebar toggle, alerts, search |
| `default-avatar.png` | 2KB | Standart avatar rasmi |

## 📦 Dependencies (requirements.txt)

```
asgiref==3.10.0          # ASGI utils
Django==5.2.7            # Web framework
pillow==12.0.0           # Image processing
sqlparse==0.5.3          # SQL parser
tzdata==2025.2           # Timezone data
```

## 🗄️ Ma'lumotlar Bazasi

### Jadvallar:
1. **auth_user** - Django foydalanuvchilari (built-in)
2. **profiles_profile** - Foydalanuvchi profillari
3. **students_student** - Talabalar ma'lumotlari

### Migratsiyalar:
- 18 ta Django built-in migratsiya (auth, admin, contenttypes, sessions)
- 1 ta profiles.0001_initial migratsiya
- 1 ta students.0001_initial migratsiya

## 🌐 URL Strukturasi

```
/                        → login_page (GET/POST)
/register/               → register_page (GET/POST)
/logout/                 → logout_view
/profile/                → profile_page (@login_required)
/students/               → students_page (@login_required)
/admin/                  → Django admin panel
/static/<path>           → Statik fayllar
/media/<path>            → Yuklangan fayllar
404                      → custom_404 handler
```

## 👤 Test Ma'lumotlari

### Superuser:
- **Username:** admin
- **Password:** admin123

### Sample Students:
| ID | Ism | Email | Telefon | Kurs |
|----|-----|-------|---------|------|
| 2024001 | Ali Valiyev | ali@test.uz | +998901234567 | 1 |
| 2024002 | Dilnoza Karimova | dilnoza@test.uz | +998901234568 | 2 |
| 2024003 | Bobur Rahimov | bobur@test.uz | +998901234569 | 3 |

## 🎨 Dizayn Xususiyatlari

### Color Scheme:
- **Primary:** #667eea (Purple)
- **Secondary:** #764ba2 (Blue)
- **Success:** #10b981
- **Danger:** #ef4444
- **Warning:** #f59e0b
- **Info:** #3b82f6

### UI Components:
- ✅ Collapsible Sidebar
- ✅ Responsive Navbar
- ✅ Statistics Cards with icons
- ✅ Data Tables with search
- ✅ Modal Forms
- ✅ Auto-hide Alerts
- ✅ Smooth Animations
- ✅ Mobile-responsive

## 🚀 Ishga Tushirish

```powershell
# 1. Virtual environment aktivlashtirish
.\.venv\Scripts\Activate.ps1

# 2. Dependencies o'rnatish
pip install -r requirements.txt

# 3. Migratsiyalar qo'llash
python manage.py migrate

# 4. Superuser yaratish
python manage.py createsuperuser

# 5. Serverni ishga tushirish
python manage.py runserver

# 6. Brauzerda ochish
http://127.0.0.1:8000/
```

## ✅ Topshiriqlar Holati

| # | Topshiriq | Status | Izoh |
|---|-----------|--------|------|
| 1 | final_project yaratish | ✅ | profiles va students apps bilan |
| 2 | Admin shablon tanlash | ✅ | Bootstrap 5 gradient dizayn |
| 3 | Sahifalar yaratish | ✅ | 6 ta sahifa (base + 5 page) |
| 4 | URLs va views | ✅ | 7 ta URL pattern + 6 views |
| 5 | Statik fayllar | ✅ | CSS, JS, images + CDN |

## 📊 Statistika

- **Jami Fayllar:** 43 ta
- **Jami Qatorlar:** ~1,500 qator kod
- **Apps:** 2 ta (profiles, students)
- **Models:** 2 ta (Profile, Student)
- **Views:** 6 ta funksiya
- **Templates:** 6 ta HTML
- **CSS:** 2 ta fayl (5.9KB)
- **JavaScript:** 1 ta fayl (3.5KB)
- **Migratsiyalar:** 20 ta
- **URL Patterns:** 7 ta

---

**Yaratilgan sana:** 2025
**Mualliflar:** [Sizning ismingiz]
**Versiya:** 1.0.0
**Framework:** Django 5.2.7
