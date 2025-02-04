with open("demo1.txt") as f:
    content = f.read()
    if("twinkle" in content):
        print(content)
        print("twinkle is present in the text")
    else:
        print("twinkle is not present in the text")

