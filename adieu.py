def main():
    #Get names
    list_names = get_names()

    #print names
    text = text_names(list_names)

    print(text)

def get_names():
    names = []
    while True:
        try: 
            names.append(input())
        except EOFError:
            return names

def text_names(names : str):
    leght  = len(names)
    text ="Adieu, adieu, to "
    if leght == 1: 
        return text + names[0]
    if leght == 2:
        return f"{text}{names[0]} and {names[1]}"
    for i, name in enumerate(names):
        if i == leght -1 :
            text += f"and {name}"
        else:
            text += f"{name}, "
    return text

if __name__ == "__main__":
    main()