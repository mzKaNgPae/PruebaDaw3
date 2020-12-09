$(function() {
    $("#mi_formulario").validate( {
        rules:
        {
            
            nombre:
            {
                required:true,
                minlength:2,
                maxlength:30
            },
            rut:
            {
                required:true,
                minlength:7,
                maxlength:10
            },
            nombre_marc:
            {
                required:true,
                minlength:4,
                maxlength:35
            },
            model:
            {
                required:true,
                minlength:4,
                maxlength:40
            },
            año:
            {
                required:true,
                minlength:4,
                maxlength:4
            },
            fecha_nac:
            {
                required:true
            },
            email:
            {
                required:true,
                email:true,
                minlength:6,
                maxlength:100
            },
            password:
            {
                required:true,
                minlength:6,
                maxlength:15
            },
            password_confirm:
            {
                required:true,
                equalTo:"#password",
            },
            comentarios:
            {
                required:true,
                maxlength:100
            },
            acepto_terminos:
            {
                required:true
            }
        },
        messages:
        {
            
            nombre:
            {
                required:"Debe ingresar tu nombre.",
                minlength:"Ingresa al menos 2 caracteres.",
                maxlength:"Estas excediendo el limite de caracteres."
            },
            rut:
            {
                required:"Debe ingresar tu rut.",
                minlength:"Ingresa al menos 9 caracteres.",
                maxlength:"Estás excediendo el límite de caracteres."
            },
            nombre_marc:
            {
                required:"Debes ingresar la marca del vehiculo.",
                minlength:"Ingresa al menos 4 caracteres.",
                maxlength:"Estas excediendo el limite permitido."
            },
            model: 
            {
                required:"Debes ingresar el modelo del vehiculo.",
                minlength:"Ingresa al menos 4 caracteres.",
                maxlength:"Estas excediendo el limite permitido."
            },
            año:
            {
                required:"Debes ingresar el año del vehiculo.",
                minlength:"Debes ingresar minimo 4 caracteres.",
                maxlength:"Estas excediendo el limite permitido." 
            },
            fecha_nac:
            {
                required:"No puedes dejar este campo vacio."
            },

            email:
            {
                required:"Ingresa tu correo electrónico.",
                email:"El formato ingresado no corresponde a una dirección de correo.",
                minlength:"Debes ingresar un correo válido.",
                maxlength:"Tu correo excede el largo máximo permitido.",
            },
            password:
            {
                required:"Debes ingresar una contraseña.",
                minlength:"Tu contraseña debe contener entre 6 y 15 caracteres.",
                maxlength:"Tu contraseña debe contener entre 6 y 15 caracteres."
            },
            password_confirm:
            {
                required:"Debes ingresar nuevamente tu contraseña.",
                equalTo:"La contraseña ingresada no es igual a la anterior."
            },
            comentarios:
            {
                required:"Debes ingresar un comentario.",
                maxlength:"Puedes ingresar un máximo de 100 caracteres."
            },
            acepto_terminos:
            {
                required:""
            }
        }
    });
});

function limitarCaracteresComentarios (e,contenido, maximoCarateres) {
    // obtenemos la tecla pulsada
    var unicode=e.keyCode? e.keyCode : e.charCode;

    // Permitimos las siguientes teclas:
    // 8 backspace
    // 46 suprimir
    // 13 enter
    // 9 tabulador
    // 37 izquierda
    // 39 derecha
    // 38 subir
    // 40 bajar
    if(unicode==8 || unicode==46 || unicode==13 || unicode==9 || unicode==37 || unicode==39 || unicode==38 || unicode==40)
    {
        return true;
    }    

    // Si ha superado el limite de caracteres devolvemos false
    if(contenido.length >= maximoCarateres)
    {
        return false;
    }
    else
    {
        return true;
    }
}


function actualizarCantidadCaracteres(maximoCarateres) {
    var elemento = document.getElementById("comentarios");
    var informacion = document.getElementById("info");

    if(elemento.value.length >= maximoCarateres)
    {
        informacion.innerHTML = "Máximo " + maximoCarateres + " caracteres";
    }
    else
    {
        informacion.innerHTML = "Puedes escribir " + (maximoCarateres - elemento.value.length) + " caracteres adicionales.";
    }
}