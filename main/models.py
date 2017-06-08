from django.db import models
from audiofield.fields import AudioField
from django.conf import settings
import os.path
from django.core.urlresolvers import reverse
# Create your models here.

class BG_image(models.Model):
    #name = models.CharField(max_length=60, blank=True, verbose_name=' название изображения')
    bg = models.ImageField(upload_to='backgrouns/%Y/%m/%d/', blank=True, verbose_name='Фоновое Изображение 1920х1080 px ')
    display = models.BooleanField(blank=True, default=True, verbose_name='Использовать как фон')
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='дата изменения')

    class Meta:
        ordering = ['bg']
        verbose_name = 'Фоновое Изображение'
        verbose_name_plural = 'Фоновые Изображения'

    def image_img(self):
        if self.bg:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.bg.url)
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True


class Photo_Alboom(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='albooms/%Y/%m/%d/', blank=True, verbose_name="Изображение Альбома")
    display = models.BooleanField(blank=True, default=True, verbose_name='Отображать на странице/ не отображать')

    class Meta:
        ordering = ['name']
        verbose_name = 'ФотоАльбом'
        verbose_name_plural = 'ФотоАльбомы'

    def image_img(self):
        if self.image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url)
        else:
            return '(Нет изображения)'
    def __str__(self):
        return self.name
    
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

    #def get_absolute_url(self):
     #   return reverse('photo', args=[self.slug])


# Модель продукта
class Photo(models.Model):
    photo_alboom = models.ForeignKey(Photo_Alboom, related_name='products', verbose_name="Фото Альбом")
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image_sm = models.ImageField(upload_to='small_photo/%Y/%m/%d/', blank=True, verbose_name="предпросмотр")
    image = models.ImageField(upload_to='lg_photo/%Y/%m/%d/', blank=True, verbose_name="фотография")
    description = models.TextField(blank=True, verbose_name="Описание фотографии")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    display = models.BooleanField(blank=True, default=True, verbose_name='Отображать на странице/ не отображать')

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return self.name

    def image_img(self):
        if self.image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url)
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

class MainText(models.Model):
    text_header = models.CharField(blank=True, max_length=300, verbose_name='Заголовок главного текста(например '
                                                                            'название группы)')
    main_text = models.TextField(blank=True, verbose_name='Главный текс (о группе)')
    display = models.BooleanField(blank=True, default=True, verbose_name='Отображать на странице/ не отображать')

    class Meta:
        ordering = ['text_header']
        verbose_name = 'Заголовок'
        verbose_name_plural = 'Главный Текст'

class Musician(models.Model):
    m_photo = models.ImageField(upload_to='musician', blank=True, verbose_name='Фотография участника группы')
    name = models.CharField(max_length=200, verbose_name='Имя(в любом формате')
    desc = models.TextField(verbose_name='Подробная информация/ описание/ биография и т.д.')
    links = models.CharField(max_length=500, blank=True, verbose_name='Ссылки на другие проекты/ профили')
    display = models.BooleanField(blank=True, default=True, verbose_name='Отображать на странице/ не отображать')

    class Meta:
        #ordering = ['name']
        verbose_name = 'Участник Группы'
        verbose_name_plural = 'Участники группы'


class News(models.Model):
    header = models.CharField(max_length=200, blank=True, verbose_name='Заголовок (200 символов)')
    body = models.TextField(blank=True, verbose_name='Текст Новостей')
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='дата изменения')
    display = models.BooleanField(blank=True, default=True, verbose_name='Отображать на странице/ не отображать')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Video(models.Model):
    header = models.CharField(max_length=200, blank=True, verbose_name='Заголовок (200 символов)')
    body = models.CharField(max_length=500, blank=True, verbose_name='код видео(заходим на YuoTube, выбираем "поделиться" и копируем все что после "https://youtu.be/" сюда!')
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='дата изменения')
    display = models.BooleanField(blank=True, default=True, verbose_name='Отображать на странице/ не отображать')

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class Afisha(models.Model):
    header1 = models.CharField(max_length=200, blank=True, verbose_name='Заголовок 1 ( h4 200 символов)')
    header2 = models.CharField(max_length=200, blank=True, verbose_name='Заголовок 2 ( h1 200 символов)')
    header3 = models.CharField(max_length=200, blank=True, verbose_name='Заголовок 3 ( h2 200 символов)')
    header4 = models.CharField(max_length=200, blank=True, verbose_name='Заголовок 4 ( h3 200 символов)')
    header5 = models.CharField(max_length=200, blank=True, verbose_name='Заголовок 5 (h4 200 символов)')
    image = models.ImageField(upload_to='afisha/%Y/%m/%d/', blank=True, verbose_name="Афиша  150х200px")
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='дата изменения')
    display = models.BooleanField(blank=True, default=True, verbose_name='Отображать на странице/ не отображать')

    class Meta:
        verbose_name = 'Афиша'
        verbose_name_plural = 'Афиши'


class AudioAlboom(models.Model):
    alboom_name = models.CharField(max_length=100,blank=True)
    image = models.ImageField(upload_to="audio_alboom", blank=True)
    desc = models.TextField(verbose_name='Описание(Не обязательно)', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='дата изменения')

    def __str__(self):
        return self.alboom_name



class AudioFile(models.Model):
    #author = models.CharField(max_length=50, blank=True)
    #alboom = models.CharField(max_length=30,blank=True)
    alboom = models.ForeignKey(AudioAlboom,related_name='alboom_namel',verbose_name='Альбом')
    name = models.CharField(max_length=30, blank=True)
    audio_file = AudioField(upload_to='audio/', blank=True,
                            ext_whitelist=(".mp3", ".wav", ".ogg"),
                            help_text=("Allowed type - .mp3, .wav, .ogg"))
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='дата изменения')

    def audio_file_player(self):
        """audio player tag for admin"""
        if self.audio_file:
            file_url = settings.MEDIA_URL + str(self.audio_file)
            player_string = '<ul class="playlist"><li style="width:250px;">\
            <a href="%s">%s</a></li></ul>' % (file_url, os.path.basename(self.audio_file.name))

            return player_string


    def path_audio_file(self):
        name = self.audio_file
        path = os.getcwd()
        return os.path.join('/media/',str(name))

    def __str__(self):
        return self.name

    audio_file_player.allow_tags = True
    audio_file_player.short_description = 'Audio file player'