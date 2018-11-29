import os
import sys
import random
import requests
import pandas as pa
#%%
class Download_urls:
    
    def __init__(self, extension):
        self.extension = extension
        
    def download(self):
        print('Do you want to download all the files with {0} extension [Y/N]: '.format(self.extension),end='')
        a=input()
        if a=='Y' or a=='y':
            ls=listing() 
            if len(ls)==0:
                print('Sorry there are no files with the given extension')
            else:
                print('The files to be downloaded are:')
                for i in ls:
                    print(i)
                download_all(ls)
            
    def download_all(self,ls):
        print('Creating new folders in the location: {0}'.format(current_dir))
        loop_download(ls)
    
    def loop_download(self,ls_file):
        if self.extension=='csv':
            ls_col_name=enter(ls_file)
            ls=dict(zip(ls_file,ls_col_name))
            download_csv(ls)
        elif self.extension=='txt':
            for file in ls_file:
                name=create_dir(file+'1')
                print('Creating the {0} folder\n'.format(name))
                print('Accessing the file {0}\n\n'.format(file))
                with open(file,'r') as f:
                    content=list(f)
                change_dir(name)
                down(content)
                cd()
            print('\n\n COMPLETED!!')
    
    def enter(self,ls):
        print('Please enter the name of the columns containing the urls')
        l=[]
        for i in ls:
            a=input(i+' : ')
            l.append(a)
        return l
    
    def download_csv(self,ls):
        """Download the urls present in the column with the specified column name"""
        try:
            for i in ls:
                name=create_dir(i+'1')
                print('Creating the {0} folder\n'.format(name))
                print('Accessing the file {0}\n\n'.format(i))
                dataset=pa.read_csv(i)
                try:
                    dataset=dataset[ls[i]]
                    down(dataset)
                except KeyError:
                    print('Specified column does not exist')
                change_dir(name)
                down(dataset)
                cd()
            print('\n\n COMPLETED!!')      
        except FileNotFoundError:
            print('No file found in the directory')
            print('Please check the location of the file and try again')
            
    
    def down(self,content): 
        for j in range(0,len(content)):
            self.extension=content[j].split('.')[-1].strip('\n')
            name_image=str(j+1)+'.'+self.extension
            print('Getting the content of line {0}\n'.format(j+1))
            con=content[j].strip('\n')
            print('Downloading...\n')
            r=requests.get(con)
            with open(name_image,'wb') as picture:
                picture.write(r.content)
                print('Storing image to the folder...')
                
    def listing(self):
        """list all the files with the specified exttension present in the current working directory"""
        x = (os.listdir(os.getcwd()))
        y=[]
        s=self.extension
        for i in x:
            i=i.split('.')[-1]
            if s==i:
                y.append(i)
        return y

    def create_dir(self,file):
        """creates a new folder in the current workign directory by the specified filename"""
        name=file.strip('.txt')
        os.mkdir(name,0o755)
        print("\nDirectory successfully created")
        return name
    
    def change_dir(self,name):
        """change the current working direcrtory to the mentioned filename in the parent directory"""
        if(os.path.exists(name)):
            os.chdir(name)
    
    def cd(self):
        """change the current working directory to the parent directory"""
        a=os.getcwd()
        a=a.split('/')[:-1]
        a=('/').join(a)
        os.chdir(a)
        
    def current():
        """return the current working directory"""
        value=os.getcwd()
        return value

    current_dir = current()