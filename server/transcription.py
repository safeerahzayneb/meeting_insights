from google.cloud import speech_v1p1beta1
from google.cloud.speech_v1p1beta1 import enums
from google.cloud import storage
import moviepy.editor as mp 

TEMP_FILE_PATH = '../test/sample.mp4'

# Insert Local Video File Path  
def convert_mp4_to_wav(vid_file_path):
    clip = mp.VideoFileClip(vid_file_path) 
    clip.audio.write_audiofile(TEMP_FILE_PATH)
    return

def upload_to_gs(file_name, bucket_name):
    # bucket_name = 'video-transcripts'

    client = storage.Client()
    bucket = client.get_bucket(bucket_name)

    object_name_in_gcs_bucket = bucket.blob(file_name)
    object_name_in_gcs_bucket.upload_from_filename(TEMP_FILE_PATH)
    print("Uploaded file {}".format(file_name))
    return "gs://{}/{}".format(bucket_name, file_name)


def sample_recognize(storage_uri, content):
    """
    Performs synchronous speech recognition on an audio file

    Args:
      storage_uri URI for audio file in Cloud Storage, e.g. gs://[BUCKET]/[FILE]
    """

    client = speech_v1p1beta1.SpeechClient()

    # The language of the supplied audio
    language_code = "en-US"

    enable_speaker_diarization = True
    diarization_speaker_count = 1
    audio_channel_count = 2

    config = {
        "language_code": language_code,
        "enable_automatic_punctuation": True,
        "enable_speaker_diarization": enable_speaker_diarization,
        "audio_channel_count": audio_channel_count,
        "diarization_speaker_count": diarization_speaker_count,
    }
    audio = {"uri": storage_uri}

    operation = client.long_running_recognize(config, audio)
    response = operation.result()

    for result in response.results:
        # First alternative has words tagged with speakers
        alternative = result.alternatives[0]
        #print("Transcript: {}".format(alternative.transcript))
        speakers = {}
        # Print the speaker_tag of each word
        for word in alternative.words:
            if not speakers.get(word.speaker_tag):
                speakers[word.speaker_tag] = [word.word]
            else:
                speakers[word.speaker_tag].append(word.word)

        #print(speakers)
    
    
    return speakers
