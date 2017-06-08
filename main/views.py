from django.shortcuts import render, get_object_or_404, render_to_response
from .models import *


def get_bg():
    bg_all = BG_image.objects.filter(display=True)

    id_bg = []
    for i in bg_all:
        id_bg.append(i.id)

    if len(bg_all)>0:
        id_max = max(id_bg)
        bg = get_object_or_404(BG_image, id=id_max)
        return bg
    else:
        return None

# Create your views here.

def main(request):
    bg = get_bg()

    main_text = get_object_or_404(MainText, display=True)
    musicians = Musician.objects.filter(display=True)

    return render(request, 'index.html', {'bg': bg,
                                          'main_text': main_text,
                                          'musicians': musicians, })


def afisha(request):
    bg = get_bg()
    afisha = Afisha.objects.filter(display=True)

    return render(request, 'afisha.html', {'bg': bg,
                                           'afisha':afisha})


def news(request):
    bg = get_bg()
    news = News.objects.filter(display=True)
    return render(request, 'news.html', {'bg': bg,
                                         'news': news,
                                         })


def media():
    bg = get_bg()
    return render_to_response('media.html', {'bg': bg})


def music(request):
    bg = get_bg()
    alboom = AudioAlboom.objects.all()
    audio = AudioFile.objects.all()

    return render(request,'music.html', {'bg': bg, 'audios':audio, 'albooms':alboom})













def photo(request, alboom_id=None):
    bg = get_bg()
    alboom = None
    albooms = Photo_Alboom.objects.filter(display=True)
    photo = Photo.objects.all()
    photos = []
    if alboom_id:
        alboom = get_object_or_404(Photo_Alboom, id=alboom_id)
        photos = photo.filter(photo_alboom=alboom)
        return render(request, 'alboom_detail.html', {
            'photos': photos,
            'alboom': alboom,
            'bg': bg
        })
    return render(request, 'photo.html', {
        'alboom': alboom,
        'albooms': albooms,
        'photos': photos,
        'bg': bg
    })

def video(request):
    bg = get_bg()
    videos = Video.objects.filter(display=True)
    return render(request, 'video.html', {'bg': bg,
                                          'videos': videos})


def contacts(request):
    bg = get_bg()
    return render(request, 'contacts.html', {'bg': bg})
