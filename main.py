import dictate
from sound_manager import play_async, play_wait
from time import sleep
from tts import say
import image_manager

# image_manager.open('CVS')
sleep(1) # Delay for image to open
play_wait("jingle")
play_wait("welcome")

def user_interaction(index=0):
    play_async("record")
    usr_input = str(dictate.dictate())

    # clean up input
    usr_input = usr_input.lower()
    usr_input = usr_input.strip()

    if usr_input in ['store hours', 'pharmacy', 'representative']: # Known command
        play_wait('success')
        sleep(1)

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
        sleep(0.75)

        if index >= 2: # Pass to rep
            play_wait("trouble")
            play_wait("ring")
            return None
        else:
            play_wait("not_quite") # Try again
            user_interaction(index + 1)

if __name__ == '__main__':
    user_interaction()
    # image_manager.kill()