import trollius as asyncio
from trollius import From

END = b'Bye-bye!\n'

@asyncio.coroutine
def echo_client():
    reader, writer = yield From(asyncio.open_connection('localhost', 8000))
    writer.write(b'Hello, world\n')
    writer.write(b'What a fine day it is.\n')
    writer.write(END)
    while True:
        line = yield From(reader.readline())
        print('received:', line)
        if line == END or not line:
            break
    writer.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(echo_client())
loop.close()
