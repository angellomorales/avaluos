
document.addEventListener('DOMContentLoaded', () => {
    // alert('funciona');
    document.querySelector('#index-rural').onmouseover = () => {
        // console.log("hover1");
        cargarImagen(1);
        
    };
    document.querySelector('#index-urbano').onmouseover = () => {
        // console.log("hover2");
        cargarImagen(2);
        
    };
});

function cargarImagen(imag){
    if(imag==1){
        document.getElementById("index-image").src = "https://images.pexels.com/photos/461960/pexels-photo-461960.jpeg";
    }else{
        document.getElementById("index-image").src = "https://images.pexels.com/photos/2679956/pexels-photo-2679956.jpeg";
    }

}

