import dictate
from sound_manager import play_async, play_wait
from time import sleep
from tts import say

script_1 = '''Please say store hours, pharmacy, or representative, and I will connect you.'''
script_2 = '''Please say your choice after the tone.'''

play_wait("ring")
say("Welcome to CVS pharmacies.")
say("I am an automated telephone assistant that can help you with what you need.")
sleep(1/5)
say(script_1)
sleep(0.2)
say(script_2)

def user_interaction(index=0):
    if index > 2:
        say("I'm having trouble understanding you. I'm connecting you to a representative who may be able to assist you better.")
        play_wait("ring")
    else:
       # collect input
        play_async("record")
        usr_input = str(dictate.dictate())

        # clean up input
        usr_input = usr_input.lower()
        usr_input = usr_input.strip()
        # pattern = "[a-zA-Z\s]"
        # usr_input = re.sub(pattern, "", usr_input)

        # print(usr_input)

        if usr_input in ['store hours', 'pharmacy', 'representative']:
            play_async('success')
            sleep(1)

        if usr_input == 'store hours':
            say("Our store hours are 7 AM to 9 PM on weekends, and 10 AM to 11 PM on weekdays.")
        elif usr_input == 'pharmacy':
            say("I am connecting you to our pharmacy now.")
            play_wait("ring")
        elif usr_input == 'representative':
            say("I am connecting you to a representative now.")
            play_wait("ring")
        else:
            play_async("error")
            sleep(1)
            if index == 1:
                say("It's difficult to understand you. Let's try one more time. Please say that again.")
            else:
                if index != 2:
                    say("I didn't quite get that. Please say it again.")
            user_interaction(index + 1)

if __name__ == '__main__':
    user_interaction()