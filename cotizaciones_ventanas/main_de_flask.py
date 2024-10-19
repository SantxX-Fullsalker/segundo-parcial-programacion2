from flask import Flask, render_template, request, redirect, url_for
from app.ventana import Ventana
from app.cotizacion import Cotizacion
from app.cliente import Cliente

app = Flask(__name__)

# Variable para almacenar las cotizaciones
cotizaciones_registradas = []

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('cliente.html')

# Ruta para capturar los datos del cliente y redirigir al formulario de las ventanas
@app.route('/cliente', methods=['POST'])
def cliente():
    nombre_cliente = request.form['nombre_cliente']
    empresa_cliente = request.form['empresa_cliente']
    cantidad_ventanas = int(request.form['cantidad_ventanas'])
    
    # Redirigimos a la página para agregar ventanas, pasando los datos del cliente
    return redirect(url_for('ventana', cantidad_ventanas=cantidad_ventanas, 
                            nombre_cliente=nombre_cliente, empresa_cliente=empresa_cliente))

# Ruta para capturar los detalles de las ventanas y generar la cotización
@app.route('/ventana/<int:cantidad_ventanas>', methods=['GET', 'POST'])
def ventana(cantidad_ventanas):
    nombre_cliente = request.args.get('nombre_cliente')
    empresa_cliente = request.args.get('empresa_cliente')

    if request.method == 'POST':
        ventanas = []
        for i in range(cantidad_ventanas):
            estilo = request.form[f'estilo_{i}']
            ancho = float(request.form[f'ancho_{i}'])
            alto = float(request.form[f'alto_{i}'])
            acabado = request.form[f'acabado_{i}']
            tipo_vidrio = request.form[f'tipo_vidrio_{i}']
            esmerilado = request.form[f'esmerilado_{i}'] == 'Sí'
            
            ventana = Ventana(estilo, ancho, alto, acabado, tipo_vidrio, esmerilado)
            ventanas.append(ventana)
        
        cliente = Cliente(nombre_cliente, empresa_cliente, cantidad_ventanas)
        cotizacion = Cotizacion(cliente, ventanas)
        total = cotizacion.calcular_total()

        # Guardar cotización
        cotizaciones_registradas.append({
            "cliente": cliente,
            "ventanas": ventanas,
            "total": total
        })

        return render_template('resumen.html', cliente=cliente, ventanas=ventanas, total=total)

    return render_template('ventana.html', cantidad_ventanas=cantidad_ventanas, 
                           nombre_cliente=nombre_cliente, empresa_cliente=empresa_cliente)

# Nueva ruta para mostrar todas las cotizaciones
@app.route('/cotizaciones')
def mostrar_cotizaciones():
    return render_template('cotizaciones.html', cotizaciones=cotizaciones_registradas)

if __name__ == "__main__":
    app.run(debug=True)