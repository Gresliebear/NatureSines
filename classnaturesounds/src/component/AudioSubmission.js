import React, { useRef, useEffect }  from 'react'
import RecordingAPI from './RecordCall';

const AudioSubmission = () => {
    // https://developers.google.com/web/fundamentals/media/recording-audio
    // https://www.npmjs.com/package/react-voice-recorder
    //https://codesandbox.io/s/81zkxw8qnl?file=/src/index.tsx:74-87
    // https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia
    const player = document.getElementById('player');
    const audioRef = useRef(null);
    
    // passing audio stream
    const handleSuccess = function(stream) {
        if (window.URL) {
        audioRef.current.srcObject = stream;
        
        } else {
        player.src = stream;
        }

        const context = new AudioContext();
        const source = context.createMediaStreamSource(stream);
        const processor = context.createScriptProcessor(1024, 1, 1);
    
        source.connect(processor);
        processor.connect(context.destination);
    
        processor.onaudioprocess = function(e) {
          // Do something with the data, e.g. convert it to WAV
          console.log(e.inputBuffer);
        };
    

    };

    const handleClick = () => {
        navigator.mediaDevices.getUserMedia({ audio: true, video: false })
            .then(handleSuccess);
    }




    return (
        <div className="AudioBox">
        <h2> Press the button to record and then submit</h2>
        {/* https://developers.google.com/web/fundamentals/media/recording-audio */}
        <form> 
        {/* <audio id="player" ref={audioRef} controls></audio>
        <button onClick={handleClick}> Record </button> */}

        </form>
        <RecordingAPI></RecordingAPI>
    
        {/* <Script>

        navigator.mediaDevices.getUserMedia({ audio: true, video: false })
            .then(handleSuccess);
        </Script>
 */}


        </div>
    )
}

export default AudioSubmission
