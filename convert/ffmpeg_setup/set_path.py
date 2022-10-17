# added path

import os

if os.environ['PATH'] == 'c:\\ffmpeg\\bin':
    print("ffmpeg is exist already")
else:
    # add to path env
    os.environ["path"] = "c:\\ffmpeg\\bin"
    print("ffmpeg added to env path")
