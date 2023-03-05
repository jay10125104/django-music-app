// need a audio object to play.
// updated moduls se baad mai update kar denghe isko ref.https://github.com/mediaelement/mediaelement/blob/master/docs/usage.md officia
var audio = {
    init: function() {
    var $that = this;
        $(function() {
            $that.components.media();
        });
    },
    components: {
        media: function(target) {
            var media = $('audio.fc-media', (target !== undefined) ? target : 'body');
            if (media.length) {
                media.mediaelementplayer({
                    audioHeight: 40,
                    features : ['playpause', 'current', 'duration', 'progress', 'volume', 'tracks', 'fullscreen'],
                    //feature required can be more increased according to client requirements.
                    alwaysShowControls: true,
                    timeAndDurationSeparator: '<span></span>',
                });
            }
        },
    },
};
audio.init();