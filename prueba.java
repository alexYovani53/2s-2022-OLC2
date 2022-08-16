
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

}


int calcularSuma(int a, int b){
    return a + b;
}







void main(){
    int a = 5;
    int b = 10;
    string saludo = "hola mundo";
    int resultado = calcularSuma(a,b);
    string cadena = concatenar(saludo, " "+resultado);
    print(cadena);

    let mut instancia = new Objeto();


}


int calcularSuma(int a, int b){
    return a + b;
}

int concatenar(string origen, string origen2){
    return origen + " " +origen2;
}


// DEFINICION DE CLASE (instruccion)   
// definicion.ejecutar(entorno)
struct Objeto {
    int a,
    string cadena
    
    funcion(){
        print(b)
    }
}