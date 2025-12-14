import asyncio

async def handle_client(reader, writer):
    try:
        # Read request (up to 1024 bytes)
        data = await reader.read(1024)
        request = data.decode()

        # Parse request line
        lines = request.split('\r\n')
        request_line = lines[0]
        method, path, _ = request_line.split(' ')

        # Handle routes
        if path == '/':
            response = b"HTTP/1.1 200 OK\r\n\r\n"

        elif path.startswith('/echo/'):
            msg = path[6:]
            body = msg.encode("utf-8")
            headers = (
                b"HTTP/1.1 200 OK\r\n"
                b"Content-Type: text/plain\r\n" +
                f"Content-Length: {len(body)}".encode() +
                b"\r\n\r\n"
            )
            response = headers + body

        elif path == '/user-agent':
            # Find User-Agent header
            user_agent = ""
            for line in lines:
                if line.lower().startswith("user-agent:"):
                    user_agent = line.split(":", 1)[1].strip()

            body = user_agent.encode("utf-8")
            headers = (
                b"HTTP/1.1 200 OK\r\n"
                b"Content-Type: text/plain\r\n" +
                f"Content-Length: {len(body)}".encode() +
                b"\r\n\r\n"
            )
            response = headers + body

        else:
            response = b"HTTP/1.1 404 Not Found\r\n\r\n"

        writer.write(response)
        await writer.drain()
    except Exception as e:
        print("Client error:", e)
    finally:
        writer.close()
        await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_client, 'localhost', 4221)
    print("Async server running on port 4221...")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
