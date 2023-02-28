from django.contrib import admin
from django.urls import path

from apps.library_app.views import get_books, get_book_by_id, create_book, update_book, delete_book
from apps.task_app.views import get_task_by_id, get_tasks, create_task, update_task, delete_task

urlpatterns = [
    path('admin/', admin.site.urls),

    path('book/<int:pk>/', get_book_by_id),
    path('books/', get_books),
    path('create_book/', create_book),
    path('update_book/<int:pk>/', update_book),
    path('delete_book/<int:pk>/', delete_book),

    path('task/<int:pk>/', get_task_by_id),
    path('tasks/', get_tasks),
    path('create_task/', create_task),
    path('update_task/<int:pk>/', update_task),
    path('delete_task/<int:pk>/', delete_task),
]
