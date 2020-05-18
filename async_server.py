import asyncio
import wave
from datetime import datetime

import const

shutdown = False


async def handle_audio_stream(reader, writer):
    address = writer.get_extra_info('peername')
    print(f'Receiving stream from {address}')
    time = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')

    with wave.open(f'{const.OUTPUT_DIR}/{address[1]}__{time}.wav', 'w') as wav:
        wav.setnchannels(const.CHANNELS)
        wav.setsampwidth(const.SAMPLE_WIDTH)
        wav.setframerate(const.FRAME_RATE)
        while not shutdown:
            data = await reader.read(4096)
            if not data:
                break
            wav.writeframesraw(data)

    print(f'Stream closed: {address}')
    writer.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(handle_audio_stream, const.HOST, const.PORT, loop=loop)
    server = loop.run_until_complete(coro)

    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    print('\nShutting down')
    shutdown = True
    server.close()
    pending = asyncio.all_tasks(loop=loop)
    loop.run_until_complete(asyncio.gather(*pending, server.wait_closed()))
    loop.close()
