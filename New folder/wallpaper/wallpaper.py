import ctypes 

ctypes.windll.user32.SystemParametersInfoW(20, 0, r"new wallpaper location address",0)

