# Script sencillo para convertir un archivo con texto simple a un srt con el formato correcto
# Cada linea del archivo va a ser una linea de subtitulo individual que se van a mostrar en secuencia. Esto con un tiempo igual para cada linea sumarizando una duración total dada

# esta funcion va a hacer la conversion de txt a srt
def convert_to_srt(file_path, total_length, output_path):
    # file_path va a ser la ruta al archivo de text que queremos convertir
    # total_length la duración total en segundos
    # output_path la ruta del archivo de salida

    # se usa esta sintaxis para que el with se encargue de abrir y cerrar el archivo
    with open(file_path, 'r') as file: 
        lines = file.readlines()

    # duración de cada tramo de subtitulo
    subtitle_duration = total_length / len(lines)

    # se inicializa la variable que va a contener todo el texto del srt
    srt_string = ""
    for i, line in enumerate(lines):
        start_time = subtitle_duration * i
        end_time = start_time + subtitle_duration
        # Para cada linea del archivo txt se inserta un bloque de texto que representa una linea de subtitulo y su duración en pantalla
        srt_string += f"{i+1}\n{format_time(start_time)} --> {format_time(end_time)}\n{line}\n\n"

    # se excribe el archivo de salida
    with open(output_path, 'w') as file:
        file.write(srt_string)

# Esta funcion ayuda a hacer el formato correcto de la marca de tiempo que debe tener cada linea de subtitulo
def format_time(time):
    hours = int(time / 3600)
    minutes = int((time % 3600) / 60)
    seconds = int(time % 60)
    milliseconds = int((time % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

# para correrlo
convert_to_srt("texto.txt", 105, "texto_v1.srt") 