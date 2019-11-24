import re
import numpy as np
import pysrt
from textblob import TextBlob
import matplotlib.pyplot as plt


def load_srt(path):
    """Method that loads the srt file"""
    # Read subtitles file
    return pysrt.open(path)


def fetch_data(subs):
    """Method that fetches text and time data from the subtitles"""
    # Fetch text values from srt file
    text = [subs[i].text for i in range(len(subs))]
    # Fetch time value from srt file
    start_time = [(subs[i].start.hours, subs[i].start.minutes, subs[i].start.seconds) for i in range(len(subs))]
    # Clean the data
    return clean_data(text), start_time


def clean_data(text):
    """Method that cleans the fetched text data"""
    # Remove <i> and </i> tags
    text = [re.sub(r'</?i>', '', line) for line in text]
    # Remove '\n' characters
    text = [re.sub('\n', ' ', line) for line in text]
    # Remove punctuations
    text = [re.sub(r'[.,;?!\'\"-]', '', line) for line in text]
    # Return the cleaned data
    return text


def time_split(total_time, time_li, n=100):
    """Method that divides the entire movie time into n chunks"""
    # Initialization of list
    li = list()
    # Iterating over each chunk index
    for j in range(n):
        # Finding approximate time for each chunk
        approx_time = float(j+1)/n * total_time
        # Initializing distance between actual and approximate value of time, and value of the chunk
        dis = total_time
        value = total_time
        # Finding value of each chunk
        for i in time_li:
            # Comparing approximate value with each actual value to find the exact value for the chunk
            if np.abs(approx_time - i) < dis:
                dis = np.abs(approx_time - i)
                value = i
        li.append(value)
    # Returning the list of time chunks
    return li


def find_sentiment_for_chunks(text, start_time):
    """Method that fetches sentiment values for chunks of the data"""
    # Find sentiment value for each text item using TextBlob
    sentiment_polarity = [TextBlob(text[i]).sentiment.polarity for i in range(len(subs))]
    # Create time array in minutes using the time details from the srt file
    time = [start_time[i][0]*60 + start_time[i][1] + start_time[i][2]/60 for i in range(len(subs))]
    # Fetch n chunks from time
    time_split_li = time_split(time[-1], time)
    # Fetch index of each chunk
    index = [0] + [time.index(item) for item in time_split_li]
    # Return time split list and sentiment polarity list
    return time_split_li, sentiment_polarity, index


def plot_data(time_split_li, sentiment_polarity, index):
    """Method that plots the data"""
    # Average sentiment polarity for each chunk to be plotted on x-axis
    y = [np.mean(sentiment_polarity[i:i+1]) for i in index[:-1]]
    # Time values to plot x-axis
    x = time_split_li
    # Creating the figure
    plt.figure()
    # Plotting the values
    plt.plot(x, y, color='b', linewidth=0.5)
    # Labeling x and y axes
    plt.xlabel('TIME in minutes')
    plt.ylabel('SENTIMENT POLARITY')
    # Plotting title of the plot
    plt.title('THE JOKER (2019)')
    plt.suptitle('SENTIMENT ANALYSIS BASED ON SUBTITLES')
    # Save image file as PNG
    plt.savefig(r'.\Output\OutputImage.png')


if __name__ == '__main__':
    # Location of SRT file
    file = r'.\Subtitles\Joker_English-subtitlesdorm.com-hdrip.srt'
    # Load subtitles
    subs = load_srt(file)
    # Fetch relevant data from the subtitles
    data, time = fetch_data(subs)
    # Find sentiment values and other relevant parameters to be used for plotting
    time_data, sentiment_data, index = find_sentiment_for_chunks(data, time)
    # Plot the data
    plot_data(time_data, sentiment_data, index)
