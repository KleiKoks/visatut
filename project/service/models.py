from django.db import models
from tinymce import HTMLField
from django.urls import reverse 


class StaticService(models.Model):
    title     = models.CharField(verbose_name=('Заголовок'), max_length=255)
    text      = HTMLField(verbose_name=("Текст"), blank=True, null=True)
    img_alt         = models.CharField(verbose_name='Альт картинки', max_length=100, blank=True, null=True, default=' ')
    thumbnail = models.ImageField(verbose_name=("Зображення"), blank=True, null=True, upload_to='static_service/')
    meta_title      = models.CharField(verbose_name='Мета-заголовок', max_length=255, blank=True, null=True)
    meta_descr      = models.TextField(verbose_name=("Мета-опис"), blank=True, null=True)
    meta_key        = models.TextField(verbose_name=("Мета-ключі"), blank=True, null=True)
    
    def get_thumbnail_url(self):
        thumbnail_url = ''
        if self.thumbnail:
            thumbnail_url = self.thumbnail.url
        return thumbnail_url
    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Сервіс' 
        verbose_name_plural = 'Сервіси' 


class Service(models.Model):
    title      = models.CharField(verbose_name=('Заголовок'), max_length=255)
    categories = models.ManyToManyField(verbose_name=("Категорії послуги"), to="service.ServiceCategory", related_name='services')
    countries  = models.ManyToManyField(verbose_name=("Країни"), to="service.Country",         related_name='services')
    header     = models.TextField(verbose_name=("Підзаголовок"), blank=True, null=True, max_length=1000)
    advantages = HTMLField(verbose_name=("Переваги"),            blank=True, null=True)
    procedure  = HTMLField(verbose_name=("Процедура відкриття"), blank=True, null=True)
    addition   = HTMLField(verbose_name=("Додаткові вимоги"),    blank=True, null=True)
    meta_title      = models.CharField(verbose_name='Мета-заголовок', max_length=255, blank=True, null=True)
    meta_descr      = models.TextField(verbose_name=("Мета-опис"), blank=True, null=True)
    meta_key        = models.TextField(verbose_name=("Мета-ключі"), blank=True, null=True)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Сервіс по країнах' 
        verbose_name_plural = 'Сервіси по країнах' 


class ServiceCategory(models.Model):
    title     = models.CharField(verbose_name=('Назва'), max_length=255)
    img_alt         = models.CharField(verbose_name='Альт картинки', max_length=100, blank=True, null=True, default=' ')
    thumbnail = models.ImageField(verbose_name=("Зображення"), blank=True, null=True, upload_to='service_category/')
    meta_title      = models.CharField(verbose_name='Мета-заголовок', max_length=255, blank=True, null=True)
    meta_descr      = models.TextField(verbose_name=("Мета-опис"), blank=True, null=True)
    meta_key        = models.TextField(verbose_name=("Мета-ключі"), blank=True, null=True)

    def __str__(self):
        return f'{self.title}'
    
    def get_thumbnail_url(self):
        thumbnail_url = ''
        if self.thumbnail:
            thumbnail_url = self.thumbnail.url
        return thumbnail_url
    
    class Meta:
        verbose_name = ('Категорія сервісу')
        verbose_name_plural = ('Категорія сервісу')



class Country(models.Model):
    title      = models.CharField(verbose_name=("Назва"), max_length=255)
    img_alt         = models.CharField(verbose_name='Альт картинки', max_length=100, blank=True, null=True, default=' ')
    thumbnail  = models.ImageField(verbose_name=("Зображення"), blank=True, null=True, upload_to='country/')
    categories = models.ManyToManyField(verbose_name=("Категорії"), to='service.ServiceCategory', related_name='countries', related_query_name='country', blank=False)
    meta_title      = models.CharField(verbose_name='Мета-заголовок', max_length=255, blank=True, null=True)
    meta_descr      = models.TextField(verbose_name=("Мета-опис"), blank=True, null=True)
    meta_key        = models.TextField(verbose_name=("Мета-ключі"), blank=True, null=True)

    def __str__(self):
        return f'{self.title}'
    
    def get_thumbnail_url(self):
        thumbnail_url = ''
        if self.thumbnail:
            thumbnail_url = self.thumbnail.url
        return thumbnail_url

    class Meta:
        verbose_name = 'Країна' 
        verbose_name_plural = 'Країни'



















