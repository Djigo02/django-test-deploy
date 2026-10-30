import os
import random

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.utils.text import slugify
from django.conf import settings

def index(request):
    message = None
    if request.method == "POST" and request.FILES.get("couverture"):
        couverture = request.FILES.get('couverture')
        titre = request.POST.get('titre')
        ext = couverture.content_type.split('/')[-1]
        uniq = random.randint(100, 10000)
        filename = slugify(titre) +"-" + str(uniq)+ "."  + ext
        dest = os.path.join(settings.BASE_DIR, "static/assets")
        print("Le nom du fichier est : ",dest)

        fs = FileSystemStorage(location=dest)
        try:
            fs.save(filename, couverture)
            message = {
                "success": True,
                "message": "Le fichier est bien enregistre",
            }
        except OSError:
            message = {
                "success" : False,
                "message" : "Le fichier n'est pas bien enregistrer"
            }

    return render(request, "index.html", {"message": message})