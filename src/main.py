from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import sounddevice as sd
import soundfile as sf
import numpy as np

FILENAME = "recorded_audio.wav"
SAMPLERATE = 44100  # Standard sample rate
DURATION = 5  # seconds

class AudioApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        btn_record = Button(text="Record Sound")
        btn_record.bind(on_press=self.record_audio)

        btn_play = Button(text="Play Normal")
        btn_play.bind(on_press=self.play_audio)

        btn_double = Button(text="Play Double Speed")
        btn_double.bind(on_press=self.play_audio_double_speed)

        btn_full_speed = Button(text="Play Full Speed")
        btn_full_speed.bind(on_press=self.play_audio)

        layout.add_widget(btn_record)
        layout.add_widget(btn_play)
        layout.add_widget(btn_double)
        layout.add_widget(btn_full_speed)

        return layout

    def record_audio(self, instance):
        print("Recording...")
        audio = sd.rec(int(SAMPLERATE * DURATION), samplerate=SAMPLERATE, channels=1)
        sd.wait()
        sf.write(FILENAME, audio, SAMPLERATE)
        print("Recording saved.")

    def play_audio(self, instance):
        print("Playing at normal speed...")
        data, fs = sf.read(FILENAME, dtype='float32')
        sd.play(data, fs)
        sd.wait()

    def play_audio_double_speed(self, instance):
        print("Playing at double speed...")
        data, fs = sf.read(FILENAME, dtype='float32')
        sd.play(data, int(fs * 2))
        sd.wait()

if __name__ == '__main__':
    AudioApp().run()
