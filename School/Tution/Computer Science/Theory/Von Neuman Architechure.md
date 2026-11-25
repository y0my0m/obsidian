# 🖥️ Von Neumann Architecture

The **Von Neumann architecture** is a computer design in which instructions and data are stored in memory and processed by the CPU.

$$
\begin{array}{c}
\text{Von Neumann Architecture}\\[6pt]
\text{Input}\;\longrightarrow\;
\underbrace{\boxed{\begin{array}{c}
\textbf{CPU}\\[4pt]
\boxed{\text{Control Unit}}\\[4pt]
\boxed{\text{ALU}}\\[4pt]
\boxed{\text{Cache Memory}}\\[4pt]
\boxed{\text{Registers}}
\end{array}};\longleftrightarrow\;\boxed{\begin{array}{c}\text{Memory Unit}\end{array}}}_{\text{Hardware}}
\;\longrightarrow\;\text{Output}
\end{array}
$$


Control Unit:
- Sends control signals to control all the other components of the computer
ALU (Arithmetic Logic Unit)
- Does arithmetic and logical calculations
Cache memory
- Stores most frequently used data and instructions


## Main Components

- **Control Unit (CU):** directs the processor’s operations and coordinates instruction execution.
- **Arithmetic Logic Unit (ALU):** performs arithmetic calculations and logical comparisons.
- **Registers:** very small, fast storage locations inside the CPU for data and instructions currently in use.
- **Cache memory:** fast memory close to the CPU that keeps frequently needed data and instructions readily available.
- **Memory unit:** stores both program instructions and data.
- **Input and output:** input provides data and instructions; output presents the results.

> [!NOTE]
> The CPU and memory communicate over buses. The sketch shows the connection as a two-way link because data and instructions move between them in both directions.


