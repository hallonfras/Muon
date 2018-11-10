# Imports
import os
import subprocess


# Declaring variables
home = os.getenv("HOME")

f = open(home + "/.cache/wal/colors")
color1 = f.readline()
color2 = f.readline()
color3 = f.readline()
color4 = f.readline()
color5 = f.readline()
color6 = f.readline()
color7 = f.readline()
color8 = f.readline()
color9 = f.readline()
color10 = f.readline()
color11 = f.readline()
color12 = f.readline()
color13 = f.readline()
color14 = f.readline()
color15 = f.readline()
color16 = f.readline()




class obTheme:
      def __init__(self, brightness):
            self.brightness = brightness

    
      def makeTheme(self):
            f = open("themerc","w")
            f.write("""!! menu background
menu.items.bg: flat
menu.items.bg.color: """+ color1 +"""
menu.overlap.x: -8

!! menu text
menu.items.text.color: """ + color16 + """
menu.items.justify: left
menu.items.disabled.text.color: #4d5066

!! menu separator
menu.separator.padding.height: 2
menu.separator.color: """+ color1 +"""

!! menu border
menu.border.width: 6
menu.border.color: """+ color1 +"""

!! menu headers
menu.title.bg: flat
menu.title.bg.color: """+ color1 +"""
menu.title.text.color: #000000
menu.title.text.justify: center

!! selected menu item
menu.items.active.bg: flat
menu.items.active.bg.color: #c5e1e3
menu.items.active.text.color: """ + color1 + """

!! titlebar
window.active.title.bg: flat
window.active.title.bg.color: """ + color3 + """
window.inactive.title.bg: flat
window.inactive.title.bg.color: """+ color1 +"""

!! titlebar text
window.label.text.justify: center
window.active.label.bg: parentrelative
window.active.label.text.color: """ + color2 + """
window.inactive.label.bg: parentrelative
window.inactive.label.text.color: """ + color15 + """

!! borders
window.active.border.color: """+ color1 +"""
window.inactive.border.color: """+ color1 +"""
padding.width: 8
padding.height: 8
window.client.padding.width: 0
window.client.padding.height: 0
border.width: 0
window.handle.width: 0

window.active.client.color:  """+ color1 +"""
window.inactive.client.color:  """+ color1 +"""

window.active.handle.bg: flat
window.active.handle.bg.color: """+ color1 +"""
window.inactive.handle.bg: flat
window.inactive.handle.bg.color: """+ color1 +"""

window.active.grip.bg: flat
window.active.grip.bg.color: """+ color1 +"""
window.inactive.grip.bg: flat
window.inactive.grip.bg.color: """+ color1 +"""

!! on-screen displays
osd.border.width: 1
osd.border.color: """+ color1 +"""
osd.label.text.color: """ + color2 + """
osd.bg: flat solid
osd.bg.color: """+ color1 +"""
osd.label.bg: flat solid
osd.label.bg.color: """+ color1 +"""
osd.hilight.bg: flat solid
osd.hilight.bg.color: """ + color3 + """
osd.unhilight.bg: flat solid
osd.unhilight.bg.color: """ + color15 + """


!! window buttons
window.*.button.*.bg: parentrelative
window.*.button.*.pressed.bg: flat

window.active.button.*.hover.bg: flat
window.active.button.*.hover.bg: parentrelative
window.active.button.*.hover.bg.color: """ + color3 + """
window.active.button.hover.image.color: #c5e1e3
window.active.button.*.pressed.bg.color: """ + color15 + """
window.active.button.toggled.image.color: #c5e1e3
window.active.button.disabled.image.color: """ + color16 + """

window.inactive.button.*.hover.bg: flat
window.inactive.button.*.hover.bg: parentrelative
window.inactive.button.hover.image.color: #c5e1e3
window.inactive.button.toggled.image.color: #c5e1e3
window.inactive.button.disabled.image.color: """ + color16 + """

window.active.button.close.unpressed.image.color: """ + color15 + """
window.active.button.close.pressed.image.color: """ + color15 + """
window.inactive.button.close.unpressed.image.color: """ + color15 + """
window.inactive.button.close.pressed.image.color: """ + color15 + """

window.active.button.max.unpressed.image.color: """ + color14 + """
window.active.button.max.pressed.image.color: """ + color14 + """
window.inactive.button.max.unpressed.image.color: """ + color14 + """
window.inactive.button.max.pressed.image.color: """ + color14 + """

window.active.button.iconify.unpressed.image.color: """ + color13 + """
window.active.button.iconify.pressed.image.color: """ + color13 + """
window.inactive.button.iconify.unpressed.image.color: """ + color13 + """
window.inactive.button.iconify.pressed.image.color: """ + color13 + """

window.active.button.shade.unpressed.image.color: #cecce2
window.active.button.shade.pressed.image.color: #cecce2
window.inactive.button.shade.unpressed.image.color: #cecce2
window.inactive.button.shade.pressed.image.color: #cecce2

window.active.button.desk.unpressed.image.color: #87e0dc
window.active.button.desk.pressed.image.color: #87e0dc
window.inactive.button.desk.unpressed.image.color: #87e0dc
window.inactive.button.desk.pressed.image.color: #87e0dc
""")
            #subprocess.call(["mv", "themerc", "Muon/openbox-3/"])
            #subprocess.call(["cp", "-R", "Muon", home + "/.themes"])
                  


obTheme = obTheme("bright")

obTheme.makeTheme()
subprocess.call(["mv", "themerc", "Muon/openbox-3/"])
subprocess.call(["cp", "-R", "Muon", home + "/.themes"])
subprocess.call(["openbox", "--reconfigure"])




