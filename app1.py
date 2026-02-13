import streamlit as st

import numpy as np 
import matplotlib.pyplot as plt
st.title('Dynamic Pressure Profile')
st.sidebar.title('Input')



k=st.sidebar.slider('permeability(md)',min_value=10,max_value=200,value=100)

mu=st.sidebar.slider('viscosity(cp)',min_value=10,max_value=50,value=15)

q=st.sidebar.slider('flowrate(stm/day)',min_value=100,max_value=200,value=150)

re=st.sidebar.number_input('outer radius of reservoir(ft)',min_value=100,max_value=10000,value=3000)

rw=st.sidebar.number_input('wellbore radius(ft)',min_value=1,max_value=10,value=1)

pe=st.sidebar.number_input('pressure at the boundary of the reservoir(psi)',min_value=100,max_value=10000,value=4000)

B=st.sidebar.number_input('formation volume factor(bbl/stb)',min_value=1,max_value=2,value=1)

h=st.sidebar.number_input('net pay thickness of reservoir(ft)',min_value=2,max_value=500,value=30)

r=np.linspace(re,re,500)
P = pe - (141.2*q*mu*B*(np.log(re/r))/k/h)
idx = np.argmin(np.abs(r - rw))
y_min = P[idx]


b=st.button('show pressure profile')

if b:
    plt.style.use('classic')
    plt.figure(figsize=(6,4))
    fig,ax=plt.subplots()
    ax.plot(r,P,linewidth=4)
    ax.grid(True)
    ax.axhline(y_min, linewidth=3, color='red')
    ax.set_xlabel('radius')
    ax.set_ylabel('pressure at radius r, (psi)')
    ax.set_title('pressure profile')
    ax.set_ylim(0,5000)
    ax.plot(r,P)
    st.pyplot(fig)
