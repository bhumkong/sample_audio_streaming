import wave

import const

if __name__ == '__main__':
    with wave.open(const.SAMPLE_WAV_FILE, 'r') as wav:
        print(wav.getparams())
