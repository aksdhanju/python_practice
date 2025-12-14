import socket  # noqa: F401
import threading  # noqa: F401


def handle_client(conn, address):
    """Handle a single client connection."""
    print(f"Connected by {address}")

    # Read the incoming request
    request_data = conn.recv(1024)
    request_str = request_data.decode('utf-8')
    
    # Parse the request line to extract the path
    # Request line format: METHOD PATH HTTP_VERSION\r\n
    request_lines = request_str.split('\r\n')
    request_line = request_lines[0]
    path = request_line.split(' ')[1]
    
    # Parse headers (lines after request line until empty line)
    headers = {}
    for line in request_lines[1:]:
        if not line:  # Empty line marks end of headers
            break
        if ':' in line:
            header_name, header_value = line.split(':', 1)
            headers[header_name.strip().lower()] = header_value.strip()
    
    # Determine response based on path
    if path.startswith('/echo/'):
        # Extract the string after /echo/
        echo_str = path[6:]  # Skip '/echo/'
        # Calculate Content-Length in bytes
        content_length = len(echo_str.encode('utf-8'))
        # Build response with headers and body
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {content_length}\r\n\r\n{echo_str}".encode('utf-8')
        print(f"response: 200 OK (echo: {echo_str})")
    elif path == '/user-agent':
        # Extract User-Agent header value
        user_agent = headers.get('user-agent', '')
        # Calculate Content-Length in bytes
        content_length = len(user_agent.encode('utf-8'))
        # Build response with headers and body
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {content_length}\r\n\r\n{user_agent}".encode('utf-8')
        print(f"response: 200 OK (user-agent: {user_agent})")
    elif path == '/':
        print(f"response: 200 OK")
        response = b"HTTP/1.1 200 OK\r\n\r\n"
    else:
        print(f"response: 404 Not Found")
        response = b"HTTP/1.1 404 Not Found\r\n\r\n"
    
    conn.sendall(response)
    
    # Close the connection
    conn.close()


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    
    # Accept multiple connections concurrently
    while True:
        conn, address = server_socket.accept()
        # Create a new thread for each connection
        client_thread = threading.Thread(target=handle_client, args=(conn, address))
        client_thread.start()


if __name__ == "__main__":
    main()
