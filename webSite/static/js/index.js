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
  })
})

function changePhoto (e) {
	var photo = document.getElementById('photo')
	var file = e.target.files[0]
	photo.src = window.URL.createObjectURL(file)
}

if (window.location.pathname === "/") {
	var socket = io.connect("http://localhost:3000/")
	var contentMessages = document.getElementById('messages')

  socket.on('message', (message) => {
    var newMessage = '<div class="message-other">Chat: '+ message.chat +'</div>'
    $('#messages').append(newMessage)
		// keep the scroll at the end
		contentMessages.scrollTop = contentMessages.scrollHeight
  })

	// send message
  $('#send-message').on("submit", (e) => {
		e.preventDefault()
    var message = $('#text-message')
    socket.emit('message', {text:message.val()})
    var myMessage = '<div class="message-yo">Yo: '+ message.val() +'</div>'
  	$('#messages').append(myMessage)
		// clean text message
		message.val('')
		// keep the scroll at the end
		contentMessages.scrollTop = contentMessages.scrollHeight
  })
}
