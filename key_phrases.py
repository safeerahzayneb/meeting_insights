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


def entity_recognition_example(client, documents):
    try:
        result = client.recognize_entities(documents=documents)[0]

        print("Named Entities:\n")
        for entity in result.entities:
            print("\tText: \t", entity.text, "\tCategory: \t", entity.category, "\tSubCategory: \t", entity.subcategory,
                  "\n\tConfidence Score: \t", round(entity.confidence_score, 2), "\n")

    except Exception as err:
        print("Encountered exception. {}".format(err))


def entity_linking_example(client, documents):
    try:
        documents = ["""Microsoft was founded by Bill Gates and Paul Allen on April 4, 1975, 
        to develop and sell BASIC interpreters for the Altair 8800. 
        During his career at Microsoft, Gates held the positions of chairman,
        chief executive officer, president and chief software architect, 
        while also being the largest individual shareholder until May 2014."""]
        result = client.recognize_linked_entities(documents=documents)[0]

        print("Linked Entities:\n")
        for entity in result.entities:
            print("\tName: ", entity.name, "\tId: ", entity.data_source_entity_id, "\tUrl: ", entity.url,
                  "\n\tData Source: ", entity.data_source)
            print("\tMatches:")
            for match in entity.matches:
                print("\t\tText:", match.text)
                print("\t\tConfidence Score: {0:.2f}".format(match.confidence_score))

    except Exception as err:
        print("Encountered exception. {}".format(err))



# list of text to be processed
# documents = ["My cat might need to see a veterinarian."]
# f = open("text.txt")
# documents = [f.read()]


text_dict = {1: ['distribution', 'function', 'function', 'function', 'action', 'models', 'can', 'be', 'traced.', 'This', 'freezing', 'is', 'common', 'in', 'the', 'theory', 'of', 'discrete', 'Choice', 'models', 'for', 'the', 'logistic', 'distribution', 'plays', 'the', 'same', 'role', 'and', 'logistic', 'regression', 'as', 'the', 'normal', 'distributions', 'as', 'in', 'David', 'regression.', 'PDF', 'of', 'this', 'distribution', 'in', 'the', 'theory', 'of', 'electron', 'properties', 'in', 'semiconductors', 'and', 'metals', 'this', 'derivative', 'sets', 'the', 'relative', 'weight', 'of', 'the', 'various', 'electron', 'energy', 'and', 'their', 'contributions', 'to', 'electron', 'transport.', 'high', 'temperature', 'I', 'just', 'think', 'that', 'we', 'should', 'arise', 'assassinate', 'distribution', 'of', 'an', 'independent', 'exponential', 'distribution', 'parameters', 'in', 'hydrology,', 'the', 'distribution', 'of', 'long', 'duration', 'River', 'discharge', 'and', 'rainfall', 'is', 'often', 'thought', 'to', 'be', 'almost', 'normal', 'according', 'to', 'the', 'central', 'limit', 'theorem.']}
text = ""
for speaker in text_dict:
    for word in text_dict[speaker]:
        text += word + " "

documents = [text]
key_phrase_extraction(client, documents)
entity_recognition_example(client, documents)
entity_linking_example(client, documents)
open("meeting_text.txt", "w").write(text)
