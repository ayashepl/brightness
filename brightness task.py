#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[22]:


img = cv2.imread('GS img.jpeg')
plt.subplot(1,2,1)
plt.title('original')
plt.imshow(img)
plt.subplot(1,2,2)
z=cv2.add(img,20)
plt.imshow(z)
plt.title('image after subtraction')


# In[23]:


img = cv2.imread('GS img.jpeg')
plt.subplot(1,2,1)
plt.title('original')
plt.imshow(img)
plt.subplot(1,2,2)
z=cv2.subtract(img,20)
plt.imshow(z)
plt.title('image after subtraction')


# In[24]:


img = cv2.imread('GS img.jpeg')
plt.subplot(1,2,1)
plt.title('original')
plt.imshow(img)
plt.subplot(1,2,2)
plt.imshow(img+10)
plt.title('image after addition')


# In[25]:


img = cv2.imread('GS img.jpeg')
plt.subplot(1,2,1)
plt.title('original')
plt.imshow(img)
plt.subplot(1,2,2)
plt.imshow(img-75)
plt.title('image after subtraction')


# In[ ]:




