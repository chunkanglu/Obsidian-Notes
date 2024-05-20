A language $L$ represents a problem $P$ iff we can map any instance of $P$ to a word $w \in L$ and vice versa
- we can study these problems then with formal languages and TMs

$L(M)$ is the language a machine $M$ which is all words the machine accepts

*Recognizable* - language $L$ is recognizable if there's a TM that accepts all words $w \in L$
*Co-recognizable* - language $L$ is co-recognizable if complement $\overline{L}$ is recognizable
- a TM can **accept** a word that **isn't** in $L$
- but **rejects or does not halt** if the input **is** in $L$
- Language of TM that don't halt on empty input is co-recognizable
*Decidable* - recognizable and co-recognizable
- TM must always halt
- ![[Pasted image 20240513113634.png]]
- **If a language is decidable, then its complement must be decidable**

> [!INFO]- https://stackoverflow.com/a/10032433
> Intuitively, a language is Turing-recognizable if there is some computer program that, given a string in the language, can confirm that the string is indeed within the language. This program might loop infinitely if the string isn't in the language, but it's guaranteed to always eventually accept if you give it a string in the language.
> 
> While it's true that a language is co-Turing-recognizable if it's the complement of a language that's Turing-recognizable, this definition doesn't shed much light on what's going on. Intuitively, if a language is co-Turing-recognizable, it means that there is a computer program that, given a string _not_ in the language, will eventually confirm that the string is not in the language. It might loop infinitely if the string is indeed within the language, though. The reason for this is simple - if some string w isn't contained within a co-Turing-recognizable language, then that string w must be contained within the complement of that co-Turing-recognizable language, which (by definition) has to be Turing-recognizable. Since w is in the Turing-recognizable complement, there must be some program that can confirm that w is indeed in the complement. This program therefore can confirm that w is not in the original co-Turing-recognizable language.
> 
> In short, Turing-recognizability means that there is a program that can confirm that a string w is in a language, and co-Turing-recognizability means that there is a program that can confirm that a string w is _not_ in the language.

