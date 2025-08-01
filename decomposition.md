# Декомпозиция задачи

1. Настройка проекта Django:

 - Создать проект Django (django-admin startproject).
 - Создать приложение для логики сети (python manage.py startapp).
 - Настроить settings.py (добавить приложение, базу данных, DRF).

2. Модели данных

2.1. Модель контактов (Contact)
 - Поля:
     - email (EmailField)
     - country (CharField)
     - city (CharField)
     - street (CharField)
     - house_number (CharField)

2.2. Модель продукта (Product)
 - Поля:
     - name (CharField)
     - model (CharField)
     - release_date (DateField)

2.3. Модель звена сети (NetworkNode)
 - Поля:
     - name (CharField)
     - contacts (OneToOne → Contact)
     - products (ManyToMany → Product)
     - supplier (ForeignKey → self, null=True, blank=True)
     - debt_to_supplier (DecimalField, max_digits=12, decimal_places=2)
     - created_at (DateTimeField, auto_now_add=True)
     - level (IntegerField, choices: 0-завод, 1-розничная сеть, 2-ИП)

3. Миграции
 - Создать миграции (python manage.py makemigrations).
 - Применить миграции (python manage.py migrate).

4. Админ-панель

4.1. Настройка отображения моделей
 - Зарегистрировать Contact, Product, NetworkNode в admin.py.
 - Добавить list_display, list_filter, search_fields.

4.2. Кастомизация страницы объекта NetworkNode
 - Добавить ссылку на поставщика (@admin.display).
 - Добавить фильтр по городу (list_filter).
 - Создать admin action для обнуления задолженности.

5. Django REST Framework (DRF)

5.1. Сериализаторы
 - Создать serializers.py для NetworkNode.
 - Запретить обновление debt_to_supplier (read_only_fields).

5.2. ViewSet (CRUD)
 - Создать ViewSet для NetworkNode.
 - Подключить ModelViewSet с кастомными ограничениями.

5.3. Фильтрация по стране
 - Использовать DjangoFilterBackend или filterset_class.

5.4. Права доступа
 - Настроить IsAuthenticated и кастомный пермишен (IsActiveUser).

6. Тестирование
 - Проверить API через Postman/Swagger.
 - Проверить админку (фильтры, действия).

## Дополнительные улучшения (если успею)
 - Логирование изменений (кто и когда менял задолженность).
 - Валидация данных (например, запрет циклических зависимостей в supplier).
 - Документация API (Swagger/Redoc).
 - Тесты (unit-тесты для моделей и API).
