function leer_temperatura(){

    fetch('/sensors/ds18b20/read').then(response.json()).then(json => {
        document,querySelector('#temperatura').innerText = json.temperature;

})
}

function enviar_temperatura(){
    let temperature_slider_value = parseInt(document.querySelector('#temperature_slider').value);
    fetch('/sensors/set/${temperature_slider_value}').then(response => response.json()).then(json => {

        document.querySelector('#buzzer-state').innerText = json.buzzer;
    });
}

function updateTemperatura(value){
    document.getElementById('temperature_slider_value').innerText = value;
    send_temperature();
}

setInterval(leer_temperatura, 500);