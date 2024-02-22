from playsound import playsound

sound_lookup = {
    #name : filepath
    "error":"sounds/error.mp3",
    "record":"sounds/recording.mp3",
    "success":"sounds/allow.mp3",
    "ring":"sounds/phone_ring.mp3",
    "jingle":"sounds/jingle.mp3",
    "pharm_connect":"speech/connect_pharmacy.mp3",
    "rep_connect":"speech/connect_representative.mp3",
    "not_quite":"speech/didn't_quite_get.mp3",
    "hours":"speech/hours.mp3",
    "trouble":"speech/trouble.mp3",
    "welcome":"speech/welcome.mp3",
    }

def play_wait(sound):
    try:
        sound_lookup[sound]
    except:
        # Fail, but keep code running
        print(f"WARNING: no matching audio file for {sound}")
        return
    
    playsound(sound_lookup[sound])




def play_async(sound):
    try:
        sound_lookup[sound]
    except:
        # Fail, but keep code running
        print(f"WARNING: no matching audio file for {sound}")
        return
    
    playsound(sound_lookup[sound], False)