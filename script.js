let offset = 0;
const sliderLine = document.querySelector('.slider-line');
document.querySelector('.slider-next').addEventListener('click', function(){
    offset += 256;
    if (offset > 1024) {
        offset = 0;
    }
    sliderLine.style.left = -offset + 'px';
});

document.querySelector('.slider-prev').addEventListener('click', function(){
    offset -= 256;
    if (offset < 0) {
        offset = 1024;
    }
    sliderLine.style.left = -offset + 'px';
});

let backgrounds = [ "url(./image/back.png)", "url(./image/back3.png)", "url(./image/back2.png)", "url(./image/back4.png)", "url(./image/back5.png)"];
document.body.style.backgroundImage = backgrounds[Math.floor(Math.random() * (backgrounds.length + 1))];
