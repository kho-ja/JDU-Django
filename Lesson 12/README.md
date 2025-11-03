# Lesson 12: Django REST Framework (DRF)

## 📚 Darsning maqsadi
Django REST Framework bilan RESTful API yaratishni o'rganish.

## 🎯 Topshiriqlar

### ✅ 1. DRF ni o'rnatish
Django REST Framework (DRF) ni o'rnating va `settings.py` faylida `rest_framework` sozlamasini amalga oshiring.

**Bajarilgan:**
- ✅ Yangi virtual environment yaratildi (`.venv`)
- ✅ Django va DRF o'rnatildi: `pip install django djangorestframework`
- ✅ `INSTALLED_APPS` ga `rest_framework` qo'shildi
- ✅ Pagination sozlamalari qo'shildi (2 post per page)

### ✅ 2. Post modelini yaratish
Post nomli model yarating, uning `title` (CharField) va `content` (TextField) maydonlari bo'lishi kerak. Modelni migrations orqali bazaga qo'shing.

**Bajarilgan:**
- ✅ `Post` modeli yaratildi:
  - `title` - CharField (max_length=200)
  - `content` - TextField
  - `created_at` - DateTimeField (auto_now_add=True)
  - `updated_at` - DateTimeField (auto_now=True)
- ✅ Migrations yaratildi va qo'llandi
- ✅ Admin panelda registratsiya qilindi

### ✅ 3. Serializer yaratish
Post modelidan foydalanadigan serializer yarating. Serializerda `title` va `content` maydonlarini qo'shing.

**Bajarilgan:**
- ✅ `PostSerializer` yaratildi (ModelSerializer)
- ✅ Barcha kerakli maydonlar qo'shildi
- ✅ Read-only fields belgilandi (id, created_at, updated_at)

### ✅ 4. APIView yaratish
Postlarni yaratish va ko'rish uchun APIView yarating. Ushbu API yordamida yangi post qo'shish va mavjud postlarni 2 tadan ko'p bo'lsa pagination bilan ko'rish mumkin bo'lishi kerak.

**Bajarilgan:**
- ✅ `PostListCreateAPIView` yaratildi (ListCreateAPIView)
- ✅ GET method: postlarni ro'yxatini qaytaradi
- ✅ POST method: yangi post yaratadi
- ✅ Pagination avtomatik ishlaydi (2 post per page)

### ✅ 5. URL qo'shish
Yaratilgan APIView uchun URL qo'shing. URL yordamida API'ga murojaat qilish imkonini yarating.

**Bajarilgan:**
- ✅ `posts/urls.py` yaratildi
- ✅ API endpoint: `/api/posts/`
- ✅ Main `config/urls.py` ga ulandi

---

## 🚀 Loyihani ishga tushirish

### 1. Virtual environment yaratish va aktivlashtirish
```bash
cd "d:\Universitet\JDU\Django\Lesson 12"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Kerakli paketlarni o'rnatish
```bash
pip install django djangorestframework
```

### 3. Django project va app yaratish
```bash
django-admin startproject config .
python manage.py startapp posts
```

### 4. Migratsiyalarni qo'llash
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Development serverni ishga tushirish
```bash
python manage.py runserver
```

### 6. API'ni test qilish
**Browser'da:**
```
http://127.0.0.1:8000/api/posts/
```

**Admin panel:**
```
http://127.0.0.1:8000/admin/
```

---

## 📁 Loyiha tuzilishi

```
Lesson 12/
├── .venv/                    # Virtual environment
├── config/
│   ├── __init__.py
│   ├── settings.py           # DRF sozlamalari
│   ├── urls.py               # Main URL routing
│   ├── wsgi.py
│   └── asgi.py
├── posts/
│   ├── migrations/
│   │   └── 0001_initial.py   # Post model migration
│   ├── __init__.py
│   ├── admin.py              # Admin panel konfiguratsiyasi
│   ├── apps.py
│   ├── models.py             # Post modeli
│   ├── serializers.py        # PostSerializer
│   ├── views.py              # PostListCreateAPIView
│   ├── urls.py               # API URL patterns
│   └── tests.py
├── manage.py
├── db.sqlite3
└── README.md
```

---

## 🔧 Asosiy komponentlar

### 1. Model (`posts/models.py`)
```python
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    content = models.TextField(verbose_name="Mazmun")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### 2. Serializer (`posts/serializers.py`)
```python
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
```

