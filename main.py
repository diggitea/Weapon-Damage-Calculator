from weaponpanel import *


def main():
    window = Tk()
    window.title('Weapon Damage Calculator')
    window.geometry('620x500')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()


if __name__ == '__main__':
    main()
