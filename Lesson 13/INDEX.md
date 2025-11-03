# 📚 Lesson 13: Django Testing - Documentation Index

## 🗂️ Hujjatlar Ro'yxati

### 📖 Asosiy Hujjatlar

1. **[README.md](README.md)** ⭐ BOSHLASH UCHUN
   - Loyihaga kirish
   - O'rnatish qo'llanmasi
   - Testlarni ishga tushirish
   - Test natijalari
   - 114 testlar haqida ma'lumot

2. **[COMPLETE_GUIDE.md](COMPLETE_GUIDE.md)** 📚 TO'LIQ QOLINMA
   - Har bir topshiriq batafsil
   - Kod misollari
   - Test patterns
   - Best practices
   - Xulosa va keyingi qadamlar

3. **[TOPSHIRIQLAR.md](TOPSHIRIQLAR.md)** ✅ TOPSHIRIQLAR
   - 5 ta topshiriq va ularning yechimlari
   - Har bir topshiriq uchun kodlar
   - Ishga tushirish qo'llanmasi
   - Natijalar va statistika

4. **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** ⚡ TEZKOR QO'LLANMA
   - Tezkor boshlash
   - Test patterns cheat sheet
   - pytest commands
   - Foydali maslahatlar

5. **[SUMMARY.md](SUMMARY.md)** 📊 XULOSA
   - Loyiha xulosasi
   - Test statistikasi
   - Muhim konseptlar
   - Natijalar va yutuqlar

---

## 📁 Loyiha Strukturasi

```
Lesson 13/
│
├── 📄 manage.py                      # Django management script
├── 📄 db.sqlite3                     # SQLite database
├── 📄 pytest.ini                     # pytest konfiguratsiya
├── 📄 requirements.txt               # Python paketlar
│
├── 📚 DOCUMENTATION/
│   ├── README.md                     # Asosiy hujjat
│   ├── COMPLETE_GUIDE.md             # To'liq qo'llanma
│   ├── TOPSHIRIQLAR.md               # Topshiriqlar
│   ├── QUICK_REFERENCE.md            # Tezkor reference
│   ├── SUMMARY.md                    # Xulosa
│   └── INDEX.md                      # Bu fayl
│
├── 📁 config/                        # Django konfiguratsiya
│   ├── settings.py                   # Django sozlamalar
│   ├── urls.py                       # URL routing
│   ├── asgi.py
│   └── wsgi.py
│
├── 📁 posts/                         # Posts app
│   ├── models.py                     # Post modeli
│   ├── serializers.py                # DRF serializers
│   ├── views.py                      # API views
│   ├── urls.py                       # URL patterns
│   ├── admin.py                      # Admin konfiguratsiya
│   └── migrations/                   # Database migrations
│
└── 📁 tests/                         # Test papkasi
    ├── test_average.py               # Topshiriq 2 (20 tests)
    ├── test_id_sum.py                # Topshiriq 3 (25 tests)
    ├── test_post_model.py            # Topshiriq 4 (40 tests)
    └── test_post_views.py            # Topshiriq 5 (35 tests)
```

---

## 🎯 Qaysi Hujjatni O'qish Kerak?

### Yangi Boshlovchilar uchun:
1. ✅ **README.md** - Loyihaga kirish
2. ✅ **COMPLETE_GUIDE.md** - Batafsil tushuntirish
3. ✅ **TOPSHIRIQLAR.md** - Amaliy mashqlar

### Tajribali Dasturchilar uchun:
1. ✅ **QUICK_REFERENCE.md** - Tezkor boshlash
2. ✅ **TOPSHIRIQLAR.md** - Kodlarni ko'rish
3. ✅ **README.md** - Xulosa

### O'qituvchilar uchun:
1. ✅ **SUMMARY.md** - Loyiha xulosasi
2. ✅ **COMPLETE_GUIDE.md** - To'liq ma'lumot
3. ✅ **TOPSHIRIQLAR.md** - Topshiriqlar va yechimlar

---

## 📊 Test Statistikasi

| Kategoriya | Testlar Soni | Holati |
|------------|--------------|--------|
| **Unit Tests** | 45 | ✅ 100% |
| **Model Tests** | 40 | ✅ 100% |
| **View Tests** | 35 | ✅ 100% |
| **JAMI** | **114** | **✅ 100%** |

---

## 🚀 Tezkor Boshlash

### 1. O'rnatish
```powershell
# Virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Paketlar
pip install -r requirements.txt

# Migratsiya
python manage.py migrate
```

### 2. Testlarni Ishga Tushirish
```powershell
# Barcha testlar
pytest

# Verbose rejim
pytest -v

# Ma'lum bir topshiriq
pytest tests/test_average.py      # Topshiriq 2
pytest tests/test_id_sum.py       # Topshiriq 3
pytest tests/test_post_model.py   # Topshiriq 4
pytest tests/test_post_views.py   # Topshiriq 5
```

