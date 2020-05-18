import socket
import time
import wave

import const


def stream_wav_to_server():
    with socket.socket() as client_socket:
        client_socket.connect((const.HOST, const.PORT))
        with wave.open(const.SAMPLE_WAV_FILE, 'r') as wave_file:
            print('Started streaming')
            while True:
                try:
                    print('.', end='', flush=True)
                    time.sleep(1)
                    data = wave_file.readframes(const.FRAME_RATE)
                    if not data:
                        print('\nFile streamed completely. Exiting')
                        break
                    client_socket.send(data)
                except KeyboardInterrupt:
                    print('\nExiting')
                    break
                except (BrokenPipeError, ConnectionResetError):
                    print('\nConnection lost. Exiting')
                    break


if __name__ == '__main__':
    stream_wav_to_server()
