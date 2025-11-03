# 10-DARS: DJANGO STATIC FILES

## ✅ Bajarilgan topshiriqlar

### 1. ✅ CSS fayl qo'shish va "JDU talabalari" styling
**File:** `static/css/style.css`

"JDU talabalari" so'zi quyidagi stillar bilan ko'rsatildi:
- **Bold (Qalin shrift):** `font-weight: bold;`
- **Italic:** `font-style: italic;`
- **Rangli:** Gradient animation bilan rangli ko'rinish

```css
.jdu-students {
    font-weight: bold;           /* Qalin shrift */
    font-style: italic;          /* Italic */
    color: #FF6B6B;             /* Rangli */
    font-size: 2.5rem;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: gradientShift 3s ease infinite;
}
```

### 2. ✅ JavaScript onclick metodi
**File:** `static/js/main.js`

Form ma'lumotlarini consolga chiqaruvchi funksiya yaratildi:

```javascript
function submitForm(event) {
    event.preventDefault();
    
    // Form ma'lumotlarini olish
    const firstName = document.getElementById("firstName").value;
    const lastName = document.getElementById("lastName").value;
    const email = document.getElementById("email").value;
    
    // Consolga chiqarish
    console.log("👤 Ism:", firstName);
    console.log("👤 Familiya:", lastName);
    console.log("📧 Email:", email);
    
    // Object sifatida
    const formData = {
        firstName, lastName, email,
        timestamp: new Date().toISOString()
    };
    console.table(formData);
}
```

### 3. ✅ Talabalar rasmlari
**Folder:** `static/images/`

Template'da static tag bilan ko'rsatish:

```django
{% load static %}

<img 
    src="{% static 'images/student1.jpg' %}" 
    alt="Talaba rasmi"
    class="student-image"
>
```

**Talabalar:**
- Alisher Aliyev (JDU2024001) - 3-kurs
- Zarina Karimova (JDU2024002) - 2-kurs
- Jasur Tursunov (JDU2024003) - 4-kurs

### 4. ✅ Video fayl ko'rsatish
**Folder:** `static/videos/`
**File:** `demo.mp4`

HTML5 video tag bilan ko'rsatish:

```django
{% load static %}

<video controls>
    <source src="{% static 'videos/demo.mp4' %}" type="video/mp4">
    Sizning browseringiz video'ni qo'llab-quvvatlamaydi.
</video>
```

---

## 📂 Loyiha strukturasi

```
Lesson 10/
├── static/                        # ⭐ Static files
│   ├── css/
│   │   └── style.css             # ⭐ Task 1: CSS styling
│   ├── js/
│   │   └── main.js               # ⭐ Task 2: JavaScript
│   ├── images/
│   │   ├── student1.jpg          # ⭐ Task 3: Student images
│   │   ├── student2.jpg
│   │   └── student3.jpg
│   └── videos/
│       └── demo.mp4              # ⭐ Task 4: Video file
├── templates/
│   ├── static_demo.html          # ⭐ Main demo page
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   └── profile.html
├── accounts/
│   ├── views.py                  # ⭐ static_demo_view added
│   ├── urls.py
│   └── ...
├── config/
│   ├── settings.py               # ⭐ STATIC_URL, STATICFILES_DIRS
│   └── ...
├── db.sqlite3
└── manage.py
```

---

## ⚙️ Settings.py sozlamalari

```python
# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

# ⭐ Static files directories
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Static files root (for production - collectstatic)
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media files (user uploads)
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
```

---

## 🚀 Loyihani ishga tushirish

```bash
# 1. Lesson 10 papkasiga o'ting
cd "d:\Universitet\JDU\Django\Lesson 10"

# 2. Virtual environment faollashtiring
.\.venv\Scripts\Activate.ps1

# 3. Serverni ishga tushiring
python manage.py runserver
```

---

## 🌐 URL'lar

| Sahifa | URL | Tavsif |
|--------|-----|--------|
| Home / Static Demo | http://127.0.0.1:8000/ | Static files demo |
| Static Demo | http://127.0.0.1:8000/static-demo/ | Barcha topshiriqlar |
| Login | http://127.0.0.1:8000/login/ | Tizimga kirish |
| Register | http://127.0.0.1:8000/register/ | Ro'yxatdan o'tish |
| Profile | http://127.0.0.1:8000/profile/ | Profil |
| Admin | http://127.0.0.1:8000/admin/ | Admin panel |

