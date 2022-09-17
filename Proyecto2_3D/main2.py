from flask import Flask, jsonify, request
from flask_cors import CORS

from AST.Definicion.Objetos.GuardarClase import GuardarClase
from AST.Error.CustomError import CustomError
from Entorno.EntornoTabla import EntornoTabla
from Entorno.Simbolos.Funcion import Funcion
from Generador3D import Generador3D
from gramatica import gramatica

app = Flask(__name__)
CORS(app)

class Consola:
    def __init__(self,consola):
        self.consola = consola

Generador3DInstancia = Generador3D()

@app.route("/prueba", methods=["POST"])
def funcionPrueba():

    data = request.json
    texto = data["text"]

    Generador3DInstancia.reiniciarGenerador()
    consola = Consola("")

    ENTORNO_RAIZ = EntornoTabla(generador= Generador3DInstancia, padre=None)

    if texto != '':
        AST = gramatica.parse(texto)
        listaErrores = gramatica.getErrores()
        if len(listaErrores) > 0:
            for err_ in listaErrores:
                v: CustomError = err_
                consola.consola +=  v.toString() + "\n"
        else:

            for i in AST.listaInstrucciones:

                if isinstance(i, Funcion):
                    existeFuncion = ENTORNO_RAIZ.existeFuncion(i.identificador)

                    if not existeFuncion:
                        ENTORNO_RAIZ.agregarFuncion(i)

                elif isinstance(i, GuardarClase):
                    i.ejecutar3D(ENTORNO_RAIZ)

            if ENTORNO_RAIZ.existeFuncion("main"):
                funcionMain = ENTORNO_RAIZ.obtenerFuncion("main")
                for instr in funcionMain.instrucciones:
                    Generador3DInstancia.agregarInstruccion(instr.ejecutar3D(ENTORNO_RAIZ))
                # grafica.view() no descomentar
            else:
                print("No existe main")


    salida = Generador3DInstancia.generarMain()

    return jsonify({
        "val": salida
    })


if __name__ == "__main__":
    app.run("localhost", 3000)
