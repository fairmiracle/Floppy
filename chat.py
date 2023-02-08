import struct
import pyaudio
import pvporcupine
import pvcobra
import openai
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import SpeechSynthesizer
from revChatGPT.Official import Chatbot

picovoice_api_key = 'xxxx'
openai_api_key = 'xxxx'
msazure_api_key = 'xxxx'
msazure_api_region = "xxxx"
porcupine_path = 'Hello-Floppy_en_windows_v2_1_0.ppn'

speech_config = speechsdk.SpeechConfig(subscription=msazure_api_key, region=msazure_api_region, speech_recognition_language="zh-CN")
chatbot = Chatbot(api_key=openai_api_key)
porcupine = pvporcupine.create(access_key=picovoice_api_key, keyword_paths=[porcupine_path])
cobra = pvcobra.create(access_key=picovoice_api_key)

# text==response by GPT3
def recognition_gpt3(text):
    response = openai.Completion.create(model="text-davinci-003", prompt=text, temperature=0, max_tokens=1000)
    print('GPT3: '+response["choices"][0].text+'\n')
    return response["choices"][0].text

# text==response by ChatGPT
def recognition_chatgpt(text):
    response = chatbot.ask(text, temperature=0.5)
    print('ChatGPT: '+response["choices"][0]["text"]+'\n')
    return response["choices"][0]["text"]

def text2voiceazure(text):
    #speech_config.speech_synthesis_voice_name = "zh-CN-XiaochenNeural"
    speech_config.speech_synthesis_voice_name = "zh-CN-XiaoyouNeural"#小孩儿
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    result = synthesizer.speak_text_async(text).get()

# voice==text
def from_mic():
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    print("ChatBot: 请开始讲话\n")
    #text2voiceazure("噔")
    result = speech_recognizer.recognize_once()
    # Checks result.
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Me: {}\n".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
    return result.text
 
p = pyaudio.PyAudio()
audio_stream = p.open(
                    rate=porcupine.sample_rate,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=porcupine.frame_length)
recording = False
buffer = []
silence_count = 0
i = 0
#text2voiceazure("噔噔")
while True:
    i += 1
    pcm = audio_stream.read(porcupine.frame_length) # 亮灯开始唤醒
    _pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
    
    if not recording:
        keyword_index = porcupine.process(_pcm)
        if keyword_index >= 0:
            # Insert detection event callback here
            print("ChatBot: 我在这呢\n")
            text2voiceazure("我在这呢")
            recording = True
            continue
        else:
            continue
    else:
        # 检测到silence 后处理
        text = from_mic()
        if "再见" in text and len(text)<5:
            break
        resp = recognition_gpt3(text)
        text2voiceazure(resp)    
        continue
