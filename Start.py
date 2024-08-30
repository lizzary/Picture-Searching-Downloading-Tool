#pyinstaller -w -F -i package\icon.ico --splash package/loading.png Start.py

from package.ui import runUi

if __name__ == "__main__":
    try:
        import pyi_splash
        pyi_splash.close()
    except ImportError:
        pass

    runUi.run()

