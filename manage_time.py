import time
import webbrowser

intervalInSeconds = 5
totalBreaks = 3

print("This program started on "+time.ctime())
for num in range(0, totalBreaks):
    time.sleep(intervalInSeconds)
    webbrowser.open("http://www.youtube.com/watch?v=o1tj2zJ2Wvg")
