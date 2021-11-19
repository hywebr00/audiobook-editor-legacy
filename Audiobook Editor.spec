# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/Users/r00-99912/Documents/GitHub/AEditor'],
             binaries=[],
             datas=[('Language/appLang_EN.qm', 'Language'), ('Language/appLang_TC.qm', 'Language'), ('Language/qt_en.qm', 'Language'), ('Language/qt_zh_TW.qm', 'Language'), ('svg/icon', 'svg/icon'), ('Noto_Sans_TC', 'Noto_Sans_TC'), ('Noto_Sans', 'Noto_Sans'), ('audiobooks.schema.json', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Audiobook Editor',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='AudiobookEditorLogo.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Audiobook Editor')
app = BUNDLE(coll,
             name='Audiobook Editor.app',
             icon='AudiobookEditorLogo.icns',
             bundle_identifier=None)
