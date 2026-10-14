import os
import shutil

from tkinter import Tk, filedialog, simpledialog, messagebox

# -------------------------
# CONFIGURACIÓN DE VENTANAS
# -------------------------
ventana = Tk()
ventana.withdraw()

# -------------------------
# SELECCIÓN DE CARPETA
# -------------------------

def seleccionar_carpeta():

    carpeta = filedialog.askdirectory(
        title="Selecciona la carpeta VIDEO",
    )
    if not carpeta:
        print("No se seleccionó ninguna carpeta. Saliendo del programa.")
        exit()
    return carpeta
carpeta_clips = seleccionar_carpeta()
print("carpeta_clips")

    
# Detiene el programa si el usuario cancela la selección

if not carpeta_clips:
    print("No se seleccionó ninguna carpeta. Saliendo del programa.")
    exit()

# Obtenemos todos los archivos que existen en la carpeta seleccionada

archivos = os.listdir(carpeta_clips)

# -------------------------
# INGRESO DE CLIPS
# -------------------------

clips = simpledialog.askstring(
    "ClipVault",
    "Escribe los clips sin usar separados por comas:"
)

# Evita continuar si el usuario cancela o no escribe nada

if not clips:
    print("No se ingresaron clips. Saliendo del programa.")
    exit()

# Convierte el texto ingresado en una lista separada por comas

clips_sin_usar = clips.split(",")

# -------------------------
# CARPETA DE DESTINO
# -------------------------

carpeta_destino = os.path.join(carpeta_clips, "Material sin usar")

# Crea la carpeta solo si todavía no existe

os.makedirs(carpeta_destino, exist_ok=True)

# -------------------------
# LISTAS DE CONTROL
# -------------------------

# Guardan el resultado del procesamiento

copiados = []
no_encontrados = []
ya_existentes = []

# Guarda los clips ya revisados para evitar duplicados
procesados = []

# -------------------------
# PROCESAMIENTO DE CLIPS
# -------------------------

for clip in clips_sin_usar:

    # Elimina espacios antes y después del nombre
    clip = clip.strip()
    # Ignora valores vacíos, por ejemplo: 01,,03
    if not clip:
        continue
    # Ignora clips que ya fueron procesados

    if clip in procesados:
        continue

    procesados.append(clip)

    # Agrega la extensión que usamos para buscar el archivo
    nombre_archivo = clip + ".mp4"

    # Comprueba si el archivo existe en la carpeta original
    if nombre_archivo in archivos:
        ruta_origen = os.path.join(carpeta_clips, nombre_archivo)
        ruta_destino = os.path.join(carpeta_destino, nombre_archivo)

        # Evita volver a copiar archivos que ya están en la carpeta destino
        if os.path.exists(ruta_destino):
            ya_existentes.append(nombre_archivo)
            print(nombre_archivo, "YA EXISTE EN LA CARPETA DESTINO")
            continue

        shutil.copy2(ruta_origen, ruta_destino)
        copiados.append(nombre_archivo)

        print(nombre_archivo, "COPIADO")

    else:
        no_encontrados.append(nombre_archivo)

        print(nombre_archivo, "NO EXISTE")

# -------------------------
# PREPARAR RESUMEN
# -------------------------

if no_encontrados:
    texto_no_encontrados = "\n".join(no_encontrados)
else:
    texto_no_encontrados = "Ninguno"

if copiados:
    texto_copiados = "\n".join(copiados)
else:
    texto_copiados = "Ninguno"

if ya_existentes:
    texto_ya_existentes = "\n".join(ya_existentes)
else:
    texto_ya_existentes = "Ninguno"

# -------------------------
# MOSTRAR RESULTADO
# -------------------------

messagebox.showinfo(
    "ClipVault",
    "Archivos copiados:\n"
    + texto_copiados
    + "\n\nArchivos no encontrados:\n"
    + texto_no_encontrados
    + "\n\nArchivos ya existentes:\n"
    + texto_ya_existentes
)

# Abre automáticamente la carpeta de destino al finalizar
os.startfile(carpeta_destino)