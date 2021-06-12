morse = {
    "a":".-",
    "b":"-...",
    "c":"-.-.",
    "d":"-..",
    "e":".",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"-.--",
    "z":"--..",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "0":"-----",
    ".":".-.-.",
    ",":'--..--',
    "?":"..--..",
    "'":".----.",
    "!":"-.-.--",
    "/":"-..-.",
    ":":"---...",
    ";":"-.-.-.",
    "=":"=...=",
    "+":".-.-.",
    "-":"-....-",
    "_":"..--.-",
    '"':".-..-.",
    "@":".--.-."
}
key_list = list(morse.keys())
val_list = list(morse.values())

def engToMorse(message):
    line = message.split()
    newLine = ""
    for word in line:
        newWord = ""
        for letter in word:
            newWord += morse[letter] + " "
        newLine += newWord + "   "
    return newLine

def morseToEng(message):
    line = message.split("   ")
    newLine = ""
    for word in line:
        splitWord = word.split()
        newWord = ""
        for letter in splitWord:
            index = val_list.index(letter)
            newWord += key_list[index]
        newLine += newWord + " "
    return newLine

