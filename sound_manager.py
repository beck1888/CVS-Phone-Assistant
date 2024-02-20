from playsound import playsound

sound_lookup = {
    #name : filepath
    "error":"sounds/error.mp3",
    "record":"sounds/recording.mp3",
    "success":"sounds/allow.mp3"
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