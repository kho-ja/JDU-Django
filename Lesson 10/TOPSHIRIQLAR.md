# 🎯 LESSON 10 - TOPSHIRIQLAR VA YECHIMLAR

## 📝 Topshiriqlar ro'yxati

1. ✅ Django loyihangizga CSS faylini qo'shing va "JDU talabalari" so'zini qalin, italic, rangli ko'rsating
2. ✅ JavaScript faylini yaratib onclick metodidan foydalanib form ma'lumotini consolga chiqaring
3. ✅ Talabalarning shaxsiy rasmlarini Django template'da ko'rsating
4. ✅ Video faylni static/videos papkasidan olib ko'rsating

---

## 📝 TOPSHIRIQ 1: CSS fayl qo'shish

### Talablar:
- Django loyihaga CSS fayl qo'shish
- Static fayllarni sozlash
- "JDU talabalari" so'zini:
  - Qalin shrift (bold)
  - Italic
  - Rangli

### ✅ Yechim:

#### 1. Static papka yaratish

```
Lesson 10/
└── static/
    └── css/
        └── style.css
```

#### 2. settings.py sozlash

```python
# config/settings.py

# Static files sozlamalari
STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

#### 3. CSS fayl yaratish

**File:** `static/css/style.css`

```css
/* JDU talabalari styling */
.jdu-students {
    font-weight: bold;           /* ⭐ Qalin shrift */
    font-style: italic;          /* ⭐ Italic */
    color: #FF6B6B;             /* ⭐ Rangli */
    font-size: 2.5rem;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    
    /* Gradient animation */
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: gradientShift 3s ease infinite;
}

@keyframes gradientShift {
    0%, 100% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
}
```

#### 4. Template'da ishlatish

```django
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <!-- CSS faylni ulash -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <!-- JDU talabalari so'zi -->
    <span class="jdu-students">JDU talabalari</span>
</body>
</html>
```

### Natija:
✅ "JDU talabalari" qalin, italic va rangli (gradient animatsiya bilan) ko'rsatildi

---

## 📝 TOPSHIRIQ 2: JavaScript onclick metodi

### Talablar:
- JavaScript fayl yaratish
- onclick metodidan foydalanish
- Form ma'lumotini olish
- Console'ga chiqarish

### ✅ Yechim:

#### 1. Static JS papka yaratish

```
static/
└── js/
    └── main.js
```

#### 2. JavaScript fayl yaratish

**File:** `static/js/main.js`

```javascript
console.log("🚀 main.js loaded successfully!");

/**
 * Form ma'lumotlarini consolga chiqarish
 */
function submitForm(event) {
    // Default submit'ni to'xtatish
    event.preventDefault();
    
    console.log("\n" + "=".repeat(50));
    console.log("📝 FORM MA'LUMOTLARI");
    console.log("=".repeat(50));
    
    // Form elementlaridan ma'lumot olish
    const firstName = document.getElementById("firstName").value;
    const lastName = document.getElementById("lastName").value;
    const email = document.getElementById("email").value;
    const studentId = document.getElementById("studentId").value;
    const course = document.getElementById("course").value;
    
    // Consolga chiqarish
    console.log("👤 Ism:", firstName);
    console.log("👤 Familiya:", lastName);
    console.log("📧 Email:", email);
    console.log("🎓 Talaba ID:", studentId);
    console.log("📚 Kurs:", course);
    console.log("⏰ Vaqt:", new Date().toLocaleString());
    
    // Object sifatida
    const formData = {
        firstName: firstName,
        lastName: lastName,
        email: email,
        studentId: studentId,
        course: course,
        timestamp: new Date().toISOString()
    };
    
    console.log("\n📦 Form Data Object:");
    console.table(formData);
    
    console.log("=".repeat(50) + "\n");
    
    // Success alert
    alert(`✅ Form ma'lumotlari consolga chiqarildi!\n\nIsm: ${firstName} ${lastName}\nEmail: ${email}`);
}

/**
 * Button click handler
 */
