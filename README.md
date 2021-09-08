AE-Hyweb
Goal & Our Promise
AE-Hyweb is demostrating the fundamental user interface and editing functionality that a W3C-spec comformant audiobook editor should provide. This project is free and public to all the world under GNU license. Welcome to join this project and make your own audiobooks by using this editor.

Development Environments
Developed on Windows 10 x64 under Anaconda with Python 3.7.9. Sure thing, you don't need Anaconda. Instead, PyQt5 and a few 3rd party packages are enough. Python 3.7+ should be sufficient to run this program.

Packages & Modules Used
backports.tempfile, beautifulsoup4, html5lib, jsonschema, multipledispatch, mutagen, pyinstaller, PyQt5, Python, Qt5, regex, requests, urllib3

Make Release Package & Make Installer
Windows
We use PyInstaller to produce the directory structure of production and Inno Setup to generate the final executable installer, both under Windows. The AEditor.spec file is for pyinstaller, just provided here to be a reference.

macOS (developed on Big Sur)
PyInstaller is still used under macOS to produce an executable .APP and DMG Canvas is used to make the final installer.

MP3 Codec/Backend
Windows
MP3 Codec on Windows 10(backend of PyQt5):　http://www.codecguide.com/configuration_tips.htm?version=1595

macOS (developed on Big Sur)
MP3 Codec is built-in on macOS.

Our team as of now:
PM: Yanni Chang
Programmer: Skyrookie Yu
UI/UX: Iris, Yuyu
Test: Wesley
