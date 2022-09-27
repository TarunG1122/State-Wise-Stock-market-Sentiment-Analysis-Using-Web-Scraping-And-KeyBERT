# State-Wise-Stock-Market-Sentiment-Analysis-Using-Web-Scraping-And-KeyBERT

**KeyBERT** :  KeyBERT is a minimal and easy-to-use keyword extraction technique that leverages BERT embedding’s to create keywords and key phrases that are most similar to a document.

**WordCloud** : A word cloud is a collection, or cluster, of words depicted in different sizes. The bigger and bolder the word appears, the more often it’s mentioned within a given text and the more important it is.

### Aim of the Project :

The main aim of the project is state-wise stock market sentiment analysis for social media keywords planning and advertisement. This project uses web scraping tools to collect text-based data from platforms like Facebook, Twitter, Pinterest, and Instagram. The data is then processed using a natural language processing algorithm (keyBERT) for specific keywords, as well as WordCloud for graphical representations of word frequency, which emphasize words that appear more frequently. The end output is a list of keywords that can be used for state-wise sentiment analysis of the stock market for social media marketing and advertisements.

### Procedure:
1. Data Extraction using web scraping:

    •	The data can be extracted by running [blogs.py](https://github.com/TarunG1122/State-Wise-Stock-market-Sentiment-Analysis-Using-Web-Scraping-And-KeyBERT/blob/main/web%20scraping%20codes/blogs.py) and [facebook.py](https://github.com/TarunG1122/State-Wise-Stock-market-Sentiment-Analysis-Using-Web-Scraping-And-KeyBERT/blob/main/web%20scraping%20codes/facebook.py) on PyCharm or spyder IDE
  
    •	Requirements: chrome driver (link: https://chromedriver.chromium.org), install and import libraries like selenium, requests , pytesseract ( OCR tool used for reading texts from images) , pillow.
   
2. Running web scraping code:

    •	In facebook.py add your login id, password and keywords. In blogs.py add keywords and run

    •	Eg for keywords: learn stock market Bangalore , learn stock market Delhi etc.

    •	The web scraping code returns a text based output as keywords.txt (eg : learn stock market Delhi.txt)

    •	Run the same codes for multiple keywords 

    •	extracted text files are stored in, [Karnataka text data](https://github.com/TarunG1122/State-Wise-Stock-market-Sentiment-Analysis-Using-Web-Scraping-And-KeyBERT/tree/main/karnataka%20web%20data%20extracted%20using%20web%20scraping) and [Gujarat text data](https://github.com/TarunG1122/State-Wise-Stock-market-Sentiment-Analysis-Using-Web-Scraping-And-KeyBERT/tree/main/gujarat%20web%20data%20extracted%20using%20web%20scraping)

3. Merging the text files:

    •	use merging tools to combine all the documents

    •	merging tool  : https://products.aspose.app/words/merger/txt

    •	merged text files are stored in [merged text files](https://github.com/TarunG1122/State-Wise-Stock-market-Sentiment-Analysis-Using-Web-Scraping-And-KeyBERT/tree/main/merged%20text%20files)

4. Importing the merged .txt file

5. Run the text file using keyBERT to get keywords and wordcloud to get visual representation of frequency of keyword.

6. Save the wordcloud model to get keywords png image, wordcloud images of both the states are saved in [wordcloud output images](https://github.com/TarunG1122/State-Wise-Stock-market-Sentiment-Analysis-Using-Web-Scraping-And-KeyBERT/tree/main/wordcloud%20output%20images).


### Web Scraping codes :

1. [blogs.py](https://github.com/TarunG1122/State-Wise-Stock-market-Sentiment-Analysis-Using-Web-Scraping-And-KeyBERT/blob/main/web%20scraping%20codes/blogs.py)

blogs.py is built using pillow,pytesseract, selenium web driver, and requests. It is an automated process that runs on chrome driver and is linked with social searcher, which links to Google search, Facebook, Instagram, Twitter, and Pinterest domains. websites are opened in the order and data is extracted from all the mentioned platforms. the query parameter keeps updating based on the keywords that are related to search keywords, the maximum scrolling or website opening is set to 10, and pytesseract is used to extract data from images. output is a text (.txt) file that consists of text-based data.

2. [facebook.py](https://github.com/TarunG1122/State-Wise-Stock-market-Sentiment-Analysis-Using-Web-Scraping-And-KeyBERT/blob/main/web%20scraping%20codes/facebook.py)

faebook.py covers all the libraries used in blogs.py. For web scraping, the user must provide a login id and keyword list. The keyword list may contain multiple keywords. We extract text and image-based data, including comments, user names, likes, shares, dates, and data from a user's post by using libraries. Text from images is extracted by Pytessaract with a scroll limit set to 100 because Facebook has infinite scrolling. output is a text (.txt) file that consists of text-based data.




### Working:

1.	run facebook.py, the code logs in to profile and collects data based on given search keywords, it collects data from posts and images 
2.	Facebook.py collect data from Facebook and blog.py collects data from various sources like blogs, Instagram, Pinterest and twitter etc. Both the web scraping tools run on chrome driver and it is controlled by automation text software selenium. 
3.	the output text file is combined using merging tool
4.	The merged txt file is processed using NLP algorithm KeyBERT.
5.	KeyBERT provides keywords for sentiment analysis.
6.	Wordcloud gives an image output consisting of multiple keywords based on word frequency.

### Expected Results:

The result is a list of keywords that can be used for state-wise sentiment analysis of the stock market. By analyzing the keywords output by keyBERT, a user is able to better plan their social media advertising by understanding what types of keywords they need to use on Facebook, Twitter, Pinterest, and Instagram, as well as the way people from different states view the stock market, and by using WordCloud, the keywords are visualized based on word frequency extracted from the input text file. The word cloud (image) is used to understand the overall sentiment of an individual state towards the stock market in a single image whereas KeyBERT helps in determining the specific keywords that need to be considered before selecting keywords and designing advertisement creatives.

### KeyBERT example:




![gujarat](https://user-images.githubusercontent.com/114280399/192149188-49cddf51-0182-490f-aef0-19b583723e82.png)

### WordCloud example:




![stmf](https://user-images.githubusercontent.com/114280399/192149242-57194866-0272-4b18-8ab9-ced84cb8a3cf.png)

### Framework required to run this jupyter notebook:

•	Python 3.6 and above

•	Matplotlib for visualization

•	keyBERT for keywords extraction

•	WordCloud for graphical representation of keywords with high frequency

•	Web scraping code blogs.py and facebook.py











