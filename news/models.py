from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150)    # обязательный параметр;для текста малой длины CharField(max_length=)
    content = models.TextField(blank=True)  # атрибут говорит, что данное поле не обязательно к заполнению; TextField
    # для контента большой длины
    created_at = models.DateTimeField(auto_now_add=True)    # при редактировании дата создания новости не изменится
    updated_at = models.DateTimeField(auto_now=True)    # дата редактирования всегда будет меняться
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/') # разбиваем файлы по дате загрузки, в папке photos будет создана папка с
    # датой загрузки и там будут фотки
    is_published = models.BooleanField(default=True)
    # Title - Varchar
    # Content - Text
    # Created_at - DateTime
    # Updated_at - DateTime
    # Photo - Image
    # Is_published - Boolean
