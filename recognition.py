import time
import speech_recognition as sr
#from text2speech import t2s
from text2speech_vn import t2s
from time import sleep

r = sr.Recognizer()
def recognize(note=""):
    #with sr.Microphone(device_index=0) as source:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 3)
        if note != "":
            t2s(note)
        t2s('START')
        try:
            audio = r.listen(source,timeout=3)
            text = r.recognize_google(audio, language='vi-VN').lower()
        except:
            try:
                t2s("Thử lại")
                t2s('START')
                audio = r.listen(source,timeout=3)
                text = r.recognize_google(audio, language='vi-VN').lower()
            except:
                text = 'error'
    print('#speech2text:' + text)
    return text

#recognize()

# # this is called from the background thread
# def callback(recognizer, audio):
#     # received audio data, now we'll recognize it using Google Speech Recognition
#     try:
#         # for testing purposes, we're just using the default API key
#         # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#         # instead of `r.recognize_google(audio)`
#         print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio, language='vi-VN'))
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))


# r = sr.Recognizer()
# m = sr.Microphone()
# with m as source:
#     r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

# # start listening in the background (note that we don't have to do this inside a `with` statement)
# stop_listening = r.listen_in_background(m, callback)
# # `stop_listening` is now a function that, when called, stops background listening

# # do some unrelated computations for 5 seconds
# for _ in range(50): time.sleep(0.1)  # we're still listening even though the main thread is doing other things

# # calling this function requests that the background listener stop listening
# stop_listening(wait_for_stop=False)

# # do some more unrelated things
# while True: time.sleep(0.1)
