$(document).ready(function() {
	// find the div.fade elements and hook the hover event
	$('.fadeThis').hover(function() {
		// on hovering over find the element we want to fade *up*
		var fade = $('> .hover', this);

		// if the element is currently being animated (to fadeOut)...
		if (fade.is(':animated')) {
			// ...stop the current animation, and fade it to 1 from current position
			fade.stop().fadeTo(500, 1);
		} else {
			fade.fadeIn(500);
		}
	}, function () {
		var fade = $('> .hover', this);
		if (fade.is(':animated')) {
			fade.stop().fadeTo(500, 0);
		} else {
			fade.fadeOut(500);
		}
	});
})
