#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import seaborn as sns


# In[3]:


path = "C:/Users/amans/Downloads/graph_metrics_2022-03-17.json"


# In[4]:


import urllib


# In[5]:


import json


# In[6]:


with open(path , encoding='utf-8') as f:
    data = json.load(f)


# In[7]:


data


# In[8]:


print(data.keys())


# In[9]:


len(data['nodes'])


# In[10]:


len(data['edges'])


# In[11]:


data['nodes'][0].keys()


# In[12]:


data['nodes'][0]['features']['5'].keys()


# In[13]:


data['edges'][0].keys()


# In[14]:


data['edges'][1001]['node1_policy']


# In[15]:


edges = pd.DataFrame(data['edges'])    


# In[16]:


edges.head()


# In[17]:


edges['node1_policy'].isna().sum()


# In[18]:


edges.isna().sum().sum()


# In[19]:


edges['node2_policy'].isna().sum()


# In[20]:


edges.shape


# In[21]:


edges.describe()


# In[22]:


edges.columns


# In[23]:


nodes = pd.DataFrame(data['nodes'])


# In[24]:


nodes.isna().sum().sum()


# In[25]:


nodes.head()


# In[26]:


nodes.shape


# In[27]:


nodes.describe()


# In[28]:


nodes.columns


# In[29]:


nodes[nodes.columns].isnull().sum()


# In[30]:


edges[edges.columns].isnull().sum()


# In[31]:


edges['capacity']


# In[32]:


edges['capacity'].value_counts()


# In[33]:


netCapacity = 0


# In[34]:


for i in edges['capacity']:
    netCapacity += int(i)


# In[35]:


netCapacity


# In[36]:


# Total Number of Nodes = len(data['nodes']) = 20864
# Total Number of Channels( edges ) = len(data['edges']) = 87523
# Total Capacity in the Network = 354789965831 satoshis = 3547.89965831 btc
# 10^8 satoshis = 1 btc


# In[37]:


# Calculate the total capacity of all nodes with more than 50 channels and 1 BTC in capacity.


# In[38]:


# If capacity hear refers to the total capacity of the node( which it has access to ) = Incoming + Outgoing( condition > 1 btc)


# In[39]:


# node1_pub is the public id of the outgoing fee from the node
# while node2_pub is the public id of the outgoing fee from the node


# In[40]:


K = edges['node1_pub'].value_counts()


# In[41]:


K


# In[42]:


outgoingNode = pd.DataFrame(K)


# In[43]:


outgoingNode


# In[44]:


ingoingNode = pd.DataFrame(edges['node2_pub'].value_counts())


# In[45]:


outgoingNode = pd.DataFrame({'node':outgoingNode.index, 'node1_pub':outgoingNode.node1_pub})


# In[46]:


outgoingNode


# In[47]:


ingoingNode = pd.DataFrame({'node':ingoingNode.index, 'node2_pub':ingoingNode.node2_pub})


# In[48]:


CopyingoingNode = pd.DataFrame({'node':ingoingNode.index, 'node2_pub':ingoingNode.node2_pub})


# In[49]:


CopyingoingNode


# In[50]:


ingoingNode


# In[51]:


ingoingNode['node2_pub'].iloc[1]


# In[52]:


ingoingNode['node1_pub'] =0
ingoingNode['Total'] =0


# In[53]:


sum = 0
L = []


# In[54]:


for i in ingoingNode['node']:
    val = 0
    t = 0
    for j in outgoingNode['node']:
        if i == j:
            val = 1
            ingoingNode['node1_pub'].iloc[sum] = outgoingNode['node1_pub'].iloc[t]
            ingoingNode['Total'].iloc[sum] = int(ingoingNode['node1_pub'].iloc[sum]) + int(ingoingNode['node2_pub'].iloc[sum])
            if ingoingNode['Total'].iloc[sum] > 50:
                L.append(i)
            sum += 1
            break
        t += 1
    if val == 0:
        ingoingNode['node1_pub'].iloc[sum] = 0
        ingoingNode['Total'].iloc[sum] = int(ingoingNode['node1_pub'].iloc[sum]) + int(ingoingNode['node2_pub'].iloc[sum])
        if ingoingNode['Total'].iloc[sum] > 50:
            L.append(i)
        sum += 1


