from WikiSearch import *


def main():
    window = Tk()
    window.title("Wikipedia Search")
    window.geometry("250x180")
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
