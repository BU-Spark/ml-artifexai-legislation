***Project Information*** 

* What is the project name?  
  * ArtifexAI: Tech-Focused Legislation Tracker 
* What is the link to your project’s GitHub repository?  
  * https://github.com/BU-Spark/ml-artifexai-legislation/
* What is the link to your project’s Google Drive folder? \*\**This should be a Spark\! Owned Google Drive folder \- please contact your PM if you do not have access\*\**  
  * https://drive.google.com/drive/folders/1tpqB3-vQwLCt7G42iU9PmEuvdhf6AYaq
* In your own words, what is this project about? What is the goal of this project?   
* Who is the client for the project?  
  * **Russ Wilcox**, CEO of **ArtifexAI**.  
* Who are the client contacts for the project?  
 * Email: [russ@artifexai.io](mailto:russ@artifexai.io)

* What class was this project part of?
  * SPARK – CDS – DS549

***Dataset Information***

* What data sets did you use in your project? Please provide a link to the data sets, this could be a link to a folder in your GitHub Repo, Spark\! owned Google Drive Folder for this project, or a path on the SCC, etc.  
* Please provide a link to any data dictionaries for the datasets in this project. If one does not exist, please create a data dictionary for the datasets used in this project. **(Example of data dictionary)**   
* What keywords or tags would you attach to the data set?  
  * Domain(s) of Application: Computer Vision, Object Detection, OCR, Image Classification, Image Segmentation, Facial Recognition, NLP, Topic Modeling, Sentiment Analysis, Named Entity Recognition, Text Classification, Summarization, Anomaly Detection, Other   
  * Sustainability, Health, Civic Tech, Voting, Housing, Policing, Budget, Education, Transportation, etc. 

*The following questions pertain to the datasets you used in your project.*   
*Motivation* 

* For what purpose was the dataset created? Was there a specific task in mind? Was there a specific gap that needed to be filled? Please provide a description. 

*Composition*

* What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)? Are there multiple types of instances (e.g., movies, users, and ratings; people and interactions between them; nodes and edges)? What is the format of the instances (e.g., image data, text data, tabular data, audio data, video data, time series, graph data, geospatial data, multimodal (please specify), etc.)? Please provide a description.   
  * The instances represent bills, the data format is text data. There is no interaction between the different bills and there is only one type of instance. 
* How many instances are there in total (of each type, if appropriate)?  
  * 70641 instances
* Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set? If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set? If so, please describe how this representativeness was validated/verified. If it is not representative of the larger set, please describe why not (e.g., to cover a more diverse range of instances, because instances were withheld or unavailable).  
  * It contains all possible instances starting from the year 2017 to the present.
* What data does each instance consist of? “Raw” data (e.g., unprocessed text or images) or features? In either case, please provide a description.   
  * Each instance contains bill data, sponsors, summary, metadata, documents, cosponsors, history, and scrape metadata.
* Is there any information missing from individual instances? If so, please provide a description, explaining why this information is missing (e.g., because it was unavailable). This does not include intentionally removed information, but might include redacted text.
  * Some instances are missing sponsors and status information. This information is missing because it was unavailable, either because the status of the bill was not reported or there were no sponsors.   
* Are there recommended data splits (e.g., training, development/validation, testing)? If so, please provide a description of these splits, explaining the rationale behind them  
  * There are no recommended data splits.
* Are there any errors, sources of noise, or redundancies in the dataset? If so, please provide a description.   
  * Some of the bill text summaries have formatting characters within the text which could be potential sources of noise. Another thing that might pose an issue in the future is that some of the sponsors for the bills are not actual people, rather they are joint committees in the senate or house, which could add difficulty to exploring the relationships between legislators and bills.
* Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)? If it links to or relies on external resources,
	 - Bill URLs, e.g., `https://malegislature.gov/Bills/183/SD2780`
		  - Text view URLs, print preview URLs, download URLs.
	- **Document storage on AWS S3:** 
		- Example: `s3://artifex-legislation-documents/state/MA/.../bill_text.pdf`.

	* Are there guarantees that they will exist, and remain constant, over time;
		- There are **no guarantees** that the external URLs will remain constant or accessible over time. 
		- Broken or invalid URLs (such as `cc` or `Invalid`) demonstrate potential instability.

	* Are there official archival versions of the complete dataset (i.e., including the external resources as they existed at the time the dataset was created)?
		* **No**, URLs may change or become inaccessible

	* Are there any restrictions (e.g., licenses, fees) associated with any of the external resources that might apply to a dataset consumer? Please provide descriptions of all external resources and any restrictions associated with them, as well as links or other access points as appropriate.
		- No specific restrictions or licenses are mentioned for accessing the URLs. However, if AWS S3 documents are privately stored, access may be restricted.


* Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals’ non-public communications)? If so, please provide a description.
	- **No.** The dataset is composed of publicly available legislative bill data and related metadata. It does not contain privileged, personal, or non-public communication data.

* Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety? If so, please describe why.
	- **No.** The dataset primarily consists of legislative documents, summaries, actions, and metadata. It is unlikely to contain offensive or harmful content unless legislative bills themselves contain sensitive topics, which is not explicitly mentioned.



* Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset? If so, please describe how.
	- **Yes.** Legislators (Sponsors and Cosponsors) are directly identifiable by their names. Their names may appear under the `sponsor` and `cosponsors` keys, though in your example data, the `sponsor` name is empty, and the `cosponsors` list is empty.
  
* Dataset Snapshot, if there are multiple datasets please include multiple tables for each dataset. 


| Size of dataset |  330,2 MB|
| :---- | :---- |
| Number of instances |  70,641 JSON files |
| Number of fields  | 18 fields per JSON file |



  
*Collection Process*

* What mechanisms or procedures were used to collect the data (e.g., API, artificially generated, crowdsourced \- paid, crowdsourced \- volunteer, scraped or crawled, survey, forms, or polls, taken from other existing datasets, provided by the client, etc)? How were these mechanisms or procedures validated?  
* If the dataset is a sample from a larger set, what was the sampling strategy (e.g., deterministic, probabilistic with specific sampling probabilities)?  
* Over what timeframe was the data collected? Does this timeframe match the creation timeframe of the data associated with the instances (e.g., recent crawl of old news articles)? If not, please describe the timeframe in which the data associated with the instances was created. 

*Preprocessing/cleaning/labeling* 

* Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)? If so, please provide a description. If not, you may skip the remaining questions in this section.   
* Were any transformations applied to the data (e.g., cleaning mismatched values, cleaning missing values, converting data types, data aggregation, dimensionality reduction, joining input sources, redaction or anonymization, etc.)? If so, please provide a description.   
* Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)? If so, please provide a link or other access point to the “raw” data, this could be a link to a folder in your GitHub Repo, Spark\! owned Google Drive Folder for this project, or a path on the SCC, etc.  
* Is the code that was used to preprocess/clean the data available? If so, please provide a link to it (e.g., EDA notebook/EDA script in the GitHub repository). 

*Uses* 

* What tasks has the dataset been used for so far? Please provide a description.   
* What (other) tasks could the dataset be used for?  
* Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?   
* Are there tasks for which the dataset should not be used? If so, please provide a description.

*Distribution*

* Based on discussions with the client, what access type should this dataset be given (eg., Internal (Restricted), External Open Access, Other)?

*Maintenance* 

* If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so? If so, please provide a description. 

*Other*

* Is there any other additional information that you would like to provide that has not already been covered in other sections?

