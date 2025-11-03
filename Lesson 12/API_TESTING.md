# 🧪 API Testing Guide - Lesson 12

## 🚀 Server Ishga Tushirish

```bash
cd "d:\Universitet\JDU\Django\Lesson 12"
.\.venv\Scripts\Activate.ps1
python manage.py runserver
```

Server manzili: **http://127.0.0.1:8000**

---

## 🌐 API Endpoints

### Base URL
```
http://127.0.0.1:8000
```

### Available Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/posts/` | Postlar ro'yxati (pagination) |
| POST | `/api/posts/` | Yangi post yaratish |
| GET | `/api/posts/?page=2` | 2-sahifa |

---

## 📖 API Test Qilish

### 1️⃣ Browser orqali (DRF Browsable API)

**URL:** http://127.0.0.1:8000/api/posts/

**GET Request:**
- Browser'da URL'ni oching
- Postlar ro'yxati ko'rinadi (JSON format)
- Pagination links ko'rinadi

**POST Request:**
- Browsable API'da pastda "HTML form" ni toping
- "Title" va "Content" maydonlarini to'ldiring
- "POST" tugmasini bosing
- Yangi post yaratiladi!

---

### 2️⃣ cURL orqali

#### GET Request - Postlar ro'yxati
```bash
curl http://127.0.0.1:8000/api/posts/
```

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
      "content": "Post matni...",
      "created_at": "2025-11-03T12:00:00Z",
      "updated_at": "2025-11-03T12:00:00Z"
    }
  ]
}
```

#### POST Request - Yangi post yaratish
```bash
curl -X POST http://127.0.0.1:8000/api/posts/ \
  -H "Content-Type: application/json" \
  -d "{\"title\": \"Test post\", \"content\": \"Test mazmun\"}"
```

**Response:**
```json
{
  "message": "Post muvaffaqiyatli yaratildi!",
  "data": {
    "id": 6,
    "title": "Test post",
    "content": "Test mazmun",
    "created_at": "2025-11-03T12:48:00Z",
    "updated_at": "2025-11-03T12:48:00Z"
  }
}
```

---

### 3️⃣ PowerShell orqali

#### GET Request
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/posts/" -Method GET
```

#### POST Request
```powershell
$body = @{
    title = "PowerShell Post"
    content = "PowerShell orqali yaratilgan post"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/posts/" `
  -Method POST `
  -Body $body `
  -ContentType "application/json"
```

---

### 4️⃣ Postman orqali

#### GET Request
1. Yangi request oching
2. Method: **GET**
3. URL: `http://127.0.0.1:8000/api/posts/`
4. Send tugmasini bosing

#### POST Request
1. Yangi request oching
2. Method: **POST**
3. URL: `http://127.0.0.1:8000/api/posts/`
4. Headers:
   - Key: `Content-Type`
   - Value: `application/json`
5. Body:
   - Type: **raw**
   - Format: **JSON**
   - Content:
   ```json
   {
     "title": "Postman Post",
     "content": "Postman orqali yaratilgan post"
   }
   ```
6. Send tugmasini bosing

---

### 5️⃣ Python Requests orqali

#### GET Request
```python
import requests

response = requests.get('http://127.0.0.1:8000/api/posts/')
print(response.json())
```

#### POST Request
```python
import requests

data = {
    'title': 'Python Post',
    'content': 'Python requests orqali yaratilgan post'
}

response = requests.post(
    'http://127.0.0.1:8000/api/posts/',
    json=data
)

print(response.json())
```

---

### 6️⃣ JavaScript Fetch orqali

#### GET Request
```javascript
fetch('http://127.0.0.1:8000/api/posts/')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

#### POST Request
```javascript
fetch('http://127.0.0.1:8000/api/posts/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    title: 'JavaScript Post',
    content: 'JavaScript Fetch orqali yaratilgan post'
  })
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

---

## 🧪 Pagination Test

### 1-sahifa (birinchi 2 ta post)
```bash
curl http://127.0.0.1:8000/api/posts/
# yoki
curl http://127.0.0.1:8000/api/posts/?page=1
```

