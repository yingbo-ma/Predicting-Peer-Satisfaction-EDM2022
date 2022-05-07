# In this paper, utterance-level multimidal feature vector X_t is a subset of an early-fused vector [a_t, v_t, l_t], each subcomponent donotes a unimodal feature from audio, video, and language modality.
# unimodal features were first z-normalized and then concatenated into a single multimodal feature
# normalization function: scipy.stat.stats.zscore()