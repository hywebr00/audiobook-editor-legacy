# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['D:\\Github\\AEditor'],
             binaries=[],
             datas=[('Noto_Sans\\*', 'Noto_Sans'), ('Noto_Sans_TC\\*', 'Noto_Sans_TC'), ('audiobooks.schema.json', '.'), ('Language\\appLang_EN.qm', 'Language'), ('Language\\appLang_TC.qm', 'Language'), ('svg\\icon\\*', 'svg\\icon'), ('AudiobookEditorLogo.ico', '.')],
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
          name='AEditor',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False)
		  
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