### 3. View (`posts/views.py`)
```python
class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

### 4. DRF Settings (`config/settings.py`)
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'posts',
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2,  # 2 posts per page
}
```

### 5. URLs (`posts/urls.py`)
```python
urlpatterns = [
    path('api/posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
]
```

---

## 🌐 API Endpoints

### GET `/api/posts/`
**Barcha postlarni ro'yxatini olish (pagination bilan)**

**Response:**
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

### POST `/api/posts/`
**Yangi post yaratish**

**Request Body:**
```json
{
  "title": "Yangi post",
  "content": "Bu yangi post matni"
}
```

**Response:**
```json
{
  "message": "Post muvaffaqiyatli yaratildi!",
  "data": {
    "id": 3,
    "title": "Yangi post",
    "content": "Bu yangi post matni",
    "created_at": "2025-11-03T12:10:00Z",
    "updated_at": "2025-11-03T12:10:00Z"
  }
}
```

---

## 💡 DRF Asosiy Kontseptsiyalar

### 1. **Serializers**
- Model'dan JSON'ga va JSON'dan model'ga konvertatsiya
- Data validation
- ModelSerializer - model asosida avtomatik serializer

### 2. **APIView & Generic Views**
- `APIView` - asosiy view class
- `ListCreateAPIView` - list va create operatsiyalari uchun
- `RetrieveUpdateDestroyAPIView` - detail, update, delete uchun

### 3. **Pagination**
- `PageNumberPagination` - sahifa raqami bilan
- `LimitOffsetPagination` - limit va offset bilan
- `CursorPagination` - cursor asosida

### 4. **ViewSets & Routers**
- ViewSet - barcha CRUD operatsiyalar bitta class'da
- Router - URL'larni avtomatik yaratish

---

## 🎨 DRF Browsable API

DRF avtomatik ravishda browsable API taqdim etadi:
- ✅ HTML interface
- ✅ Form'lar POST/PUT requests uchun
- ✅ API documentation
- ✅ Authentication UI

Browser'da `http://127.0.0.1:8000/api/posts/` ochganda interactive API ko'rasiz!

---

## 🔐 Admin Panel

Admin panelni ishlatish:

1. **Superuser yaratish:**
```bash
python manage.py createsuperuser
```

2. **Admin panel:**
```
http://127.0.0.1:8000/admin/
```

Post'larni admin paneldan ham boshqarish mumkin!

---

## 📊 Test qilish

### Browser orqali
1. `http://127.0.0.1:8000/api/posts/` ga o'ting
2. DRF browsable API'da POST form'dan foydalaning
3. POST yarating va natijani ko'ring

### cURL orqali

**GET request:**
```bash
curl http://127.0.0.1:8000/api/posts/
```

**POST request:**
```bash
curl -X POST http://127.0.0.1:8000/api/posts/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Test post", "content": "Test mazmun"}'
```

### Postman orqali
1. GET: `http://127.0.0.1:8000/api/posts/`
2. POST: `http://127.0.0.1:8000/api/posts/`
   - Body: `raw` > `JSON`
   - Data: `{"title": "...", "content": "..."}`

---

## 🎓 O'rganilgan Django REST Framework kontseptsiyalari

✅ DRF o'rnatish va sozlash  
✅ ModelSerializer  
✅ ListCreateAPIView  
✅ Pagination (PageNumberPagination)  
✅ API endpoints yaratish  
✅ Browsable API  
✅ Serializer validation  
✅ Generic views  
✅ REST_FRAMEWORK settings  

---

## 📝 Keyingi qadamlar

Qo'shimcha funksionallik qo'shish mumkin:
- Authentication (Token, JWT)
- Permissions (IsAuthenticated, IsAdminUser)
- Filtering va searching
- ViewSets va Routers
- Detail, Update, Delete endpoints
- File upload
- Custom pagination
- API versioning

---

## ✅ Barcha topshiriqlar bajarildi!

Server ishlamoqda: **http://127.0.0.1:8000/api/posts/**

DRF browsable API'da postlarni ko'rish va yaratish mumkin! 🚀
