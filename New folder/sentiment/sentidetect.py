# pip install vaderSentiment

import tkinter as tk
from numpy import positive
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

root = tk.Tk()
root.title("Sentiment Detector")
root.resizable(0, 0)
root.configure(bg='#00003c')
root.geometry("300x300")

entry = tk.Entry(root, width=20, font=('ariel',14))
entry.place(x=5, y=20)

btn = tk.Button(root,text='Analyze',bg='#201d2e', font=('ariel',10),command=detectSentiment)
btn.place(x=232,y=20)

frame = tk.Frame(root,bd=2, relief=tk.RIDGE, bg='#201d2e')
frame.place(x=10,y=70, height=220,width=280)

label = tk.Label(frame,text='Result', bg='#201d2e', fg='white',font=('ariel',12,'bold'))
label.place(x=10,y=5)

text =tk.Text(frame,bd=2, relief=tk.SUNKEN, font=('Calibri',12,'bold'))
text.place(x=10, y=30, width=255,height=150)

title_label = tk.Label(frame,text='SAMCODEHUB',font=('ariel',12,'bold'),fg='#ffffff',bg='#201d2e')
title_label.place(x=65,y=185)

root.mainloop()

def detectSentiment():
    # get whole input content from textbox
    sentence = entry.get() 
    text.delete(0,0,tk.END)
    # create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
    # polarity_scores method of the SentimentIntensityAnalyzer
    # object gives a sentiment dictionary
    # which contains pos, neg, neutral and compound scores
    sentiment_dict = sid_obj.polarity_scores(sentence)
    
    negative_string = str(sentiment_dict['neg']*100) + "% Negative"
    text.insert(tk.END, negative_string+'\n')
    
    neutral_string = str(sentiment_dict['neu']*100) + "% neutral"
    text.insert(tk.END, neutral_string+'\n')
    
    positive_string = str(sentiment_dict['pos']*100) + "% positive"
    text.insert(tk.END, positive_string+'\n')
    
    # choose the sentiment as negative positive or neutral
    if sentiment_dict['compound'] >= 0.05:
        string = "Positive"
    elif sentiment_dict['compound'] <= -0.05:
        string = "Negative"
    else:
        string = "Neutral"
    text.insert(tk.END, f"Overall Result : {string}")