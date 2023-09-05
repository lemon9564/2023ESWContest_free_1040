import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import openai
from translate import Translator

# OpenAI API 설정
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
openai.api_key = OPENAI_API_KEY


def speak(text):
    tts = gTTS(text=text, lang='ko')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def recognize_korean_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("말씀해주세요...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language='ko-KR')
            return text
        except sr.UnknownValueError:
            print("음성을 인식할 수 없습니다.")
            return None
        except sr.RequestError as e:
            print("음성 인식 에러:", e)
            return None


def translate_to_english(text):
    translator = Translator(to_lang="en")
    translated_text = translator.translate(text)
    return translated_text


def gpt3_generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        api_key=OPENAI_API_KEY
    )
    return response.choices[0].text.strip()


def translate_to_korean(text):
    translator = Translator(to_lang="ko")
    translated_text = translator.translate(text)
    return translated_text


if __name__ == "__main__":
    korean_input = recognize_korean_audio()

    if korean_input:
        print("입력된 음성:", korean_input)

        english_input = translate_to_english(korean_input)

        gpt3_input = f"번역된 텍스트: {english_input}\n대화:"
        gpt3_response = gpt3_generate_response(gpt3_input)

        korean_response = translate_to_korean(gpt3_response)
        print("응답:", korean_response)

        speak(korean_response)
