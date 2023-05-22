from django.db import models

CATEGORY_CHOICES = (
    ("PR", "Происшествия"),
    ("POL", "Политика"),
    ("SP", "Спорт"),
    ("KU", "Культура"),
)


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    created = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    category = models.CharField(
        max_length=15, choices=CATEGORY_CHOICES, default="SP", verbose_name="Категория"
    )
    status = models.BooleanField(default=True, verbose_name="Статус публикации")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Запись блога"
        verbose_name_plural = "Записи блога"
        ordering = ("-created",)


class Comment(models.Model):
    username = models.CharField(max_length=16, verbose_name="Имя пользователя")
    text = models.CharField(max_length=300, verbose_name="Текст комментария")
    created = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name="Пост", related_name="post_comment"
    )

    def __str__(self):
        return f"{self.username} - {self.post.title}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
