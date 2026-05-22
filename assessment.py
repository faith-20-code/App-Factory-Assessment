text = input("Enter text: ")

x = text.lower().split()

if len(text) < 1 or len(text) > 1000:
    print("your text is too short/too long")
    text = input("Enter text: ")
else:
    print("Input accepted.")


 