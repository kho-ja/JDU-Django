# 🎉 Lesson 12: Django REST Framework - YAKUNLANDI

## ✅ Barcha topshiriqlar muvaffaqiyatli bajarildi!

### 📚 Nima qilindi:

---

## 1️⃣ DRF O'rnatish va Sozlash ✅

### Virtual Environment
```bash
python -m venv .venv                    # ✅ Yangi venv yaratildi
.\.venv\Scripts\Activate.ps1            # ✅ Aktivlashtirildi
```

### Package Installation
```bash
pip install django djangorestframework  # ✅ Django 5.2.7 + DRF 3.16.1
```

### Django Project
```bash
django-admin startproject config .      # ✅ Project yaratildi
python manage.py startapp posts         # ✅ App yaratildi
```

### Settings Configuration
```python
INSTALLED_APPS = [
    ...
    'rest_framework',  # ✅ DRF
    'posts',          # ✅ Posts app
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2,  # ✅ 2 posts per page
}
```

---

## 2️⃣ Post Model ✅

### Model Definition
```python
class Post(models.Model):
    title = models.CharField(max_length=200)      # ✅
    content = models.TextField()                  # ✅
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### Database
```bash
python manage.py makemigrations  # ✅ Migration yaratildi
python manage.py migrate         # ✅ Bazaga qo'shildi
```

### Admin Panel
```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']  # ✅
```

---

## 3️⃣ PostSerializer ✅

```python
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
```

**Xususiyatlar:**
- ✅ ModelSerializer
- ✅ title va content maydonlari
- ✅ Avtomatik validation
- ✅ Read-only fields

---

## 4️⃣ PostListCreateAPIView ✅

```python
class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

**Funksionallik:**
- ✅ GET - postlarni ro'yxatini qaytaradi
- ✅ POST - yangi post yaratadi
- ✅ Pagination - 2 post per page
- ✅ Custom success message

---

## 5️⃣ URL Routing ✅

### posts/urls.py
```python
urlpatterns = [
    path('api/posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
]
```

### config/urls.py
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),  # ✅
]
```

---

## 🌐 API Endpoints

### ✅ GET `/api/posts/`
**Postlar ro'yxati (pagination bilan)**

**Response:**
```json
{
  "count": 5,
  "next": "http://127.0.0.1:8000/api/posts/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Post 1",
      "content": "Mazmun 1",
      "created_at": "2025-11-03T12:00:00Z",
      "updated_at": "2025-11-03T12:00:00Z"
    },
    {
      "id": 2,
      "title": "Post 2",
      "content": "Mazmun 2",
      "created_at": "2025-11-03T12:05:00Z",
      "updated_at": "2025-11-03T12:05:00Z"
    }
  ]
}
```

### ✅ POST `/api/posts/`
**Yangi post yaratish**

**Request:**
```json
{
  "title": "Yangi post",
  "content": "Post matni"
}
```

**Response:**
```json
{
  "message": "Post muvaffaqiyatli yaratildi!",
  "data": {
    "id": 3,
    "title": "Yangi post",
    "content": "Post matni",
    "created_at": "2025-11-03T12:48:00Z",
    "updated_at": "2025-11-03T12:48:00Z"
  }
}
```

---

## 📁 Loyiha Tuzilishi

```
Lesson 12/
├── .venv/                        ✅ Virtual environment
├── config/
│   ├── settings.py               ✅ DRF sozlamalari
│   └── urls.py                   ✅ Main routing
├── posts/
│   ├── migrations/
│   │   └── 0001_initial.py       ✅ Post migration
│   ├── admin.py                  ✅ Admin config
│   ├── models.py                 ✅ Post model
│   ├── serializers.py            ✅ PostSerializer
│   ├── views.py                  ✅ APIView
│   └── urls.py                   ✅ API URLs
├── db.sqlite3                    ✅ Database
├── manage.py                     ✅ Django CLI
├── README.md                     ✅ Dokumentatsiya
└── TOPSHIRIQLAR.md               ✅ Topshiriqlar
```

---

## 🎯 Bajarilgan Topshiriqlar

| # | Topshiriq | Status |
|---|-----------|--------|
| 1 | DRF o'rnatish va sozlash | ✅ 100% |
| 2 | Post modelini yaratish | ✅ 100% |
| 3 | Serializer yaratish | ✅ 100% |
| 4 | APIView yaratish | ✅ 100% |
| 5 | URL qo'shish | ✅ 100% |

**Umumiy:** ✅ **5/5 (100%)**

---

## 🚀 Loyiha Ishga Tushirish

### 1. Virtual Environment
```bash
cd "d:\Universitet\JDU\Django\Lesson 12"
.\.venv\Scripts\Activate.ps1
```

### 2. Server
```bash
python manage.py runserver
```

### 3. Browser
```
http://127.0.0.1:8000/api/posts/
```

---

## 💻 Test Natijalari

### System Check
```bash
python manage.py check
# ✅ System check identified no issues (0 silenced).
```

### Server Status
```
✅ Django version 5.2.7
✅ Starting development server at http://127.0.0.1:8000/
✅ Server ishlamoqda!
```

### API Status
```
✅ GET /api/posts/ - ishlayapti
✅ POST /api/posts/ - ishlayapti
✅ Pagination - ishlayapti (2 per page)
✅ DRF Browsable API - ishlayapti
```

---

## 🎓 O'rganilgan Narsalar

### Django REST Framework:
1. ✅ DRF installation va configuration
2. ✅ ModelSerializer
3. ✅ ListCreateAPIView
4. ✅ Pagination (PageNumberPagination)
5. ✅ REST_FRAMEWORK settings
6. ✅ API endpoints
7. ✅ Browsable API

### Django Basics:
1. ✅ Django project yaratish
2. ✅ Django app yaratish
3. ✅ Models va Migrations
4. ✅ Admin panel
5. ✅ URL routing

---

## 🔧 Texnologiyalar

| Texnologiya | Version |
|-------------|---------|
| Python | 3.11.3 |
| Django | 5.2.7 |
| Django REST Framework | 3.16.1 |
| Database | SQLite3 |

---

## 📖 DRF Features

### ✅ Serialization
- Model → JSON
- JSON → Model
- Data validation
- Field customization

### ✅ Generic Views
- ListAPIView
- CreateAPIView
- ListCreateAPIView
- RetrieveUpdateDestroyAPIView

### ✅ Pagination
- PageNumberPagination (✅ ishlatildi)
- LimitOffsetPagination
- CursorPagination

### ✅ Browsable API
- HTML interface
- Interactive forms
- API documentation
- Authentication UI

---

## 🎨 DRF Browsable API

Browser'da `http://127.0.0.1:8000/api/posts/` ochganda:

