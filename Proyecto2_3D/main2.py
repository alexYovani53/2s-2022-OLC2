from flask import Flask, jsonify, request
from flask_cors import CORS

from AST.Definicion.Objetos.GuardarClase import GuardarClase
from AST.Error.CustomError import CustomError
from Entorno.EntornoTabla import EntornoTabla
from Entorno.Simbolos.Funcion import Funcion
from gramatica import gramatica

app = Flask(__name__)
CORS(app)

class Consola:
    def __init__(self,consola):
        self.consola = consola


@app.route("/prueba", methods=["POST"])
def funcionPrueba():
    data = request.json
    texto = data["text"]

    consola = Consola("")

    ENTORNO_RAIZ = EntornoTabla(consola, None)

    if texto != '':
        AST = gramatica.parse(texto)
        listaErrores = gramatica.getErrores()
        for err_ in listaErrores:
            v: CustomError = err_
            consola.consola +=  v.toString() + "\n"

        for i in AST.listaInstrucciones:

            if isinstance(i, Funcion):
                existeFuncion = ENTORNO_RAIZ.existeFuncion(i.identificador)

                if not existeFuncion:
                    ENTORNO_RAIZ.agregarFuncion(i)

            elif isinstance(i, GuardarClase):
                i.ejecutar3D(ENTORNO_RAIZ)

        if ENTORNO_RAIZ.existeFuncion("main"):
            funcionMain = ENTORNO_RAIZ.obtenerFuncion("main")
            # grafica.view() no descomentar
        else:
            print("No existe main")



    return jsonify({
        "val": consola.consola
    })


if __name__ == "__main__":
    app.run("localhost", 3000)
