class Device:
    def init(self):
        print("Device initialized")

    def del(self):
        print("Device destroyed")


class Camera(Device):
    def init(self):
        print("Camera initialized")
        super().init()

    def del(self):
        print("Camera destroyed")
        super().del()


class Microphone(Device):
    def init(self):
        print("Microphone initialized")
        super().init()

    def del(self):
        print("Microphone destroyed")
        super().del()


class Speaker(Device):
    def init(self):
        print("Speaker initialized")
        super().init()

    def del(self):
        print("Speaker destroyed")
        super().del()


class VoiceModule(Microphone, Speaker):
    def init(self):
        print("VoiceModule initialized")
        super().init()

    def del(self):
        print("VoiceModule destroyed")
        super().del()


class SmartAssistant(Camera, VoiceModule):
    def init(self):
        print("SmartAssistant initialized")
        super().init()

    def del(self):
        print("SmartAssistant destroyed")
        super().del()

assistant = SmartAssistant()

print(SmartAssistant.mro)

del assistant
