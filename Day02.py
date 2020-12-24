#!/usr/bin/env python
# coding: utf-8

# In[53]:


#variable
#syntax

var=123
#memory location
print("memory location : " ,id(var))
print("data in bar     :",var)


# In[ ]:





# In[6]:


#example:create a student record
std1_name = "Muskan"
std1_roll = 456
std2_name = "Smile"
std2_roll = 457


# In[4]:


#user defined names are called identifiers-Examples(Variables)
  #purpose of identifpiers - to give name entities to variables , functions or classes.
  #limitations - we can use alphabets , we can use integers , we can use underscores .
  #don't start with a digit
  #don't use special characters 
  
  


# In[5]:


#limitatione of identifiers
_std_name5="bhsh"
print("_std_name5")


# In[6]:


#don't start with a number
5_std_name5="bhsh"
print("5_std_name5")


# In[7]:


#don't start with a special character
get_ipython().system('_std_name5="bhsh"')
print("!_std_name5")


# In[8]:


#data types
#two types of data types in python
# 1. fundamental data types - which hold a single type of data
  #int
    #float
    #complex
    #bool
    #none type
# 2. sequential data type - which hold multiple data types
   #str
    #list
    #tuple
    #set
    #dict
    


# In[1]:


#datatype
#int
a=-12734687
b=0
c=34743
print(type(a))
print(type(b))
print(type(c))


# In[2]:


#float data type <<<--real floating /pointing nnumbers /continuous
a=-12.544444444
b=0.0000
c=12323.3948
print(type(a))
print(type(b))
print(type(c))


# In[3]:


#complex <<<=== real+imaginary ===>>>X+Yj
a=12+45j
b=0+0j
print(type(a))
print(type(b))


# In[4]:


#book datatype
a=True
b=False
print(type(a))
print(type(b))


# In[5]:


#None data type --->>>None/Null-There is no data.
a= None
print(type(a))


# In[7]:


#string data --->group of characters / '' / " " /''''''''''/""""""""""
a='python'
b="python"
c='''python'''
d="""python"""
print(type(a))
print(type(b))
print(type(c))
print(type(d))


# In[8]:


#Task - what is the difference between single/double/triple qquotes.


# In[9]:


#list data type --->collection of dissimilar data type elements within the []
a=[1,2,3,4]
b=[1,4.3,4+5j,True]
print(type(a))
print(type(b))


# In[10]:


#tuple --->collection of dissimilar datatype elemnets within ()
a=(1,2,3,4)
b=(1,4.3,4+5j,True)
print(type(a))
print(type(b))


# In[11]:


#set -->collection of dissimilar datatype elements within {}
a={1,2,3,4}
b={1,4.3,4+5j,True}
print(type(a))
print(type(b))


# In[9]:


#dictionary datatype--->collection of dissimilar data items (key : value) with in{}
a={3 : 30 , 6 :60}
print(type(a))


# In[13]:


#Indexing -->to access the data elements from sequential datatype variable

#Positive indexing --->0 to ten -1
a="python"# 6<<<---len of a
print(a[0]) #p
print(a[1]) #y
print(a[2]) #t
print(a[3]) #h
print(a[4]) #o
print(a[5]) #n


# In[15]:


#Negative indexing
print(a[-1]) #n
print(a[-2]) #o
print(a[-3]) #h
print(a[-4]) #t
print(a[-5]) #y
print(a[-6]) #p


# In[16]:


#DifFerence b/w list , set , tuple 


# In[17]:


#List indexing
a=[1,2,3]
print(a[0])
print(a[1])
print(a[2])
print(a[-1])
print(a[-2])
print(a[-3])


# In[19]:


#tuple indexing
a=(1,2,3)
print(a[0])
print(a[1])
print(a[2])
print(a[-1])
print(a[-2])
print(a[-3])


# In[20]:


#set indexing
a={1,2,3}
print(a[0])
print(a[1])
print(a[2])
print(a[-1])
print(a[-2])
print(a[-3])

#set datatype doesn't support indexing


# In[22]:


#dict indexing
a={10 : 34,89:70}
print(a[10])
print(a[89])


# In[23]:


#string replacement
a="python"
print(a)
a[0]="p"
print(a)


# In[25]:


#list replacement
a=[1,2,3]
print(a)
a[1]=200
print(a)


# In[26]:


a={23,90,34,23}
print(a)


# In[27]:


a=[23,90,34,23]
print(a)


# In[28]:


a={5,8,2,0,45,100,-45} #unordered data type --->>indexing is not supported
print(a)


# In[34]:


a="python ah HHH"
print(a.lower())
print(a.upper())
print(a.title())
print(a.capitalize())
print(a.swapcase())
print(a.split())


# In[35]:


a=["python ah HHH"]
print(" ".join(a))


# In[36]:


a=[1,2,3]
print(a)
a.append(100)
print(a)


# In[37]:


a=[9,4,90,12,67]
print(a)
a.sort()
print(a)


# In[38]:


a=[9,4,90,12,67]
print(a)
a.reverse()
print(a)


# In[39]:


a=[9,4,90,12,67]
print(a)
a.remove(90)
print(a)


# In[40]:


a=[9,4,90,12,67]
print(a)
a.pop(2)
print(a)


# In[42]:


a=[1,2,3]
b=[4,5,6]
print(a)
a.extend(b)
print(a)


# In[43]:


a={1,2,3,4}
b={3,4,5,6}
print(a.union(b))


# In[44]:


a={1,2,3,4}
b={3,4,5,6}
print(a.intersection(b))


# In[46]:


a={1,2,3,4}
b={3,4,5,6}
print(a.difference(b))
print(b.difference(a))


# In[47]:


a={1,2,3,4}
b={3,4,5,6}
#union intersection
print(a.symmetric_difference(b))


# In[49]:


a={1,2,4,5}
print(a)
a.discard(4)
print(a)


# In[50]:


a={1,2,4,5}
print(a)
a.remove(4)
print(a)


# In[52]:


a={12:45 , 90:34}
print(a.keys())
print(a.values())
print(a.items())


# In[ ]:




