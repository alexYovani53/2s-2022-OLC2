
void main(){
    int a = 5;
    int b = 10;
    string saludo = "hola mundo";
    int resultado = calcularSuma(a,b);

    boolean op1 = true;
    boolean op2 = false;
    boolean op3 = false;
    boolean op4 = true;

    if (op1 && op2){
        print("If correcto");
    }else if(op3 && op4) {
        print("Else");
    }else if(op1 && op4) {
        print("Else verdadero");
    }else {
        print("Ninguna opción");
    }

    crearObjeto();
}


int calcularSuma(int a, int b){
    return a + b;
}

void crearObjeto(){
    Curso compiladores = new Curso("Compiladores","N",10);
    print(compiladores.nombre);
}


class Curso {
    string nombre;
    string seccion;
    int valor:
}
