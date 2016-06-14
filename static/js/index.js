var portada = document.getElementById('id_portada')
if ( portada !== null ) portada.addEventListener('change', changePhoto)

$('#subscribe').on('submit', (e) => {
	e.preventDefault()
	var $form = $('#subscribe')

	$.ajax({
    url: $('#subscribe').attr('action'),
    type: 'POST',
    data: $form.serialize(),
    success: (message) => {
      $('#id_name').val('')
      $('#id_email').val('')
      $('#message').html(message)
    }
  });
})

function changePhoto (e) {
	var photo = document.getElementById('photo')
	var file = e.target.files[0]
	photo.src = window.URL.createObjectURL(file)
}
