pyCharGen
---------------

This is a character generator designed for the Rolemaster Universal (RMU) role-playing system.
Direct downloads of pyCharGen can be found at the releases section <https://github.com/EldritchCheese/pyCharGen/releases>,
 which contain stand-alone executables for both Windows and Linux.

Features
----------------
- Create and modify characters for use in RMU.
- Add items, which contribute bonuses to stats and skills.
- Save and load characters in a human-readable text format.
- Export characters to pdf format


pyCharGen is written in python 2.7, and requires the following external packages to be run from source.  Again, no external programs are needed when running from the packaged binaries, only when running from source.
   - pygtk ("sudo apt-get install python-gtk2" in linux or <http://ftp.gnome.org/pub/GNOME/binaries/win32/pygtk/2.24/pygtk-all-in-one-2.24.2.win32-py2.7.msi> for Windows)
   - pyparsing, v2.0 or higher <http://sourceforge.net/projects/pyparsing/>
   - pdftex.exe for Windows, or pdflatex for Linux (Needed for pdf output of character)
   - pyinstaller <http://pyinstaller.org> (Needed only for packaging standalone executable)
   - pywin32 <http://sourceforge.net/projects/pywin32/> (Needed only for packaging standalone executable)
