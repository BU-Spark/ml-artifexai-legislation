***Report of Missing Values***

* 'municipality' =  0.9434464404524284

* 'cosponsors' = 0.5173058139041067 

* ‘summary/text' = 0.05835138234169958 

* 'sponsor/url' = 0.025806542942483825 

* 'sponsor/name' =  0.013547373338429524

* 'sponsor' = 0.024390934443170396

* 'history' = 0.004388386347871633

***Strategy for Handling Missing Values***
* In order to handle missing values, we dropped all rows that did not have sponsors since our tripartite graph that we would later construct with edges between bills and legislatorsrequires each row to have a sponsor. Otherwise, there would be disconnected nodes that are bills with no sponsors. Next, we created a subset of the data that has a municipality assigned to it. This is because these bills with municipalities are called home rule bills, and we want to further investigate the relationships and dynamics at play with home rule bills specifically. For the history column, the missing histories were filled in with an empty list instead of a NoneType.