# In[55]:


ingoingNode


# In[56]:


L


# In[57]:


len(L)


# In[58]:


outgoingNode['node2_pub'] =0
outgoingNode['Total'] =0


# In[59]:


sum = 0
L = []


# In[60]:


for i in outgoingNode['node']:
    val = 0
    t = 0
    for j in CopyingoingNode['node']:
        if i == j:
            val = 1
            outgoingNode['node2_pub'].iloc[sum] = CopyingoingNode['node2_pub'].iloc[t]
            outgoingNode['Total'].iloc[sum] = int(outgoingNode['node1_pub'].iloc[sum]) + int(outgoingNode['node2_pub'].iloc[sum])
            if outgoingNode['Total'].iloc[sum] > 50:
                L.append(i)
            sum += 1
            break
        t += 1
    if val == 0:
        outgoingNode['node2_pub'].iloc[sum] = 0
        outgoingNode['Total'].iloc[sum] = int(outgoingNode['node1_pub'].iloc[sum]) + int(outgoingNode['node2_pub'].iloc[sum])
        if outgoingNode['Total'].iloc[sum] > 50:
            L.append(i)
        sum += 1


# In[61]:


outgoingNode


# In[62]:


len(L)


# In[63]:


NodesWithChannels = {}


# In[64]:


ingoingNode


# In[65]:


# Looping through the outgoingNode to select Nodes with Channels > 50


# In[66]:


for i in range(0,13515):
    if outgoingNode['Total'].iloc[i] > 50:
        NodesWithChannels[outgoingNode['node'].iloc[i]] = outgoingNode['Total'].iloc[i]


# In[67]:


NodesWithChannels


# In[68]:


len(NodesWithChannels)


# In[69]:


# Looping through the ingoingNode to select Nodes with Channels > 50


# In[70]:


for i in range(0,14202):
    if ingoingNode['Total'].iloc[i] > 50:
        NodesWithChannels[ingoingNode['node'].iloc[i]] = ingoingNode['Total'].iloc[i]


# In[71]:


NodesWithChannels


# In[72]:


len(NodesWithChannels)


# In[73]:


# Getting all these Nodes with 50+ channels ( keys of the NodeWithChannels dictionary) and storing it in a list


# In[74]:


L = list(NodesWithChannels.keys())


# In[75]:


len(L)


# In[76]:


edges.head()


# In[77]:


from collections import defaultdict


# In[78]:


FinalNodes = []
FinalCaps = []
Finaldict = {}
TotalCapacity = 0
NodeWithCap = defaultdict(int)


# In[79]:


for i in L:
    j = 0
    for k in edges['node1_pub']:
        if i == k:
            NodeWithCap[i] += (int(edges['capacity'].iloc[j])/10**8)
        j += 1 


# In[80]:


NodeWithCap


# In[81]:


for i in L:
    j = 0
    for k in edges['node2_pub']:
        if i == k:
            NodeWithCap[i] += (int(edges['capacity'].iloc[j])/10**8)
        j += 1 


# In[82]:


NodeWithCap


# In[83]:


len(NodeWithCap)


# In[84]:


for i,j in NodeWithCap.items():
    if j>1:
        FinalNodes.append(i)
        FinalCaps.append(j)
        Finaldict[i] = j
        TotalCapacity += j


# In[85]:


FinalNodes


# In[86]:


FinalCaps


# In[87]:


Finaldict


# In[88]:


len(FinalNodes)


# In[89]:


TotalCapacity


# In[156]:


# FinalNodes => List of Nodes which have more than 50 channels and total capacity more than 1 Btc
# FinalCaps => The capacity of all these FinalNodes which have 50+ channels and total capacity more than 1 Btc
# TotalCapacity => 5162.234176330001 Btc is the total capacity of all the nodes with 50+ channels and total capacity more than 1 Btc
# Total Number of such nodes = 426.
# (Note : Capacity of a particular node was calculated using addition of incoming and outgoing capacity of the nodes ( capacity(channels from node1_pub) + capacity(channels to node2_pub) ) through the channels/edges )
# ( I did this as per my limited understanding of Lightning Networks ( currently still reading the book and articles )), hence
# if any improvements to be made I am up for it.


