import threading

import numpy as np
import sounddevice as sd
import soundfile as sf

data1, fs1 = sf.read('audio/song.wav', dtype='float32')
w_data = np.frombuffer(data1, np.float32)
w_data.shape = -1, 2
w_data = w_data.T


class PlayChannel(threading.Thread):
    def __init__(self, data, device_id):
        threading.Thread.__init__(self)
        self.data = data
        self.device_id = device_id

    def run(self):
        sd.play(self.data, fs1, device=self.device_id)
        print('playing on ', self.device_id)
        sd.wait()


# sd.query_devices() , will display connected audio devices and modify the device numbers below

left = PlayChannel(w_data[0], 1)  # 1 laptop speaker
right = PlayChannel(w_data[1], 3)  # 3 connected bluetooth headset
left.start()
right.start()
