# Automatic Tags Generation

The aim of the project was to generate captions/tags for a given video which could be further used for recommendation or categorization. Generating tags for a video has a lot of applications.

Darknet, an open source neural network framework written in C and CUDA is used for this task. The algorithm is simple and works in the following way.

- Initially the audio of the video is converted into text.
- Then using darknet we find the key objects present in the video by dividing it into sequence of image frames.
- Then Topic Modelling using LDA is done on the text obtained from the audio.
- Then the best tags from both audio and video are chosen and presented.


 *Note : Many APIs are used to achieve our result. You can find all the packages installed by referring to the import commands in the file `automaticTagging.py`*

All the funcitons are written in a single script - `automaticTagging.py`. This can be imported and used.
 ### Steps to use :
 Initially install all the required packages required by referring to `automaticTagging.py`.

 Open Makefile.
 <br>
 Then Accordingly set flags to 1, as per system specifications

 ```
GPU=0          
CUDNN=0    
OPENCV=0
OPENMP=0
DEBUG=0
 ```

Run `make`.
<br>
Now darknet can be used.
*For more information refer `README_TO_CONFIGURE.md`*

The functions can be used as follows :
First import the package written
``` python
import automaticTagging
```

The video used here is for demonstration purpose only.
``` python
# The format of the file argument and
# file path should specify the same format.
data =
automaticTagging.process_speech_to_text("data/video.mp4","mp4")
```
`data` contains the text obtained from the speech.

``` python
# The data is unicoded string
# (str(<something>)) is sufficient if Python 3.
# The threshold for NLP model can be specified
# for it. The default is 0.5
audio_tags =
automaticTagging.get_tags_for_audio(data,threshold=0.5)
```

``` Python
# The argument is the path to video file.
# The number of frames that can be skipped can be specified as n_frames.
# The default is 25. i.e. automaticTagging.get_tags_for_video('data/video.mp4',n_frames=25).
# If it is 1 nothing is skipped.
video_tags =
automaticTagging.get_tags_for_video('data/video.mp4')
```


*The code is tested only on CPU due to lack of resources. And on CPU all the functions take a lot of time to process but the tags obtained are reasonable.*
