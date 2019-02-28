const socket = io();

//DOM Elements
var espacio_solucion = document.getElementById('response-area');
var boton_solucion = document.getElementById('conseguir-solucion');

//Button function
boton_solucion.addEventListener('click', function(){
	/*//===Debug area
	var estados = crear_estado_prueba();
	console.log(estados);
	estados.forEach(estado => {
		nuevo_tablero = crear_tablero(estado);
		espacio_solucion.appendChild(nuevo_tablero);
	});
	
	//====*/
	//emitir mensaje a python
	socket.emit('request', "solucion");

});

//Socket function
socket.on('response', function(message){
	//console.log("Desde python: "+message);
	
	var estados = cadena_matriz(message); //lista con tableros
	estados.forEach(estado => {
		nuevo_tablero = crear_tablero(estado);
		espacio_solucion.appendChild(nuevo_tablero);
	});
});

function crear_estado_prueba(){

	var estados = [];

	for(var k = 0; k<8; k++){
		var estado = [];
		var row = [];

		for(var j = 0; j<8; j++){
			row.push(0)
		}
		for( var i = 0; i<8; i++){
			estado.push(row);
		}

		estado[2] = [0,0,0,2,0,0,0,0];
		estado[7] = [0,2,0,0,0,0,0,0];

		estados.push(estado)
	}
	return estados;
}

function cadena_matriz(message){
	var estados = [];

	//transformación
	var matrices = message.split(":")
	matrices.forEach(matriz => {
		var nueva_matriz = [];
		filas = matriz.split(".");
		filas.forEach(fila => {
			var nueva_fila = [];
			items = fila.split(",")
			items.forEach(item => {
				var nuevo_item = parseInt(item)
				nueva_fila.push(nuevo_item);
			});
			nueva_matriz.push(nueva_fila);
		});
		estados.push(nueva_matriz);
	});

	return estados
}

function crear_tablero(estado){
	var tablero = document.createElement("DIV");
	tablero.classList.add('tablero');
	var index = 0;

	estado.forEach(row => {
		index++;
		row.forEach(casilla => {
			index++;
			var casilla_dom = document.createElement("DIV");
			if(index%2 == 0){
				casilla_dom.classList.add('casilla-blanca');
			} else {
				casilla_dom.classList.add('casilla-negra');
			}
			console.log(casilla);
			if (casilla == 2) {
				reina = document.createElement("IMG");
				reina.setAttribute("src", "img/reina.jpg");
				casilla_dom.appendChild(reina);
			}
			tablero.appendChild(casilla_dom);
		});
	});

	return tablero;
}