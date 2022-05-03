# EDM22_submission_55
Source code for EDM22 submission (id: 55) for Double-blind Reviewing

<h2>Code Structure</h2>

Directories: 

(1) Features: this folder contains Python codes for feature extraction and post-processing described in Section 4.

(2) Prediction_Models: this folder contains Python codes for prediction models described in Section 5.

(3) For other data postprocessing details, please refer to my another personal repo: https://github.com/yingbo-ma/Daily-Research-Testing

<h2>Prerequisites</h2>
<p>Basics</p>
<pre>
Python3 
</pre>

<p>Audio-based Feature Extraction: Loudness, Pitch, Shimmer, Jitter, MFCCs</p> 
<pre>
audiofile v1.0.0
opensmile v2.2.0
</pre>

<p>Language-based Feature Extraction: Word Count, Speech Rate, Word2Vec, Pre-trained BERT</p> 
<pre>
nltk v3.5
gensim v3.8.0
bert-for-tf2 v0.14.9
tensowflow-gpu v2.4.1
</pre>

<p>Video-based Feature Extraction: Eye Gaze, Head Pose, Facial AUs, Body Pose</p> 
<pre>
Feature extraction process was performed through command line arguments.
</pre>

<p>Prediction Models</p> 
<pre>
tensowflow-gpu v2.4.1
NVIDIA GPU + CUDA CuDNN
</pre>
