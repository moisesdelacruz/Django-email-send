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
