
import pathlib
import subprocess as sub


build_cmd = [r'{}\anaconda3\pkgs\pyqt-5.9.2-py39hd77b12b_6\Library\bin\pyrcc5.bat'.format(pathlib.Path.home()), "-o", "resources.py", "resources.qrc"]
print(f"INFO: Creating: qrc: {' '.join(build_cmd)}")
sub.call(build_cmd)
