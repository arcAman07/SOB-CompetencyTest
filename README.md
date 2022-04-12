# SOB-CompetencyTest

# Routing Node research and automation

# Description:

We’re developing a capital management system for routing nodes named Torq. An important part of building Torq is exploring the data collected by Torq. The goal is to help routing node operators improve the efficiency and return of their invested bitcoin. This can be done in various ways, for example by automating actions based on the data that is collected, or provide hints and insight to the user. In this project you will get the opportunity to dive into several exploratory projects on the cutting edge of lightning and routing nodes.

# Skills Required: 

Python
Jupyter, Pandas or experience with similar tools in Python.
Basic analytical skills and some experience cleaning and wrangling data into useful features.

# Competency Test:
Produce a Jupyter Notebook that loads the channel graph exported by LND into a Pandas dataframe or a Graph tool.
You can download the graph here:
https://drive.google.com/file/d/1FwBVCRbB6LsmwyKpnSzUB0H_GFGkT2uw/view?usp=sharing

Then:

Count the number of nodes, channels and total capacity in the network. 
Calculate the total capacity of all nodes with more than 50 channels and 1 BTC in capacity.
Calculate the median outgoing fee for each node of the top 300 nodes ranked by total capacity.
Calculate the median incoming fee for each node of the top 300 nodes ranked by total capacity.
(optional) Bonus points if you also calculate the average fee weighted by channel size/capacity for the two tasks above.
Write a short summary of the results from the tasks above. Optionally dig a bit deeper into the data to add more context to your summary.
