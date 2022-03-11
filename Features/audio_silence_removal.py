# Python codes for removing silence periods contained in audios, described in Section 4.1

from pydub import AudioSegment, silence

myaudio = AudioSegment.from_wav("absolute_path_of_audio_file") # read an audio file
speech = silence.detect_nonsilent(myaudio, min_silence_len=200, silence_thresh=-6) # select the silence threshold. In this paper we tried -6, -16, and -30.
speech = [((start / 1000), (stop / 1000)) for start, stop in speech]  # extract speech time index, convert to sec

if (len(speech) == 0): # if no speech was detected
    myaudio.export(audio_out_path + "\{}.wav".format(audio_index), format="wav")
    print("exporting edited " + audio_file_name + " done!")
else: # if speech was detected
    first_speech_starting_point = list(speech[0])[0]
    last_speech_ending_point = list(speech[-1])[1]

    speech_remove_eou = myaudio[first_speech_starting_point * 1000 : last_speech_ending_point * 1000] # extract speech segments
    speech_remove_eou.export(audio_out_path + "\{}.wav".format(audio_index), format="wav") # export speech segments

    print("exporting edited " + audio_file_name + " done!")
