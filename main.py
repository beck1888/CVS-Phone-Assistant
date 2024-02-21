import dictate
from sound_manager import play_async, play_wait
from time import sleep
from tts import say
import image_manager

image_manager.open('CVS')
sleep(1) # Delay for image to open
play_wait("jingle")
play_wait("welcome")

def user_interaction(index=0):
    if index == 2:
        play_wait("trouble")
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

        if usr_input in ['store hours', 'pharmacy', 'representative']: # Known command
            play_async('success')
            sleep(1)
        elif usr_input == 'error - no sound input': # Fail command - no mic audio taken
            play_wait('error')
            if index != 1:
                play_wait("no_sound")
            user_interaction(index + 1)
        
        # If the returned result for user_input was not a fail, then route command accordingly
        if usr_input == 'store hours':
            play_wait("hours")
        elif usr_input == 'pharmacy':
            play_wait("pharm_connect")
            play_wait("ring")
        elif usr_input == 'representative':
            play_wait("rep_connect")
            play_wait("ring")
        else:
            play_async("error")
            sleep(1)
            if index == 1:
                say("It's difficult to understand you. Let's try one more time. Please say that again.")
            else:
                if index != 2:
                    play_wait("difficult")
            user_interaction(index + 1)

if __name__ == '__main__':
    user_interaction()
    image_manager.kill()