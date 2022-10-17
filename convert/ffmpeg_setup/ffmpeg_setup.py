"""

first unzip file
rename dir
move dir
remove dir
check if dir path exists in env path variable # TODO:- check if dir path exists in env path variable
added to path env       # TODO:- add to path env
"""

import os
import zipfile
import shutil


class main():
    # check if dir path exists in env path variable
    def check_path():
        if os.path.exists("c:\\ffmpeg\\bin")==False:
            print("ffmpeg")
        else:
            # add to path env
            os.environ["PATH"] += os.pathsep + os.pathsep.join(["c:\\ffmpeg\\bin"])
            print("ffmpeg added to env path")

    def unzip_file():
        with zipfile.ZipFile("E:\\ffmpeg.zip", "r") as zip_ref:
            zip_ref.extractall()

    def rename_file():
        os.rename("ffmpeg-2022-10-02-git-5f02a261a2-full_build", "ffmpeg")

    def move_file():
        shutil.move(".\\ffmpeg", "c:\\")

    if os.path.isdir("c:\\ffmpeg") == False:
        print("ffmpeg setup start .... ")
        unzip_file()
        rename_file()
        move_file()
        print("setup ffmpeg succeeded")

    else:
        print("ffmpeg is exist already")

    check_path()


main()
