
from KeyboardConfig import Config, ExecuteKey
from evdev import InputDevice, categorize, ecodes
import evdev

dev = None
DeviceCaptured = False
# keycodes = {}
def main():
      DeviceCaptured = False
      print("Starting the event bus to capture events from the device")
      devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
      for device in devices:
          if(device.name == Config['keyboard']):
            print("The device is")
            print(device.path, device.name)
            dev = InputDevice(device.path) 
            dev.grab()
            DeviceCaptured = True

      if DeviceCaptured:
        print("Listening to events now")
        for event in dev.read_loop():
          if event.type == ecodes.EV_KEY:
            key = categorize(event)
            if key.keystate == key.key_down:
                print(key, key.keycode)
                try:
                  ExecuteKey(key.keycode)
                except Exception as e:
                  print("Could not process the keycode")
                  print(key)
                  print(e)
      else: 
          print("Sorry there was no device found in that name")

# press('a')
# typewrite('quick brown fox')
# hotkey('ctrl', 'w')

if(__name__ == "__main__"):
    main()