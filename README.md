# Sentiment Analysis of Subtitles
A mini-project in NLP to perform sentiment analysis on subtitles of movies using TextBlob. Currently under development.

### Requirements
- Python version: 3.7.4
- Python modules: numpy, re, matplotlib, [pysrt](https://github.com/byroot/pysrt), [textblob](https://textblob.readthedocs.io/en/dev/)
- Subtitle files to be placed in the ```Subtitles/``` folder

### Process followed
- SRT file is loaded using the pysrt module
- Text and time data collected from the subtitles
- Text data is cleaned and time data converted into desirable format
- TextBlob is used to find [sentiment polarity](https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis) for each text item
- Time divided into n chunks (default value of n set to 100) and average sentiment found for each of these n time periods
- Graph plotted with x axis being the time and y axis being the sentiment polarity using matplotlib
- Sentiment polarity values classified as follows: 0 - Neutral, >1 - Positive, <1 - Negative

### Work to be done
- Using own method to load subtitles and data to remove dependency on pysrt
- Trying to fetch more data using the sentiment values
- Cleaning of data to get more accurate sentiment values
- Using other sentiment analyzers to find the sentiment values
- Developing own sentiment analyzer by training already classified data
- Improving visualization of the output data

### ** Still a work under progress **

Also check out [Mubaris](https://mubaris.com/)
