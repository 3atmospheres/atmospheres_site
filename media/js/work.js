$(function(){
	$('#gallery').gallerify();
});


jQuery.fn.gallerify = function() {
	return this.each(function(){
		var images = $('div.thumb',this);
		images.hide().css({opacity:0});
		$(images[0]).show().css({opacity:1});
		if (images.length > 1) {
			$(this).after('<ul id="gallery_changer"></ul>');
			var changer = $('#gallery_changer');
			images.each(function(){
				var numberLink = (images.index(this)+1).toString();
				if (numberLink.length == 1) numberLink = '0' + numberLink;
				$('<li><a href="#">'+numberLink+'</a></li>').click(showImage).appendTo(changer);
			});
			$('li:first',changer).addClass('first current');
		}

		function showImage() {
			$(this).addClass('current').siblings().removeClass('current');
			var clicked = this;
			images.each(function(){
				if ($(this).is(':visible')) {
					$(this).animate({opacity:0},200,function(){
						$(this).hide();
						var next_image = $(images[$(clicked).parent().children('li').index(clicked)])
						next_image.css({display:'block'}).animate({opacity:1},200);
					});
				}
			});
			return false;
		}
	});
}
