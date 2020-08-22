key = "66809a9c3def40138dcf988dd9b13db5"
endpoint = "https://textkeywords.cognitiveservices.azure.com/"

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, credential=ta_credential)
    return text_analytics_client


client = authenticate_client()


def key_phrase_extraction(client, documents):
    try:

        response = client.extract_key_phrases(documents=documents)[0]

        if not response.is_error:
            print("Entire meeting text:\n")
            print(documents[0] + "\n")
            print("Key Phrases:")
            key_phrases = ""
            key_phrases_list = []
            for phrase in response.key_phrases:
                key_phrases += phrase + ", "
                key_phrases_list.append(phrase)
            print(key_phrases)
            return key_phrases_list
        else:
            print(response.id, response.error)

    except Exception as err:
        print("Encountered exception. {}".format(err))


# list of text to be processed
# documents = ["My cat might need to see a veterinarian."]
# f = open("text.txt")
# documents = [f.read()]


text_dict = {
    1: ['so', 'I', 'guess', "we're", 'recording', 'right', 'now', 'okay', "haven't", 'seen', 'it', 'going', 'is', 'the',
        'weather', "it's", 'quite', 'hot', 'and', 'warm', 'your', 'voice', 'is', 'cutting', 'off', 'Hayward', '41',
        'seconds', 'do', 'you', 'want', 'to', 'go', 'for', 'a', 'minute', 'hello', 'okay', 'I', 'was', 'saying',
        "we're", 'at', 'a', 'minute', 'almost', '56', 'seconds', 'is', 'that', 'good']}

text = ""
for speaker in text_dict:
    for word in text_dict[speaker]:
        text += word + " "

documents = [text]
key_phrase_extraction(client, documents)


from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx


def read_article(file_name):
    file = open(file_name, "r")
    filedata = file.readlines()
    article = filedata[0].split(". ")
    sentences = []

    for sentence in article:
        print(sentence)
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop()

    return sentences


def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []

    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]

    all_words = list(set(sent1 + sent2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1

    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1

    return 1 - cosine_distance(vector1, vector2)


def build_similarity_matrix(sentences, stop_words):
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))

    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:  # ignore if both are same sentences
                continue
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix


def generate_summary(file_name, top_n=5):
    stop_words = stopwords.words('english')
    summarize_text = []

    # Step 1 - Read text anc split it
    sentences = read_article(file_name)

    # Step 2 - Generate Similary Martix across sentences
    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)

    # Step 3 - Rank sentences in similarity martix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)

    # Step 4 - Sort the rank and pick top sentences
    ranked_sentence = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    print("Indexes of top ranked_sentence order are ", ranked_sentence)

    for i in range(top_n):
        summarize_text.append(" ".join(ranked_sentence[i][1]))

    # Step 5 - Offcourse, output the summarize texr
    print("Summarize Text: \n", ". ".join(summarize_text))


# let's begin
generate_summary("meeting_text.txt", 2)
