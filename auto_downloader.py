import random
import os
import sys
import requests
#%% get the current directory
def current():
    """return the current working directory"""
    value=os.getcwd()
    return value
#%% list all the txt file of the current directory
def listing():
    x = (os.listdir(os.getcwd()))
    y=[]
    s='.txt'
    for i in x:
        if s in i:
            y.append(i)
    return y
#%% return file content as a list
#def file_det(file):
##    if '.txt' in file:
##        name=file
##    elif '.' not in file:
##        name=file+'.txt'
##    else:
##        pass
#    with open(str(file),'r') as f:
#        v=list(f)
#    return v
        
#%%
def create_dir(file):
    name=file.strip('.txt')
    os.mkdir(name,0o755)
    print("\nDirectory successfully created")
    return name
#%%
def change_dir(name):
    if(os.path.exists(name)):
        os.chdir(name)
#%%
#def download(file):
ls=listing()    
print(ls)

for file in ls:
    name=create_dir(file+'1')
    print('Creating the {0} folder\n'.format(name))
    print('Accessing the file {0}\n\n'.format(file))
    with open(file,'r') as f:
        content=list(f)
    change_dir(name)
#        numbers=ramdom.sample(range(0,10000),len(content))
    for j in range(0,len(content)):
        extension=content[j].split('.')[-1].strip('\n')
        name_image=str(j+1)+extension
        print('Getting the content of the line {0}\n'.format(j+1))
        con=content[j].strip('\n')
        print('Downloading...\n')
        r=requests.get(con)
        with open(name_image,'wb') as picture:
            picture.write(r.content)
            print('Storing image to the folder...')

#%%
            
            
            
            
#            select the to-be-downloaded data on the basis of extension(jpg,jpeg,JPG,JPEG,png,PNG)
#            no gifs