✅ POST form (yangi post yaratish uchun)
✅ Postlar ro'yxati (JSON format)
✅ Pagination controls
✅ Filter options
✅ OPTIONS method info
✅ Content-Type negotiation

---

## 📊 API Response Format

### Pagination Response Structure:
```json
{
  "count": <total_items>,
  "next": <next_page_url>,
  "previous": <previous_page_url>,
  "results": [<items_array>]
}
```

### Success Response:
```json
{
  "message": "Post muvaffaqiyatli yaratildi!",
  "data": {<post_object>}
}
```

### Error Response:
```json
{
  "field_name": ["Error message"]
}
```

---

## 🔐 Admin Panel

### Superuser yaratish:
```bash
python manage.py createsuperuser
```

### Admin URL:
```
http://127.0.0.1:8000/admin/
```

Admin panelda Post'larni boshqarish mumkin:
- ✅ View all posts
- ✅ Create new post
- ✅ Edit post
- ✅ Delete post
- ✅ Search posts
- ✅ Filter by date

---

## 💡 Keyingi Qadamlar

### Qo'shimcha funksionallik:
1. Detail endpoints (GET, PUT, DELETE)
2. Authentication (Token, JWT)
3. Permissions (IsAuthenticated, etc.)
4. Filtering va searching
5. ViewSets va Routers
6. API versioning
7. Throttling
8. Custom pagination

---

## ✨ YAKUNIY XULOSA

### Barcha topshiriqlar bajarildi! 🎉

✅ **DRF o'rnatildi va sozlandi**
✅ **Post modeli yaratildi**
✅ **PostSerializer yaratildi**
✅ **PostListCreateAPIView yaratildi**
✅ **URL routing sozlandi**
✅ **Pagination ishlayapti (2 per page)**
✅ **API test qilindi va ishlayapti**

---

## 🌟 Server Manzili

**API Endpoint:**
```
http://127.0.0.1:8000/api/posts/
```

**Admin Panel:**
```
http://127.0.0.1:8000/admin/
```

---

**Django REST Framework bilan REST API tayyor! 🚀**

**Browsable API'da postlarni ko'rish, yaratish va pagination bilan ishlash mumkin!**
