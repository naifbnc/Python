import speech_recognition as sr
import pyttsx3
import datetime

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Sizi dinliyorum. Bir şey söyleyin.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Sesiniz tanınıyor. Şimdi bir şey söyleyin...")
        text = recognizer.recognize_google(audio, language="tr-TR")
        return text.lower()
    except sr.UnknownValueError:
        print("Ses anlaşılamadı.")
        return None
    except sr.RequestError as e:
        print(f"Hata alındı; {e}")
        return None

def respond_to_command(command):
    if "merhaba" in command:
        speak("Merhaba! Seninle konuşmaktan mutluluk duyuyorum.")
    elif "nasılsın" in command:
        speak("Ben bir programım, bu yüzden duygularım yok, ama teşekkür ederim!")
    elif "saat kaç" in command:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")
        speak(f"Şu anda saat {current_time}.")
    elif "güle güle" or "hoşçakal" or "allaha emanet" or "görüşürüz" in command:
        speak("Güle güle! Başka bir şey istersen bana söyle.")
        quit
    else:
        speak("Üzgünüm, anlamadım. Tekrar eder misiniz?")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Sesli asistanınız başlatıldı. Size nasıl yardımcı olabilirim?")

    while True:
        command = recognize_speech()

        if command:
            print("Anlaşılan Komut:", command)
            respond_to_command(command)
