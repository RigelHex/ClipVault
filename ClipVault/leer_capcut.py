import json

from tkinter import Tk, filedialog

# -------------------------
# CONFIGURACIÓN DE VENTANAS
#--------------------------

ventana = Tk()
ventana.withdraw()

#-------------------------
# SELECCIÓN DE ARCHIVO CAPCUT
#--------------------------

ruta_json = filedialog.askopenfilename(
    title="Selecciona draft_content.json",
    filetypes=[("Archivos JSON", "*.json")]
)

if not ruta_json:
    print("No se seleccionó ningún archivo. Saliendo del programa.")
    exit()


#-------------------------
# LEER ARCHIVO JSON
#--------------------------


with open(ruta_json, "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

#-------------------------
# MOSTRAR DATOS BÁSICOS
#--------------------------

print("FPS:", datos["fps"])
print("Duración:", datos["duration"])

pistas = datos["tracks"]

print("Cantidad de pistas:", len(pistas))
