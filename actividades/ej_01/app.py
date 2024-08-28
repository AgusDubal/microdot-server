from microdot import Microdot, send_file # Importamos la clase Microdot y la función send_file

app = Microdot() # Instanciamos la clase Microdot

# Definimos la ruta raíz
@app.route('/')
async def index(request):
    return send_file('index.html')


@app.route('/<dir>/<file>') # Definimos la ruta con dos parámetros
async def index(request, dir, file):
    return send_file("/" + dir + "/" + file) # Cambiamos el nombre del archivo a enviar

# Corremos el servidor creado en el puerto 80
app.run(port=80)
