import sys
from pathlib import Path
from PIL import Image, ImageOps

# =========================
# CONFIGURACIÓN
# =========================

LADO_LARGO_MAX = 2000
CALIDAD_JPG = 82
CONVERTIR_A_JPG = True
EXTENSIONES = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff"}

def optimizar_imagen(ruta_entrada: Path, ruta_salida: Path) -> None:
    """
    Toma una imagen, la redimensiona a A5 (~2000px lado largo), 
    la convierte a JPG y la guarda comprimida.
    """
    with Image.open(ruta_entrada) as img:
        # Corrige orientación EXIF de móviles/cámaras
        img = ImageOps.exif_transpose(img)

        # Convierte a RGB para JPG
        if img.mode in ("RGBA", "LA", "P"):
            fondo = Image.new("RGB", img.size, (255, 255, 255))
            if img.mode == "P":
                img = img.convert("RGBA")
            fondo.paste(img, mask=img.split()[-1] if img.mode in ("RGBA", "LA") else None)
            img = fondo
        else:
            img = img.convert("RGB")

        ancho, alto = img.size
        lado_largo_actual = max(ancho, alto)

        # Redimensiona solo si es más grande
        if lado_largo_actual > LADO_LARGO_MAX:
            escala = LADO_LARGO_MAX / lado_largo_actual
            nuevo_ancho = round(ancho * escala)
            nuevo_alto = round(alto * escala)

            img = img.resize(
                (nuevo_ancho, nuevo_alto),
                Image.Resampling.LANCZOS
            )

        # Guarda como JPG optimizado
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)

        # Forzar extensión de salida si el path no termina en jpg
        if CONVERTIR_A_JPG and ruta_salida.suffix.lower() not in ['.jpg', '.jpeg']:
            ruta_salida = ruta_salida.with_suffix('.jpg')

        img.save(
            ruta_salida,
            format="JPEG",
            quality=CALIDAD_JPG,
            optimize=True,
            progressive=True,
            dpi=(300, 300)
        )

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python optimizar_imagenes_a5.py <carpeta_entrada> <carpeta_salida>")
        sys.exit(1)
        
    entrada = Path(sys.argv[1])
    salida_dir = Path(sys.argv[2])
    
    salida_dir.mkdir(parents=True, exist_ok=True)

    imagenes = [
        p for p in entrada.rglob("*")
        if p.is_file() and p.suffix.lower() in EXTENSIONES
    ]

    if not imagenes:
        print(f"No se han encontrado imágenes en: {entrada.resolve()}")
        sys.exit(0)

    for ruta in imagenes:
        relativa = ruta.relative_to(entrada)
        salida = salida_dir / relativa
        if CONVERTIR_A_JPG:
            salida = salida.with_suffix(".jpg")

        peso_antes = ruta.stat().st_size / 1024 / 1024
        try:
            optimizar_imagen(ruta, salida)
            peso_despues = salida.stat().st_size / 1024 / 1024
            print(f"OK: {ruta.name} {peso_antes:.2f} MB -> {peso_despues:.2f} MB")
        except Exception as ex:
            print(f"ERROR en {ruta.name}: {ex}")
