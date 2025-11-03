# 15-dars: Yakuniy Loyiha

## 🎯 Maqsad

Django admin panel loyihasini yaratish va ma'lumotlar bazasi bilan ishlash. Talabalar ma'lumotlarini boshqarish tizimi.

## 📋 Topshiriqlar

1. ✅ Yakuniy loyihada students va profile modellarini yarating
2. ✅ sign_in, sign_up va logout viewlarini ishlatish
3. ✅ Barcha talabalarni ko'rsatish
4. ✅ Yangi talaba qo'shish, o'chirish va o'zgartirish funksiyalari
5. ✅ Guruh va jdu_id bo'yicha qidiruv

## 🚀 Ishga Tushirish

```powershell
# Lesson 15 papkasiga o'tish
cd "d:\Universitet\JDU\Django\Lesson 15"

# Virtual environment aktivlashtirish
.\.venv\Scripts\Activate.ps1

# Serverni ishga tushirish
python manage.py runserver
```

## 🔐 Test Ma'lumotlar

### Superuser:
- **Username:** admin
- **Password:** admin123
- **Email:** admin@jdu.uz

### Talabalar:
1. Ali Valiyev - JDU001 - N11 guruh
2. Dilnoza Karimova - JDU002 - N11 guruh
3. Bobur Rahimov - JDU003 - N12 guruh

## 📱 Sahifalar

- **http://127.0.0.1:8000/** - Sign In (Login)
- **http://127.0.0.1:8000/sign-up/** - Sign Up (Register)
- **http://127.0.0.1:8000/students/** - Talabalar ro'yxati
- **http://127.0.0.1:8000/profile/** - Profil
- **http://127.0.0.1:8000/admin/** - Django Admin Panel

## ✨ Funksiyalar

### 1. Autentifikatsiya
- ✅ Sign In (username va password tekshirish)
- ✅ Sign Up (yangi foydalanuvchi yaratish)
- ✅ Logout (redirect bilan)
- ✅ Profile boshqaruvi

### 2. Student CRUD
- ✅ **Create:** Yangi talaba qo'shish
- ✅ **Read:** Barcha talabalarni ko'rish
- ✅ **Update:** Talaba ma'lumotlarini tahrirlash
- ✅ **Delete:** Talabani o'chirish

### 3. Qidiruv
- ✅ JDU ID bo'yicha qidiruv
- ✅ Guruh bo'yicha qidiruv
- ✅ Ism bo'yicha qidiruv
- ✅ Familiya bo'yicha qidiruv

### 4. Admin Panel
- ✅ Superadmin foydalanuvchi
- ✅ Students admin interface
- ✅ Profiles admin interface
- ✅ Qidiruv va filtrlash

## 📊 Model Strukturasi

### Student Model
```python
- jdu_id: CharField (unique)
- first_name: CharField
- last_name: CharField
- email: EmailField (unique)
- phone: CharField
- guruh: CharField
- course: IntegerField
- created_at: DateTimeField
- updated_at: DateTimeField
```

### Profile Model
```python
- user: OneToOneField(User)
- bio: TextField
- avatar: ImageField
- phone: CharField
- address: TextField
- birth_date: DateField
- created_at: DateTimeField
- updated_at: DateTimeField
```

## 🎨 UI Features

- Modern Bootstrap 5 dizayn
- Responsive layout
- Modal forms (Add/Edit)
- Search bar
- Statistics cards
- Icon lar (Font Awesome)
- Success/Error messages
- Confirm dialogs

## 📝 O'zgarishlar (Lesson 14 dan)

1. ✅ `student_id` → `jdu_id` (model field rename)
2. ✅ `guruh` maydoni qo'shildi
3. ✅ `login_page` → `sign_in` (view rename)
4. ✅ `register_page` → `sign_up` (view rename)
5. ✅ Search funksiyasi qo'shildi (guruh va jdu_id)
6. ✅ CRUD operatsiyalari to'liq amalga oshirildi

## ✅ Natija

Barcha topshiriqlar muvaffaqiyatli bajarildi! Loyiha to'liq ishga tushirildi va test qilindi.

**Server URL:** http://127.0.0.1:8000/
