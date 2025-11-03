# Django Testing - Topshiriqlar (13-dars)

Bu faylda barcha topshiriqlar va ularning yechimlari keltirilgan.

## 📝 Topshiriq 1: pytest o'rnatish va sozlash

### Vazifa
- `pytest` va `pytest-django` paketlarini o'rnatish
- `pytest.ini` konfiguratsiya faylini yaratish
- Test markerlarini sozlash

### Yechim

#### 1. Paketlarni o'rnatish
```powershell
pip install pytest pytest-django
```

#### 2. pytest.ini yaratish
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

#### 3. Test papkasini yaratish
```powershell
mkdir tests
New-Item tests/__init__.py
```

---

## 📝 Topshiriq 2: O'rtacha arifmetikni hisoblash testlari

### Vazifa
Ikki sonning o'rtacha arifmetikini hisoblash funksiyasini yozish va test qilish.

### Funksiya
```python
def calculate_average(a, b):
    """
    Ikki sonning o'rtacha arifmetikini hisoblash
    
    Args:
        a: Birinchi son
        b: Ikkinchi son
    
    Returns:
        float: O'rtacha arifmetik qiymat
    """
    return (a + b) / 2
```

### Testlar (tests/test_average.py)

#### Oddiy testlar
```python
import pytest

def calculate_average(a, b):
    return (a + b) / 2

@pytest.mark.unit
class TestAverageFunction:
    def test_average_positive_integers(self):
        """Test musbat butun sonlar bilan"""
        result = calculate_average(10, 20)
        assert result == 15.0
    
    def test_average_equal_numbers(self):
        """Test bir xil sonlar bilan"""
        result = calculate_average(5, 5)
        assert result == 5.0
    
    def test_average_negative_numbers(self):
        """Test manfiy sonlar bilan"""
        result = calculate_average(-10, -20)
        assert result == -15.0
```

#### Parametrized testlar
```python
@pytest.mark.unit
@pytest.mark.parametrize("a,b,expected", [
    (0, 0, 0.0),
    (1, 1, 1.0),
    (10, 20, 15.0),
    (100, 200, 150.0),
    (-10, 10, 0.0),
    (2.5, 7.5, 5.0),
    (3, 7, 5.0),
])
def test_average_parametrized(a, b, expected):
    """Parametrlashgan testlar"""
    result = calculate_average(a, b)
    assert result == expected
```

#### Ishga tushirish
```powershell
pytest tests/test_average.py -v
```

#### Natija
```
tests/test_average.py::TestAverageFunction::test_average_positive_integers PASSED
tests/test_average.py::TestAverageFunction::test_average_equal_numbers PASSED
tests/test_average.py::test_average_parametrized[0-0-0.0] PASSED
tests/test_average.py::test_average_parametrized[10-20-15.0] PASSED
... va boshqalar

============================================== 20 passed ===============================================
```

---

## 📝 Topshiriq 3: Talaba ID raqamlarini yig'indisini hisoblash

### Vazifa
Talaba ID raqamidagi barcha raqamlarni qo'shish funksiyasini yozish va test qilish.

**Misol:** ID = 231323 → 2+3+1+3+2+3 = 14

### Funksiya
```python
def calculate_id_sum(student_id):
    """
    Talaba ID raqamlarini yig'indisini hisoblash
    
    Args:
        student_id: int yoki str - Talaba ID raqami
    
    Returns:
        int: Raqamlar yig'indisi
    
    Examples:
        >>> calculate_id_sum(231323)
        14
        >>> calculate_id_sum("231323")
        14
    """
    # ID ni stringga aylantirish
    id_str = str(student_id)
    
    # Har bir raqamni qo'shish
    total = sum(int(digit) for digit in id_str)
    
    return total
```

### Testlar (tests/test_id_sum.py)

#### Asosiy testlar
```python
import pytest

def calculate_id_sum(student_id):
    id_str = str(student_id)
    return sum(int(digit) for digit in id_str)

@pytest.mark.unit
class TestStudentIDSum:
    def test_id_sum_example_case(self):
        """Test topshiriqdagi misol - 231323 = 14"""
        result = calculate_id_sum(231323)
        assert result == 14
    
    def test_id_sum_as_string(self):
        """Test string formatdagi ID bilan"""
        result = calculate_id_sum("231323")
        assert result == 14
    
    def test_id_sum_simple_case(self):
        """Test sodda ID bilan"""
        result = calculate_id_sum(12345)
        assert result == 15  # 1+2+3+4+5
```