function handleButtonClick() {
    console.log("🔘 Button bosildi!");
    console.log(`⏰ Click vaqti: ${new Date().toLocaleTimeString()}`);
    alert("Button bosildi! Console'ni tekshiring (F12)");
}
```

#### 3. Template'da HTML form

```django
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Form Demo</title>
</head>
<body>
    <!-- Form with onclick -->
    <form id="studentForm" onsubmit="submitForm(event)">
        <input type="text" id="firstName" placeholder="Ism" required>
        <input type="text" id="lastName" placeholder="Familiya" required>
        <input type="email" id="email" placeholder="Email" required>
        <input type="text" id="studentId" placeholder="Talaba ID">
        <select id="course">
            <option value="">Kurs tanlang</option>
            <option value="1-kurs">1-kurs</option>
            <option value="2-kurs">2-kurs</option>
            <option value="3-kurs">3-kurs</option>
            <option value="4-kurs">4-kurs</option>
        </select>
        
        <button type="submit">📤 Yuborish</button>
        <button type="button" onclick="handleButtonClick()">🔘 Test Button</button>
    </form>
    
    <!-- JavaScript faylni ulash -->
    <script src="{% static 'js/main.js' %}"></script>
</body>
</html>
```

### Console Output:

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

📦 Form Data Object:
┌───────────┬────────────────────────────┐
│  (index)  │          Values            │
├───────────┼────────────────────────────┤
│ firstName │        'Alisher'           │
│ lastName  │        'Aliyev'            │
│   email   │     'alisher@jdu.uz'       │
│ studentId │      'JDU2024001'          │
│  course   │        '3-kurs'            │
│ timestamp │ '2025-10-27T11:30:45.123Z' │
└───────────┴────────────────────────────┘
==================================================
```

### Natija:
✅ Form ma'lumotlari console'ga chop etildi
✅ console.log() va console.table() ishlatildi
✅ onclick metodi ishladi

---

## 📝 TOPSHIRIQ 3: Talabalar rasmlari

### Talablar:
- static/images papkasi yaratish
- Talabalar shaxsiy rasmlarini qo'shish
- Django template'da ko'rsatish
- {% static %} tag ishlatish

### ✅ Yechim:

#### 1. Images papka yaratish

```
static/
└── images/
    ├── student1.jpg
    ├── student2.jpg
    └── student3.jpg
```

#### 2. View'da context

**File:** `accounts/views.py`

```python
def static_demo_view(request):
    context = {
        'students': [
            {
                'id': 1,
                'first_name': 'Alisher',
                'last_name': 'Aliyev',
                'email': 'alisher@jdu.uz',
                'student_id': 'JDU2024001',
                'course': '3-kurs',
                'image': 'images/student1.jpg',  # ⭐ Static image path
            },
            {
                'id': 2,
                'first_name': 'Zarina',
                'last_name': 'Karimova',
                'email': 'zarina@jdu.uz',
                'student_id': 'JDU2024002',
                'course': '2-kurs',
                'image': 'images/student2.jpg',
            },
            {
                'id': 3,
                'first_name': 'Jasur',
                'last_name': 'Tursunov',
                'email': 'jasur@jdu.uz',
                'student_id': 'JDU2024003',
                'course': '4-kurs',
                'image': 'images/student3.jpg',
            },
        ]
    }
    return render(request, 'static_demo.html', context)
```

#### 3. Template'da ko'rsatish

```django
{% load static %}

<h2>📝 Topshiriq 3: Talabalarning rasmlari</h2>

{% for student in students %}
<div class="student-profile">
    <!-- ⭐ Static image with {% static %} tag -->
    <img 
        src="{% static student.image %}" 
        alt="{{ student.first_name }} {{ student.last_name }}"
        class="student-image"
        onerror="this.src='https://ui-avatars.com/api/?name={{ student.first_name }}+{{ student.last_name }}&size=150'"
    >
    
    <div class="student-info">
        <div class="student-name">
            {{ student.first_name }} {{ student.last_name }}
        </div>
        <div class="student-details">
            <p>📧 Email: {{ student.email }}</p>
            <p>🎓 ID: {{ student.student_id }}</p>
            <p>📚 Kurs: {{ student.course }}</p>
        </div>
    </div>
</div>
{% endfor %}
```

#### 4. CSS styling

```css
.student-profile {
    display: flex;
    align-items: center;
    gap: 20px;
    padding: 20px;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    border-radius: 15px;
    margin-bottom: 20px;
}

.student-image {
    width: 150px;
    height: 150px;
    border-radius: 50%;           /* Doira shakli */
    object-fit: cover;            /* Rasmni to'g'ri crop qilish */
    border: 5px solid white;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.student-info {
    flex: 1;
}

.student-name {
    font-size: 1.8rem;
    font-weight: bold;
    color: #333;
    margin-bottom: 5px;
}

.student-details {
    color: #666;
    font-size: 1.1rem;
}
```

