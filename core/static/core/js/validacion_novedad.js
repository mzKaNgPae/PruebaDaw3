$(function() {
    $("#validar_novedad").validate( {
        rules:
        {
            correo_novedad:
            {
                required:true,
                email:true,
                minlength:6,
                maxlength:100
            }
        },

        messages:
        {
            correo_novedad:
            {
                required:"Debes ingresar tu correo electrónico",
                email:"El formato ingresado no corresponde a una dirección de correo.",
                minlength:"Deber ingresar un correo válido.",
                maxlength:"Tu correo excede el largo máximo permitido.",
            }
        }
    });
})