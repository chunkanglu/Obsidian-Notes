# 1
## a
## b
i. $0\textvisiblespace$
ii. $\textvisiblespace$
iii. $1$
## c
$$
L(M) = \left\{ 0 \in w | w \in \mathbb{N} \right\}
$$
All strings that contain a 0 *somewhere*
## d
### i
$$
f(w) =
\begin{cases}
\text{Makes rightmost 0 character a 1}  & 0 \in w \\
\perp & \text{otherwise}
\end{cases}
$$
# 2
1. Write $ at the beginning & shift everything over right 1 character (accomodate overflow bit)
2. Add 2 (by essentially adding 1 starting from second-rightmost char)
3. If overflow $ char not used, shift everything over left 1 character, then accept
4. Otherwise, accept (should already be at start of string after adding)
### Diagram
![[Drawing 2024-05-19 20.05.01.excalidraw]]
#### Shift Right 1
- Start in $q_0$
- $q_1$ means character to the left was originally a $0$
- $q_2$ means character to the left was originally a $1$
- Keep writing the previous character on the current position until end
- At this point in $q_3$ we are at the empty to the right of string
### Add 2
- Start in $q_4$ at last character of string
- Move left 1 character to $q_5$ because we add 2 (which is adding 1 to the second-last bit)
- Idea is that we go from right to left and stop at the first $0$ we see and change it to $1$ ($q_5 \to q_7$). Along the way, $1$s are changed to $0$ (the $q_5 \to q_5$ loop). If we ever hit the $\$$ at the beginning, that means the original string was all $1$s (like $1, 11, 111, \ldots$) and we use $\$$ as an overflow bit ($q_5 \to q_6$).
### Shift Left 1 (if needed)
- If we used the overflow $\$$ in the last step, then tape head is already at the start and we accept in $q_6$
- Otherwise, we start at the last character of the string, starting to shift left by 1, and knowing the last character is replaced by $\textvisiblespace$
	- Same idea as in [[Tutorial 1#Shift Right 1|above]]
	- $q_9$ means character to the right was originally a 0
	- $q_{10}$ means character to the right was originally a 1
	- Once we read $\$$ we know we hit the start and we can accept
	- **Note:** the $q_9 \to q_{11}$ transition is probably not needed if we know the string entered won't have leading $0$s
### LaTex

```latex
\documentclass[12pt]{article}
\usepackage{tikz}

\begin{document}

\begin{center}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (3.8,-9.3) circle (3);
\draw (3.8,-9.3) node {$q_0$};
\draw [black] (21.5,-9.3) circle (3);
\draw (21.5,-9.3) node {$q_1$};
\draw [black] (21.5,-22.5) circle (3);
\draw (21.5,-22.5) node {$q_2$};
\draw [black] (40.6,-9.3) circle (3);
\draw (40.6,-9.3) node {$q_3$};
\draw [black] (53.4,-9.3) circle (3);
\draw (53.4,-9.3) node {$q_4$};
\draw [black] (66.8,-14.3) circle (3);
\draw (66.8,-14.3) node {$q_5$};
\draw [black] (66.8,-4.3) circle (3);
\draw (66.8,-4.3) node {$q_6$};
\draw [black] (66.8,-4.3) circle (2.4);
\draw [black] (66.8,-23.8) circle (3);
\draw (66.8,-23.8) node {$q_7$};
\draw [black] (66.8,-39.2) circle (3);
\draw (66.8,-39.2) node {$q_8$};
\draw [black] (47.7,-39.2) circle (3);
\draw (47.7,-39.2) node {$q_9$};
\draw [black] (47.7,-50.6) circle (3);
\draw (47.7,-50.6) node {$q_1_0$};
\draw [black] (24.6,-39.2) circle (3);
\draw (24.6,-39.2) node {$q_1_1$};
\draw [black] (24.6,-39.2) circle (2.4);
\draw [black] (6.8,-9.3) -- (18.5,-9.3);
\fill [black] (18.5,-9.3) -- (17.7,-8.8) -- (17.7,-9.8);
\draw (12.65,-9.8) node [below] {$0:\mbox{ }$,R$};
\draw [black] (6.2,-11.09) -- (19.1,-20.71);
\fill [black] (19.1,-20.71) -- (18.75,-19.83) -- (18.15,-20.63);
\draw (8.83,-16.4) node [below] {$1:\mbox{ }$,\mbox{ }R$};
\draw [black] (24.5,-9.3) -- (37.6,-9.3);
\fill [black] (37.6,-9.3) -- (36.8,-8.8) -- (36.8,-9.8);
\draw (31.05,-9.8) node [below] {$_:\mbox{ }0,\mbox{ }R$};
\draw [black] (23.97,-20.79) -- (38.13,-11.01);
\fill [black] (38.13,-11.01) -- (37.19,-11.05) -- (37.76,-11.87);
\draw (34.73,-16.4) node [below] {$_:\mbox{ }1,\mbox{ }R$};
\draw [black] (22.902,-11.943) arc (20.38098:-20.38098:11.364);
\fill [black] (22.9,-19.86) -- (23.65,-19.28) -- (22.71,-18.93);
\draw (24.11,-15.9) node [right] {$1:\mbox{ }0,\mbox{ }R$};
\draw [black] (20.492,-19.679) arc (-165.87992:-194.12008:15.492);
\fill [black] (20.49,-12.12) -- (19.81,-12.77) -- (20.78,-13.02);
\draw (19.52,-15.9) node [left] {$0:\mbox{ }1,\mbox{ }R$};
\draw [black] (43.6,-9.3) -- (50.4,-9.3);
\fill [black] (50.4,-9.3) -- (49.6,-8.8) -- (49.6,-9.8);
\draw (47,-9.8) node [below] {$_:\mbox{ }L$};
\draw [black] (56.21,-10.35) -- (63.99,-13.25);
\fill [black] (63.99,-13.25) -- (63.41,-12.5) -- (63.06,-13.44);
\draw (56.89,-12.38) node [below] {$0/1:\mbox{ }L$};
\draw [black] (66.8,-11.3) -- (66.8,-7.3);
\fill [black] (66.8,-7.3) -- (66.3,-8.1) -- (67.3,-8.1);
\draw (67.3,-9.3) node [right] {$$:\mbox{ }1,\mbox{ }L$};
\draw [black] (23.245,-24.926) arc (63.46232:-224.53768:2.25);
\draw (23.72,-29.9) node [below] {$1:\mbox{ }R$};
\fill [black] (20.64,-25.36) -- (19.83,-25.85) -- (20.73,-26.3);
\draw [black] (20.177,-6.62) arc (234:-54:2.25);
\draw (21.5,-2.05) node [above] {$0:\mbox{ }R$};
\fill [black] (22.82,-6.62) -- (23.7,-6.27) -- (22.89,-5.68);
\draw [black] (69.48,-12.977) arc (144:-144:2.25);
\draw (74.05,-14.3) node [right] {$1:\mbox{ }0,\mbox{ }L$};
\fill [black] (69.48,-15.62) -- (69.83,-16.5) -- (70.42,-15.69);
\draw [black] (66.8,-17.3) -- (66.8,-20.8);
\fill [black] (66.8,-20.8) -- (67.3,-20) -- (66.3,-20);
\draw (66.3,-19.05) node [left] {$0:\mbox{ }1,\mbox{ }R$};
\draw [black] (69.48,-22.477) arc (144:-144:2.25);
\draw (74.05,-23.8) node [right] {$0/1:\mbox{ }R$};
\fill [black] (69.48,-25.12) -- (69.83,-26) -- (70.42,-25.19);
\draw [black] (66.8,-26.8) -- (66.8,-36.2);
\fill [black] (66.8,-36.2) -- (67.3,-35.4) -- (66.3,-35.4);
\draw (66.3,-31.5) node [left] {$_:\mbox{ }L$};
\draw [black] (49.023,-53.28) arc (54:-234:2.25);
\draw (47.7,-57.85) node [below] {$1:\mbox{ }L$};
\fill [black] (46.38,-53.28) -- (45.5,-53.63) -- (46.31,-54.22);
\draw [black] (46.377,-36.52) arc (234:-54:2.25);
\draw (47.7,-31.95) node [above] {$0:\mbox{ }L$};
\fill [black] (49.02,-36.52) -- (49.9,-36.17) -- (49.09,-35.58);
\draw [black] (63.8,-39.2) -- (50.7,-39.2);
\fill [black] (50.7,-39.2) -- (51.5,-39.7) -- (51.5,-38.7);
\draw (57.25,-38.7) node [above] {$0:\mbox{ }_,\mbox{ }L$};
\draw [black] (65.01,-41.605) arc (-40.0261:-78.31144:25.47);
\fill [black] (50.67,-50.17) -- (51.55,-50.49) -- (51.35,-49.51);
\draw (62.15,-47.6) node [below] {$1:\mbox{ }_,\mbox{ }L$};
\draw [black] (44.7,-39.2) -- (27.6,-39.2);
\fill [black] (27.6,-39.2) -- (28.4,-39.7) -- (28.4,-38.7);
\draw (36.15,-38.7) node [above] {$$:\mbox{ }0,\mbox{ }L$};
\draw [black] (45.01,-49.27) -- (27.29,-40.53);
\fill [black] (27.29,-40.53) -- (27.79,-41.33) -- (28.23,-40.43);
\draw (32.46,-45.42) node [below] {$$:\mbox{ }1,\mbox{ }L$};
\draw [black] (49.031,-41.876) arc (17.76841:-17.76841:9.909);
\fill [black] (49.03,-47.92) -- (49.75,-47.31) -- (48.8,-47.01);
\draw (50,-44.9) node [right] {$0:\mbox{ }1,\mbox{ }L$};
\draw [black] (46.575,-47.828) arc (-165.34551:-194.65449:11.573);
\fill [black] (46.58,-41.97) -- (45.89,-42.62) -- (46.86,-42.87);
\draw (45.7,-44.9) node [left] {$1:\mbox{ }0,\mbox{ }L$};
\end{tikzpicture}
\end{center}

\end{document}
```


# 3
**Map from path problem to PCP**
Given an instance of PATH create an instance of PCP that is a yes-instance iff PATH is yes-instance.
PATH given $G = (V, E), s, tis there a path from $s$ to $t$

decision tree BFS
graph turn into path finding
tiles hav something to do with edges of graph
mark starting and ending tile with like $\frac{\$S}{\$}$ , $\frac{\$}{T\$}$ 
