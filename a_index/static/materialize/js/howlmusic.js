

// mapsSouce = '../../../materialize/music/wavinTrimmed.mp3'
source = 'materialize/music/wavinTrimmed.mp3'
toPlay1 = document.createElement('audio');
toPlay1.controls = true;
toPlay1.src = source;
toPlay1.type = 'audio/ogg';

function runPlayed() {
    toPlay1.play()
}
function runPlay(whatPlay) {
    console.log('\n\n Running runPlay() _____- js/howlmusic.js \n\n');
    whatPlay.play()
    playingDuration = whatPlay.duration
    volDur = (parseFloat(playingDuration) - 8) * 1000
    setTimeout(() => {
        initVol = 1;

        volumeDown = setInterval(() => {
            if (whatPlay.volume >= 0) {
                initVol -= 0.1
                whatPlay.volume = initVol
            } else {
                clearInterval(volumeDown);
            }
        }, 1000);
    }, volDur)
}

// console.log(Playit)
// if (Playit) {
//     toPlay1.play()
// }
// PlaytheMusic(source)
function ClickFooter() {
    console.log('ClickFooter()  ____-js/howlmusic.js')
    // document.querySelector("#modalfooter").click();
    // document.querySelector("#1asd").click() 
    document.elementFromPoint(1, 1).click();
}
// function PlaytheMusic(src) { NOT NEEd ACTUALLY FUCKED!
//     toPlay1 = document.createElement('audio');
//     toPlay1.controls = false;
//     toPlay1.src = src;
//     toPlay1.type = 'audio/ogg';
//     document.body.append(toPlay1)

//     function BrowserChecker() {
//         if ((navigator.userAgent.indexOf("Opera") || navigator.userAgent.indexOf('OPR')) != -1) {
//             return 'Opera';
//         }
//         else if (navigator.userAgent.indexOf("Edg") != -1) {
//             return 'Edge';
//         }
//         else if (navigator.userAgent.indexOf("Chrome") != -1) {
//             return 'Chrome';
//         }
//         else if (navigator.userAgent.indexOf("Safari") != -1) {
//             return 'Safari';
//         }
//         else if (navigator.userAgent.indexOf("Firefox") != -1) {
//             return 'Firefox';
//         }
//         else if ((navigator.userAgent.indexOf("MSIE") != -1) || (!!document.documentMode == true)) //IF IE > 10
//         {
//             return 'IE';
//         }
//         else {
//             return 'unknown';
//         }
//     }
//     if (BrowserChecker() == 'Safari') {
//         console.log(BrowserChecker())
//         var toPlay1 = new Howl({
//             src: ['sound.webm', src],
//             onend: function () {
//                 alert('Finished!');
//             }
//         });
//         toPlay1.once('load', function () {
//             console.log('Play Starting')
//             toPlay1.play();
//             console.log('playing..')
//         });
//         toPlay1.on('end', function () {
//             console.log('FinishesLog!');
//         });

//     }
//     else if (BrowserChecker() == 'Chrome') {
//         toPlay1.oncanplay = function () {
//             promise = toPlay1.play().catch((err) => { console.log('ERROR: ', err) });
//             if (promise !== undefined) {
//                 promise.then(_ => {
//                     console.log('auto')
//                     // Autoplay started!
//                 }).catch(error => {
//                     console.log('Not auto');
//                     toPlay1.controls = true
//                 });
//             }
//             console.log('Playin ')
//         };
//     }

// }