### Natija:
✅ Har bir talaba rasmi bilan ko'rsatildi
✅ Doira shaklidagi (circle) rasm
✅ Fallback avatar agar rasm yo'q bo'lsa

---

## 📝 TOPSHIRIQ 4: Video fayl ko'rsatish

### Talablar:
- static/videos papkasi yaratish
- Video fayl qo'shish
- Template'da ko'rsatish
- HTML5 video tag ishlatish

### ✅ Yechim:

#### 1. Videos papka yaratish

```
static/
└── videos/
    └── demo.mp4
```

#### 2. View'da video context

**File:** `accounts/views.py`

```python
def static_demo_view(request):
    context = {
        'video': {
            'title': 'JDU Ta\'lim Tizimi - Tanishtiruv Videosi',
            'path': 'videos/demo.mp4',  # ⭐ Static video path
            'description': 'Jizzax Davlat Universiteti haqida qisqacha ma\'lumot',
        }
    }
    return render(request, 'static_demo.html', context)
```

#### 3. Template'da video ko'rsatish

```django
{% load static %}

<h2>📝 Topshiriq 4: Video fayl ko'rsatish</h2>

<h3 class="video-title">{{ video.title }}</h3>
<p>{{ video.description }}</p>

<div class="video-container">
    <!-- ⭐ HTML5 video tag with static file -->
    <video 
        class="video-player" 
        controls 
        poster="https://via.placeholder.com/800x450/667eea/ffffff?text=JDU+Video"
    >
        <source src="{% static video.path %}" type="video/mp4">
        <p>Sizning browseringiz video'ni qo'llab-quvvatlamaydi.</p>
    </video>
</div>
```

**Video attributes:**
- `controls` - Play, pause, volume button'lari
- `poster` - Video yuklanmadan ko'rinadigan thumbnail
- `type="video/mp4"` - Video format
- Fallback `<p>` tag browser support bo'lmasa

#### 4. CSS styling

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

.video-title {
    text-align: center;
    color: #333;
    font-size: 1.5rem;
    margin-bottom: 15px;
    font-weight: 600;
}
```

#### 5. Qo'shimcha video xususiyatlari

```django
<!-- Autoplay -->
<video controls autoplay>
    <source src="{% static 'videos/demo.mp4' %}" type="video/mp4">
</video>

<!-- Loop -->
<video controls loop>
    <source src="{% static 'videos/demo.mp4' %}" type="video/mp4">
</video>

<!-- Muted -->
<video controls muted>
    <source src="{% static 'videos/demo.mp4' %}" type="video/mp4">
</video>

<!-- Preload -->
<video controls preload="metadata">
    <source src="{% static 'videos/demo.mp4' %}" type="video/mp4">
</video>
```

### Natija:
✅ Video HTML5 player bilan ko'rsatildi
✅ Play/pause/volume controls mavjud
✅ Poster image ko'rsatildi
✅ Responsive design

---

## 📊 Barcha topshiriqlar - Umumiy kod

### Complete View

**File:** `accounts/views.py`

```python
from django.shortcuts import render

def static_demo_view(request):
    """
    Static Files Demo sahifasi
    Barcha 4 topshiriqni ko'rsatadi
    """
    context = {
        'page_title': 'Django Static Files Demo',
        
        # Topshiriq 3: Students data
        'students': [
            {
                'id': 1,
                'first_name': 'Alisher',
                'last_name': 'Aliyev',
                'email': 'alisher@jdu.uz',
                'student_id': 'JDU2024001',
                'course': '3-kurs',
                'image': 'images/student1.jpg',
            },
            {
                'id': 2,
                'first_name': 'Zarina',
                'last_name': 'Karimova',
                'email': 'zarina@jdu.uz',
                'student_id': 'JDU2024002',
                'course': '2-kurs',
                'image': 'images/student2.jpg',
            },
            {
                'id': 3,
                'first_name': 'Jasur',
                'last_name': 'Tursunov',
                'email': 'jasur@jdu.uz',
                'student_id': 'JDU2024003',
                'course': '4-kurs',
                'image': 'images/student3.jpg',
            },
        ],
        
        # Topshiriq 4: Video data
        'video': {
            'title': 'JDU Ta\'lim Tizimi - Tanishtiruv Videosi',
            'path': 'videos/demo.mp4',
            'description': 'Jizzax Davlat Universiteti haqida qisqacha ma\'lumot',
        }
    }
    
    return render(request, 'static_demo.html', context)
