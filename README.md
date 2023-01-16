# Dynamic Emergency Vehicular Evacuation (DEVE)

#### By Vanshika Sinha

## Communication Model

DEVE is a peer-to-peer based network fabric aiming at finding the safest and shortest path which updates real time using the information shared from the peers. The network consists of stationary nodes and mobile nodes. DEVE can be implemented using Zigbee network controllers.

## Application Layer

In this layer, when an evacuation has begun, the dormant stationary network receives a message from the mobile node about the evacuation. This is where Dijkstra's Shortest Path Algorithm comes into play to calculate the path fastest to an evacuation point.

## Transport Layer

This layer uses UDP as it is fast and best suited for the network. For reliability, RDT 3.0 is used which waits for the confirmation that the packet is received before sending next sequence of packet. 

## Network Layer

In this layer, each node broadcasts their IP port and time to live every 20 seconds. This broadcast is then caught by other nodes who add this information to a list of peers. Each node has a buffer which stores the address of the peers and their time to live. 

## Link Layer

Since the network uses a shared medium of Wi-Fi, collisions can occur which can be solved by placing the stationary nodes on the roads themselves so that it is swamped with that signal when a car passes by them. Then, before sending the data into the channel, it is encoded using a CRC. 