# In[91]:


# Calculate the median outgoing fee for each node of the top 300 nodes ranked by total capacity.


# In[92]:


edges.head()


# In[93]:


edges['node1_policy'].iloc[20000]


# In[94]:


# Calculate the median incoming fee for each node of the top 300 nodes ranked by total capacity.


# In[95]:


# 1 ) Calculating Total Capacity of each node in the network


# In[96]:


NodesWithCapacity = {}


# In[97]:


for i in range(0,len(edges['node1_pub'])):
    if edges['node1_pub'].iloc[i] in NodesWithCapacity:
        NodesWithCapacity[edges['node1_pub'].iloc[i]] += int(edges['capacity'].iloc[i])/10**8
    else:
        NodesWithCapacity[edges['node1_pub'].iloc[i]] = int(edges['capacity'].iloc[i])/10**8
        


# In[98]:


NodesWithCapacity


# In[99]:


len(NodesWithCapacity)


# In[100]:


for i in range(0,len(edges['node2_pub'])):
    if edges['node2_pub'].iloc[i] in NodesWithCapacity:
        NodesWithCapacity[edges['node2_pub'].iloc[i]] += int(edges['capacity'].iloc[i])/10**8
    else:
        NodesWithCapacity[edges['node2_pub'].iloc[i]] = int(edges['capacity'].iloc[i])/10**8


# In[101]:


NodesWithCapacity


# In[102]:


len(NodesWithCapacity)


# In[103]:


import operator


# In[104]:


sortedNodesWithCapacity = dict( sorted(NodesWithCapacity.items(), key=operator.itemgetter(1),reverse=True))


# In[105]:


sortedNodesWithCapacity


# In[106]:


TopNodes = []
TopCaps = []
TopNodesWithCaps = {}


# In[107]:


# Getting all Node


# In[108]:


k = 0
for i,j in sortedNodesWithCapacity.items():
    if k<300:
        TopNodes.append(i)
        TopCaps.append(j)
        TopNodesWithCaps[i] = j
    else:
        break
    k += 1


# In[109]:


len(TopNodes)


# In[110]:


TopNodesWithCaps


# In[111]:


edges.head()


# In[112]:


# Outgoing fee from the channel to another node is referred to node1_pub


# In[113]:


# {'time_lock_delta': 40,
#  'min_htlc': '1000',
#  'fee_base_msat': '1000',
#  'fee_rate_milli_msat': '1',
#  'disabled': False,
#  'max_htlc_msat': '247500000',
#  'last_update': 1647492303}


# In[114]:


# As we are not aware total no of payements so that we can exact fee by = fee_base_msat + (Capacity) * fee_rate_milli_msat


# In[115]:


edges['node1_policy'].iloc[0] != None


# In[116]:


edges.dtypes


# In[117]:


edges['node1_policy'].iloc[10000]['fee_base_msat']


# In[118]:


OutgoingNodeWithTotFees = {}
OutgoingNodeWithTotChannels = {}
MedianOutgoingNodes = {}


# In[119]:


len(TopNodes)


# In[120]:


TopNodes[26]


# In[121]:


