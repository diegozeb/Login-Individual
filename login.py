from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("register.html")
    
@app.route("/datos", methods=["POST"])
def datos():
    
    nombre = request.form.get("name")
    apellido = request.form.get("lastname")
    correo = request.form.get("adress")
    usuario = request.form.get("user")
    contraseña = request.form.get("password")
    fecha = request.form.get("date")
    
    
    return render_template("datos.html", nombre1=nombre, apellido1=apellido, correo1=correo, usuario1=usuario, contraseña1=contraseña, fecha1=fecha)
    

 

