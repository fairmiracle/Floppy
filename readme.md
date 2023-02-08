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
replace ``picovoice_api_key``, ``openai_api_key``, ``msazure_api_key``, ``msazure_api_region`` with the corresponding values, and ``porcupine_path`` is the wake-up words detection model file downloaded from [picovoice](https://console.picovoice.ai).


```
python chat.py
```

and then speak out the wake-up words.

Have fun.


