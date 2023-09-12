from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_exe_options = {
    "packages": ["tkinter", "keyboard", "pyautogui", "time"],
    "include_files": [],
    "excludes": []
}

base = None

setup(
    name="AutoTyper",
    version="0.1",
    description="An application to auto-type text",
    options={"build_exe": build_exe_options},
    executables=[Executable("rough2.py", base=base)]
)
