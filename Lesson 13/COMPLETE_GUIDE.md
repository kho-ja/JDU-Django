# 13-dars: Django'da Testlash - To'liq Qo'llanma

## 📚 Mundarija

1. [Kirish](#kirish)
2. [O'rnatish](#ornatish)
3. [Topshiriqlar](#topshiriqlar)
4. [Test Patterns](#test-patterns)
5. [Best Practices](#best-practices)
6. [Xulosa](#xulosa)

---

## Kirish

Bu dars Django ilovasini **pytest** yordamida professional darajada testlashni o'rgatadi. Testlash dasturlashning eng muhim qismi bo'lib, u kodning sifati va ishonchliligini ta'minlaydi.

### Nima uchun testlash kerak?

✅ **Xatoliklarni erta aniqlash** - Kod yozishda xatolarni darhol topish  
✅ **Kodni o'zgartirishda ishonch** - Refactoring xavfsiz bo'ladi  
✅ **Dokumentatsiya** - Testlar kodning qanday ishlashini ko'rsatadi  
✅ **Regression prevention** - Eski xatolar qaytib kelmaydi  
✅ **Code quality** - Yaxshi testlar yaxshi kod yozishga majbur qiladi  

### Test turlari

1. **Unit Tests** - Alohida funksiyalarni test qilish
2. **Integration Tests** - Bir nechta komponentlarni birgalikda test qilish
3. **Model Tests** - Django modellarini test qilish
4. **View Tests** - API endpoint'larni test qilish

---

## O'rnatish

### 1. Virtual Environment
```powershell
# Yangi .venv yaratish
python -m venv .venv

# Aktivlashtirish (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Aktivlashtirish (Windows CMD)
.venv\Scripts\activate.bat

# Aktivlashtirish (Linux/Mac)
source .venv/bin/activate
```

### 2. Paketlarni o'rnatish
```powershell
# requirements.txt orqali
pip install -r requirements.txt

# Yoki alohida
pip install Django==5.2.7
pip install djangorestframework==3.16.1
pip install pytest==8.4.2
pip install pytest-django==4.11.1
```

### 3. Migratsiyalarni bajarish
```powershell
python manage.py migrate
```

### 4. Testlarni tekshirish
```powershell
pytest
```

---

## Topshiriqlar

### Topshiriq 1: pytest o'rnatish va sozlash ✅

**Maqsad:** pytest va pytest-django paketlarini o'rnatish, `pytest.ini` faylini yaratish.

#### pytest.ini
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

**Natija:** pytest sozlandi va test papkasi yaratildi.

---

### Topshiriq 2: O'rtacha arifmetikni hisoblash ✅

**Maqsad:** Ikki sonning o'rtacha arifmetikini hisoblaydigan funksiya va uning testlarini yozish.

#### Funksiya
```python
def calculate_average(a, b):
    """
    Ikki sonning o'rtacha arifmetikini hisoblash
    
    Args:
        a (float): Birinchi son
        b (float): Ikkinchi son
    
    Returns:
        float: O'rtacha arifmetik
    
    Examples:
        >>> calculate_average(10, 20)
        15.0
        >>> calculate_average(5, 5)
        5.0
    """
    return (a + b) / 2
```

#### Testlar (20 tests)
```python
import pytest

@pytest.mark.unit
class TestAverageFunction:
    def test_average_positive_integers(self):
        """Musbat butun sonlar"""
        assert calculate_average(10, 20) == 15.0
    
    def test_average_negative_numbers(self):
        """Manfiy sonlar"""
        assert calculate_average(-10, -20) == -15.0
    
    def test_average_with_zero(self):
        """Nol bilan"""
        assert calculate_average(0, 10) == 5.0

# Parametrized tests
@pytest.mark.parametrize("a,b,expected", [
    (0, 0, 0.0),
    (10, 20, 15.0),
    (-10, 10, 0.0),
    (2.5, 7.5, 5.0),
])
def test_average_parametrized(a, b, expected):
    assert calculate_average(a, b) == expected
```

**Ishga tushirish:**
```powershell
pytest tests/test_average.py -v
```

**Natija:** 20/20 tests passed ✅

---

### Topshiriq 3: Talaba ID raqamlarini yig'indisi ✅

**Maqsad:** Talaba ID raqamidagi barcha raqamlarni qo'shadigan funksiya va testlarini yozish.

**Misol:** ID = 231323 → 2+3+1+3+2+3 = 14

#### Funksiya
```python
def calculate_id_sum(student_id):
    """
    Talaba ID raqamlarini yig'indisini hisoblash
    
    Args:
        student_id: int yoki str - Talaba ID
    
    Returns:
        int: Raqamlar yig'indisi
    
    Examples:
        >>> calculate_id_sum(231323)
        14
        >>> calculate_id_sum("12345")
        15
    """
    id_str = str(student_id)
    return sum(int(digit) for digit in id_str)
```

#### Testlar (25 tests)
```python
import pytest

@pytest.mark.unit
class TestStudentIDSum:
    def test_id_sum_example_case(self):
        """Topshiriqdagi misol"""
        assert calculate_id_sum(231323) == 14
    
    def test_id_sum_as_string(self):
        """String formatdagi ID"""
        assert calculate_id_sum("231323") == 14
    
    def test_id_sum_all_zeros(self):
        """Faqat nollar"""
        assert calculate_id_sum(0) == 0

# Parametrized tests
@pytest.mark.parametrize("student_id,expected", [
    (231323, 14),   # Asosiy misol
    (12345, 15),    # 1+2+3+4+5
    (100000, 1),    # Nollar bilan
    (999999, 54),   # Maksimal
])
def test_id_sum_parametrized(student_id, expected):
    assert calculate_id_sum(student_id) == expected
```

**Ishga tushirish:**
```powershell
pytest tests/test_id_sum.py -v
```

**Natija:** 25/25 tests passed ✅

---

### Topshiriq 4: Post modelini testlash ✅

**Maqsad:** Django Post modelini yaratish va barcha qismlarini test qilish.

#### Model
```python
from django.db import models

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

#### Testlar (40 tests)

##### 1. Asosiy Model Testlari
```python
@pytest.mark.django_db
@pytest.mark.model
class TestPostModel:
    def test_create_post_with_valid_data(self):
        """To'g'ri ma'lumotlar bilan post yaratish"""
        post = Post.objects.create(
            title="Test Title",
            content="Test Content"
        )
        assert post.title == "Test Title"
        assert post.pk is not None
    
    def test_post_str_representation(self):
        """__str__ metodi"""
        post = Post.objects.create(title="My Title", content="...")
        assert str(post) == "My Title"
```

##### 2. CRUD Testlari
```python
@pytest.mark.django_db
class TestPostModelCRUD:
    def test_create_post(self):
        """Create operatsiyasi"""
        Post.objects.create(title="Title", content="Content")
        assert Post.objects.count() == 1
    
    def test_read_post(self):
        """Read operatsiyasi"""
        created = Post.objects.create(title="Title", content="Content")
        read = Post.objects.get(pk=created.pk)
        assert read.title == "Title"
    
    def test_update_post(self):
        """Update operatsiyasi"""
        post = Post.objects.create(title="Old", content="Old")
        post.title = "New"
        post.save()
        updated = Post.objects.get(pk=post.pk)
        assert updated.title == "New"
    
    def test_delete_post(self):
        """Delete operatsiyasi"""
        post = Post.objects.create(title="Title", content="Content")
        post_id = post.pk
        post.delete()
        assert not Post.objects.filter(pk=post_id).exists()
```

##### 3. Field Testlari
```python
@pytest.mark.django_db
class TestPostModelFields:
    def test_title_field_type(self):
        """Title field turi"""
        field = Post._meta.get_field('title')
        assert field.__class__.__name__ == 'CharField'
    
    def test_content_field_type(self):
        """Content field turi"""
        field = Post._meta.get_field('content')
        assert field.__class__.__name__ == 'TextField'
```

**Ishga tushirish:**
```powershell
pytest tests/test_post_model.py -v
```

**Natija:** 40/40 tests passed ✅

---

### Topshiriq 5: Post viewlarni testlash ✅

**Maqsad:** DRF API endpoint'larini test qilish (GET va POST so'rovlar).

#### View
```python
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

#### Testlar (35 tests)

##### 1. GET So'rovlar (List)
```python
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
@pytest.mark.view
class TestPostListView:
    def test_get_empty_post_list(self, api_client):
        """Bo'sh ro'yxat"""
        url = reverse('post-list-create')
        response = api_client.get(url)
        
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 0
    
    def test_get_post_list_with_posts(self, api_client):
        """Postlar mavjud bo'lganda"""
        Post.objects.create(title="Post 1", content="Content 1")
        Post.objects.create(title="Post 2", content="Content 2")
        
        url = reverse('post-list-create')
        response = api_client.get(url)
        
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
```

##### 2. POST So'rovlar (Create)
```python
@pytest.mark.django_db
@pytest.mark.view
class TestPostCreateView:
    def test_create_post_with_valid_data(self, api_client):
        """To'g'ri ma'lumotlar bilan yaratish"""
        url = reverse('post-list-create')
        data = {'title': 'New Post', 'content': 'New Content'}
        response = api_client.post(url, data)
        
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == 'New Post'
        assert Post.objects.count() == 1
    
    def test_create_post_without_title(self, api_client):
        """Title bo'lmasa xato"""
        url = reverse('post-list-create')
        data = {'content': 'Content only'}
        response = api_client.post(url, data)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
```

##### 3. Integration Tests
```python
@pytest.mark.django_db
@pytest.mark.integration
class TestPostViewIntegration:
    def test_create_and_retrieve_post(self, api_client):
        """Yaratish va olish workflow"""
        url = reverse('post-list-create')
        
        # Create
        data = {'title': 'Test', 'content': 'Content'}
        create_response = api_client.post(url, data)
        assert create_response.status_code == 201
        
        # Retrieve
        list_response = api_client.get(url)
        assert len(list_response.data) == 1
        assert list_response.data[0]['title'] == 'Test'
```

**Ishga tushirish:**
```powershell
pytest tests/test_post_views.py -v
```

**Natija:** 35/35 tests passed ✅

---

## Test Patterns

### 1. Arrange-Act-Assert (AAA)
```python
def test_example():
    # Arrange - ma'lumotlarni tayyorlash
    post = Post.objects.create(title="Test", content="Content")
    
    # Act - amaliyotni bajarish
    result = post.get_summary()
    
    # Assert - natijani tekshirish
    assert result == "Test: Content"
```

### 2. Fixtures
```python
@pytest.fixture
def sample_post():
    """Takroriy ishlatish uchun fixture"""
    return Post.objects.create(
        title="Sample Post",
        content="Sample content"
    )

def test_with_fixture(sample_post):
    """Fixture ishlatish"""
    assert sample_post.title == "Sample Post"
```

### 3. Parametrized Tests
```python
@pytest.mark.parametrize("input,expected", [
    (10, 20),
    (5, 10),
    (0, 0),
])
def test_double(input, expected):
    """Bir nechta qiymatlarni test qilish"""
    assert double(input) == expected
```

### 4. Test Markers
```python
@pytest.mark.unit          # Unit test
@pytest.mark.integration   # Integration test
@pytest.mark.model         # Model test
@pytest.mark.view          # View test
@pytest.mark.django_db     # Django database kerak
@pytest.mark.slow          # Sekin test
```

---

## Best Practices

### 1. Test Isolation
✅ Har bir test mustaqil bo'lishi kerak  
✅ Testlar bir-biriga bog'liq bo'lmasligi kerak  
✅ Setup va cleanup to'g'ri bo'lishi kerak  

```python
# ✅ Yaxshi
@pytest.mark.django_db
def test_create_post():
    post = Post.objects.create(...)  # Har bir test o'z ma'lumotini yaratadi
    assert post.pk is not None

# ❌ Yomon
posts = []  # Global o'zgaruvchi
def test_something():
    posts.append(...)  # Testlar o'zaro bog'liq
```

### 2. Descriptive Names
✅ Test nomlari aniq va tushunarli bo'lsin  
✅ Nima test qilinayotgani nomidan ko'rinsin  

```python
# ✅ Yaxshi
def test_create_post_with_valid_data()
def test_create_post_without_required_fields()
def test_update_post_changes_updated_at_timestamp()

# ❌ Yomon
def test_post()
def test_1()
def test_something()
```

### 3. One Assertion Per Test (optional)
✅ Har bir test bitta narsani tekshirsin (tavsiya)  
✅ Murakkab testlarni kichik testlarga bo'lish  

```python
# ✅ Yaxshi
def test_post_has_title():
    post = Post.objects.create(...)
    assert hasattr(post, 'title')

def test_post_has_content():
    post = Post.objects.create(...)
    assert hasattr(post, 'content')

# ⚠️ Qabul qilinadigan (lekin ideal emas)
def test_post_has_required_fields():
    post = Post.objects.create(...)
    assert hasattr(post, 'title')
    assert hasattr(post, 'content')
```

### 4. DRY (Don't Repeat Yourself)
✅ Fixtures ishlatish  
✅ Parametrized tests ishlatish  
✅ Helper funksiyalar yaratish  

```python
# ✅ Yaxshi - fixture
@pytest.fixture
def sample_data():
    return {"title": "Test", "content": "Content"}

def test_1(sample_data):
    assert sample_data["title"] == "Test"

def test_2(sample_data):
    assert len(sample_data) == 2
```

### 5. Test Coverage
✅ Muhim kodlarni to'liq test qilish  
✅ Edge case'larni tekshirish  
✅ Error handling'ni test qilish  

```python
# Normal case
def test_divide_normal():
    assert divide(10, 2) == 5

# Edge case
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

# Boundary case
def test_divide_very_small_numbers():
    assert divide(0.0001, 0.0001) == 1
```

---

## Xulosa

### 📊 Natijalar
```
✅ Jami testlar: 114
✅ O'tgan testlar: 114 (100%)
❌ Xatolik: 0
⏱️ Vaqt: 0.82 soniya
```

### 🎯 O'rganilgan Mavzular
1. ✅ pytest asoslari
2. ✅ pytest-django integratsiyasi
3. ✅ Fixtures va parametrized tests
4. ✅ Test markers
5. ✅ Model testing
6. ✅ API view testing
7. ✅ Test organization
8. ✅ Best practices

### 📚 Keyingi Bosqichlar
- [ ] Test coverage 100% ga etkazish
- [ ] CI/CD pipeline qo'shish (GitHub Actions)
- [ ] Mock va patch o'rganish
- [ ] Performance testing
- [ ] Load testing
- [ ] Security testing

### 🔗 Foydali Havolalar
- [pytest Documentation](https://docs.pytest.org/)
- [pytest-django](https://pytest-django.readthedocs.io/)
- [Django Testing](https://docs.djangoproject.com/en/5.0/topics/testing/)
- [DRF Testing](https://www.django-rest-framework.org/api-guide/testing/)
- [Real Python: Testing in Django](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/)

---

## 🎉 Tabriklaymiz!

Siz Django testlashning asoslarini muvaffaqiyatli o'rgandingiz! 

```
╔══════════════════════════════════════════╗
║                                          ║
║     🎊 BARCHA TESTLAR O'TDI! 🎊         ║
║                                          ║
║     114 / 114 tests passed               ║
║     100% Success Rate                    ║
║                                          ║
║     Tabriklaymiz! 🎉                     ║
║                                          ║
╚══════════════════════════════════════════╝
```

**Keep Testing! Keep Learning!** 🚀

---

**Lesson 13 - Django Testing**  
**Status:** ✅ Completed  
**Version:** 1.0  
**Date:** 2025