---

## 🎯 Topshiriqlar detallari

### Topshiriq 1: CSS fayl qo'shish

**Maqsad:** "JDU talabalari" so'zini qalin, italic va rangli qilish

**Bajarilgan:**
1. `static/css/style.css` fayli yaratildi
2. `.jdu-students` class yaratildi
3. Quyidagi stillar qo'shildi:
   - `font-weight: bold` - Qalin shrift
   - `font-style: italic` - Italic
   - `background: linear-gradient(...)` - Rangli gradient
   - `animation: gradientShift` - Animatsiya

**Template'da ishlatish:**
```django
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">

<span class="jdu-students">JDU talabalari</span>
```

**Natija:** ✅ "JDU talabalari" qalin, italic va rangli animatsiya bilan ko'rsatildi

---

### Topshiriq 2: JavaScript onclick metodi

**Maqsad:** Form ma'lumotlarini consolga chiqarish

**Bajarilgan:**
1. `static/js/main.js` fayli yaratildi
2. `submitForm(event)` funksiyasi yaratildi
3. Form elementlaridan ma'lumot olish
4. Console'ga chiqarish
5. `console.table()` bilan object ko'rsatish

**Template'da ishlatish:**
```django
{% load static %}
<script src="{% static 'js/main.js' %}"></script>

<form onsubmit="submitForm(event)">
    <input type="text" id="firstName">
    <button type="submit">Yuborish</button>
</form>
```

**Qo'shimcha funksiyalar:**
- `handleButtonClick()` - Button click logger
- `handleInputChange(event)` - Input change logger
- `generateRandomStudent()` - Random data generator
- `fillTestData()` - Form'ni test data bilan to'ldirish
- `exportFormData()` - JSON export

**Console Output:**
```
==================================================
📝 FORM MA'LUMOTLARI
==================================================
👤 Ism: Alisher
👤 Familiya: Aliyev
📧 Email: alisher@jdu.uz
🎓 Talaba ID: JDU2024001
📚 Kurs: 3-kurs
⏰ Vaqt: 27.10.2025, 14:30:45
==================================================
```

**Natija:** ✅ Form ma'lumotlari consolga chop etildi

---

### Topshiriq 3: Talabalar rasmlari

**Maqsad:** Talabalarning shaxsiy rasmlarini ko'rsatish

**Bajarilgan:**
1. `static/images/` papkasi yaratildi
2. Student rasmlari qo'shildi:
   - `student1.jpg` - Alisher Aliyev
   - `student2.jpg` - Zarina Karimova
   - `student3.jpg` - Jasur Tursunov
3. Template'da `{% static %}` tag bilan ko'rsatildi

**Template code:**
```django
{% load static %}

{% for student in students %}
<div class="student-profile">
    <img 
        src="{% static student.image %}" 
        alt="{{ student.first_name }} {{ student.last_name }}"
        class="student-image"
        onerror="this.src='https://ui-avatars.com/api/?name={{ student.first_name }}+{{ student.last_name }}'"
    >
    <div class="student-info">
        <div class="student-name">
            {{ student.first_name }} {{ student.last_name }}
        </div>
        <p>📧 Email: {{ student.email }}</p>
        <p>🎓 ID: {{ student.student_id }}</p>
        <p>📚 Kurs: {{ student.course }}</p>
    </div>
</div>
{% endfor %}
```

**View context:**
```python
context = {
    'students': [
        {
            'first_name': 'Alisher',
            'last_name': 'Aliyev',
            'email': 'alisher@jdu.uz',
            'student_id': 'JDU2024001',
            'course': '3-kurs',
            'image': 'images/student1.jpg',
        },
        # ...
    ]
}
```

**Natija:** ✅ Har bir talaba rasmi bilan ko'rsatildi

---

### Topshiriq 4: Video fayl ko'rsatish

**Maqsad:** Video faylni static papkadan ko'rsatish

**Bajarilgan:**
1. `static/videos/` papkasi yaratildi
2. `demo.mp4` video fayli qo'shildi
3. HTML5 `<video>` tag bilan ko'rsatildi

