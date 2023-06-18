from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, verbose_name=(
        "İstifadəçi Adı"), on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(verbose_name="Başlıq", max_length=255)
    description = models.TextField(
        verbose_name="Aşıqlama", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Aktiv", default=True)
    is_completed = models.BooleanField(
        verbose_name="Tamamlandı", default=False)
    created_at = models.DateTimeField(
        verbose_name="Yaradılma Vaxtı", auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name="Yenilənmə Vaxtı", auto_now=True)
    is_deleted = models.BooleanField(verbose_name="Silindi", default=False)
    slug = AutoSlugField(populate_from='title', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("Todo")
        verbose_name_plural = ("Todolar")


class Favorite(models.Model):
    user = models.OneToOneField(
        User, related_name='favorited_by', on_delete=models.CASCADE, verbose_name=("İstifadəçi"))
    todos = models.ManyToManyField(
        'Todo', related_name='favorites', verbose_name=("Favorilər"))

    def __str__(self):
        return f"{self.user}"

    def add_todo_to_favorites(self, todo):
        self.todos.add(todo)

    def remove_todo_from_favorites(self, todo):
        self.todos.remove(todo)

    class Meta:
        verbose_name = ("Favori")
        verbose_name_plural = ("Favorilər")
