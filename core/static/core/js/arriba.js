function irArriba(){
    window.addEventListener('scroll', ()=> {
        var scroll = document.documentElement.scrollTop;
        console.log(scroll);
        var boton_arriba=document.getElementById('boton_arriba');
        if(scroll>300){
            boton_arriba.style.right = 20 + "px";
        }else{
            boton_arriba.style.right = -100 + "px";
        }

    })
}
irArriba()