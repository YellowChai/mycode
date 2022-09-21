#!/usr/bin/env python3


def main():
    # import additional code to complete our task
    import shutil
    import os
    
    """ code to move files around """
    # move into the working directory
    os.chdir("/home/student/mycode/")

    # copy the fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # remove the existing backup directory from previous practice  and copy the entire directoryA to directoryB 
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")


if __name__ == "__main__":
    main()
