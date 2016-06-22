// Subscribe Email
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

// START SHOW END HIDE /U/S/E/R/S/ START //
$('.users-connect').on('click', (e) => {
	$('.users').css('left', '0')
})

$('.close-menu').on('click', (e) => {
	$('.users').css('left', '-100%')
})
// START EMOJIS /E/M/O/J/I/S START //
// Emojis show and hide
function showEmojis (e) {
	e.stopPropagation()
	$('div.content-emojis').show()
}

function hideEmojis (e) {
	e.stopPropagation()
	$('div.content-emojis').hide()
}

// show emojis content
$('.button-emojis').on('click', (e) => {
	if ($('div.content-emojis').is(':visible')) {
		hideEmojis(e)
		$('#text-message').focus()
	} else {
		showEmojis(e)
	}
})

// hide Emojis
// $('body').on('click', (e) => hideEmojis(e))

// selec emojis
$('div.content-emojis div').on('click', (e) => {
	var $emoji = $(e.target)[0]
	var $message = $('#text-message')
	$message.val($message.val() + `(${$emoji.title})`)
	hideEmojis(e)
	$message.focus()
})

// END EMOJIS /E/M/O/J/I/S END //

// Change cover sheet
function changePhoto (e) {
	var photo = document.getElementById('photo')
	var file = e.target.files[0]
	photo.src = window.URL.createObjectURL(file)
}

// Chat /C/H/A/T/ Chat //
// method of receive message
function receiveMessage (username, message, who) {
	var newMessage = ''
	if (who === 'me') {
		newMessage = `<div class="message-yo">${username}: ${message}<div class="exit">X</div></div>`
	} else if (who === 'other') {
		newMessage = `<div class="message-other">${username}: ${message}<div class="exit">X</div></div>`
	}
	$('#messages').append(newMessage)
	// Clean Message
	$('div.exit').on('click', (e) => {
		$(e.target).parent().remove()
	})
}

// method of message format
function formatMessage (message) {
	var http = /(\b(https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/ig
  return message.replace(http,"<a href='$1' target='_black'>$1</a>")
								.replace(/\r?\n/g, "<br>")

								.replace(/(\(smiley\)|:\))/ig, '<img alt="smiley" src="/static/js/ckeditor/plugins/smiley/images/regular_smile.png" style="height:23px; width:23px" title="smiley" />')
								.replace(/(\(sad\)|:\()/ig, '<img alt="sad" src="/static/js/ckeditor/plugins/smiley/images/sad_smile.png" style="height:23px; width:23px" title="sad" />')
								.replace(/(\(crying\)|;\()/ig, '<img alt="crying" src="/static/js/ckeditor/plugins/smiley/images/cry_smile.png" style="height:23px; width:23px" title="crying" />')
								.replace(/(\(wink\))/ig, '<img alt="wink" src="/static/js/ckeditor/plugins/smiley/images/wink_smile.png" style="height:23px; width:23px" title="wink" />')
								.replace(/(\(frown\))/ig, '<img alt="frown" src="/static/js/ckeditor/plugins/smiley/images/confused_smile.png" style="height:23px; width:23px" title="frown" />')
								.replace(/(\(surprise\))/ig, '<img alt="surprise" src="/static/js/ckeditor/plugins/smiley/images/omg_smile.png" style="height:23px; width:23px" title="surprise" />')
								.replace(/(\(heart\))/ig, '<img alt="heart" src="/static/js/ckeditor/plugins/smiley/images/heart.png" style="height:23px; width:23px" title="heart" />')
								.replace(/(\(mail\))/ig,'<img alt="mail" src="/static/js/ckeditor/plugins/smiley/images/envelope.png" style="height:23px; width:23px" title="mail" />')
								.replace(/(\(yes\))/ig,'<img alt="yes" src="/static/js/ckeditor/plugins/smiley/images/thumbs_up.png" style="height:23px; width:23px" title="yes" />')
								.replace(/(\(no\))/ig,'<img alt="no" src="/static/js/ckeditor/plugins/smiley/images/thumbs_down.png" style="height:23px; width:23px" title="no" />')
}

if (window.location.pathname === "/") {
	var socket = io.connect("http://200.7.98.41:8002/")
	var contentMessages = document.getElementById('messages')
	var chat = document.getElementById('send-message')
	chat.addEventListener('submit', sendMessage)
	chat.addEventListener('keypress', (e) => {
    var key = e.which || e.keyCode
		if (key === 13 && !e.shiftKey) { // 13 is enter
		  sendMessage(e)
		}
	})

	// send message
	function sendMessage (e) {
		e.preventDefault()
		var message = $('#text-message')
		var username = $('#username').text()
		// Check whether it is acceptable
		var exp = /.\S/i
		var res = exp.test(message.val())
		if (res === true) {
			// Emit message al server
			socket.emit('message', { text:message.val(), username })
			// Mostrar Message
			var text = formatMessage(message.val())
			receiveMessage(username, text, 'me')
			// clean text message
			message.val('')
			// keep the scroll at the end
			contentMessages.scrollTop = contentMessages.scrollHeight
		} else {
			console.log('no se puede enviar')
		}
		message.focus()
	}

  socket.on('message', (message) => {
		var text = formatMessage(message.message)
		receiveMessage(message.username, text, 'other')
		// keep the scroll at the end
		contentMessages.scrollTop = contentMessages.scrollHeight
  })
}
