# TOPSHIRIQLAR - Lesson 12: Django REST Framework

## 📋 Dars topshiriqlari (Barchasi bajarildi! ✅)

---

### ✅ Topshiriq 1: DRF ni o'rnatish

**Talab:**
- Django REST Framework (DRF) ni o'rnating
- `settings.py` faylida `rest_framework` sozlamasini amalga oshiring

**Bajarilgan:**

1. **Yangi virtual environment yaratildi:**
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. **Django va DRF o'rnatildi:**
```bash
pip install django djangorestframework
```

3. **INSTALLED_APPS ga qo'shildi:**
```python
INSTALLED_APPS = [
    ...
    'rest_framework',  # ✅ DRF qo'shildi
    'posts',           # ✅ Local app qo'shildi
]
```

4. **DRF sozlamalari:**
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2,  # ✅ 2 post per page (talab bo'yicha)
}
```

**Natija:** ✅ DRF muvaffaqiyatli o'rnatildi va sozlandi

---

### ✅ Topshiriq 2: Post modelini yaratish

**Talab:**
- Post nomli model yaratish
- `title` (CharField) maydoni
- `content` (TextField) maydoni
- Modelni migrations orqali bazaga qo'shish

**Bajarilgan:**

1. **Post modeli yaratildi (`posts/models.py`):**
```python
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    content = models.TextField(verbose_name="Mazmun")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created_at"]
    
    def __str__(self):
        return self.title
