## Data packet, payload and trailer

A data packet is made up of a header, payload and trailer:

$$
\boxed{\begin{array}{c}\text{Sender's IP address}\\\text{Receiver's IP address}\\\text{Packet number}\end{array}}
\;\;\underbrace{\boxed{\hspace{4cm}\text{Data}\hspace{4cm}}}_{\text{Payload}}\;\;
\boxed{\begin{array}{c}\text{Marks the end of the packet}\\\text{Verification data}\end{array}}
$$

| Part        | Contents / purpose                                                          |
| ----------- | --------------------------------------------------------------------------- |
| **Header**  | Contains the sender's IP address, receiver's IP address, and packet number. |
| **Payload** | Contains the actual data being sent.                                        |
| **Trailer** | Marks the end of the packet and contains data used by verification systems. |


## Chunking and sequencing

A large file is split into smaller chunks. Each chunk is assigned a **sequence number** so the receiver can put the data back in the correct order.

$$
\begin{array}{c|c}
\textbf{Sequence number} & \textbf{Chunk size} \\
\hline
1 & 500\,\text{MB} \\
2 & 250\,\text{MB} \\
3 & 100\,\text{MB} \\
4 & 150\,\text{MB} \\
5 & 300\,\text{MB} \\
6 & 350\,\text{MB} \\
7 & 200\,\text{MB} \\
8 & 150\,\text{MB}
\end{array}
$$

When transmitting, packets may arrive out of order:

$$
\boxed{\text{Sender A}}
\quad \xrightarrow{\quad 1\;2\;3\;4\;5\;6\;7\;8\quad} \quad
\boxed{\text{Receiver B}}
$$

$$
\begin{array}{c}
\text{Packets received: } 3\;8\;4\;7\;2\;5\;6\;1 \\
\downarrow\;\text{Reorganise by sequence number} \\
\text{Reassembled output: } 1\;2\;3\;4\;5\;6\;7\;8
\end{array}
$$


## Packet switching

In **packet switching**, packets travel from the sender to the receiver through routers. Different packets can take different routes through the network.

$$
\begin{array}{ccccccccccc}
& & \boxed{R_2} & & & & & \boxed{R_6} & & & \\
& \nearrow & & \searrow & & & \nearrow & & \searrow & & \\
\boxed{\text{Sender A}} & \longrightarrow & \boxed{R_1} & \longrightarrow & \boxed{R_4} & \longrightarrow & \boxed{R_5} & & \boxed{R_8} & \longrightarrow & \boxed{\text{Receiver B}} \\
& \searrow & & \nearrow & & \searrow & & \nearrow & & & \\
& & \boxed{R_3} & & & & & \boxed{R_7} & & &
\end{array}
$$

| Symbol                         | Meaning                                        |
| ------------------------------ | ---------------------------------------------- |
| $\boxed{\text{Sender A}}$      | Device sending the packets.                    |
| $\boxed{R_1}$ to $\boxed{R_8}$ | Routers that forward packets between networks. |
| $\boxed{\text{Receiver B}}$    | Device receiving the packets.                  |

- A method of transmitting data packets across a network, each data packet is able to takes an individual pathway across the network
- A routers is a device, that controls each pathway that will be used to transmit each packet
## Data transmission

### Construction

$$
\begin{array}{c@{\qquad\qquad}c}
\textbf{Serial data transmission} & \textbf{Parallel data transmission} \\
\boxed{A}\;\xrightarrow{\text{one core}}\;\boxed{B} &
\boxed{A}\;\begin{array}{c}\longrightarrow\\[-3pt]\longrightarrow\\[-3pt]\longrightarrow\end{array}\;\boxed{B} \\
\text{One bit at a time} & \text{Multiple bits at a time} \\
\text{Good for long distances} & \text{Good for shorter distances}
\end{array}
$$

| Transmission type | Cores | Bits sent at a time | Best suited to |
|---|---:|---:|---|
| **Serial** | One | One | Long distances |
| **Parallel** | Multiple | Multiple | Shorter distances |

### Direction

$$
\begin{array}{c}
\textbf{Simplex} \\
\boxed{A}\;\longrightarrow\;\boxed{B} \\
\text{One direction only}
\end{array}
\qquad\qquad
\begin{array}{c}
\textbf{Half-duplex} \\
\boxed{A}\;\longrightarrow\;\boxed{B} \\
\boxed{A}\;\leftarrow\boxed{B} \\
\text{Both directions, but not at the same time} \\
\text{The dotted line shows the direction waiting to transmit.}
\end{array}
\qquad\qquad
\begin{array}{c}
\textbf{Full-duplex} \\
\boxed{A}\;\longleftrightarrow\;\boxed{B} \\
\text{Both directions at the same time}
\end{array}
$$

| Mode | Direction of data flow |
|---|---|
| **Simplex** | One direction only. |
| **Half-duplex** | Both directions, but devices take turns transmitting; the unused direction is shown dotted. |
| **Full-duplex** | Both directions simultaneously. |
