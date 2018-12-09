import automaticTagging

print("Library loaded")
# The format of the file argument and file path should specify the same format.
data = automaticTagging.process_speech_to_text("data/video.mp4","mp4")

print(data)
print()

# The data is unicoded string (str(<something>)) is sufficient if Python 3. The threshold for NLP model can be specified
# for it. The default is 0.5
audio_tags = automaticTagging.get_tags_for_audio(data,threshold=0.5)
print(audio_tags)

# The argument is the path to video file. The number of frames that can be skipped can be specified as n_frames. The
# default is 20. i.e. automaticTagging.get_tags_for_video('data/video.mp4',n_frames=25). If 1 nothing is skipped.
video_tags = automaticTagging.get_tags_for_video('data/video.mp4')
print(video_tags)

# The entire tags can be converted into json file. But the audio_tags and video_tags should be in 
# the format the getter functions get them.
automaticTagging.create_json_file('kay_tags.json',audio_tags,video_tags)