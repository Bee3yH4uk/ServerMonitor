import argparse
from tkinter import filedialog, Tk

from src.server_monitor.main import start_parse


def get_file_name():
    print("Выберите файл с хостами")
    root = Tk()
    root.wm_withdraw()
    root.attributes("-topmost", True)
    root.lift()
    root.focus()
    file_name = filedialog.askopenfilename()
    root.destroy()
    root.mainloop()
    return file_name


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', '-p')
    parser.add_argument('--ignore_errors', '-i', default='F')

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
    print(namespace)
    if not namespace.path:
        f_path = get_file_name()
    else:
        f_path = namespace.path
    start_parse(f_path, ignore_errors=True if namespace.ignore_errors == "T" else False)