```

2. **Migrations yaratildi:**
```bash
python manage.py makemigrations
# Output: Migrations for 'posts':
#   posts\migrations\0001_initial.py
#     + Create model Post
```

3. **Migrations qo'llandi:**
```bash
python manage.py migrate
# Output: Applying posts.0001_initial... OK
```

4. **Admin panelda registratsiya:**
```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', 'content']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
```

**Natija:** ✅ Post modeli yaratildi va bazaga qo'shildi

---

### ✅ Topshiriq 3: Serializer yaratish

**Talab:**
- Post modelidan foydalanadigan serializer yaratish
- `title` va `content` maydonlarini qo'shish

**Bajarilgan:**

**PostSerializer yaratildi (`posts/serializers.py`):**
```python
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for Post model.
    Serializes title and content fields.
    """
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
```

**Xususiyatlar:**
- ✅ ModelSerializer ishlatildi (avtomatik field generation)
- ✅ `title` va `content` maydonlari qo'shildi
- ✅ Qo'shimcha maydonlar: `id`, `created_at`, `updated_at`
- ✅ Read-only fields belgilandi
- ✅ Avtomatik validation

**Natija:** ✅ Serializer muvaffaqiyatli yaratildi

---

### ✅ Topshiriq 4: APIView yaratish

**Talab:**
- Postlarni yaratish va ko'rish uchun APIView yaratish
- Yangi post qo'shish imkoni
- Mavjud postlarni ko'rish
- 2 tadan ko'p bo'lsa pagination bilan ko'rish

**Bajarilgan:**

**PostListCreateAPIView yaratildi (`posts/views.py`):**
```python
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    """
    API View for listing and creating posts.
    
    GET: Returns paginated list of all posts (2 per page)
    POST: Creates a new post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get(self, request, *args, **kwargs):
        """List all posts with pagination"""
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        """Create a new post"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Post muvaffaqiyatli yaratildi!",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

**Funksionallik:**
- ✅ GET method: postlarni ro'yxatini qaytaradi
- ✅ POST method: yangi post yaratadi
- ✅ Pagination avtomatik ishlaydi (2 post per page)
- ✅ Custom success message
- ✅ Error handling

**Natija:** ✅ APIView muvaffaqiyatli yaratildi

---

### ✅ Topshiriq 5: URL qo'shish

**Talab:**
- Yaratilgan APIView uchun URL qo'shish
- API'ga murojaat qilish imkonini yaratish

**Bajarilgan:**

1. **posts/urls.py yaratildi:**
```python
from django.urls import path
from .views import PostListCreateAPIView

urlpatterns = [
    path('api/posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
]
```

2. **config/urls.py ga ulandi:**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),  # ✅ Posts URLs ulandi
]
```

**Endpoint:**
- ✅ `GET /api/posts/` - postlar ro'yxati (pagination bilan)
- ✅ `POST /api/posts/` - yangi post yaratish

**Natija:** ✅ URL routing muvaffaqiyatli sozlandi

---

## 📊 Umumiy natijalar

### Yaratilgan fayllar:

```
Lesson 12/
├── .venv/                           ✅ Virtual environment
├── config/
│   ├── settings.py                  ✅ DRF sozlandi
│   └── urls.py                      ✅ Routing sozlandi
├── posts/
│   ├── migrations/
│   │   └── 0001_initial.py          ✅ Migration
│   ├── admin.py                     ✅ Admin panel
│   ├── models.py                    ✅ Post modeli
│   ├── serializers.py               ✅ PostSerializer
│   ├── views.py                     ✅ PostListCreateAPIView
│   └── urls.py                      ✅ API endpoints
├── db.sqlite3                       ✅ Database
├── manage.py                        ✅ Django CLI
└── README.md                        ✅ Dokumentatsiya
```

### Ishlatilgan texnologiyalar:

- ✅ Django 5.2.7
- ✅ Django REST Framework 3.16.1
- ✅ Python 3.11.3
- ✅ SQLite database

---

## 🚀 Test natijalari

### 1. System Check
```bash
python manage.py check
# System check identified no issues (0 silenced). ✅
```

### 2. Server
```bash
python manage.py runserver
# Starting development server at http://127.0.0.1:8000/ ✅
```

### 3. API Endpoints
- ✅ `http://127.0.0.1:8000/api/posts/` - ishlayapti!
- ✅ DRF Browsable API - ishlayapti!
- ✅ Pagination - ishlayapti!

---

## 📖 API Qo'llanma

### GET Request - Postlarni ro'yxatini olish

**URL:** `GET http://127.0.0.1:8000/api/posts/`

**Response (birinchi sahifa, 2 ta post):**
```json
{
  "count": 5,
  "next": "http://127.0.0.1:8000/api/posts/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Birinchi post",
      "content": "Bu birinchi post matni",
      "created_at": "2025-11-03T12:00:00Z",
      "updated_at": "2025-11-03T12:00:00Z"
    },
    {
      "id": 2,
      "title": "Ikkinchi post",
      "content": "Bu ikkinchi post matni",
      "created_at": "2025-11-03T12:05:00Z",
      "updated_at": "2025-11-03T12:05:00Z"
    }
  ]
}
```

### POST Request - Yangi post yaratish

**URL:** `POST http://127.0.0.1:8000/api/posts/`

**Request Body:**
```json
{
  "title": "Yangi post sarlavhasi",
  "content": "Bu yerda post matni bo'ladi"
}
```

**Response:**
```json
{
  "message": "Post muvaffaqiyatli yaratildi!",
  "data": {
    "id": 6,
    "title": "Yangi post sarlavhasi",
    "content": "Bu yerda post matni bo'ladi",
    "created_at": "2025-11-03T12:48:00Z",
    "updated_at": "2025-11-03T12:48:00Z"
  }
}
```

---

## 🎓 O'rganilgan kontseptsiyalar

### DRF Asoslari:
1. ✅ **Installation** - DRF o'rnatish va sozlash
2. ✅ **Serializers** - ModelSerializer bilan ishlash
3. ✅ **Generic Views** - ListCreateAPIView ishlatish
4. ✅ **Pagination** - PageNumberPagination
5. ✅ **URL Routing** - API endpoints yaratish

### Django asoslari:
1. ✅ **Models** - Post modeli
2. ✅ **Migrations** - Database schema
3. ✅ **Admin** - Admin panel konfiguratsiyasi
4. ✅ **Settings** - REST_FRAMEWORK sozlamalari

---

## 💡 Keyingi bosqichlar

Qo'shimcha funksionallik qo'shish mumkin:

### 1. Detail Endpoints
- GET `/api/posts/<id>/` - bitta post
- PUT `/api/posts/<id>/` - post yangilash
- DELETE `/api/posts/<id>/` - post o'chirish

### 2. Authentication
- Token authentication
- JWT authentication
- Session authentication

### 3. Permissions
- IsAuthenticated
- IsAdminUser
- Custom permissions

### 4. Filtering
- Search
- Filtering
- Ordering

### 5. ViewSets
- ModelViewSet
- ReadOnlyModelViewSet
- Custom ViewSets

---

## ✨ YAKUNIY NATIJA

**Barcha 5 ta topshiriq 100% bajarildi!**

✅ DRF o'rnatildi va sozlandi  
✅ Post modeli yaratildi  
✅ PostSerializer yaratildi  
✅ PostListCreateAPIView yaratildi  
✅ URL routing sozlandi  
✅ Pagination ishlayapti (2 per page)  
✅ API muvaffaqiyatli test qilindi  

**Server ishlamoqda:** http://127.0.0.1:8000/api/posts/

**DRF browsable API orqali postlarni ko'rish va yaratish mumkin! 🚀**
