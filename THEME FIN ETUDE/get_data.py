# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 16:51:21 2020

@author: aitam
"""

def get_data(path,width,height,dis_file,t):
   
    #1)recuperation du contenu du dossier c:\dossier\
        import matplotlib.image as mpimg
        import os
        import numpy as np
        from skimage.transform import resize
        import csv
        from PIL import Image
       
        contenu=os.listdir(path)

        data = np.array([]) 
        Xdata = np.array([])
        
        for n in contenu:
            img = np.array(Image.open(path+n))
    
            img = resize(img, (width, height), anti_aliasing=True)

            v=np.ravel(np.array((img[:,:,0]+img[:,:,1]+img[:,:,2])/3))
    
            data = np.append(data,v)

        data= np.reshape(data,(len(contenu),width*height))
        if t==1 :
             y=np.ones((len(contenu)))
        
        else :
             y=np.zeros(len(contenu))
      
        data= np.c_[data,y]

#file = open("out.csv" , "w")
#writer= csv.writer(file) 
#writer.writerow(data


        with open(dis_file, 'w', newline='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')    
            for row in data:
                writer.writerow(row)
        
        csvfile.close()