from gtts import gTTS
import playsound


class GVoice:
    def __init__(self):
        self.text = "show OCD2 on DP"
        self.first_keypoint = "Hey Google, "
        self.language = "en"
        self.file_name = "audio.mp3"

    def switch_voice_process(self):
        gTTS(text=f"{self.first_keypoint}{self.text}", lang=self.language, slow=False).save(self.file_name)
        playsound.playsound(f"{self.file_name}", True)


if __name__ == '__main__':
    GVoice().switch_voice_process()