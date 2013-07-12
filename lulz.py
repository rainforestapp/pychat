import curses
stdscr = curses.initscr()

begin_x = 20 ; begin_y = 7
height = 5 ; width = 40
win = curses.newwin(height, width, begin_y, begin_x)



stdscr.addstr(12, 25, "MOAR LULZ", curses.A_BLINK)
stdscr.refresh()

s = ''

while 1:
    c = stdscr.getch()
    if c == 27:
        break
    else:
        s += chr(c)
        stdscr.addstr(10, 20, s)
        stdscr.refresh()

curses.nocbreak(); stdscr.keypad(0); curses.echo()
curses.endwin()