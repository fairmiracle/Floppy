# ChatGPT: voice control by Python

A python script to make you chat with ChatGPT by voice. Inspired by [GPTHunt](https://zhuanlan.zhihu.com/p/599181411).

## Requirement (Python >= 3.8.0)
    - PyAudio: accept the first human voice, hopefully the wake-up words.
    - pvporcupine: detects wake-up words (here "Hello, Floppy" is trained online, which is the name of the dog in the Oxford tree).
    - pvcobra: detects the wake-up words is finished
    - openai: Official API by OpenAI.
    - revChatGPT: Reverse Engineered ChatGPT API by OpenAI.
    - azure.cognitiveservices.speech: provides the voice service, including text and voice exchange and human-like voice synthesis.
  
## Run
Apply the API keys from [picovoice](https://console.picovoice.ai), [OpenAI](https://openai.com/api), and [Azure](https://azure.microsoft.com/en-us/free/ai), and make sure to set the environment values ``picovoice_api_key``, ``openai_api_key``, ``msazure_api_key``, ``msazure_api_region`` first. 

``porcupine_path`` is the wake-up words detection model file downloaded from [picovoice](https://console.picovoice.ai).
``hellowords`` is what it say to start the chat.
``goodbyewords`` is what you say to finish the chat.

then
```
python chat.py
```

and speak out the wake-up words: Hello, Floppy!



