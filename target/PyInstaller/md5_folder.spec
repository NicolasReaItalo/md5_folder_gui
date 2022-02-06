# -*- mode: python -*-

block_cipher = None


a = Analysis(['/Users/user/Documents/DEF/Version_0-5/md5_folder_gui/src/main/python/main.py'],
             pathex=['/Users/user/Documents/DEF/Version_0-5/md5_folder_gui/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/Users/user/Documents/DEF/Version_0-5/md5_folder_gui/venv/lib/python3.6/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/Users/user/Documents/DEF/Version_0-5/md5_folder_gui/target/PyInstaller/fbs_pyinstaller_hook.py'],
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
          name='md5_folder',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='/Users/user/Documents/DEF/Version_0-5/md5_folder_gui/target/Icon.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='md5_folder')
app = BUNDLE(coll,
             name='md5_folder.app',
             icon='/Users/user/Documents/DEF/Version_0-5/md5_folder_gui/target/Icon.icns',
             bundle_identifier=None)
