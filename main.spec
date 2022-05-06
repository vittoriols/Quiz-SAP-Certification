# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\VittorioLorisSimonet\\Desktop\\Personale\\PY\\APP\\QUIZ HANA'],
             binaries=[],
             datas=[('ConfigQuiz.xlsx', '.'), ('iconafinale.ico', '.'), ('iconafinale2.ico', '.'), ('Guida.pdf', '.'), ('group.qrc', '.'), ('GUIDefinitiva.ui', '.'), ('splash_screen.ui', '.')],
             hiddenimports=['MainDefinitivo.py', 'ui_main.py', 'ui_splash_screen.py', 'group_rc.py', 'addonsfunctions.py', 'pkg_resources.py2_warn'],
             hookspath=[],
             hooksconfig={},
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
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='iconafinale.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
