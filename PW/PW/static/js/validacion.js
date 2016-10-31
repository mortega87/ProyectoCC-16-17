function validarFormulario(){
  var nombre = document.forms["formulario"]["nombre"].value;
  var apellidos = document.forms["formulario"]["apellidos"].value;
  var username = document.forms["formulario"]["username"].value;
  var pass = document.forms["formulario"]["contrasenia"].value;
  var direccion = document.forms["formulario"]["direccion"].value;
  var ciudad = document.forms["formulario"]["ciudad"].value;
  var post = document.forms["formulario"]["direccion_postal"].value;
  var provincia = document.forms["formulario"]["provincia"].value;
  var dni = document.forms["formulario"]["dni"].value;
  var tarjeta = document.forms["formulario"]["tarjeta"].value;

  var numero
  var letr
  var letra
  var expresion_regular_dni
  var error = false;

  if(nombre == ""){
    alert('Nombre erroneo, campo obligatorio');
    error = true;
  }

  if(username == ""){
    alert('Username erroneo, campo obligatorio');
    error = true;
  }

  if(pass == ""){
    alert('Password erroneo, campo obligatorio')
    error = true;
  }

  if(ciudad == ""){
    alert('Ciudad erronea, campo obligatorio')
    error = true;
  }

  if(post == ""){
    alert('CP erroneo, campo obligatorio')
    error = true;
  }


  expresion_regular_dni = /^\d{8}[a-zA-Z]$/;

  if(expresion_regular_dni.test (dni) == true){
     numero = dni.substr(0,dni.length-1);
     letr = dni.substr(dni.length-1,1);
     numero = numero % 23;
     letra='TRWAGMYFPDXBNJZSQVHLCKET';
     letra=letra.substring(numero,numero+1);
    if (letra!=letr.toUpperCase()) {
       alert('Dni erroneo, la letra del NIF no se corresponde');
     }

  }else{
     alert('Dni erroneo, formato no válido');
     error = true;
  }

  if(tarjeta == "" || tarjeta.length != 19){
    document.getElementById("nombre").style.border="1px solid red";
    alert('Tarjeta erronea, formato no válido');
    error = true;
  }

  if(error){
    return false;
  }
  return true;
}
