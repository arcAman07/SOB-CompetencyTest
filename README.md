# SOB-CompetencyTest

# Routing Node research and automation

# Description:

We’re developing a capital management system for routing nodes named Torq. An important part of building Torq is exploring the data collected by Torq. The goal is to help routing node operators improve the efficiency and return of their invested bitcoin. This can be done in various ways, for example by automating actions based on the data that is collected, or provide hints and insight to the user. In this project you will get the opportunity to dive into several exploratory projects on the cutting edge of lightning and routing nodes. <br>

# Expected Outcomes:

One or more exploratory research projects that produce new insight useful to routing nodes and users of Torq. <br>
If the findings suggest that some sort of automation can help users, then a proof of concept can be developed using Python, Typescript or Go. <br>
(optional) Implement a successful proof of concept into Torq. <br>
Write one or more short articles that explain the process and findings for each project. <br>

# Skills Required: 

1) Python <br>
2) Jupyter, Pandas or experience with similar tools in Python. <br>
3) Basic analytical skills and some experience cleaning and wrangling data into useful features. <br>

# Competency Test:
Produce a Jupyter Notebook that loads the channel graph exported by LND into a Pandas dataframe or a Graph tool.
You can download the graph here:
https://drive.google.com/file/d/1FwBVCRbB6LsmwyKpnSzUB0H_GFGkT2uw/view?usp=sharing

Then:

1) Count the number of nodes, channels and total capacity in the network. <br>
2) Calculate the total capacity of all nodes with more than 50 channels and 1 BTC in capacity. <br>
3) Calculate the median outgoing fee for each node of the top 300 nodes ranked by total capacity. <br>
4) Calculate the median incoming fee for each node of the top 300 nodes ranked by total capacity. <br>
5) (optional) Bonus points if you also calculate the average fee weighted by channel size/capacity for the two tasks above. <br>
6) Write a short summary of the results from the tasks above. Optionally dig a bit deeper into the data to add more context to your summary. <br>