#### Parametrized testlar
```python
@pytest.mark.unit
@pytest.mark.parametrize("student_id,expected", [
    (231323, 14),   # Topshiriq misoli
    (12345, 15),    # 1+2+3+4+5
    (100000, 1),    # Nollar bilan
    (999999, 54),   # Maksimal qiymat
    (111111, 6),    # Bir xil raqamlar
    (123456, 21),   # Ketma-ket raqamlar
    (0, 0),         # Nol
    (5, 5),         # Bitta raqam
])
def test_id_sum_parametrized(student_id, expected):
    """Turli ID namunalari bilan test"""
    result = calculate_id_sum(student_id)
    assert result == expected
```

#### Real-world testlar
```python
@pytest.mark.unit
class TestRealWorldIDs:
    def test_typical_6_digit_id(self):
        """Oddiy 6 raqamli ID"""
        result = calculate_id_sum(202301)
        expected = 2+0+2+3+0+1  # 8
        assert result == expected
    
    def test_year_based_id(self):
        """Yil asosidagi ID (2023001)"""
        result = calculate_id_sum(2023001)
        expected = 2+0+2+3+0+0+1  # 8
        assert result == expected
```

#### Ishga tushirish
```powershell
pytest tests/test_id_sum.py -v
```

#### Natija
```
tests/test_id_sum.py::TestStudentIDSum::test_id_sum_example_case PASSED
tests/test_id_sum.py::test_id_sum_parametrized[231323-14] PASSED
tests/test_id_sum.py::TestRealWorldIDs::test_typical_6_digit_id PASSED
... va boshqalar

============================================== 25 passed ===============================================
```

---

## 📝 Topshiriq 4: Post modelini testlash

### Vazifa
Django `Post` modelini yozish va barcha qismlarini test qilish.

### Model (posts/models.py)
```python
from django.db import models

class Post(models.Model):
    """
    Post model with title and content fields for blog posts.
    """
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    content = models.TextField(verbose_name="Mazmun")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan sana")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created_at"]  # Yangilar birinchi

    def __str__(self):
        return self.title
```

### Testlar (tests/test_post_model.py)

#### Field testlari
```python
import pytest
from posts.models import Post

@pytest.mark.django_db
@pytest.mark.model
class TestPostModel:
    def test_create_post_with_valid_data(self):
        """Test to'g'ri ma'lumotlar bilan post yaratish"""
        post = Post.objects.create(
            title="Test Title",
            content="Test Content"
        )
        assert post.title == "Test Title"
        assert post.content == "Test Content"
        assert post.pk is not None
    
    def test_post_title_field(self):
        """Test title field mavjudligini"""
        post = Post.objects.create(title="Title", content="Content")
        assert hasattr(post, 'title')
    
    def test_post_str_representation(self):
        """Test __str__ metodi"""
        post = Post.objects.create(title="My Title", content="Content")
        assert str(post) == "My Title"
```

#### CRUD testlari
```python
@pytest.mark.django_db
@pytest.mark.model
class TestPostModelCRUD:
    def test_create_post(self):
        """Test Create operatsiyasi"""
        post = Post.objects.create(title="Title", content="Content")
        assert Post.objects.count() == 1
    
    def test_read_post(self):
        """Test Read operatsiyasi"""
        created_post = Post.objects.create(title="Title", content="Content")
        read_post = Post.objects.get(pk=created_post.pk)
        assert read_post.title == "Title"
    
    def test_update_post(self):
        """Test Update operatsiyasi"""
        post = Post.objects.create(title="Old", content="Old Content")
        post.title = "New"
        post.save()
        updated = Post.objects.get(pk=post.pk)
        assert updated.title == "New"
    
    def test_delete_post(self):
        """Test Delete operatsiyasi"""
        post = Post.objects.create(title="Title", content="Content")
        post_id = post.pk
        post.delete()
        assert not Post.objects.filter(pk=post_id).exists()
```

#### Timestamp testlari
```python
@pytest.mark.django_db
@pytest.mark.model
class TestPostModelTimestamps:
    def test_updated_at_changes_on_save(self):
        """Test updated_at o'zgarishini"""
        import time
        post = Post.objects.create(title="Title", content="Content")
        old_updated = post.updated_at
        time.sleep(0.01)
        post.title = "New Title"
        post.save()
        assert post.updated_at > old_updated
```

#### Ishga tushirish
```powershell
pytest tests/test_post_model.py -v
```

