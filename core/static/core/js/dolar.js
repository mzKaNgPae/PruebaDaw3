function moneda(){

    this.nombre
    this.tipoDeCambio
    this.mensaje = "Por favor ingrese el monto."

    this.convertir = function(monto){

        resultado = monto * this.tipoDeCambio
        var mensajeHTML
        if(resultado <= 0){
            mensajeHTML=this.mensaje
        }else{
            mensajeHTML = monto + " doláres son " + resultado + " " + this.nombre
        }
        document.getElementById('resultadoCLP').innerHTML= mensajeHTML
    }
}

var clp = new moneda()
    clp.nombre = "Peso Chilenos (CLP)"
    clp.tipoDeCambio = 798.80

function convertirMoneda(){

    var montoSeleccionado = document.getElementById('monto').value
    clp.convertir(montoSeleccionado)

}