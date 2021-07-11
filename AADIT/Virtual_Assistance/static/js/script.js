const informationSection = document.querySelector(".info");
const informationContent = document.querySelector(".info-content");
const chatSection = document.querySelector(".chat");
const logo = document.querySelector(".logo");
const messages = document.querySelector(".messages");
const textArea = document.querySelector("#chat-text-area");
const sendBtn = document.querySelector("#send");
const mic = document.querySelector("#mic");
_Objdata = {};
var message_user;
var answer;

let addSpaceBeforeInfo = function () {
  if (window.innerHeight > informationContent.clientHeight) {
    // logo.style.paddingTop = "2.5rem";
    informationSection.style.alignItems = "center";
    informationSection.style.justifyContent = "center";
    informationContent.style.marginTop = "auto";
    informationContent.style.marginBottom = "auto";
    informationContent.style.paddingBottom = "0";
  } else {
    // logo.style.paddingTop = `${window.innerHeight * 0.02}px`;
    informationSection.style.alignItems = "stretch";
    informationSection.style.justifyContent = "flex-start";
    informationContent.style.marginTop = "0";
    informationContent.style.marginBottom = "0";
    informationContent.style.paddingBottom = "2rem";
  }

  //   if (informationContent.scrollHeight == informationContent.clientHeight) {
  //     console.log("hi");
  //     informationSection.style.marginTop = `${
  //       window.innerHeight - informationContent.clientHeight - 20
  //     }px`;
  //   }

  //   messages.style.height = `${
  //     window.innerHeight -
  //     parseInt(logo.style.paddingTop) -
  //     parseInt(logo.clientHeight) -
  //     parseInt(logo.style.paddingTop) -
  //     (parseInt(logo.style.paddingBottom) || 0) -
  //     textArea.clientHeight
  //   }px`;

  //   if (window.innerHeight < informationContent.clientHeight) {
  //     informationContent.style.transform = "scale(0.8)";
  //     informationSection.style.marginTop = 20;
  //   } else {
  //     informationContent.style.transform = "scale(1)";
  //   }
};

let sendMessage = function (event) {
  if (
    (event.keyCode === 13 || event.target === sendBtn || event.type == "end") &&
    textArea.value.trim().length !== 0
  ) {
    
    message_user = textArea.value;
    
    message_html = `
    <div class="chat-bubble--user chat-bubble ">
    <img src="static/images/user.png" alt="" class="chat-bubble-pic"> 
    <div class="chat-bubble-text-container chat-bubble-text-container--user">
      <span class="chat-bubble-text-content">${message_user}</span>
    </div>
  </div>`;
    messages.insertAdjacentHTML("beforeend", message_html);
    textArea.value = "";
    messages.scrollTop = messages.scrollHeight;
    getData();
  }
};

function getData(){
  _Objdata.message_from_user = message_user;
  
  // Run Ajax
  $.ajax({
    url:'/chat-bot',
    data:_Objdata,
    dataType:'json',
    beforeSend:function(){
       $(".ajaxloader").show();
    },
    success:function(res){
       answer = res;
       //$("#filteredcars").html(res.data);
       //$(".ajaxloader").hide();
       getRandomReply();
       
    }
    
  });

};


let getRandomReply = function () {

  
  message = `<div class="chat-bubble--bot chat-bubble ">
  <img src="static/images/bot.png" alt="" class="chat-bubble-pic chat-bubble-pic--bot"> 
  <div class="chat-bubble-text-container chat-bubble-text-container--bot">
    <span class="chat-bubble-text-content">${answer.answer}</span>
  </div> 
</div>`;


  messages.insertAdjacentHTML("beforeend", message);
  textArea.value = "";
  messages.scrollTop = messages.scrollHeight;
};

//////SPEECH RECOGNITION

if (!("webkitSpeechRecognition" in window)) {
  textArea.placeholder = "Sorry, your browser does not support Web Speech API.";
} else {
  let voiceInputStatus = false;
  var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
  var SpeechGrammarList = SpeechGrammarList || webkitSpeechGrammarList;
  var SpeechRecognitionEvent =
    SpeechRecognitionEvent || webkitSpeechRecognitionEvent;
  var speechRecognitionList = new SpeechGrammarList();

  let recognition = new SpeechRecognition();

  recognition.continuous = false;
  recognition.lang = "en-IN";
  recognition.interimResults = true;
  recognition.maxAlternatives = 1;

  recognition.onnomatch = function (e) {
    textArea.placeholder = "I didn't catch that...";
    mic.style.opacity = "65%";
    voiceInputStatus = false;
  };
  recognition.onerror = function (e) {
    console.log(e.error);
    voiceInputStatus = false;
    if (e.error == "no-speech") {
      textArea.placeholder = "No speech was detected.";
    } else if (e.error == "audio-capture") {
      textArea.placeholder = "No microphone was found.";
    } else if (e.error == "not-allowed") {
      textArea.placeholder = "Please allow microphone access.";
    } else if (e.error == "service-not-allowed") {
      textArea.placeholder = "Browser not supported";
    } else if (e.error == "aborted") {
      mic.style.opacity = "100%";
    }
  };

  recognition.onspeechend = function () {
    console.log("speechend");
    setTimeout(recognition.stop(), 5000);
    mic.style.opacity = "65%";
  };

  recognition.onresult = function (onresultEvent) {
    textArea.value = onresultEvent.results[0][0].transcript;
    sendMessage(onresultEvent);
    textArea.placeholder =
      "Type here (or) Press Space to activate voice command.";
  };
  recognition.addEventListener("end", function (e) {
    sendMessage(e);
    textArea.value = "";
    mic.style.opacity = "65%";
  });

  function toggleVoiceInput(toggleVoiceInputEvent) {
    console.log(toggleVoiceInputEvent?.keyCode);
    if (
      (toggleVoiceInputEvent?.keyCode === 32 &&
        textArea.value.trim().length === 0) ||
      toggleVoiceInputEvent?.target == mic
    ) {
      toggleVoiceInputEvent.preventDefault();
      toggleVoiceInput();
      voiceInputStatus != voiceInputStatus;
      if (voiceInputStatus) {
        console.log("stop");
        recognition.stop();
        textArea.placeholder =
          "Type here (or) Press Space to activate voice command.";
      } else {
        mic.style.opacity = "100%";
        recognition.start();
        console.log("start");
        textArea.placeholder = "Speak now...";
      }
    }
  }
}

// startSpeechRecognition();

window.addEventListener("resize", addSpaceBeforeInfo);
window.addEventListener("load", addSpaceBeforeInfo);
window.addEventListener("change", addSpaceBeforeInfo);
textArea.addEventListener("keydown", sendMessage);
sendBtn.addEventListener("click", sendMessage);
mic.addEventListener("click", toggleVoiceInput);
textArea.addEventListener("keydown", toggleVoiceInput);
