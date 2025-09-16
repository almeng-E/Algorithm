def main():
    n = int(input())
    if n < 425:
        print("Violet")
        return
    if n < 450:
        print("Indigo")
        return
    if n < 495:
        print("Blue")
        return
    if n < 570:
        print("Green")
        return
    if n < 590:
        print("Yellow")
        return
    if n < 620:
        print("Orange")
        return
    print("Red")
main()