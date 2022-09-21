#!/usr/bin/env python3

def main():


    import shutil
    import os

    # make it start in the home user directory by calling os.chdir()
    os.chdir('/home/student/mycode/')
    
    # move the file to the path destination, returning a string of the absolute path of the new location. if the file is already in the destination, it will overwrite  
   
    #shutil.move('ranor.obj','ceph_storage/')
    
    # prompt to user for the new name of the file 
    xname = input('what is the first name of your childhood bestfriend?')
    
    #Rename kerrigan.obj file(by changing the path?)
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

    


if __name__ == "__main__":
    main()
