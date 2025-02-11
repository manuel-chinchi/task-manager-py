APP_TITLE = "Adminstrador de procesos"
APP_ICON = "taskmgr.exe_14_107.ico"
# WINDOW_SIZE = "640x480"
WINDOW_SIZE="800x600"

# IDs controls
COLUMN_ID = 101
COLUMN_PROCESS_NAME = 102
COLUMN_STATUS = 103
COLUMN_LOCATION = 1031
BUTTON_SEARCH = 104
BUTTON_UPDATE = 105
LABEL_TOTAL = 106
BUTTON_SETTINGS =107
CHECKBOX_ADJUST_AUTOMATIC_COLS=108
CHECKBOX_DARK_THEME=110
BUTTON_CLOSE_SETTINGS = 109

COLUMN_HEADERS = {
    COLUMN_ID : "Id",
    COLUMN_PROCESS_NAME : "Nombre",
    COLUMN_STATUS : "Estado",
    COLUMN_LOCATION: "Ubicación"
}

BOTTOM_FRAME = {
    BUTTON_SEARCH : "Buscar",
    BUTTON_UPDATE : "Actualizar",
    BUTTON_SETTINGS : "Configuración",
    LABEL_TOTAL : "Total"
}

SETTINGS_OPTIONS = {
    CHECKBOX_ADJUST_AUTOMATIC_COLS: "Ajuste automático de columna",
    CHECKBOX_DARK_THEME: "Activar tema nocturno",
    BUTTON_CLOSE_SETTINGS: "Cerrar"
}

SORT_ASC_ICON = "▲"
SORT_DESC_ICON = "▼"

def adjust_dpi():
    # @TODO solucion DPI alto en pantallas https://stackoverflow.com/questions/62794931/high-dpi-tkinter-re-scaling-when-i-run-it-in-spyder-and-when-i-run-it-direct-in
    import ctypes
    try: # >= win 8.1
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except: # win 8.0 or less
        ctypes.windll.user32.SetProcessDPIAware()