document.addEventListener('DOMContentLoaded', () => {
    // alert('funciona');
    document.querySelector('#index-rural').onmouseover = () => {
        const el = document.getElementById("index-image");
        el.classList.add("animate-img")
        cargarImagen(1,el);

    };
    document.querySelector('#index-urbano').onmouseover = () => {
        const el = document.getElementById("index-image");
        el.classList.add("animate-img")
        // console.log("hover2");
        cargarImagen(2,el);

    };
});

function cargarImagen(imag,el) {
    el.style.animationPlayState = 'running';
    el.addEventListener('animationend', () => {
        
        if (imag == 1) {
            el.src = "https://images.pexels.com/photos/461960/pexels-photo-461960.jpeg";
        } else {
            el.src = "https://images.pexels.com/photos/2679956/pexels-photo-2679956.jpeg";
        }
        el.classList.remove("animate-img")
    });


}