for i in TopNodes:
    totFee = 0
    totChannel = 0
    a = 0
    valueFee = []
    for j in edges['node1_pub']:
        if i == j:
            totChannel += 1
            if edges['node1_policy'].iloc[a] != None:
                fee_base_msat = edges['node1_policy'].iloc[a]['fee_base_msat']
                fee_rate_milli_msat = edges['node1_policy'].iloc[a]['fee_rate_milli_msat']
                capacity = edges['capacity'].iloc[a]
                fees = float(fee_base_msat) + float(capacity) * (float(fee_rate_milli_msat)/10**6)
                valueFee.append(fees)
                totFee += fees
            else:
                valueFee.append(0.0)
        a += 1
    if totChannel == 0:
        MedianOutgoingNodes[i] = 0
        OutgoingNodeWithTotFees[i] = 0
        OutgoingNodeWithTotChannels[i] = 0
        continue
    else:
        valueFee.sort(key=float)
        if totChannel % 2 == 0:
            median = (valueFee[(totChannel//2)-1] + valueFee[(totChannel//2)])/2
        else:
            median = valueFee[((totChannel+1)//2)-1]
        MedianOutgoingNodes[i] = median
        OutgoingNodeWithTotFees[i] = totFee
        OutgoingNodeWithTotChannels[i] = totChannel


# In[122]:


len(OutgoingNodeWithTotFees)


# In[123]:


OutgoingNodeWithTotChannels


# In[124]:


OutgoingNodeWithTotFees


# In[125]:


# This shows the median outgoing fee for each node of the top 300 nodes ranked by total capacity( in satoshis )


# In[126]:


len(MedianOutgoingNodes)


# In[127]:


MedianOutgoingNodes


# In[128]:


# Incoming fee from the channel to the node is referred to node2_pub


# In[129]:


IngoingNodeWithTotFees = {}
IngoingNodeWithTotChannels = {}
MedianIngoingNodes = {}


# In[130]:


for i in TopNodes:
    totFee = 0
    totChannel = 0
    a = 0
    valueFee = []
    for j in edges['node2_pub']:
        if i == j:
            totChannel += 1
            if edges['node2_policy'].iloc[a] != None:
                fee_base_msat = edges['node2_policy'].iloc[a]['fee_base_msat']
                fee_rate_milli_msat = edges['node2_policy'].iloc[a]['fee_rate_milli_msat']
                capacity = edges['capacity'].iloc[a]
                fees = float(fee_base_msat) + float(capacity) * (float(fee_rate_milli_msat)/10**6)
                valueFee.append(fees)
                totFee += fees
            else:
                valueFee.append(0.0)
        a += 1
    if totChannel == 0:
        MedianIngoingNodes[i] = 0
        IngoingNodeWithTotFees[i] = 0
        IngoingNodeWithTotChannels[i] = 0
        continue
    else:
        valueFee.sort(key=float)
        if totChannel % 2 == 0:
            median = (valueFee[(totChannel//2)-1] + valueFee[(totChannel//2)])/2
        else:
            median = valueFee[((totChannel+1)//2)-1]
        MedianIngoingNodes[i] = median
        IngoingNodeWithTotFees[i] = totFee
        IngoingNodeWithTotChannels[i] = totChannel


# In[131]:


len(IngoingNodeWithTotFees)


# In[132]:


IngoingNodeWithTotChannels


# In[133]:


IngoingNodeWithTotFees


# In[134]:


# This shows the median incoming fee for each node of the top 300 nodes ranked by total capacity


# In[135]:


MedianIngoingNodes


# In[136]:


len(MedianIngoingNodes)


# In[137]:


# (optional) Bonus points if you also calculate the average fee weighted by channel size/capacity for the two tasks above.


# In[138]:


# For this we can use the dictionaries which we defined above which has stored the details of the total fee and capacity of a paticular node


# In[147]:


AvgIncomingFee = {}


# In[148]:


for a,b in OutgoingNodeWithTotChannels.items():
    node = a
    totChannels = b
    totFees = OutgoingNodeWithTotFees[a]
    if b != 0:
        avg = totFees/totChannels
    else:
        avg = 0
    AvgIncomingFee[node] = avg


# In[149]:


len(AvgIncomingFee)


# In[150]:


AvgIncomingFee # ( in totFees( in satoshis ) / capacity )


# In[151]:


AvgOutgoingFee = {}


# In[152]:


for a,b in IngoingNodeWithTotChannels.items():
    node = a
    totChannels = b
    totFees =IngoingNodeWithTotFees[a]
    if b != 0:
        avg = totFees/totChannels
    else:
        avg = 0
    AvgOutgoingFee[node] = avg


# In[153]:


len(AvgOutgoingFee)


# In[154]:


AvgOutgoingFee # ( in totFees( in satoshis ) / capacity )


# In[155]:


# END OF THE NOTEBOOK WITH ALL THE ANSWERS. WILL SEND U A BRIEF SUMMARY SOON IN MARKODWN FORMAT. HOPEFULLY U WERNT BORED.


# In[ ]:




