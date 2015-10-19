import subprocess

path = "'C:\Program Files (x86)\Steam\steamapps\common\TUG\Game\Core'"

subprocess.call("del /S /A [:*.dds *.hkt] {}".format(path), shell=True)
