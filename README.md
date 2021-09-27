# 有聲書編輯器（Audiobook Editor）

## 關於（About）

本專案提供一個具基本介面與功能，可用來產出符合`W3C Audiobooks`標準有聲書之軟體。本專案係由凌網科技股份有限公司開發以用於HyRead電子書平台內部使用。凌網科技與HyRead團隊基於推廣數位出版與`W3C有聲書`標準之精神，將本專案之相關成果與原始碼以MIT授權方式開放供公眾使用，您可以在MIT授權的條件下免費且自由地運用本專案。也歡迎您加入本專案共同開發更多好用的功能或直接下載安裝程式製作您的有聲書。
如您有任何問題請在 [Github 建立 Issues](https://github.com/hywebr00/audiobook-editor/issues)。

This project provides a fundamental user interface and editing functionality to produce audiobooks complying with the `W3C Audiobooks` standard. Hyweb Technology developed this project for use within the HyRead eBook platform. To promote digital publishing and the `W3C Audiobooks` standard, Hyewb and the HyRead team have made this project for the public under the MIT license. Welcome to join this project to make it better or just download this tool to make your own audiobooks.
Please [create issues on Github](https://github.com/hywebr00/audiobook-editor/issues) if you have any problems.

## 安裝檔下載（Binary Download）
本專案提供 Windows 之預編譯執行檔供下載（macOS 將於近期提供），如需其他版本請自行編譯。

This project provides pre-built Windows binary files (macOS is on the way).

下載安裝檔（Download Installer）：https://github.com/hywebr00/audiobook-editor/releases

## 開發環境（Development Environments）

### 開發環境版本（Env. Versions）
- Windows 10 x64 with Python 3.9.6
- PySide2 for the GUI.

### 套件與模組（Packages & Modules Used）
- backports.tempfile
- beautifulsoup4
- html5lib
- jsonschema
- multipledispatch
- tinytag
- pyinstaller
- PySide2
- regex
- requests
- urllib3

### 字體（Fonts）
- Noto Sans
- Noto Sans TC

These fonts are licensed under the <a href="https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&amp;id=OFL">Open Font License</a>.

### 編譯與安裝檔制作（Make Release Package & Installer）
#### Windows
This project use `PyInstaller` to produce the directory structure of production and `Inno Setup` to generate the final executable installer, both under Windows. 
The `AEditor.spec` file is for pyinstaller, just provided here to be a reference.

#### macOS (developed on Big Sur)
`PyInstaller` is still used under macOS to produce an executable .APP. The <a href="https://www.araelium.com/dmgcanvas">`DMG Canvas`</a> is used to make the final installer.

#### MP3 Codec/Backend
- Windows
MP3 Codec on Windows 10(audio backend of Qt): <a href="http://www.codecguide.com/configuration_tips.htm?version=1595">`K-Lite Codec Pack`</a> 

- macOS (developed on Big Sur)
MP3 Codec is built-in on macOS.

## 貢獻者（Contributors）
**Hyweb Technology Co., Ltd.**
- PM: Yu-Wei Chang (Yanni)
- Programmer: Skyrookie Yu
- UI/UX: Iris Chung, Yuyu Lin
- Testing: Wesley Chiou

## W3C有聲書標準（W3C Audiobooks Spec）
- English (Official): https://www.w3.org/TR/audiobooks/
- 中文版（台灣數位出版聯盟翻譯）：https://github.com/dpublishing/audiobooks-specs-tc
- 有聲書範本（台灣數位出版聯盟製作）：https://github.com/dpublishing/audiobooks-samples
