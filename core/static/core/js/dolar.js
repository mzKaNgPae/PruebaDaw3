function moneda(){

    this.nombre
    this.tipoDeCambio
    this.mensaje = "Por favor ingrese el monto."
    this.tipoDeCambio

    this.convertir = function(monto){
        monto = monto.replace(',','.')
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

function convertirMoneda(valorClp){
    var clp = new moneda()
    console.log(valorClp)
    clp.nombre = "Pesos Chilenos (CLP)"
    clp.tipoDeCambio = valorClp
    var montoSeleccionado = document.getElementById('monto').value
    clp.convertir(montoSeleccionado)

}