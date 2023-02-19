import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
#import pyjokes
import requests,os
from pyChatGPT import ChatGPT
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

session_token = str(os.getenv("CHAT_GPT_SESSION_TOKEN"))
session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..BXkBSWZsFGQ36Ejr.Q-KjfIpM47RkS_Ex4O5zvVxcGt4MmUCRy2BAv8R0C2VMPAhlfqH3OVoBp9BWA3xHn3PWZ8De_RWMl5cuvgcp_dZUfvDZ2LZjPzboR-23t6NI2Zq5GPYptTFfLAaAVWBtC9tEQg9rAq4uI5NyRvojqgiSlio0ZYyl8a_VhL8zjyNNbxr2l69bz9QHRyQO2qCtfIW2nlmMd5T-05px75aBM9IUHP-j9N4-cl2Im1sZTmvJmf0YvJ1lVgbmkChov8elEoG205Kt0O05ksFDAsSs7MF_0mKV7bj3y3hyr6HCn6HuHyiq1QCaiXCarcT3-vA9X_N7Y1Nq4Kp5h6_w3g97rIG82dq7vtWpaHHwq3l0EK9gzxByEdtbAtgocAk9zu4S9mKDr-PrV5MElM52IOouTEpblcDgq1Gj51n-EPlGxlQ28lHjtzBrlStZ4oanPNVlMn_QOGaZZFRo5haBBdrzCj72N5SUmXnRNmhiE_R5Tu2BOpl4CVgUIZssM3vPTLOR40-m8zICE0E5zO3OafIx1GNsV9nO3b-qBGhtIoPnDF-9CDKN-l0rTQWlaYBvqh6S07LQZgxvaGQowqLjeX2AAhKwY0DAqdqiJ7wyGi_bpjfyvwwsFOfY_J6Vukc0OsL2WFtX1CAXgGu2xtFbWLb4sw8eA_m6SH8JHVGb5Rgwr0MF3mN5xFb6hZoOWSmZ_aLcSSdPvYNjrml5ILGUmh3Vd0ukEFCOqJGkWb-bo6QiXPLRz5lY5q3muu0jsb1MfbkgsXjEep2SnOgkomcZd-lLRz520en4GJp843H-cHT-cPV2DmEHP3S_mFNKYvMVwqdfHSIME9X_jhlv_IRQugW7aJJfmWRD9Owk2_gNzEQDXgPe--m9BvJDIQ3rNrL5nQlQGX6qxPJFdP2L7X4q-zeeAaXaaG3A2c1_ufLF1RptrSrxxMJ-GBLzc3eiCmWotsHdhBKdXtuqAmGx2It-16WoR3FMVKMEPswGquqZQhkGczT5OwhbYW5Zpyhm_W8yW-UXByqiojsVd0SfL44yQh8tf1tnHUpqd0Sn7hx2L6maTJSJ3RMcOhX0XcpqONMq2MnuKcBbkEaJARqIaEWUQIPtpSeY8NAoXTnFOfSj4Oi2n5tT3Hx9s3_VwWaRoE0B2K4vPaEAev8oO3Wzi8QEwgUdPfLdHFUaMIB2iDgZcpeWNsDide-rXJ34DrLoVCuLps4Vn80sxHLiJKrxdcZqwu1QZUdxKi-wgyDPPLUbs94vbp25aFTkXc6bPrrnoaezTcJuLoSytoIPv-tODjhBrziE49xuwJv0uN6Ujwif-sOhwrCbsBxuK7e4UWM2lpkYOgfVZ_pYnf9AIlAwhAdNvrqmUHi-KX7TEqhbQ1cLO9vV2RBrDr5MD5XifHRVe6V7bcRXX202JGpvwFy1XIwuUA_ZhnhdFP5R2pjavrARCNtDj_0_4xXm9-38x7ZExQ1iJKrpqDb7OPWVotkKh8pUlFq5tA08OIxzWKAE3R6n4yeJ7z7wyv0KtV2UWayH_4zmfz9FsSw3fB3N1049yKuxyP1vLuhZ5QlLCijOQwhqxmvoT6mDe41IPM_pvXKowk62lfaLAa1p1Id63ipKy-DNErqH4vvO0rCBwhUxdcDjmdgsBonQMGoZ6atUTMhpW5K8WoEskmRzfD7ekBLheIOEvVTL7CToEA8WxQn-gNH-BAXUpAs5jhX_Hvbj5X0CUoLXu8phV02J58QX-FohaTNBZN6xPzV1AhN9epIqzcTomK5mPkY6yb8jaAly_pXC6CL7ciIpPNdlf0KBXJ2h2xp1rNX0FTR6fPGYBIFv7VVh996FPbw2ezv6BsfbtoLPsYTG2pG-CgVbysAacVOAEKdLhkBITP5V6k3fvVYiC5N5XyA5y6sdBAXD2srP6KY-lYH-B8Lgps-24RCeWbj0hECMZp0VMfliVu5kyVhiA6tUcucf7TOK1OI2vQBEm86og26gsA41iZUEysegYqXi6QsB7RjgDdiJL8vFsn94nsXSyobGk0E-Fy3eXmmL1uIJj38NFlmmlxTW4HrDbidGZFUOZerhAlZ5w4Cu-JVgQyotZq36sl8ajX6xvTHihR14chIqnuvH_W4wf_eZkJU-kRZHbqsTqOAIddMUN1u4tFymbRYoocCXhM7DkvV17gFiCiKs5S5Ha8solPnSgtkt2T-Wpy475hkLzcWEMVr_9Vu3_jyuC2TSJX2wSQFc1TA1jLaTEhBqReqAD33URIe1aSSCW2xod1IaR9KYpHU4sLWCKQlAHFzO0Oym53xHHMddWladWHdqwicTEx-5NJdOhSJ5BAOQ7m7aKngbMM5sbBz7oDRLI259Y65PrzvCF2HwICJv1XnC9Y5whNCRNdM0dW7HSURVKYHrV4zcvxsw2nBoHVsBYl8I03yWl4SwdYzO7EPrW1fVBewxgc4ez_qpeGDScvbm0GiLR4gjkPd_WfSyCSR8dEOF1nXhLO8HgL8A0KMbkYkY.nc-pVVw8b8MRvS4Xs3EIEg"

