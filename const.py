import os

FRAME_RATE = 44100
CHANNELS = 2
SAMPLE_WIDTH = 2

PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = f'{PROJECT_ROOT_DIR}/server_output'
SAMPLE_WAV_FILE = f'{PROJECT_ROOT_DIR}/file_example_WAV_5MG.wav'

HOST = '127.0.0.1'
PORT = 5000
