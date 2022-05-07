# Predicting-Peer-Satisfaction-EDM2022
<h2>Description</h2>
<p>This is the repository for the following paper at the EDM conference 2022:</p> 
<p><em>Investigating Multimodal Predictors of Peer Satisfaction for Collaborative Coding in Middle School</em></p>

<h3>Introduction</h3>
Collaborative learning is a complex process during which two or more learners exchange opinions, construct shared knowledge, and solve problems together. While engaging in this interactive process, learners' satisfaction toward their partners plays a crucial role in defining the success of the collaboration. If intelligent systems could predict peer satisfaction early during collaboration, they could intervene with adaptive support. However, while extensive studies have associated peer satisfaction with factors such as social presence, communication, and trustworthiness, there is no research on automatically predicting learners’ satisfaction toward their partners. To fill this gap, this paper investigates the automatic prediction of peer satisfaction by analyzing 44 middle school learners’ interactions during collaborative coding tasks. We extracted three types of features from dialogues: 1) linguistic features indicating semantics; 2) acoustic-prosodic features including energy and pitch; and 3) visual features including eye gaze, head pose, facial behaviors, and body pose. We then trained several regression models to predict the peer satisfaction scores that learners received from their partners. The results revealed that head position and body location were significant indicators of peer satisfaction: lower head and body distances between partners were associated with more positive peer satisfaction. This work is the first to investigate the multimodal prediction of peer satisfaction during collaborative problem solving, and represents a step toward the development of real-time intelligent systems that support collaborative learning.

<h3>Authors</h3>
Yingbo Ma, Mehmet Celepkolu, Kristy Elizabeth Boyer

<h3>Citation</h3>
<pre></pre>

<h2>Code Structure</h2>

Directories: 

(1) Features: this folder contains Python codes for feature extraction and post-processing described in Section 4.

(2) Prediction_Models: this folder contains Python codes for prediction models described in Section 5.

(3) For other data postprocessing details, please refer to my another personal repo: https://github.com/yingbo-ma/Daily-Research-Testing

(4) Images: this folder contains the images displaying each feature's variation over time. We only provided feature: *head_distance* in the paper since it is the only significant feature found in this study; here we also plots the variations for other non-significant features.

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
