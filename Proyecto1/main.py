import tkinter.ttk

from ctypes import windll
from tkinter import font

from AST.Definicion.Objetos.GuardarClase import GuardarClase
from AST.Error.CustomError import CustomError
from Entorno.EntornoTabla import EntornoTabla
from Entorno.Simbolos.Funcion import Funcion
from gramatica import gramatica
# from graphivz import grafica, agregarInicio            no descomentar


class UI(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.lineNumber = None
        self.consola = None
        self.editorTexto = None
        # self.attributes('-alpha', 0.8)
        self.initSize()
        self.initGrid()
        self.initButtonsLeft()
        self.initEditor()
        self.initMenu()
        self.initConsola()
        self.title('Organización de lenguajes y compiladores 2 - seccion N')

    def initSize(self):
        width = 1200
        height = 650
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        centerX = int(screenWidth / 2 - width / 2)
        centerY = int(screenHeight / 2 - height / 2)
        self.geometry(f'{width}x{height}+{centerX}+{centerY}')

    def initGrid(self):
        self.rowconfigure(0, weight=10, minsize=500)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, minsize=600, weight=1)

    def initButtonsLeft(self):
        # relief = reliefe, bd = border
        frameButtons = tkinter.Frame(self, bd=2)
        button = tkinter.Button(frameButtons, text='Limpiar')
        button2 = tkinter.Button(frameButtons, text='Ejecutar', command=self.ejecutar)
        button.grid(column=0, row=0, ipadx=20, ipady=5, padx=10, pady=5, sticky='ew')
        button2.grid(column=0, row=1, ipadx=20, ipady=5, padx=10, pady=5, sticky='ew')
        frameButtons.grid(column=0, row=0, sticky='news')

    def initEditor(self):
        frameEditor = tkinter.Frame(self, relief=tkinter.RAISED, bd=2)
        self.lineNumber = tkinter.Text(frameEditor, wrap=tkinter.NONE, width=4, padx=2, state='disabled', takefocus=0,
                                       background='grey')
        self.lineNumber.tag_configure("center", justify='right')
        self.lineNumber.pack(side='left', fill='y')

        self.editorTexto = tkinter.Text(frameEditor, wrap=tkinter.WORD)
        self.editorTexto.pack(expand='yes', fill='both')
        self.bind('<Any-KeyPress>', self.updateLines)

        frameEditor.grid(row=0, column=1, sticky='news')

    def initConsola(self):
        frameLabel = tkinter.LabelFrame(self, text='Consola')
        self.consola = tkinter.Text(frameLabel, wrap=tkinter.WORD)
        self.consola.pack(expand=1, fill='both', padx=25, pady=10)
        frameLabel.grid(row=1, column=0, columnspan=2, sticky='sewn')
        pass

    def initMenu(self):
        menuBar = tkinter.Menu(self, relief=tkinter.SOLID)
        mmenu_archivo = tkinter.Menu(menuBar, tearoff=False)
        mmenu_archivo.add_command(
            label="Nuevo",
            accelerator="Ctrl+N",
            font=font.Font(family="Times", size=14),
            # Color de fondo.
            background="#ADD8E6",
            # Color del texto.
            foreground="#FF0000",
            # Color de fondo cuanto el botón tiene el foco.
            activebackground="#32CDFF",
            # Color del texto cuando el botón tiene el foco.
            activeforeground="#FFFF00"
        )
        menuBar.add_cascade(menu=mmenu_archivo, label="Archivo")
        self.config(menu=menuBar)

    def getLineNumbers(self):
        output = ""
        row, column = self.editorTexto.index('end').split('.')
        for i in range(1, int(row)):
            output += str(i) + '\n'
        return output

    def updateLines(self, event=None):
        lineNumberBar = self.getLineNumbers()
        self.lineNumber.config(state='normal')
        self.lineNumber.delete(1.0, tkinter.END)
        self.lineNumber.insert(1.0, lineNumberBar)
        self.lineNumber.config(state='disabled')
        self.lineNumber.tag_add("center", "1.0", "end")

    def ejecutar(self):
        texto = self.editorTexto.get(1.0, tkinter.END)

        self.consola.delete('1.0', 'end')

        ENTORNO_RAIZ = EntornoTabla(self.consola, None )

        if texto != '':
            AST  = gramatica.parse(texto)
            listaErrores = gramatica.getErrores()
            for err_ in listaErrores:
                v:CustomError = err_
                self.consola.insert(tkinter.END,v.toString()+"\n")

            for i  in AST.listaInstrucciones:
                # agregarInicio(i.__str__()) no descomentar

                if isinstance( i, Funcion):
                    existeFuncion = ENTORNO_RAIZ.existeFuncion(i.identificador)

                    if not existeFuncion:
                        ENTORNO_RAIZ.agregarFuncion(i)

                elif isinstance(i, GuardarClase):
                    i.ejecutarInstr(ENTORNO_RAIZ)

            if ENTORNO_RAIZ.existeFuncion("main"):
                funcionMain = ENTORNO_RAIZ.obtenerFuncion("main")
                funcionMain.ejecutarInstr(ENTORNO_RAIZ)
                # grafica.view() no descomentar
            else:
                print("No existe main")


if __name__ == '__main__':
    windll.shcore.SetProcessDpiAwareness(1)
    ventana = UI()
    ventana.mainloop()

