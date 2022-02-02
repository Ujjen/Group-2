#
import librosa
import matplotlib.pyplot as plt
from dtw import dtw

y1, sr1 = librosa.load('/home/user/Desktop/1.wav')
y2, sr2 = librosa.load('/home/user/Desktop/2.wav')

plt.subplot(1, 2, 1)
mfcc1 = librosa.feature.mfcc(y1,sr1)
librosa.display.specshow(mfcc1)

plt.subplot(1, 2, 2)
mfcc2 = librosa.feature.mfcc(y2, sr2)
librosa.display.specshow(mfcc2)

dist, cost, path = dtw(mfcc1.T, mfcc2.T)
print("The normalized distance between the two : ",dist)

plt.imshow(cost.T, origin = 'lower', cmap=plt.get_cmap('gray'), interpolation = 'nearest')
plt.plot(path[0], path[1], 'w')

plt.show()