**Template code:**
```django
{% load static %}

<div class="video-container">
    <video 
        class="video-player" 
        controls 
        poster="https://via.placeholder.com/800x450/667eea/ffffff?text=JDU+Video"
    >
        <source src="{% static 'videos/demo.mp4' %}" type="video/mp4">
        <p>Sizning browseringiz video'ni qo'llab-quvvatlamaydi.</p>
    </video>
</div>
```

**Video properties:**
- `controls` - Play/pause/volume buttons
- `poster` - Thumbnail image
- `type="video/mp4"` - Video format
- Fallback text for unsupported browsers

**CSS styling:**
```css
.video-container {
    position: relative;
    width: 100%;
    max-width: 800px;
    margin: 20px auto;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.video-player {
    width: 100%;
    height: auto;
    display: block;
}
```

**Natija:** ✅ Video HTML5 player bilan ko'rsatildi

---

## 📚 Static Files bilan ishlash

### 1. {% load static %} tag

Har bir template'da static fayllar ishlatishdan oldin:

```django
{% load static %}
```

### 2. CSS faylni ulash

```django
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

### 3. JavaScript faylni ulash

```django
<script src="{% static 'js/main.js' %}"></script>
```

### 4. Rasm ko'rsatish

```django
<img src="{% static 'images/photo.jpg' %}" alt="Photo">
```

### 5. Video ko'rsatish

```django
<video controls>
    <source src="{% static 'videos/video.mp4' %}" type="video/mp4">
</video>
```

### 6. Download link

```django
<a href="{% static 'files/document.pdf' %}" download>Download PDF</a>
```

---

## 🔧 Static Files Configuration

### Development (Debug=True)

```python
# settings.py
DEBUG = True
STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

Django avtomatik ravishda `static/` papkalardan fayllarni topadi.

### Production (Debug=False)

```bash
# Static fayllarni yig'ish
python manage.py collectstatic
```

Bu komanda barcha static fayllarni `STATIC_ROOT` ga yig'adi:

```python
# settings.py
STATIC_ROOT = BASE_DIR / "staticfiles"
```

---

## 🎨 CSS Classes

`style.css` faylida quyidagi classlar mavjud:

### Typography
- `.jdu-students` - Gradient animated text
- `.jdu-students-simple` - Simple colored text
- `.bold` - Bold text
- `.italic` - Italic text

### Layout
- `.container` - Main container
- `.main-container` - Content container
- `.grid-2` - 2-column grid
- `.text-center` - Center aligned text

### Components
- `.card` - Card component
- `.card-title` - Card title
- `.card-content` - Card content
- `.btn` - Button base
- `.btn-primary` - Primary button
- `.btn-success` - Success button
- `.btn-danger` - Danger button

### Forms
- `.form-group` - Form group
- `.form-label` - Form label
- `.form-control` - Form input/textarea/select

### Student Profile
- `.student-profile` - Student card
- `.student-image` - Student photo (150x150 circle)
- `.student-info` - Student information
- `.student-name` - Student name
- `.student-details` - Student details

### Video
- `.video-container` - Video wrapper
- `.video-player` - Video element
- `.video-title` - Video title

### Alerts
- `.alert` - Alert base
- `.alert-info` - Info alert (blue)
- `.alert-success` - Success alert (green)
- `.alert-warning` - Warning alert (yellow)

---

## 📱 Responsive Design

CSS faylida responsive media queries mavjud:

```css
@media (max-width: 768px) {
    .jdu-students {
        font-size: 1.8rem;
    }
    
    .student-profile {
        flex-direction: column;
        text-align: center;
    }
    
    .grid-2 {
        grid-template-columns: 1fr;
    }
}
```

Mobile qurilmalarda:
- Font o'lchamlari kichikroq
- Student profile vertikal
- Grid 1 column

---

## 🧪 Test

### 1. Static files ishlashini tekshirish

```bash
# Serverni ishga tushiring
python manage.py runserver

# Browser'da oching
http://127.0.0.1:8000/
```

**Tekshirish:**
- ✅ "JDU talabalari" rangli va animatsiyali ko'rinishi kerak
- ✅ Sahifa styling'i to'g'ri bo'lishi kerak
- ✅ Form button'lar ishlamasi kerak

