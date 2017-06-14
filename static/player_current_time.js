<script>
	var curTime = document.getElementsByClassName('mejs__time  mejs__currenttime-container')
	var durTime = document.getElementsByClassName('mejs__time mejs__duration-container')
	var buttonPlay = getElementsByClassName('mejs__button mejs__playpause-button mejs__play')
	buttonPlay.click(function(){
    curTime.addClass("hide_over");
});
</script>