```

### Complete Template

**File:** `templates/static_demo.html`

```django
{% load static %}
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page_title }}</title>
    
    <!-- ⭐ TOPSHIRIQ 1: CSS -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <div class="container">
        <div class="main-container">
            <h1>🎓 Lesson 10: Django Static Files</h1>
            
            <!-- ⭐ TOPSHIRIQ 1: Styled text -->
            <div class="text-center">
                <span class="jdu-students">JDU talabalari</span>
            </div>
            
            <!-- ⭐ TOPSHIRIQ 2: Form with JavaScript -->
            <div class="card">
                <h2>📝 Topshiriq 2: JavaScript Form</h2>
                <form id="studentForm" onsubmit="submitForm(event)">
                    <input type="text" id="firstName" placeholder="Ism" required>
                    <input type="text" id="lastName" placeholder="Familiya" required>
                    <input type="email" id="email" placeholder="Email" required>
                    <button type="submit">Yuborish</button>
                </form>
            </div>
            
            <!-- ⭐ TOPSHIRIQ 3: Student Images -->
            <div class="card">
                <h2>📝 Topshiriq 3: Talabalar Rasmlari</h2>
                {% for student in students %}
                <div class="student-profile">
                    <img 
                        src="{% static student.image %}" 
                        alt="{{ student.first_name }}"
                        class="student-image"
                    >
                    <div class="student-info">
                        <div class="student-name">
                            {{ student.first_name }} {{ student.last_name }}
                        </div>
                        <p>📧 {{ student.email }}</p>
                        <p>🎓 {{ student.student_id }}</p>
                    </div>
                </div>
                {% endfor %}
            </div>
            
            <!-- ⭐ TOPSHIRIQ 4: Video -->
            <div class="card">
                <h2>📝 Topshiriq 4: Video</h2>
                <h3>{{ video.title }}</h3>
                <div class="video-container">
                    <video class="video-player" controls>
                        <source src="{% static video.path %}" type="video/mp4">
                    </video>
                </div>
            </div>
        </div>
    </div>
    
    <!-- ⭐ TOPSHIRIQ 2: JavaScript -->
    <script src="{% static 'js/main.js' %}"></script>
</body>
</html>
```

### URLs Configuration

**File:** `accounts/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.static_demo_view, name="home"),
    path("static-demo/", views.static_demo_view, name="static_demo"),
    # ... other URLs
]
```

---

## 🧪 Test va Natijalar

### Test 1: CSS Styling
**URL:** http://127.0.0.1:8000/
**Ko'rish:** "JDU talabalari" rangli, qalin va italic

### Test 2: JavaScript Console
**Amallar:**
1. Formani to'ldiring
2. "Yuborish" ni bosing
3. F12 (Developer Tools) oching
4. Console tab'ni tanlang
5. Form ma'lumotlarini ko'ring

### Test 3: Student Images
**Ko'rish:** 
- Alisher Aliyev rasmi
- Zarina Karimova rasmi
- Jasur Tursunov rasmi

### Test 4: Video Player
**Amallar:**
1. Video player ko'ring
2. Play tugmasini bosing
3. Volume sozlang
4. Fullscreen mode

---

## 📁 Final Project Structure

```
Lesson 10/
├── static/                         # ⭐ Static files root
│   ├── css/
│   │   └── style.css              # ⭐ Task 1
│   ├── js/
│   │   └── main.js                # ⭐ Task 2
│   ├── images/
│   │   ├── student1.jpg           # ⭐ Task 3
│   │   ├── student2.jpg
│   │   └── student3.jpg
│   └── videos/
│       └── demo.mp4               # ⭐ Task 4
├── templates/
│   └── static_demo.html           # Main demo page
├── accounts/
│   ├── views.py                   # static_demo_view
│   └── urls.py                    # URL patterns
├── config/
│   └── settings.py                # STATIC_URL, STATICFILES_DIRS
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 🎯 Xulosa

Lesson 10'da barcha 4 topshiriq muvaffaqiyatli bajarildi:

| # | Topshiriq | Status | File |
|---|-----------|--------|------|
| 1 | CSS - JDU talabalari styling | ✅ | static/css/style.css |
| 2 | JavaScript - onclick console | ✅ | static/js/main.js |
| 3 | Images - Student photos | ✅ | static/images/*.jpg |
| 4 | Video - Demo video | ✅ | static/videos/demo.mp4 |

**Barcha topshiriqlar 100% bajarildi!** 🎉

---

**Lesson 10 - Django Static Files**
*27-Oktabr, 2025*
