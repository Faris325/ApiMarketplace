📦 Products REST API (Django + DRF)

REST API для управления товарами и историей изменения цен.
Проект позволяет создавать товары, отслеживать изменения цен и получать аналитику по росту/снижению стоимости.

🚀 Технологии
Python 3.x
Django
Django REST Framework
SimpleJWT (аутентификация)
Djoser (регистрация/управление пользователями)
Django Filter
📌 Основные возможности
CRUD операции с товарами
Автоматическое сохранение истории цен
Получение средней цены товара за период
Расчёт процентного изменения цены
Получение топа товаров по росту цены
JWT авторизация
🔐 Авторизация

Используется JWT.

Получить токен:
POST /api/v1/token/

Body:

{
  "username": "user",
  "password": "password"
}
Refresh токена:
POST /api/token/refresh/
Проверка токена:
POST /api/token/verify/
📦 Endpoints

Базовый URL:

/api/v1/
🛍️ Products API
📥 Получить список товаров
GET /api/v1/product/

📌 Поддерживается:

пагинация (page, page_size)
фильтрация (через ProductFilter)
➕ Создать товар
POST /api/v1/product/

Body:

{
  "name": "iPhone 15",
  "category": "phones",
  "price": 1000,
  "quantity": 5
}

📌 При создании автоматически сохраняется история цены.

🔍 Получить товар
GET /api/v1/product/{id}/
✏️ Обновить товар
PUT /api/v1/product/{id}/

📌 При изменении цены автоматически создаётся запись в PriceHistory.

❌ Удалить товар
DELETE /api/v1/product/{id}/
📊 Дополнительные endpoints
📈 Средняя цена товара
GET /api/v1/product/{id}/average_price/
🔹 С параметрами даты:
GET /api/v1/product/{id}/average_price/?start=2024-01-01&end=2024-12-31

Ответ:

{
  "avg_price": 123.45
}
📉 Изменение цены в процентах
GET /api/v1/product/{id}/price_change_percentage/

Ответ:

{
  "price_change": 15.5,
  "unit": "%"
}
🚀 Топ товаров по росту цены
GET /api/v1/product/top_price_growth_products/

📌 Возвращает топ товаров с наибольшим ростом цены.

Ответ:

{
  "results": [
    {
      "name": "iPhone 15",
      "category": "phones",
      "price": 1200,
      "quantity": 3,
      "price_change": 25.3
    }
  ]
}
🧠 Особенности логики
📌 При создании товара автоматически создаётся запись в PriceHistory
📌 При изменении цены сохраняется новая история
📌 Аналитика считается на основе исторических данных
⚙️ Установка и запуск
git clone <repo-url>
cd <project>

python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
📌 Пример фильтрации

(если настроено через ProductFilter)

GET /api/v1/product/?category=phones&price__gte=500
