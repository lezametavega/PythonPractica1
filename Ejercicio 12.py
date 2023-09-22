# 
def tipo_mime(nombre_archivo):
    extension = nombre_archivo.split('.')[-1].lower()

    extensiones = {
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'zip': 'application/zip'
    }

    tipo_mime = extensiones.get(extension, 'application/octet-stream')
    return tipo_mime

nombre_archivo = input("Nombre Archivo: ")
tipo_mime = tipo_mime(nombre_archivo)
print("Salida Esperada:", tipo_mime)