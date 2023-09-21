
import pathlib
import subprocess as sub

for path in pathlib.Path.cwd().glob("*.ui"):

    build_cmd = [r'{}\anaconda3\Scripts\pyuic5'.format(pathlib.Path.home()), "-o", f"{path.stem}.py", str(path)]
    print(f"INFO: Creating: ui -> py: {' '.join(build_cmd)}")
    sub.call(build_cmd)
    pathlib.Path(f"{path.stem}.py").write_text(
        pathlib.Path(f"{path.stem}.py").read_text().replace("import resources_rc",
                                                            "from resources import resources"))