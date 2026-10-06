from tkinter import Tk, filedialog

ventana = Tk()
ventana.withdraw()

carpeta_clips = filedialog.askdirectory(
    title="Selecciona la carpeta VIDEO"
)

print("Carpeta seleccionada:")
print(carpeta_clips)