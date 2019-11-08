from auairtools.auair import AUAIR

# Paths to annotation file and source data.
annotFile = '/home/ilker/Desktop/baum/workspace/DATASET/annotations.json'
dataDir = '/home/ilker/Desktop/baum/workspace/DATASET/images'

# Create a AUAIR object.
auairdataset = AUAIR(annotation_file=annotFile, data_folder = dataDir)

##############################################################
############# Get frame sequences for video processing #######
##############################################################
seq_len = 5 # Number of frames in a sequence.
window_gap = 200 # Maximum time difference (in millisecond) between two consecutive sequences.
overlap = 4 # Number of frames allowed to overlap.

print("Get frame sequences for given properties: ")
print(" -> Each sequence consists of %d frames." % seq_len)
print(" -> Maximum time difference between two consecutive sequences is %d milliseconds." % window_gap)
print(" -> The number of frames allowed to overlap is %d." % overlap)

frame_seq = auairdataset.get_frame_seqeunces(seq_len=5, window_gap=200, overlap=4)
print("Num of sequences: %d" % len(frame_seq))
print("Done")
##############################################################

