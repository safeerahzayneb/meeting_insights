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


def key_phrase_extraction(client, meeting_content):
    try:

        response = client.extract_key_phrases(documents=meeting_content)[0]
        out = ""

        if not response.is_error:
            out += "Entire meeting text:\n"
            out += meeting_content[0] + "\n"
            out += "Key Phrases:"

            # print("Entire meeting text:\n")
            # print(meeting_content[0] + "\n")
            # print("Key Phrases:")
            key_phrases = ""
            for phrase in response.key_phrases:
                key_phrases += phrase + ", "
            # print(key_phrases)
            out += key_phrases
            return out
        else:
            print(response.id, response.error)

    except Exception as err:
        print("Encountered exception. {}".format(err))


def entity_recognition_example(client, meeting_content):
    try:
        result = client.recognize_entities(documents=meeting_content)[0]
        out = ""
        # print("Named Entities:\n")
        for entity in result.entities:
            out += "\tText: " + entity.text
            out += "\tCategory: " + entity.category
            if entity.subcategory is not None:
                out += "\tSubCategory: " + entity.subcategory
            out += "\n\tConfidence Score:" + str(round(entity.confidence_score, 2))
            # print("\tText: \t", entity.text, "\tCategory: \t", entity.category, "\tSubCategory: \t", entity.subcategory,
                  # "\n\tConfidence Score: \t", round(entity.confidence_score, 2), "\n")
        return out

    except Exception as err:
        print("Encountered exception. {}".format(err))


def entity_linking_example(client, meeting_content):
    try:
        result = client.recognize_linked_entities(documents=meeting_content)[0]
        out = ""
        print("Linked Entities:\n")
        for entity in result.entities:
            out += "\tName: " + entity.name + "\tId: " + entity.data_source_entity_id + "\tUrl: " + entity.url + \
                  "\n\tData Source: " + entity.data_source
            # print("\tName: ", entity.name, "\tId: ", entity.data_source_entity_id, "\tUrl: ", entity.url,
            #       "\n\tData Source: ", entity.data_source)
            # print("\tMatches:")
            for match in entity.matches:
                out += "\t\tText:" + match.text
                out += "\t\tConfidence Score: {0:.2f}".format(match.confidence_score)
                # print("\t\tText:", match.text)
                # print("\t\tConfidence Score: {0:.2f}".format(match.confidence_score))
        return out
    except Exception as err:
        print("Encountered exception. {}".format(err))


def sentiment_analysis_example(client, meeting_content):
    out = ""
    response = client.analyze_sentiment(documents = meeting_content)[0]
    out += "Meeting Sentiment: {}".format(response.sentiment)
    out += "Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
        response.confidence_scores.positive,
        response.confidence_scores.neutral,
        response.confidence_scores.negative,
    )
    # print("Meeting Sentiment: {}".format(response.sentiment))
    # print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
    #     response.confidence_scores.positive,
    #     response.confidence_scores.neutral,
    #     response.confidence_scores.negative,
    # ))
    return out
