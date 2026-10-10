import os
import shutil

from tkinter import Tk, filedialog, simpledialog, messagebox

ventana = Tk()
ventana.withdraw()

carpeta_clips = filedialog.askdirectory(
    title="Selecciona la carpeta VIDEO"
)

if not carpeta_clips:
    print("No se seleccionó ninguna carpeta. Saliendo del programa.")
    exit()

archivos = os.listdir(carpeta_clips)

clips = simpledialog.askstring(
    "ClipVault",
    "Escribe los clips sin usar separados por comas:"
)

if not clips:
    print("No se ingresaron clips. Saliendo del programa.")
    exit()

clips_sin_usar = clips.split(",")

carpeta_destino = os.path.join(carpeta_clips, "Material sin usar")

os.makedirs(carpeta_destino, exist_ok=True)

copiados = []
no_encontrados = []

for clip in clips_sin_usar:
    clip = clip.strip()
    if not clip:
        continue

    nombre_archivo = clip + ".mp4"

    if nombre_archivo in archivos:
        ruta_origen = os.path.join(carpeta_clips, nombre_archivo)
        ruta_destino = os.path.join(carpeta_destino, nombre_archivo)

        shutil.copy2(ruta_origen, ruta_destino)
        copiados.append(nombre_archivo)

        print(nombre_archivo, "COPIADO")

    else:
        no_encontrados.append(nombre_archivo)

        print(nombre_archivo, "NO EXISTE")


    if no_encontrados:
        texto_no_encontrados = "\n".join(no_encontrados)
    else:
        texto_no_encontrados = "Ninguno"

    if copiados:
        texto_copiados = "\n".join(copiados)
    else:texto_copiados = "Ninguno"


messagebox.showinfo(
    "ClipVault",
    "Archivos copiados:\n"
    + texto_copiados
    + "\n\nArchivos no encontrados:\n"
    + texto_no_encontrados
)

os.startfile(carpeta_destino)