def talk(text):
    engine.say(text)
    engine.runAndWait()

#main command


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening ...........\n")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                reply = Hello_reply(command)
                talk(reply)

        return command
    except Exception as e:
        pass
        talk("Please command me !")
        print("Error :",str(e))
        #run_alexa()
        exit()


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def Hello_reply(userstr=None):
    import os
    if userstr.lower().strip() in ['hello python', 'hi python', 'hello', 'hi']:
        user_name = os.getlogin()
        reply = "Hello " + 'Anil Kumar Sir' + "! \n"
        reply += "How May I help you  ?"

        print(reply)
        return reply
    else:
        reply = "Sorry !\nPlease train me ."

        return ''


def get_location():

    ip_address = get_ip()

    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    #print(response)
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "latitude":response.get("latitude"),
        "longitude":response.get("longitude")
    }
    address_name = response.get("city") + " " + response.get("region") + " " + response.get("country_name")
    return address_name


def AnswerByChatGPT(session_token, command):
    try:
        session_url = "https://chat.openai.com/api/auth/session"
        api = ChatGPT(session_token)
        resp = api.send_message(command)
        answer = resp['message'].split(" ")
        answer = answer[0:100]
        answer = " ".join(answer)
        return answer
    except Exception as e:
        text = "Please train me on this ."
        talk(text)
        print("Error :", str(e))


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        try:
            song = command.replace('play', '')
            text = "playing "+song
            talk(text)
            print(text)
            pywhatkit.playonyt(song)
        except Exception as e:
            talk("Sorry ! Please train me about this .")

    elif "your boss" in command:
        text = "My Boss is AK Sonker"
        talk(text)
        print(text)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("Current time is "+time)

    elif "info" in command or "detail" in command or "wiki" in command or 'about' in command or "who" in command:
        try:
            sub = command.replace("detail of", '').replace("about", '')
            info = wikipedia.summary(sub, 1)
            talk(info)
            print(info)
        except Exception as e:
            talk("Sorry ! Please train me about this .")

    elif "search" in command:
        try:
            text = command.replace("search", "")
            pywhatkit.search(text)
            text_ = "Searching :" + text
            talk(text_)

            text = pywhatkit.info(text, lines=2)
            talk(text)
            print(text)
        except Exception as e:
            talk("Sorry ! Please train me about this .")
            exit()

    elif "location" in command:
        text = get_location()
        talk("Your Current Location is :"+text)
        print(text)

    elif "whatsapp" in command:
        try:
            name = command.replace("whatsapp", "").replace("to", "").strip()
            get_contact = {"name": "Abhishek", "contact": "+917861004444"}
            print("Name :", name, "\n","contact :", get_contact["contact"])

            if name in get_contact["name"].lower():
                number = get_contact["contact"]
                text = "ready to send Message to "+name
                talk(text)
                print(text)
                text = "Please tell your message"
                talk(text)
                my_message = "Please ignore the text message"

                pywhatkit.sendwhatmsg_instantly(
                    phone_no=number,
                    message=my_message,
                )
                talk("Your message to " + str(name) + "has been sent .")
            else:
                talk("Sorry No Contact found with "+name)
        except Exception as e:
            talk("Sorry ! Please train me on this")
            print("Error :", str(e))

    elif "stop" in command:
        text = "Okay Sure Sir !"
        talk(text)
        print(text)
        exit()

    elif "good" in command:
        text = "It is my Pleasure to serve you Sir !"
        talk(text)
        print(text)

    else:
        if not "hello" in command:
            answer = AnswerByChatGPT(session_token, command)
            talk(answer)


while True:
    run_alexa()