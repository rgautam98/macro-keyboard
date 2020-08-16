from pyautogui import press, typewrite, hotkey, press
# Check that for more info: https://pyautogui.readthedocs.io/en/latest/keyboard.html 

# most basic function usage
# press('a')
# typewrite('quick brown fox')
# hotkey('ctrl', 'w')

# VsCode
def GitSync():
    hotkey('ctrl', 'shift', 'p')
    typewrite('git.sync')
    press('enter')
    return True

def GitCommitAndSync():
    hotkey('ctrl', 'enter')
    GitSync()
    return True

def GitIntermediateCommit():
    hotkey('ctrl', 'shift', 'g')
    typewrite('Intermediate Commit')
    GitCommitAndSync()
    return True

def GenerateUUID():
    hotkey('ctrl', 'shift', 'p')
    typewrite('uuid.generate')
    press('enter')
    return True
# VsCode Ends
# Terminal
def Deploy():
    typewrite('make deploy')
    press('enter')
    return True
# Terminal Ends
# General Linux Commands
def OpenGFolder():
    hotkey('alt', 'space')
    typewrite('Gautam')
    press('enter')
    return True

# Other Macros
def MakeAPICall():
    print("making an api all")

Config = {
    "keys": {
        'KEY_I': GitIntermediateCommit,
        'KEY_C': GitCommitAndSync,
        'KEY_S': GitSync,
        'KEY_D': Deploy,
        'KEY_G': OpenGFolder,
        'KEY_SPACE': GenerateUUID
     },
    "keyboard": "Your Keyboard Name Comes Here"
}

def GetKeys():
    return Config['keys']

def ExecuteKey(keyCode):
    # Reload config logic comes here
    print("Time to execute key here")
    functionToExecute = None
    keys = GetKeys()

    try:
        functionToExecute = keys[keyCode]
        functionToExecute()
    except Exception as e:
        # If you dont find the key as a macro function, then execute it in the normal fashion
        print(f'The keycode {keyCode} does not exist. Fallback to normal')
        keyCode = keyCode.split("_")[1]
        keyCode = keyCode.lower()
        print(f'Executing::{keyCode}')
        press(keyCode)