### 2-sahifa (keyingi 2 ta post)
```bash
curl http://127.0.0.1:8000/api/posts/?page=2
```

### 3-sahifa
```bash
curl http://127.0.0.1:8000/api/posts/?page=3
```

**Eslatma:** Agar sahifada post bo'lmasa, 404 xato qaytadi.

---

## ✅ Expected Responses

### Success Response (201 Created)
```json
{
  "message": "Post muvaffaqiyatli yaratildi!",
  "data": {
    "id": 1,
    "title": "...",
    "content": "...",
    "created_at": "...",
    "updated_at": "..."
  }
}
```

### Pagination Response (200 OK)
```json
{
  "count": 10,
  "next": "http://127.0.0.1:8000/api/posts/?page=2",
  "previous": null,
  "results": [
    {...},
    {...}
  ]
}
```

### Error Response (400 Bad Request)
```json
{
  "title": ["This field is required."],
  "content": ["This field is required."]
}
```

### Not Found (404)
```json
{
  "detail": "Invalid page."
}
```

---

## 📊 Test Scenarios

### Scenario 1: Empty Database
```bash
# GET request
curl http://127.0.0.1:8000/api/posts/
```
**Expected:** 
```json
{
  "count": 0,
  "next": null,
  "previous": null,
  "results": []
}
```

### Scenario 2: Create First Post
```bash
curl -X POST http://127.0.0.1:8000/api/posts/ \
  -H "Content-Type: application/json" \
  -d '{"title": "First Post", "content": "Hello World"}'
```
**Expected:** Status 201, post created

### Scenario 3: Get Posts (1 item)
```bash
curl http://127.0.0.1:8000/api/posts/
```
**Expected:** 1 post in results

### Scenario 4: Create Multiple Posts
```bash
# Post 2
curl -X POST http://127.0.0.1:8000/api/posts/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Second Post", "content": "Post 2"}'

# Post 3
curl -X POST http://127.0.0.1:8000/api/posts/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Third Post", "content": "Post 3"}'
```

### Scenario 5: Test Pagination (3 posts = 2 pages)
```bash
# Page 1 (2 posts)
curl http://127.0.0.1:8000/api/posts/?page=1

# Page 2 (1 post)
curl http://127.0.0.1:8000/api/posts/?page=2
```

### Scenario 6: Invalid Data
```bash
# Empty title
curl -X POST http://127.0.0.1:8000/api/posts/ \
  -H "Content-Type: application/json" \
  -d '{"title": "", "content": "Test"}'
```
**Expected:** Status 400, validation error

---

## 🔍 Validation Rules

### Title Field
- ✅ Required
- ✅ Max length: 200 characters
- ❌ Cannot be empty

### Content Field
- ✅ Required
- ✅ No max length (TextField)
- ❌ Cannot be empty

---

## 🎯 Quick Test Commands

### Test GET
```bash
curl http://127.0.0.1:8000/api/posts/
```

### Test POST
```bash
curl -X POST http://127.0.0.1:8000/api/posts/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Quick Test", "content": "Testing API"}'
```

### Test Pagination
```bash
curl http://127.0.0.1:8000/api/posts/?page=1
curl http://127.0.0.1:8000/api/posts/?page=2
```

---

## 🛠️ Troubleshooting

### Error: Connection refused
**Solution:** Server ishlaganini tekshiring
```bash
python manage.py runserver
```

### Error: 404 Not Found
**Solution:** URL to'g'riligini tekshiring
```
✅ http://127.0.0.1:8000/api/posts/
❌ http://127.0.0.1:8000/posts/
❌ http://127.0.0.1:8000/api/post/
```

### Error: 400 Bad Request
**Solution:** Request body'ni tekshiring
- Content-Type: application/json
- Valid JSON format
- Required fields present

---

## 📝 Notes

- Har bir GET request 2 ta post qaytaradi (pagination)
- 3 ta post bo'lsa, 2 sahifa bo'ladi
- Admin paneldan ham post yaratish mumkin
- DRF Browsable API orqali test qilish eng oson

---

## ✨ Barcha testlar tayyor!

API ishlamoqda va test qilish uchun tayyor! 🚀
