# audio-multi-channel-player
Play each audio channels in different connected audio devices.

pip install -r requirements.txt

Check connected audio devices
open python console 
 >>> import sounddevice as sd
 >>> ds.query_devices()

modify device numbers in player.py

run -> python3 ./player.py
