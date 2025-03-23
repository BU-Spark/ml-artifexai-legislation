## **Tools And Evaluation Research**

### **Graph Analysis**

* networkX  
* neo4j (legislators, bills \= nodes; sponsorships \= edges)  
* igraph (clustering algorithms)  
* graph-tool (large graphs, advanced)  
* gephi (good for visualization)

### **ML frameworks**

* Scikit-learn  
* XG Boost  
  * Use for gradient boosting to optimize models  
* PyG (graph neural networks → predict bill outcomes based on sponsorship network)  
* Graph Neural Networks  
  * Moderate ease of integration into project(most time consuming part would be creating the graph and fine-tuning the model’s parameters)  
  * Graph link prediction to forecast potential sponsors  
  * GNN classification for bill pass/fail  
  * graph-based binary classifier for likelihood of bill stalling  
* Pytorch (if we use GNN models)

### **NLP Libraries & LLMs**

* Hugging Face Transformers: for **bill similarity & stance prediction**  
  * Easy to integrate with Python projects  
  * Access to hundreds of pre-trained models for legal and general text  
  * Supports both embedding generation and zero-shot/fine-tuned classification  
* [legal- BERT](https://huggingface.co/nlpaueb/legal-bert-base-uncased) :  Pre-trained Transformer model specialized in legal language.   
  * Use case: understanding bill language, similarity clustering  
  * Easy to use via Hugging Face  
  * Can use for embeddings(reduce text to dense vectors that capture the semantics of the text) to then perform clustering with either K-means or GMMs  
  * Evaluation: Clustering accuracy or classification metrics (precision, recall, F1)  
* LLAMA 3: LLM. Alternative to Legal-BERT  
  * Use case: Advanced bill summarization, Prompt-based topic  
  * Requires **prompt engineering** or **fine-tuning** for best performance  
  * Higher resource requirement (vs. Legal-BERT)

### **External Datasets**

* [mass legislature API](https://openstates.org/): Retrieve up-to-date information on bills, including their statuses, sponsors, and associated actions  
  * [Documentation](https://malegislature.gov/api/swagger/index.html?url=/api/swagger/v1/swagger.json)  
  * [Example Implementation](https://mybinder.org/v2/gh/bhrutledge/ma-legislature-api/HEAD?urlpath=lab)   
* [Ballotpedia](https://ballotpedia.org/Main_Page): Comprehensive source for legislator profiles, election data, policy positions, and ballot measures. Useful for enriching legislator data and tracking political trends.  
  * Scrape legislator pages to add background, voting history, or policy stances.   
  * Use these features in predictive models or for network enrichment.  
* [follow the money](https://www.followthemoney.org/): Tracks campaign finance data, including donations from individuals, corporations, and PACs to state-level candidates. Helps uncover funding influence on legislation.  
* [open secrets (pac and corporate donations)](https://www.opensecrets.org/): Provides detailed data on federal campaign contributions, lobbying, and PAC activity. Useful for understanding broader influence networks tied to state legislators.  
* [list of current mass legislators](https://malegislature.gov/Legislators)  
  * Not formatted data, just a website with list of current legislators and their information  
  * Would need to either manually or automate input information from website into table or datastructure  
* [Massachusetts Office of Campaign and Political Finance (OCPF):](https://www.ocpf.us/) Tracks campaign contributions and expenditures for candidates and committees in Massachusetts. Offers granular data on local funding sources.  
  *  link financial records to legislators to analyze whether certain donations align with patterns in bill sponsorship or voting behavior.  
* social media: public perception?  
* economic datasets

### **Data Visualization Tools**

* matplotlib / seaborn  
  * Best for basic statistical plots and quick visualizations  
  * Simple and easy to use  
  * Easily integrates with **NetworkX** to visualize graph structures  
  * Not ideal for interactive or large-scale data visualizations  
* NetworkX \- for graphs  
  * Best for building and analyzing graph structures  
  * Good for small to medium-sized graphs  
  * Limited built-in visualization capabilities (depends on matplotlib)  
  * High memory usage and performance issues with large graphs  
* Graphviz \- for graph visualization  
  * Best for structured, hierarchical graph visualizations  
  * Suitable for flowcharts and dependency graphs  
  * Harder to implement and customize  
  * Visual layouts may be less appealing  
  * Limitations in handling large graphs with many nodes or edges  
*  Plotly / Dash:   
  * Best for interactive, web-based dashboards  
  * Enables features like zoom, hover, filtering, and tooltips  
  * Suitable for final presentations or client-facing tools  
  * Slightly more complex setup compared to matplotlib

### **Model Evaluation Metrics**

* Binary classification (bill pass/fail): Accuracy, F1, ROC-AUC  
* Topic clustering: Topic coherence, Purity, Manual inspection

### **Possible approach**

* Build a graph based off of bill data and who sponsored what bill  
  * Use LEGAL-BERT to create embeddings from bill text data to perform classification on the bills  
  * Could use combination of graph neural networks and binary classifiers and maybe a custom model that assigns probabilities to each cosponsor based off the bill and who is main sponsor and you maximize  
  * Link prediction using graph neural network to predict cosponsors  
  * Use PyTorch Geometric or Deep Graph Library