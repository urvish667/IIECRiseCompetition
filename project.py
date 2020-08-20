import os

def wordFinder(str):
    if "chrome" in str or "browser" in str: 
        return "chrome"
    elif "cmd" in str:
        return "cmd"
    elif "notepad" in str or "editor" in str or "":
        return "notepad"
    elif "anaconda" in str:
        return "anaconda"
    elif "paint" in str:
        return "paint"
    elif "excel" in str:
        return "excel"
    elif "msword" in str or "microsoft word" in str:
        return "word"
    else:
        return None

while True:
    print("Enter your requirement: ", end = '')
    req = input()
    req.lower()
    if("run" in req or "show" in req or "execute" in req or "open" in req):
        if(wordFinder(req) == None):
            print("Not Understand")
            continue
        else:
            os.system(wordFinder(req))
    elif("stop" in req or "exit" in req or "exit" in req):
        break
    else:
        print("Not Understand:(")
