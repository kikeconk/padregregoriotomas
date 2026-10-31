from pathlib import Path
from django.conf import settings
from django.shortcuts import render

def inicio(request):
    carpeta_galeria = Path(settings.BASE_DIR) / "static" / "galeria"
    carpeta_biografia = Path(settings.BASE_DIR) / "static" / "biografia"

    extensiones = {".jpg", ".jpeg", ".png", ".webp"}

    imagenes = sorted([
        f.name for f in carpeta_galeria.iterdir()
        if f.is_file() and f.suffix.lower() in extensiones
    ]) if carpeta_galeria.exists() else []

    fotos_biografia = sorted([
        f.name for f in carpeta_biografia.iterdir()
        if f.is_file() and f.suffix.lower() in extensiones
    ]) if carpeta_biografia.exists() else []

    return render(request, "index.html", {
        "imagenes": imagenes,
        "fotos_biografia": fotos_biografia,
    })
