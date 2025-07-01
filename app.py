from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'df565a575859c06799fbb08b98020faae1d32d6c37f08ad8'

PRODUCTOS = [
    {
        'id': 1,
        'nombre': 'Laptop',
        'precio': 1299.99,
        'imagen': 'https://tse4.mm.bing.net/th/id/OIP.XfPNlJErG936WWiLBnvgugHaFj?rs=1&pid=ImgDetMain&o=7&rm=3',
        'descripcion': 'Laptop de alto rendimiento para gaming'
    },
    {
        'id': 2,
        'nombre': 'Televisor',
        'precio': 699.99,
        'imagen': 'https://tse1.mm.bing.net/th/id/OIP.4pH1kUmcFWJsHoXBf6xjnQHaEK?rs=1&pid=ImgDetMain&o=7&rm=3',
        'descripcion': 'Televisor de gran tamaño y calidad excelente'
    },
    {
        'id': 3,
        'nombre': 'Impresora',
        'precio': 449.99,
        'imagen': 'https://tse3.mm.bing.net/th/id/OIP.c3Ai3HR25R3aIR6pdGNM9wHaGE?w=1448&h=1186&rs=1&pid=ImgDetMain&o=7&rm=3',
        'descripcion': 'Impresiones con gran calidad'
    }
]

@app.route('/')
def catalogo():
    if 'carrito' not in session:
        session['carrito'] = []
    return render_template('catalogo.html', productos=PRODUCTOS)

@app.route('/agregar/<int:id_producto>')
def agregar(id_producto):
    producto = next((p for p in PRODUCTOS if p['id'] == id_producto), None)
    if producto:
        session['carrito'].append(producto)
        session.modified = True
    return redirect(url_for('catalogo'))

@app.route('/carrito')
def carrito():
    carrito = session.get('carrito', [])
    total = sum(p['precio'] for p in carrito)
    return render_template('carrito.html', carrito=carrito, total=total)

@app.route('/vaciar')
def vaciar():
    session['carrito'] = []
    return redirect(url_for('carrito'))

if __name__ == '__main__':
    app.run(debug=True)