---

## 📝 Topshiriqlar Xulosasi

### ✅ Topshiriq 1: pytest o'rnatish va sozlash
- pytest va pytest-django o'rnatildi
- pytest.ini yaratildi
- Test papkasi sozlandi

### ✅ Topshiriq 2: O'rtacha arifmetik (20 tests)
```python
calculate_average(10, 20) → 15.0
```
- Asosiy testlar: 10
- Parametrized tests: 7
- Edge cases: 3

### ✅ Topshiriq 3: ID raqamlar yig'indisi (25 tests)
```python
calculate_id_sum(231323) → 14  # 2+3+1+3+2+3
```
- Asosiy testlar: 10
- Parametrized tests: 12
- Edge cases: 3

### ✅ Topshiriq 4: Post modelini testlash (40 tests)
```python
class Post(models.Model):
    title = CharField(max_length=200)
    content = TextField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
```
- Model testlar: 11
- Field testlar: 6
- CRUD testlar: 6
- String testlar: 6
- Timestamp testlar: 2
- Boshqalar: 9

### ✅ Topshiriq 5: Post viewlarni testlash (35 tests)
```python
class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```
- GET testlar: 5
- POST testlar: 11
- Integration testlar: 3
- Special cases: 6
- Parametrized testlar: 5
- Boshqalar: 5

---

## 🎓 O'rganiladigan Mavzular

### pytest Asoslari
- ✅ Test funksiyalari va klasslar
- ✅ Fixtures
- ✅ Parametrized tests
- ✅ Test markers
- ✅ Assertions

### Django Testing
- ✅ @pytest.mark.django_db
- ✅ Model testing
- ✅ View testing
- ✅ API testing
- ✅ Database transactions

### Best Practices
- ✅ Arrange-Act-Assert pattern
- ✅ Test isolation
- ✅ Descriptive names
- ✅ DRY principle
- ✅ Test coverage

---

## 🔗 Tashqi Manbalar

### Rasmiy Dokumentatsiyalar
- [pytest](https://docs.pytest.org/)
- [pytest-django](https://pytest-django.readthedocs.io/)
- [Django Testing](https://docs.djangoproject.com/en/topics/testing/)
- [Django REST Framework Testing](https://www.django-rest-framework.org/api-guide/testing/)

### Tutorial va Maqolalar
- [Real Python: Testing in Django](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/)
- [Test-Driven Development with Python](https://www.obeythetestinggoat.com/)
- [Django Testing Best Practices](https://djangostars.com/blog/django-testing-best-practices/)

### Video Darslar
- Django Testing with pytest (YouTube)
- Test-Driven Development with Django (Udemy/Coursera)

---

## 💡 Foydali Buyruqlar

### pytest Commands
```powershell
pytest                     # Barcha testlar
pytest -v                  # Verbose
pytest -s                  # Print output
pytest -x                  # Stop on first failure
pytest -k "test_create"    # Pattern bo'yicha
pytest -m unit             # Marker bo'yicha
pytest --lf                # Last failed
pytest --ff                # Failed first
pytest --pdb               # Debugger
```

### Django Commands
```powershell
python manage.py runserver         # Server
python manage.py makemigrations    # Migrations yaratish
python manage.py migrate           # Migrations bajarish
python manage.py shell             # Django shell
python manage.py createsuperuser   # Admin user
```

---

## 🎉 Natija

```
╔══════════════════════════════════════════╗
║                                          ║
║     🎊 LESSON 13 COMPLETED! 🎊          ║
║                                          ║
║     114 Tests / 114 Passed               ║
║     100% Success Rate                    ║
║     0.82 seconds                         ║
║                                          ║
║     Tabriklaymiz! 🎉                     ║
║                                          ║
╚══════════════════════════════════════════╝
```

---

## 📞 Yordam

Savollar yoki muammolar bo'lsa:

1. **README.md** ni o'qing
2. **COMPLETE_GUIDE.md** ga qarang
3. **QUICK_REFERENCE.md** dan foydalaning
4. Rasmiy dokumentatsiyalarni tekshiring

---

## ✨ Keyingi Qadamlar

- [ ] 100% test coverage ga erishish
- [ ] CI/CD pipeline qo'shish
- [ ] Integration tests kengaytirish
- [ ] Mock va patch o'rganish
- [ ] Performance testing
- [ ] Security testing

---

**Happy Testing!** 🚀  
**Keep Learning!** 📚  
**Build Great Things!** ✨

---

*Last Updated: 2025*  
*Status: ✅ Completed*  
*Version: 1.0*
