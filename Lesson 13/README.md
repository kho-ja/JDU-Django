# Lesson 13: Django'da Testlash (Testing in Django)

Bu dars Django ilovasini **pytest** yordamida testlashni o'rgatadi. Testlash - dasturlashning eng muhim qismidir, chunki u kodni sifatli va ishonchli qiladi.

## 📋 O'rnatilgan Paketlar

```
Django==5.2.7
djangorestframework==3.16.1
pytest==8.4.2
pytest-django==4.11.1
```

## 🎯 Topshiriqlar

### 1-topshiriq: pytest o'rnatish va konfiguratsiya
- `pytest` va `pytest-django` o'rnatildi
- `pytest.ini` faylida sozlamalar qo'shildi
- Test markerlar qo'shildi: `unit`, `integration`, `model`, `view`

### 2-topshiriq: Sodda funksiyani testlash
**Funksiya:** Ikki sonning o'rtacha arifmetikini hisoblash
```python
def calculate_average(a, b):
    return (a + b) / 2
```

**Testlar:** `tests/test_average.py`
- 20+ test cases
- Parametrized tests
- Edge cases (manfiy sonlar, katta sonlar, 0)

### 3-topshiriq: Talaba ID raqamlarini yig'indisini hisoblash
**Funksiya:** ID raqamidagi barcha raqamlarni qo'shish
```python
def calculate_id_sum(student_id):
    # Misol: 231323 -> 2+3+1+3+2+3 = 14
```

**Testlar:** `tests/test_id_sum.py`
- 25+ test cases
- String va integer formatlar
- Real-world ID namunalari
- Property-based tests

### 4-topshiriq: Post modelini testlash
**Model:** `posts/models.py`
```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

**Testlar:** `tests/test_post_model.py`
- 40+ test cases
- Field validation tests
- CRUD operations
- String representation
- Timestamps
- Unicode and special characters

### 5-topshiriq: Post viewlarni testlash
**View:** `posts/views.py` - `PostListCreateAPIView`

**Testlar:** `tests/test_post_views.py`
- 35+ test cases
- GET requests (list)
- POST requests (create)
- Validation tests
- Integration tests
- Error handling

## 🏗️ Loyiha Strukturasi

```
Lesson 13/
├── manage.py
├── db.sqlite3
├── pytest.ini              # pytest konfiguratsiya
├── requirements.txt
├── README.md
├── TOPSHIRIQLAR.md
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── posts/
│   ├── __init__.py
│   ├── models.py           # Post modeli
│   ├── serializers.py      # PostSerializer
│   ├── views.py            # PostListCreateAPIView
│   ├── urls.py
│   └── migrations/
└── tests/
    ├── __init__.py
    ├── test_average.py     # Topshiriq 2
    ├── test_id_sum.py      # Topshiriq 3
    ├── test_post_model.py  # Topshiriq 4
    └── test_post_views.py  # Topshiriq 5
```

## 🚀 O'rnatish

### 1. Virtual environment yaratish
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Paketlarni o'rnatish
```powershell
pip install -r requirements.txt
```

### 3. Migratsiyalarni bajarish
```powershell
python manage.py migrate
```

## 🧪 Testlarni Ishga Tushirish

### Barcha testlarni ishga tushirish
```powershell
pytest
```

### Verbose rejimda (batafsil)
```powershell
pytest -v
```

### Faqat ma'lum bir faylni test qilish
```powershell
pytest tests/test_average.py
```

### Faqat ma'lum bir test class
```powershell
pytest tests/test_post_model.py::TestPostModel
```

### Faqat ma'lum bir test funksiyasi
```powershell
pytest tests/test_average.py::TestAverageFunction::test_average_positive_integers
```

### Test markerlar bo'yicha
```powershell
pytest -m unit          # Faqat unit testlar
pytest -m integration   # Faqat integration testlar
pytest -m model         # Faqat model testlar
pytest -m view          # Faqat view testlar
```

### Test coverage bilan
```powershell
pytest --cov=posts --cov=tests
```

## 📊 Test Natijalari

```
============================================== test session starts ===============================================
platform win32 -- Python 3.11.3, pytest-8.4.2, pluggy-1.6.0
django: version: 5.2.7, settings: config.settings (from ini)
rootdir: D:\Universitet\JDU\Django\Lesson 13
configfile: pytest.ini
plugins: django-4.11.1
collected 114 items

tests/test_post_model.py ..............................                                                     [ 26%]
tests/test_post_views.py ...........................                                                        [ 50%]
tests/test_average.py ....................                                                                  [ 68%]
tests/test_id_sum.py ..............................                                                         [100%]

============================================== 114 passed in 0.82s ===============================================
```

## 🎓 O'rganiladigan Mavzular

1. **pytest asoslari**
   - Test funksiyalari va classlar
   - Fixtures
   - Parametrized tests
   - Test markers

2. **Django Testing**
   - `@pytest.mark.django_db` decorator
   - Model testing
   - View testing
   - API testing

3. **Test Organizatsiyasi**
   - Test klasslari
   - Test fixtures
   - Test markers
   - Test discovery

4. **Yaxshi Test Amaliyotlari**
   - Arrange-Act-Assert pattern
   - Test isolation
   - Descriptive test names
   - Edge case testing

## 🔍 Qo'shimcha Ma'lumotlar

### pytest.ini sozlamalari
```ini
[pytest]
DJANGO_SETTINGS_MODULE = config.settings
python_files = test_*.py
python_classes = Test*
python_functions = test_*
testpaths = tests
addopts = 
    --reuse-db
    --nomigrations
    -v
markers = 
    unit: Unit tests
    integration: Integration tests
    model: Model tests
    view: View tests
```

### Test Fixtures
Fixtures - bu testlar uchun ma'lumotlarni tayyorlash usuli:

```python
@pytest.fixture
def sample_post():
    """Create a sample post for testing"""
    return Post.objects.create(
        title="Sample Post",
        content="Sample content"
    )
```

### Parametrized Tests
Bir nechta input qiymatlarni test qilish:

```python
@pytest.mark.parametrize("a,b,expected", [
    (0, 0, 0.0),
    (10, 20, 15.0),
    (-10, 10, 0.0),
])
def test_average_parametrized(a, b, expected):
    result = calculate_average(a, b)
    assert result == expected
```

## 📚 Foydali Havolalar

- [pytest Documentation](https://docs.pytest.org/)
- [pytest-django Documentation](https://pytest-django.readthedocs.io/)
- [Django Testing](https://docs.djangoproject.com/en/5.0/topics/testing/)
- [Django REST Framework Testing](https://www.django-rest-framework.org/api-guide/testing/)

## 👨‍💻 Muallif

Bu loyiha Django darslarining bir qismi sifatida tayyorlandi.

---

**Eslatma:** Testlash - dasturlashning muhim qismi! Har bir feature uchun test yozing! 🧪
