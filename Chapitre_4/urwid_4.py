#!/usr/bin/env python3
import urwid


def main():
    question = urwid.Text("Quel est votre nom ? ")
    reponse = urwid.Edit(edit_text="")
    bonjour = urwid.Text("")
    sortir = urwid.Button("Sortir")

    div = urwid.Divider()

    pile = urwid.Pile([question, div, reponse, div, bonjour, div, sortir])

    hote = urwid.Filler(pile, valign="top")

    def dis_bonjour(bouton, txt):
        bonjour.set_text(f"Bonjour {txt} ! Comment allez-vous ?")

    def quitter(bouton):
        raise urwid.ExitMainLoop()

    urwid.connect_signal(reponse, "change", dis_bonjour)
    urwid.connect_signal(sortir, "click", quitter)

    main = urwid.MainLoop(hote)
    main.run()


if __name__ == "__main__":
    main()
