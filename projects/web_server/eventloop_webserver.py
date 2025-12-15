import asyncio

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"[CONNECT] Client connected: {addr}")

    try:
        # Read request (up to 1024 bytes)
        data = await reader.read(1024)
        print(f"[RECEIVE] From {addr}: {data!r}")

        if not data:
            print(f"[DISCONNECT] Empty data from {addr}, closing connection.")
            return

        request = data.decode()
        print(f"[DECODE] Request from {addr}:\n{request}")

        # Parse request line
        lines = request.split('\r\n')
        request_line = lines[0]
        print(f"[PARSE] Request line from {addr}: {request_line}")

        method, path, _ = request_line.split(' ')
        print(f"[PARSE] Method={method}, Path={path}")

        # Handle routes
        if path == '/':
            response = b"HTTP/1.1 200 OK\r\n\r\n"
            print(f"[ROUTE] {addr}: Respond 200 OK /")

        elif path.startswith('/echo/'):
            msg = path[6:]
            print(f"[ROUTE] {addr}: Echo message: {msg}")
            body = msg.encode("utf-8")
            headers = (
                b"HTTP/1.1 200 OK\r\n"
                b"Content-Type: text/plain\r\n" +
                f"Content-Length: {len(body)}".encode() +
                b"\r\n\r\n"
            )
            response = headers + body

        elif path == '/user-agent':
            print(f"[ROUTE] {addr}: User-Agent requested.")
            user_agent = ""
            for line in lines:
                if line.lower().startswith("user-agent:"):
                    user_agent = line.split(":", 1)[1].strip()

            print(f"[HEADER] User-Agent from {addr}: {user_agent}")

            body = user_agent.encode("utf-8")
            headers = (
                b"HTTP/1.1 200 OK\r\n"
                b"Content-Type: text/plain\r\n" +
                f"Content-Length: {len(body)}".encode() +
                b"\r\n\r\n"
            )
            response = headers + body

        else:
            print(f"[ROUTE] {addr}: 404 Not Found for path {path}")
            response = b"HTTP/1.1 404 Not Found\r\n\r\n"

        writer.write(response)
        await writer.drain()
        print(f"[SEND] Response sent to {addr}")

    except Exception as e:
        print(f"[ERROR] Client {addr} error: {e}")

    finally:
        print(f"[CLOSE] Closing connection for {addr}")
        writer.close()
        await writer.wait_closed()
        print(f"[CLOSE] Connection closed for {addr}")


async def main():
    server = await asyncio.start_server(handle_client, 'localhost', 4221)
    print("[SERVER] Async server running on port 4221...")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
