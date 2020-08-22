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
            for phrase in response.key_phrases:
                key_phrases += phrase + ", "
            print(key_phrases)
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
