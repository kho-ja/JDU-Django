# Lesson 13 - Quick Reference

## 🚀 Tezkor Boshlash

### O'rnatish
```powershell
# Virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Paketlar
pip install -r requirements.txt

# Migratsiya
python manage.py migrate
```

### Testlar
```powershell
pytest              # Barcha testlar
pytest -v           # Batafsil
pytest -m unit      # Faqat unit testlar
pytest --cov        # Coverage bilan
```

## 📝 Topshiriqlar (114 tests)

| # | Topshiriq | Testlar | Fayl |
|---|-----------|---------|------|
| 2 | O'rtacha hisoblash | 20 | test_average.py |
| 3 | ID yig'indisi | 25 | test_id_sum.py |
| 4 | Post modeli | 40 | test_post_model.py |
| 5 | Post viewlar | 35 | test_post_views.py |

## 🧪 Test Patterns

### Oddiy Test
```python
def test_example():
    result = my_function(10)
    assert result == 20
```

### Django Model Test
```python
@pytest.mark.django_db
def test_create_post():
    post = Post.objects.create(title="Test")
    assert post.pk is not None
```

### API View Test
```python
@pytest.mark.django_db
def test_api_get(api_client):
    url = reverse('post-list-create')
    response = api_client.get(url)
    assert response.status_code == 200
```

### Parametrized Test
```python
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 1.5),
    (10, 20, 15.0),
])
def test_average(a, b, expected):
    assert calculate_average(a, b) == expected
```

### Fixture
```python
@pytest.fixture
def sample_post():
    return Post.objects.create(
        title="Sample",
        content="Content"
    )
```

## 🎯 Test Markers

```python
@pytest.mark.unit           # Unit test
@pytest.mark.integration    # Integration test
@pytest.mark.model          # Model test
@pytest.mark.view           # View test
@pytest.mark.django_db      # Django database
```

## 📦 Paketlar

```
Django==5.2.7
djangorestframework==3.16.1
pytest==8.4.2
pytest-django==4.11.1
```

## 🔧 pytest.ini

```ini
[pytest]
DJANGO_SETTINGS_MODULE = config.settings
python_files = test_*.py
testpaths = tests
markers = 
    unit: Unit tests
    model: Model tests
    view: View tests
```

## 📊 Test Commands

```powershell
# Run all tests
pytest

# Verbose output
pytest -v

# Specific file
pytest tests/test_average.py

# Specific test
pytest tests/test_average.py::test_average_positive_integers

# By marker
pytest -m unit
pytest -m model

# With coverage
pytest --cov=posts

# Stop on first failure
pytest -x

# Show local variables
pytest -l

# Quiet mode
pytest -q
```

## 🏗️ Project Structure

```
Lesson 13/
├── manage.py
├── pytest.ini
├── requirements.txt
├── config/
│   ├── settings.py
│   └── urls.py
├── posts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
└── tests/
    ├── test_average.py
    ├── test_id_sum.py
    ├── test_post_model.py
    └── test_post_views.py
```

## 💡 Foydali Maslahatlar

### 1. Test Isolation
Har bir test mustaqil bo'lishi kerak:
```python
@pytest.mark.django_db
def test_something():
    # Setup
    post = Post.objects.create(...)
    
    # Test
    assert post.title == "Test"
    
    # No need for cleanup, pytest-django handles it
```

### 2. Descriptive Names
Test nomlari aniq va tushunarli bo'lsin:
```python
def test_create_post_with_valid_data()  # ✅ Yaxshi
def test_post()                          # ❌ Yomon
```

### 3. Arrange-Act-Assert
```python
def test_example():
    # Arrange - ma'lumotlarni tayyorlash
    post = Post.objects.create(...)
    
    # Act - amaliyotni bajarish
    result = post.get_summary()
    
    # Assert - natijani tekshirish
    assert result == "..."
```

### 4. Use Fixtures
Bir xil setup'ni qayta ishlatish:
```python
@pytest.fixture
def sample_data():
    return {"title": "Test", "content": "Content"}

def test_with_fixture(sample_data):
    assert sample_data["title"] == "Test"
```

## 🔍 Debugging

```powershell
# Print output
pytest -s

# PDB debugger
pytest --pdb

# Last failed
pytest --lf

# Failed first
pytest --ff

# Verbose traceback
pytest --tb=long
```

## 📈 Coverage

```powershell
# Basic coverage
pytest --cov=posts

# HTML report
pytest --cov=posts --cov-report=html

# Terminal report
pytest --cov=posts --cov-report=term-missing
```

## 🎓 Resources

- **pytest docs**: https://docs.pytest.org/
- **pytest-django**: https://pytest-django.readthedocs.io/
- **Django testing**: https://docs.djangoproject.com/en/topics/testing/
- **DRF testing**: https://www.django-rest-framework.org/api-guide/testing/

## ✅ Checklist

- [x] pytest o'rnatildi
- [x] pytest.ini konfiguratsiya qilindi
- [x] Test papkasi yaratildi
- [x] 20 unit testlar (average)
- [x] 25 unit testlar (id_sum)
- [x] 40 model testlar
- [x] 35 view testlar
- [x] Barcha 114 test o'tdi ✨

---

**Success Rate: 100%** 🎉
