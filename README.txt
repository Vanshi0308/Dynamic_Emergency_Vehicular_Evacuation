A UDP peer-to-peer communtication program

Dependencies:
    python
    pickle Library
    scoket Library
    threading Library


1. Run the client.py using "python client.py" command.
2. Enter the port you want to use to bind the socket(eg 3000) (Any port numeber > 1023) works.
3. Enter the address and destination of peer client.
** If using localhost use 127.0.0.1 as peer_address **

4. On another terminal/command prompt run p_client.py using "python p_client" command.
5. Repeat steps 2-3 usng different port number then enter port number used in client.py.
6. Enter port number of p_client.py on client.py terminal.
7. Now Conenction has been established.
8. You can enter any message on the terminal.
9. To trigger an event just type EVENT and press enter.