### 2. JavaScript test

1. Formani to'ldiring
2. "Yuborish" ni bosing
3. F12 ni bosing (Developer Console)
4. Console'da form ma'lumotlari ko'rinishi kerak

**Console'da:**
```
📝 FORM MA'LUMOTLARI
👤 Ism: Alisher
👤 Familiya: Aliyev
...
```

### 3. Images test

- ✅ Har bir talaba profil rasmi ko'rinishi kerak
- ✅ Agar rasm yo'q bo'lsa, fallback avatar ko'rinishi kerak

### 4. Video test

- ✅ Video player ko'rinishi kerak
- ✅ Play/pause button'lar ishlashi kerak
- ✅ Poster image ko'rinishi kerak

---

## 💡 Best Practices

### 1. Static files organizatsiyasi

```
static/
├── css/
│   ├── style.css
│   ├── admin.css
│   └── responsive.css
├── js/
│   ├── main.js
│   ├── utils.js
│   └── validation.js
├── images/
│   ├── logo.png
│   ├── favicon.ico
│   └── students/
├── videos/
└── fonts/
```

### 2. Performance

- Minify CSS va JS files (production'da)
- Optimize images (compress)
- Use CDN for libraries (Bootstrap, jQuery)
- Lazy load images va videos

### 3. Naming conventions

```
# ✅ Yaxshi
student-profile.css
main-app.js
hero-banner.jpg

# ❌ Yomon
Style1.css
file.js
img.jpg
```

### 4. Template'da

```django
{# ✅ Yaxshi - har doim {% load static %} #}
{% load static %}
<link href="{% static 'css/style.css' %}" rel="stylesheet">

{# ❌ Yomon - hardcoded path #}
<link href="/static/css/style.css" rel="stylesheet">
```

---

## 🚀 Production Deployment

### 1. Collect static files

```bash
python manage.py collectstatic
```

### 2. Configure web server (Nginx)

```nginx
location /static/ {
    alias /path/to/staticfiles/;
}

location /media/ {
    alias /path/to/media/;
}
```

### 3. Use WhiteNoise (alternative)

```python
# settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ← Add this
    # ...
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

```bash
pip install whitenoise
```

---

## 📖 O'rganilgan kontseptsiyalar

### Django Static Files
- ✅ STATIC_URL sozlamasi
- ✅ STATICFILES_DIRS configuration
- ✅ {% load static %} template tag
- ✅ {% static %} path resolution
- ✅ collectstatic command

### CSS
- ✅ External stylesheet
- ✅ Class selectors
- ✅ Gradient backgrounds
- ✅ Animations
- ✅ Responsive design
- ✅ Flexbox va Grid layouts

### JavaScript
- ✅ External script files
- ✅ onclick event handlers
- ✅ Form data manipulation
- ✅ console.log() va console.table()
- ✅ Event preventDefault()
- ✅ DOM manipulation

### HTML5 Media
- ✅ <img> tag bilan static images
- ✅ <video> tag bilan video files
- ✅ controls attribute
- ✅ poster attribute
- ✅ Fallback content

---

## 🎯 Xulosa

**Lesson 10** da Django Static Files to'liq o'rganildi:

### ✅ Nima qildik:

1. **CSS fayl qo'shdik** - "JDU talabalari" qalin, italic, rangli
2. **JavaScript yaratdik** - onclick bilan console logging
3. **Images ko'rsatdik** - Talabalar profil rasmlari
4. **Video qo'shdik** - HTML5 player bilan video ko'rsatish

### ✅ Nima o'rgandik:

- ✅ Static files configuration (STATIC_URL, STATICFILES_DIRS)
- ✅ {% load static %} va {% static %} template tags
- ✅ CSS styling va animations
- ✅ JavaScript onclick event handlers
- ✅ HTML5 media elements (img, video)
- ✅ Responsive design
- ✅ Best practices

### ✅ Files Created:

- `static/css/style.css` (300+ lines)
- `static/js/main.js` (200+ lines)
- `static/images/` (3 student photos)
- `static/videos/demo.mp4`
- `templates/static_demo.html` (300+ lines)

---

**Keyingi darsda ko'rishamiz!** 🚀

**Lesson 10 - Django Static Files**
*27-Oktabr, 2025*
