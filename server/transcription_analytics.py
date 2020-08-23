from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from textanalytics_azure import *
from transcription import *

key = "66809a9c3def40138dcf988dd9b13db5"
endpoint = "https://textkeywords.cognitiveservices.azure.com/"


def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, credential=ta_credential)
    return text_analytics_client


#def meeting_analytics();

#client authentication
client = authenticate_client()

#speech to text transcription
content = {}
# Test Data
vid_file_path='./sample2.mp4'
file_name='test.wav'
bucket_name='meeting_insights'

convert_mp4_to_wav(vid_file_path)
gs_uri = upload_to_gs(file_name, bucket_name)
content = sample_recognize(gs_uri, content)

#transcription analytics (azure API)
text_dict = content
text = ""
output = ""
for speaker in text_dict:
    for word in text_dict[speaker]:
        text += word + " "

meeting_content = [text]
key_phrases_out = key_phrase_extraction(client, meeting_content)
entity_recog_out = entity_recognition(client, meeting_content)
entity_linking_out = entity_linking(client, meeting_content)
sentiment_analysis_out = sentiment_analysis(client, meeting_content)

print(key_phrases_out + "\n" + entity_recog_out + "\n" + entity_linking_out + "\n" + sentiment_analysis_out + "\n")
open("meeting_text.txt", "w").write(text)

