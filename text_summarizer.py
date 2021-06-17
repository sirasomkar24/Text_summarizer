import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest 
stopwords = list(STOP_WORDS)
nlp = spacy.load('en_core_web_sm')
punctuation = punctuation + "\n"
print(punctuation)
def get_summary(file_name):
    myfile = open(file_name, "r")
    text = myfile.read()
    print(text)
    doc = nlp(text)
    print(doc)
    tokens = [token.text for token in doc]
    print(tokens)
    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text]  += 1
    print(word_frequencies)                
    max_frequencies = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/ max_frequencies
        
    print(word_frequencies)   # normalized word frequencies

    sentence_tokens = [sent for sent in doc.sents]
    print(sentence_tokens)

    sentencse_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentencse_scores.keys():
                    sentencse_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentencse_scores[sent] += word_frequencies[word.text.lower()]
    print(sentencse_scores)               

    # get 20% of sentence with maximum score         

    select_length = int(len(sentence_tokens) * 0.2)
    select_length
    summary = nlargest(select_length, sentencse_scores, key= sentencse_scores.get)
    summary
    final_summary = [word.text for word in summary]
    summary = " ".join(final_summary)
    print(summary)
    len(text)
    return print(summary)

get_summary("C:/Users/Sony/Desktop/Test/dataset/stories_text_summarization_dataset_train/0006021f772fad0aa78a977ce4a31b3faa6e6fe5.story")

