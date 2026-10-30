from uuid import uuid4

import qrcode
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.text import slugify

from django.conf import settings


# Create your views here.
def index(request):
    # request.POST.get('url')
    create_qr('https://www.youtube.com/watch?v=oecbll5hk-o&pp=kggWbXZzLWFjcS15Y20tZGh1Yi13ZWIwYQ%3D%3D')
    return HttpResponse("QR GENERER")

def create_qr(chemin):
    dossier = settings.MEDIA_ROOT / "qr"
    dossier.mkdir(parents=True, exist_ok=True)

    image = qrcode.make(chemin)
    nom = f'{uuid4().hex}.png'
    destination = settings.MEDIA_ROOT / 'qr' / nom
    image.save(destination)
    print(destination)
