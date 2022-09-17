
import CodeEditor from "@uiw/react-textarea-code-editor";
import React, { useRef } from 'react';
import  './css/editor.css'
import Editor from "./view/Editor";
import axios from "axios";

export default function App() {

     const [code, setCode] = React.useState(`

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
  
  
  int calcularSuma(* int a, int b){
      return a + b;
  }
  
  void crearObjeto(){
      Curso compiladores = new Curso("Compiladores","N",10);
      print(compiladores.nombre);
  
      int [][][] array = [
          [
              [5,77],[1,21],[1,5]
          ],
          [
              [89,5],[5,75],[4,6]
          ]
       ];
  
      int [][][] array2 = new int[5][10][10];
      print(array[0][0][0]);
      print(array[0][0][1]);
      print(array[0][1][0]);
      print(array[0][1][1]);
      print(array[1][0][0]);
      print(array[1][0][1]);
      print(array[1][1][0]);
      print(array[1][1][1]);
      print(array2[0][1][9]);
  }
  
  
  
  class Curso {
      string nombre;
      string seccion;
      int valor;
  }
      
    `);
  const editor1  = useRef();
  const editor2  = useRef();


  const setFocus =()=>{
    editor1.current.focus();
  }

  const enviarDatos = ()=>{

    console.log(editor1.current.getCode())

    axios.post("http://localhost:3000/prueba",{
      text:editor1.current.getCode()
    })
    .then(result=>{
      console.log(result)
      if(result.data.val){
        editor2.current.establecerCodigo(result.data.val);
      }
    })
    .catch(err=>console.log(err))
  }


  return (
    <div className="pagina">
{/* 
          <CodeEditor
            value={code}
            language="js"
            placeholder="Please enter JS code."
            onChange={(evn) => setCode(evn.target.value)}
            padding={15}

            style={{
              fontSize: 12,
              backgroundColor: "#f5f5f5",
              fontFamily: 'ui-monospace,SFMono-Regular,SF Mono,Consolas,Liberation Mono,Menlo,monospace',
            }}
          /> */}
          <div className="container" >
            <Editor className="editorT" ref={editor1} cod={code} onClick={setFocus}></Editor>
            <Editor className="editorT" ref={editor2} cod={""}></Editor>
          </div>
          <button className="enviar" onClick={enviarDatos}> Enviar</button>
    </div>

  );
}