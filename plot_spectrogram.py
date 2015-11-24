"""
A spectrogram, or sonogram, is a visual representation of the spectrum
of frequencies in a sound.  Horizontal axis represents time, Vertical axis
represents frequency, and color represents amplitude.


remove blank border arount pyplot:
http://stackoverflow.com/questions/11837979/removing-white-space-around-a-saved-image-in-matplotlib


"""
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import os
import wave
import matplotlib
matplotlib.use("Agg")
import pylab
import subprocess





class Spectrogram(QWidget):

    # send keypress event to mainwindow
    procStart = pyqtSignal(QEvent)

    def __init__(self, fileName1stChunk, parent = None):

        super(Spectrogram, self).__init__(parent)

        self.pixmap = QPixmap()
        self.pixmap.load( fileName1stChunk )
        self.w, self.h = self.pixmap.width(), self.pixmap.height()

        '''print( 'pixmap.width(), pixmap.height()', self.pixmap.width(), self.pixmap.height() )'''

        self.setGeometry(300, 300, 1000, self.h + 50)
        self.setMinimumHeight( self.h + 50)
        self.setMaximumHeight( self.h + 50)

        self.scene = QGraphicsScene(self)
        self.scene.setBackgroundBrush (QColor(0, 0, 0, 255))

        self.scene.setSceneRect(0, 0, 100, 100)

        self.line = QGraphicsLineItem(0, 0, 0, self.h, scene = self.scene)
        self.line.setPen(QPen(QColor(255, 0, 0, 255), 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        self.line.setZValue(100.0)
        self.scene.addItem(self.line)

        self.view = QGraphicsView(self.scene)
        #self.view.showMaximized()

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.view)

        self.setWindowTitle("Spectrogram")

        self.installEventFilter(self)

    def eventFilter(self, receiver, event):
        if(event.type() == QEvent.KeyPress):
            print(event.text())
            # send keypress event to mainwindow
            self.procStart.emit(event)
            return True
        else:
            return False

def graph_spectrogram(mediaFile, tmp_dir, chunk_size):

    fileName1stChunk = ''

    mediaBaseName = os.path.basename( mediaFile )

    wav_file = extract_wav(mediaFile, tmp_dir)
    if not wav_file:
        return None

    sound_info, frame_rate = get_wav_info(wav_file)

    wav_length = round(len(sound_info) / frame_rate, 0)
    #print('wav tot length', wav_length)
    if wav_length < chunk_size:
        chunk_size = round(wav_length)

    i = 0
    while True:

        chunkFileName = "{}.{}-{}.spectrogram.png".format(wav_file, i, i + chunk_size)
        if not os.path.isfile(chunkFileName):

            sound_info_slice = sound_info[i * frame_rate: (i + chunk_size) * frame_rate]

            #print( [i * frame_rate, (i + chunk_size) * frame_rate] )

            pylab.figure(num=None, dpi=100, figsize=(int( len(sound_info_slice)/frame_rate  ), 1))
            pylab.gca().set_axis_off()
            pylab.margins(0, 0)
            pylab.gca().xaxis.set_major_locator(pylab.NullLocator())
            pylab.gca().yaxis.set_major_locator(pylab.NullLocator())
            pylab.specgram(sound_info_slice, Fs=frame_rate, cmap=matplotlib.pyplot.get_cmap('Greys'))
            pylab.savefig(chunkFileName, bbox_inches='tight', pad_inches=0)
            pylab.clf()
            pylab.close()

        '''
        else:
            print(chunkFileName + ' already exists')
        '''
        if not fileName1stChunk:
            fileName1stChunk = chunkFileName

        i += chunk_size
        if i >= wav_length:
            break

    return fileName1stChunk


def extract_wav(mediaFile, tmp_dir):
    '''extract wav from media file'''

    wavTmpPath = "{tmp_dir}{sep}{mediaBaseName}.wav".format(tmp_dir=tmp_dir,
                                                              sep=os.sep,
                                                              mediaBaseName=os.path.basename(mediaFile))

    if os.path.isfile(wavTmpPath):
        return wavTmpPath
    else:
        p = subprocess.Popen( 'ffmpeg -i "{mediaFile}" -y -ac 1 -vn "{wavTmpPath}"'.format(mediaFile=mediaFile,
                                                                                                  wavTmpPath=wavTmpPath),
                                                                                                   stdout=subprocess.PIPE,
                                                                                                    stderr=subprocess.PIPE,
                                                                                                     shell=True )
        out, error = p.communicate()
        out, error = out.decode("utf-8"), error.decode("utf-8")

        if not out:
            return wavTmpPath
        else:
            return None


def get_wav_info(wav_file):

    wav = wave.open(wav_file, "r")
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, "Int16")
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate


if __name__ == "__main__":
    media_file = sys.argv[1]
    graph_spectrogram(media_file, 20)