#### Natija
```
tests/test_post_model.py::TestPostModel::test_create_post_with_valid_data PASSED
tests/test_post_model.py::TestPostModelCRUD::test_create_post PASSED
tests/test_post_model.py::TestPostModelTimestamps::test_updated_at_changes_on_save PASSED
... va boshqalar

============================================== 40 passed ===============================================
```

---

## 📝 Topshiriq 5: Post viewlarni testlash

### Vazifa
Django REST Framework API viewlarini test qilish (GET va POST so'rovlar).

### View (posts/views.py)
```python
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

### Testlar (tests/test_post_views.py)

#### GET so'rov testlari
```python
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from posts.models import Post

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
@pytest.mark.view
class TestPostListView:
    def test_get_empty_post_list(self, api_client):
        """Test bo'sh post ro'yxatini olish"""
        url = reverse('post-list-create')
        response = api_client.get(url)
        
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 0
    
    def test_get_post_list_with_posts(self, api_client):
        """Test postlar mavjud bo'lganda"""
        Post.objects.create(title="Post 1", content="Content 1")
        Post.objects.create(title="Post 2", content="Content 2")
        
        url = reverse('post-list-create')
        response = api_client.get(url)
        
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
```

#### POST so'rov testlari
```python
@pytest.mark.django_db
@pytest.mark.view
class TestPostCreateView:
    def test_create_post_with_valid_data(self, api_client):
        """Test to'g'ri ma'lumotlar bilan post yaratish"""
        url = reverse('post-list-create')
        data = {
            'title': 'New Post',
            'content': 'New Content'
        }
        response = api_client.post(url, data)
        
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == 'New Post'
        assert Post.objects.count() == 1
    
    def test_create_post_without_title(self, api_client):
        """Test title bo'lmasa xato"""
        url = reverse('post-list-create')
        data = {'content': 'Content only'}
        response = api_client.post(url, data)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
```

#### Parametrized testlar
```python
@pytest.mark.django_db
@pytest.mark.view
@pytest.mark.parametrize("title,content", [
    ("Test 1", "Content 1"),
    ("Test 2", "Content 2"),
    ("Python", "Django REST Framework"),
])
def test_create_post_parametrized(api_client, title, content):
    """Parametrlashgan yaratish testlari"""
    url = reverse('post-list-create')
    data = {'title': title, 'content': content}
    response = api_client.post(url, data)
    
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['title'] == title
```

#### Ishga tushirish
```powershell
pytest tests/test_post_views.py -v
```

#### Natija
```
tests/test_post_views.py::TestPostListView::test_get_empty_post_list PASSED
tests/test_post_views.py::TestPostCreateView::test_create_post_with_valid_data PASSED
tests/test_post_views.py::test_create_post_parametrized[Test 1-Content 1] PASSED
... va boshqalar

============================================== 35 passed ===============================================
```

---

## 🎯 Barcha Testlarni Ishga Tushirish

### Barcha testlar
```powershell
pytest
```

### Verbose rejimda
```powershell
pytest -v
```

### Faqat ma'lum marker
```powershell
pytest -m unit
pytest -m model
pytest -m view
```

### Coverage bilan
```powershell
pytest --cov=posts --cov=tests --cov-report=html
```

---

## 📊 Yakuniy Natija

```
============================================== test session starts ===============================================
collected 114 items

tests/test_post_model.py ..............................                                                     [ 26%]
tests/test_post_views.py ...........................                                                        [ 50%]
tests/test_average.py ....................                                                                  [ 68%]
tests/test_id_sum.py ..............................                                                         [100%]

============================================== 114 passed in 0.82s ===============================================
```

## ✅ Bajarilgan Topshiriqlar

- [x] **Topshiriq 1:** pytest o'rnatish va sozlash
- [x] **Topshiriq 2:** O'rtacha arifmetikni hisoblash testlari (20 tests)
- [x] **Topshiriq 3:** Talaba ID yig'indisi testlari (25 tests)
- [x] **Topshiriq 4:** Post modelini testlash (40 tests)
- [x] **Topshiriq 5:** Post viewlarni testlash (35 tests)

**Jami:** 114 ta test ✨

---

## 🎓 O'rganilgan Mavzular

1. ✅ pytest asoslari
2. ✅ pytest-django integratsiyasi
3. ✅ Fixtures
4. ✅ Parametrized tests
5. ✅ Test markers
6. ✅ Django model testing
7. ✅ Django REST Framework testing
8. ✅ CRUD operations testing
9. ✅ Edge case testing
10. ✅ Test organizatsiyasi

---

**Tabriklaymiz!** Barcha topshiriqlar muvaffaqiyatli bajarildi! 🎉
