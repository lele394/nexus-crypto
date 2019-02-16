import numpy as np
from ressources.character import *


""" #cube structure = xyz
#les listes prennent une suite de x, donc une ligne y
"""


#z1------------------------
z1y1 = np.array([a,b,c,d,e,f])
z1y2 = np.array([g,h,i,j,k,l])
z1y3 = np.array([m,n,o,p,q,r])
z1y4 = np.array([s,t,u,v,w,x])
z1y5 = np.array([y,z,point,virgule,apostrophe,espace])
z1y6 = np.array([é,è,à,doubleApostrophe,oParenthese,cParenthese])


#z2----------------------
z2y1 = np.array([l,g,h,i,j,k])
z2y2 = np.array([r,m,n,o,p,q])
z2y3 = np.array([x,s,t,u,v,w])
z2y4 = np.array([espace,y,z,point,virgule,apostrophe])
z2y5 = np.array([cParenthese,é,è,à,doubleApostrophe,oParenthese])
z2y6 = np.array([f,a,b,c,d,e])


#z3---------------------
z3y1 = np.array([q,r,m,n,o,p])
z3y2 = np.array([w,x,s,t,u,v])
z3y3 = np.array([apostrophe,espace,y,z,point,virgule])
z3y4 = np.array([oParenthese,cParenthese,é,è,à,doubleApostrophe])
z3y5 = np.array([e,f,a,b,c,d])
z3y6 = np.array([k,l,g,h,i,j])


#z4---------------------
z4y1 = np.array([v,w,x,s,t,u])
z4y2 = np.array([virgule,apostrophe,espace,y,z,point])
z4y3 = np.array([doubleApostrophe,oParenthese,cParenthese,é,è,à])
z4y4 = np.array([d,e,f,a,b,c])
z4y5 = np.array([j,k,l,g,h,i])
z4y6 = np.array([p,q,r,m,n,o])


#z5--------------------
z5y1 = np.array([point,virgule,apostrophe,espace,y,z])
z5y2 = np.array([à,doubleApostrophe,oParenthese,cParenthese,é,è])
z5y3 = np.array([c,d,e,f,a,b])
z5y4 = np.array([i,j,k,l,g,h])
z5y5 = np.array([o,p,q,r,m,n])
z5y6 = np.array([u,v,w,x,s,t])


#z6--------------------
z6y1 = np.array([è,à,doubleApostrophe,oParenthese,cParenthese,é])
z6y2 = np.array([b,c,d,e,f,a])
z6y3 = np.array([h,i,j,k,l,g])
z6y4 = np.array([n,o,p,q,r,m])
z6y5 = np.array([t,u,v,w,x,s])
z6y6 = np.array([z,point,virgule,apostrophe,espace,y])


#plan par z
z1 = np.array([z1y1,z1y2,z1y3,z1y4,z1y5,z1y6]) #11
z2 = np.array([z2y1,z2y2,z2y3,z2y4,z2y5,z2y6]) #12
z3 = np.array([z3y1,z3y2,z3y3,z3y4,z3y5,z3y6]) #13
z4 = np.array([z4y1,z4y2,z4y3,z4y4,z4y5,z4y6]) #14
z5 = np.array([z5y1,z5y2,z5y3,z5y4,z5y5,z5y6]) #15
z6 = np.array([z6y1,z6y2,z6y3,z6y4,z6y5,z6y6]) #16

#plan par y
y1 = np.array([z1y1,z2y1,z3y1,z4y1,z5y1,z6y1]) #17
y2 = np.array([z1y2,z2y2,z3y2,z4y2,z5y2,z6y2]) #18
y3 = np.array([z1y3,z2y3,z3y3,z4y3,z5y3,z6y3]) #19
y4 = np.array([z1y4,z2y4,z3y4,z4y4,z5y4,z6y4]) #20
y5 = np.array([z1y5,z2y5,z3y5,z4y5,z5y5,z6y5]) #21
y6 = np.array([z1y6,z2y6,z3y6,z4y6,z5y6,z6y6]) #22
