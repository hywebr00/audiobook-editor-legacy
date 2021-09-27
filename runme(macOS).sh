pyinstaller -F -n AEditor \
-i AudiobookEditorLogo.icns \
--add-data="Language/appLang_TC.qm:Language" \
--add-data="Language/appLang_EN.qm:Language" \
--add-data="svg/icon:svg/icon" \
--add-data="Noto_Sans_TC:Noto_Sans_TC" \
--add-data="Noto_Sans:Noto_Sans" \
--add-data="audiobooks.schema.json:." \
--add-data="about_licenses.html:." \
--windowed --noconfirm \
main.py
