# Products API

API для управления товарами и отслеживания истории изменения цен. Предоставляет возможности CRUD операций с товарами, анализ ценовых изменений и рейтинг товаров по росту цены.

## 📋 Содержание

- [Технологии](#технологии)
- [Функциональность](#функциональность)
- [Установка и запуск](#установка-и-запуск)
- [Конфигурация](#конфигурация)
- [API Эндпоинты](#api-эндпоинты)
- [Примеры запросов](#примеры-запросов)
- [Модели данных](#модели-данных)
- [Docker](#docker)

## 🛠 Технологии

- Django + Django REST Framework
- PostgreSQL
- Djoser (аутентификация)
- SimpleJWT (JWT токены)
- Docker & Docker Compose
- Django Filters

## ✨ Функциональность

- **CRUD операции** с товарами
- **Автоматическое отслеживание истории цен** при создании/обновлении товара
- **Фильтрация товаров** по различным параметрам
- **Пагинация** (10 товаров на страницу, настраивается)
- **Анализ цен**:
  - Средняя цена товара за период
  - Процент изменения цены
  - Топ-100 товаров с наибольшим ростом цены
- **JWT аутентификация**

## 🚀 Установка и запуск
---------------------------------------------------------

## 🔐 Аутентификация

| Метод | URL | Пример тела запроса |
|:-----:|-----|---------------------|
| **POST** | `/auth/users/` | `{"username": "user", "password": "pass123", "email": "user@example.com"}` |
| **POST** | `/auth/jwt/create/` | `{"username": "user", "password": "pass123"}` |
| **POST** | `/api/token/` | `{"username": "user", "password": "pass123"}` |
| **POST** | `/api/token/refresh/` | `{"refresh": "your_refresh_token"}` |
| **POST** | `/api/token/verify/` | `{"token": "your_access_token"}` |

---

## 📦 Товары (CRUD)

| Метод | URL | Описание |
|:-----:|-----|----------|
| **GET** | `/api/v1/product/` | 📋 Список товаров (с фильтрацией и пагинацией) |
| **POST** | `/api/v1/product/` | ✨ Создать новый товар |
| **GET** | `/api/v1/product/{id}/` | 🔍 Получить товар по ID |
| **PUT** | `/api/v1/product/{id}/` | 🔄 Полностью обновить товар |
| **PATCH** | `/api/v1/product/{id}/` | ✏️ Частично обновить товар |
| **DELETE** | `/api/v1/product/{id}/` | 🗑️ Удалить товар |

---

## 🔍 Параметры фильтрации для GET `/api/v1/product/`

| Параметр | Тип | Пример | Описание |
|:--------:|:---:|--------|----------|
| `price_min` | `number` | `?price_min=500` | 💰 Цена **больше или равна** |
| `price_max` | `number` | `?price_max=1500` | 💰 Цена **меньше или равна** |
| `category` | `string` | `?category=Смартфоны` | 🏷️ Точное совпадение категории |
| `date_min` | `date` | `?date_min=2024-01-01` | 📅 Дата создания **после или равна** |
| `date_max` | `date` | `?date_max=2024-12-31` | 📅 Дата создания **до или равна** |
| `date` | `date` | `?date=2024-06-15` | 📆 Точное совпадение даты |

---
## 📈 Специальные эндпоинты

| Метод | Эндпоинт | Параметры | Что возвращает |
|:-----:|----------|-----------|----------------|
| **GET** | `/api/v1/product/{id}/average_price/` | `?start=2024-01-01&end=2024-12-31` | 📊 Средняя цена товара |
| **GET** | `/api/v1/product/{id}/price_change_percentage/` | — | 📈 % изменения цены |
| **GET** | `/api/v1/product/top_price_growth_products/` | `?page=1&page_size=20` |Топ-100 товаров по росту цены|


## 📊 Поля товара (Product)

| Поле | Что это | Пример |
|------|---------|--------|
| `name` | Название товара | `"iPhone 15"` |
| `category` | Категория | `"Смартфоны"` |
| `price` | Цена | `999.99` |
| `quantity` | Количество на складе | `50` |
| `created_at` | Дата создания | `"2024-01-15"` |


---


📌 Примеры запросов с фильтрацией

```bash
# Товары в категории "Смартфоны" ценой от 500 до 1000
GET /api/v1/product/?category=Смартфоны&price_min=500&price_max=1000

# Товары, созданные в январе 2024 года
GET /api/v1/product/?date_min=2024-01-01&date_max=2024-01-31

# Товары, созданные 15 июня 2024
GET /api/v1/product/?date=2024-06-15

# Комбинированный фильтр
GET /api/v1/product/?category=Ноутбуки&price_min=1000&date_min=2024-01-01



### Локальный запуск

1. Клонировать репозиторий:
```bash
git clone <your-repo-url>
cd <project-name>
2. Запустиь контейнеры 
docker compose up
3. После запуска Api будет доступно по адресу:
http://localhost:8000



### Примеры HTTP-запросов

# Получить список товаров
GET http://localhost:8000/api/v1/product/

# Получить товар по ID
GET http://localhost:8000/api/v1/product/1/

# Создать новый товар
POST http://localhost:8000/api/v1/product/
Content-Type: application/json

{
    "name": "iPhone 15",
    "category": "Смартфоны",
    "price": 999.99,
    "quantity": 10
}

# Получить среднюю цену товара за период
GET http://localhost:8000/api/v1/product/1/average_price/?start=2024-01-01&end=2024-12-31

# Получить процент изменения цены
GET http://localhost:8000/api/v1/product/1/price_change_percentage/

# Получить топ-100 товаров по росту цены
GET http://localhost:8000/api/v1/product/top_price_growth_products/?page=1&page_size=20

# Получить JWT токен
POST http://localhost:8000/api/token/
Content-Type: application/json

{
    "username": "admin",
    "password": "your_password"
}
