function onSuccessXml(data) {
	$(data).find('cita').each(function(){
		var texto = $(this).find('texto').text();
		$("<div></div>").attr('class','well').html(texto).appendTo("#quotes");
	});
}

function cargarCitas() {
	$.ajax({
		type: "GET",
		url: "data/citas.xml",
		contentType: "text/xml",
		success: onSuccessXml
	});
}

function procesarCitas() {
	var texto = document.getElementById('texto').value;
	
	if (texto.length > 0) {

		var quotes = $('.well')

		for(quote of quotes) {
			if(quote.textContent.search(texto) != -1) {
				$(quote).attr('class','well mostrar')
			} else {
				$(quote).attr('class', 'well ocultar')
			}
		}

	} else {
		var quotes = $('.well')

		for(quote of quotes) {
			quote.setAttribute('class','well mostrar')
		}
	}
}

(function(){

	document.getElementById("buscar").onclick=procesarCitas;
	
	document.getElementById("texto").onkeyup=procesarCitas;
	$('#texto').on('keyup',procesarCitas)
	
	cargarCitas();

})();