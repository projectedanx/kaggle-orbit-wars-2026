> Source: https://en.wikipedia.org/wiki/Entropy_in_thermodynamics_and_information_theory

Entropy in thermodynamics and information theory - Wikipedia
Jump to content [-]
Main menu
Main menu
move to sidebar hide
Navigation
Main page
Contents
Current events
Random article
About Wikipedia
Contact us
Contribute
Help
Learn to edit
Community portal
Recent changes
Upload file
Special pages
Search
Search [-]
Appearance
Donate
Create account
Log in [-]
Personal tools
Donate
Create account
Log in
Contents
move to sidebar hide
(Top)
1 Equivalence of form of the defining expressions
2 Theoretical relationship
3 Information is physical Toggle Information is physical subsection
3.1 Szilard's engine
3.2 Landauer's principle
4 Negentropy
5 Quantum theory
6 See also
7 References
8 Further reading
9 External links [-]
Toggle the table of contents
Entropy in thermodynamics and information theory
[-]
1 language
עברית
Edit links
Article
Talk [-]
English
Read
Edit
View history [-]
Tools
Tools
move to sidebar hide
Actions
Read
Edit
View history
General
What links here
Related changes
Upload file
Permanent link
Page information
Cite this page
Get shortened URL
Edit interlanguage links
Print/export
Download as PDF
Printable version
In other projects
Wikidata item
Appearance
move to sidebar hide
Text
[-] 0 Small [x] 1 Standard [-] 2 Large
This page always uses small font size
Width
[x] 1 Standard [-] 0 Wide
The content is as wide as possible for your browser window.
Color (beta)
[-] os Automatic [x] day Light [-] night Dark
This page is always in light mode.
From Wikipedia, the free encyclopedia
Relationship between the concepts of thermodynamic entropy and information entropy
Because the mathematical expressions for information theory developed by Claude Shannon and Ralph Hartley in the 1940s are similar to the mathematics of statistical thermodynamics worked out by Ludwig Boltzmann and J. Willard Gibbs in the 1870s, in which the concept of entropy is central, Shannon was persuaded to employ the same term 'entropy' for his measure of uncertainty. Information entropy is often presumed to be equivalent to physical (thermodynamic) entropy.
Equivalence of form of the defining expressions
[ edit] 
Boltzmann's grave in the Zentralfriedhof, Vienna, with bust and entropy formula
The defining expression for entropy in the theory of statistical mechanics established by Ludwig Boltzmann and J. Willard Gibbs in the 1870s, is of the form:
S = − k B ∑ i p i ln  p i , {\displaystyle S=-k_{\text{B}}\sum {i}p{i}\ln p_{i},} 
where p i {\displaystyle p_{i}} 
is the probability of the microstate i taken from an equilibrium ensemble, and k B {\displaystyle k_{B}} 
is the Boltzmann constant.
The defining expression for entropy in the theory of information established by Claude E. Shannon in 1948 is of the form:
H = − ∑ i p i log b  p i , {\displaystyle H=-\sum {i}p{i}\log {b}p{i},} 
where p i {\displaystyle p_{i}} 
is the probability of the message m i {\displaystyle m_{i}} 
taken from the message space M, and b is the base of the logarithm used. Common values of b are 2, Euler's number e, and 10, and the unit of entropy is shannon (or bit) for b = 2, nat for b = e, and hartley for b = 10. [1]
Mathematically H may also be seen as an average information, taken over the message space, because when a certain message occurs with probability p i, the information quantity −log( p i) (called information content or self-information) will be obtained.
If all the microstates are equiprobable (a microcanonical ensemble), the statistical thermodynamic entropy reduces to the form, as given by Boltzmann,
S = k B ln  W , {\displaystyle S=k_{\text{B}}\ln W,} 
where W is the number of microstates that corresponds to the macroscopic thermodynamic state. Therefore S depends on temperature.
If all the messages are equiprobable, the information entropy reduces to the Hartley entropy
H = log b  | M | , {\displaystyle H=\log _{b}|M|\ ,} 
where | M | {\displaystyle |M|} 
is the cardinality of the message space M.
The logarithm in the thermodynamic definition is the natural logarithm. It can be shown that the Gibbs entropy formula, with the natural logarithm, reproduces all of the properties of the macroscopic classical thermodynamics of Rudolf Clausius. (See article: Entropy (statistical views)).
The logarithm can also be taken to the natural base in the case of information entropy. This is equivalent to choosing to measure information in nats instead of the usual bits (or more formally, shannons). In practice, information entropy is almost always calculated using base-2 logarithms, but this distinction amounts to nothing other than a change in units. One nat is about 1.44 shannons.
For a simple compressible system that can only perform volume work, the first law of thermodynamics becomes
d E = − p d V + T d S . {\displaystyle dE=-pdV+TdS.} 
But one can equally well write this equation in terms of what physicists and chemists sometimes call the 'reduced' or dimensionless entropy, σ = S/ k, so that
d E = − p d V + k B T d σ . {\displaystyle dE=-pdV+k_{\text{B}}Td\sigma .} 
Just as S is conjugate to T, so σ is conjugate to k B T (the energy that is characteristic of T on a molecular scale).
Thus the definitions of entropy in statistical mechanics (The Gibbs entropy formula S = − k B ∑ i p i log  p i {\displaystyle S=-k_{\mathrm {B} }\sum {i}p{i}\log p_{i}} 
) and in classical thermodynamics ( d S = δ Q rev T {\displaystyle dS={\frac {\delta Q_{\text{rev}}}{T}}} 
, and the fundamental thermodynamic relation) are equivalent for microcanonical ensemble, and statistical ensembles describing a thermodynamic system in equilibrium with a reservoir, such as the canonical ensemble, grand canonical ensemble, isothermal–isobaric ensemble. This equivalence is commonly shown in textbooks. However, the equivalence between the thermodynamic definition of entropy and the Gibbs entropy is not general but instead an exclusive property of the generalized Boltzmann distribution. [2]
Furthermore, it has been shown that the definitions of entropy in statistical mechanics is the only entropy that is equivalent to the classical thermodynamics entropy under the following postulates: [3]
The probability density function is proportional to some function of the ensemble parameters and random variables.
Thermodynamic state functions are described by ensemble averages of random variables.
At infinite temperature, all the microstates have the same probability.
Theoretical relationship
[ edit]
Despite the foregoing, there is a difference between the two quantities. The information entropy Η can be calculated for any probability distribution (if the "message" is taken to be that the event i which had probability p i occurred, out of the space of the events possible), while the thermodynamic entropy S refers to thermodynamic probabilities p i specifically. The difference is more theoretical than actual, however, because any probability distribution can be approximated arbitrarily closely by some thermodynamic system. [citationneeded]
Moreover, a direct connection can be made between the two. If the probabilities in question are the thermodynamic probabilities p i: the (reduced) Gibbs entropy σ can then be seen as simply the amount of Shannon information needed to define the detailed microscopic state of the system, given its macroscopic description. Or, in the words of G. N. Lewis writing about chemical entropy in 1930, "Gain in entropy always means loss of information, and nothing more". To be more concrete, in the discrete case using base two logarithms, the reduced Gibbs entropy is equal to the average of the minimum number of yes–no questions needed to be answered in order to fully specify the microstate, given that we know the macrostate.
Furthermore, the prescription to find the equilibrium distributions of statistical mechanics—such as the Boltzmann distribution—by maximising the Gibbs entropy subject to appropriate constraints (the Gibbs algorithm) can be seen as something not unique to thermodynamics, but as a principle of general relevance in statistical inference, if it is desired to find a maximally uninformative probability distribution, subject to certain constraints on its averages. (These perspectives are explored further in the article Maximum entropy thermodynamics.)
The Shannon entropy in information theory is sometimes expressed in units of bits per symbol. The physical entropy may be on a "per quantity" basis ( h) which is called " intensive" entropy instead of the usual total entropy which is called "extensive" entropy. The "shannons" of a message ( Η) are its total "extensive" information entropy and is h times the number of bits in the message.
A direct and physically real relationship between h and S can be found by assigning a symbol to each microstate that occurs per mole, kilogram, volume, or particle of a homogeneous substance, then calculating the 'h' of these symbols. By theory or by observation, the symbols (microstates) will occur with different probabilities and this will determine h. If there are N moles, kilograms, volumes, or particles of the unit substance, the relationship between h (in bits per unit substance) and physical extensive entropy in nats is:
S = k B ln  ( 2 ) N h {\displaystyle S=k_{\mathrm {B} }\ln(2)Nh} 
where ln(2) is the conversion factor from base 2 of Shannon entropy to the natural base e of physical entropy. N h is the amount of information in bits needed to describe the state of a physical system with entropy S. Landauer's principle demonstrates the reality of this by stating the minimum energy E required (and therefore heat Q generated) by an ideally efficient memory change or logic operation by irreversibly erasing or merging N h bits of information will be S times the temperature which is
E = Q = T k B ln  ( 2 ) N h , {\displaystyle E=Q=Tk_{\mathrm {B} }\ln(2)Nh,} 
where h is in informational bits and E and Q are in physical Joules. This has been experimentally confirmed. [4]
Temperature is a measure of the average kinetic energy per particle in an ideal gas (kelvins = 2/ 3 joules/ k B) so the J/K units of k B is dimensionless (joule/joule). k b is the conversion factor from energy in 3/ 2 kelvins to joules for an ideal gas. If kinetic energy measurements per particle of an ideal gas were expressed as joules instead of kelvins, k b in the above equations would be replaced by 3/2. This shows that S is a true statistical measure of microstates that does not have a fundamental physical unit other than the units of information, in this case nats, which is just a statement of which logarithm base was chosen by convention.
Information is physical
[ edit]
Szilard's engine
[ edit] 
N-atom engine schematic
A physical thought experiment demonstrating how just the possession of information might in principle have thermodynamic consequences was established in 1929 by Leó Szilárd, in a refinement of the famous Maxwell's demon scenario [5] (and a reversal of the Joule expansion thought experiment).
Consider Maxwell's set-up, but with only a single gas particle in a box. If the demon knows which half of the box the particle is in (equivalent to a single bit of information), it can close a shutter between the two halves of the box, close a piston unopposed into the empty half of the box, and then extract k B T ln  2 {\displaystyle k_{\text{B}}T\ln 2} 
joules of useful work if the shutter is opened again. The particle can then be left to isothermally expand back to its original equilibrium occupied volume. In just the right circumstances therefore, the possession of a single bit of Shannon information (a single bit of negentropy in Brillouin's term) really does correspond to a reduction in the entropy of the physical system. The global entropy is not decreased, but information to free energy conversion is possible.
This thought experiment has been physically demonstrated, using a phase-contrast microscope equipped with a high speed camera connected to a computer, acting as the demon. [6] In this experiment, information to energy conversion is performed on a Brownian particle by means of feedback control; that is, synchronizing the work given to the particle with the information obtained on its position. Computing energy balances for different feedback protocols, has confirmed that the Jarzynski equality requires a generalization that accounts for the amount of information involved in the feedback.
Landauer's principle
[ edit]
Main article: Landauer's principle
In fact one can generalise: any information that has a physical representation must somehow be embedded in the statistical mechanical degrees of freedom of a physical system.
Thus, Rolf Landauer argued in 1961, if one were to imagine starting with those degrees of freedom in a thermalised state, there would be a real reduction in thermodynamic entropy if they were then re-set to a known state. This can only be achieved under information-preserving microscopically deterministic dynamics if the uncertainty is somehow dumped somewhere else – i.e. if the entropy of the environment (or the non information-bearing degrees of freedom) is increased by at least an equivalent amount, as required by the Second Law, by gaining an appropriate quantity of heat: specifically kT ln(2) of heat for every 1 bit of randomness erased.
On the other hand, Landauer argued, there is no thermodynamic objection to a logically reversible operation potentially being achieved in a physically reversible way in the system. It is only logically irreversible operations – for example, the erasing of a bit to a known state, or the merging of two computation paths – which must be accompanied by a corresponding entropy increase. When information is physical, all processing of its representations, i.e. generation, encoding, transmission, decoding and interpretation, are natural processes where entropy increases by consumption of free energy. [7]
Applied to the Maxwell's demon/Szilard engine scenario, this suggests that it might be possible to "read" the state of the particle into a computing apparatus with no entropy cost; but only if the apparatus has already been SET into a known state, rather than being in a thermalised state of uncertainty. To SET (or RESET) the apparatus into this state will cost all the entropy that can be saved by knowing the state of Szilard's particle.
In 2008 and 2009, researchers showed that Landauer's principle can be derived from the second law of thermodynamics and the entropy change associated with information gain, developing the thermodynamics of quantum and classical feedback-controlled systems. [8] [9]
Negentropy
[ edit]
Main article: Negentropy
Shannon entropy has been related by physicist Léon Brillouin to a concept sometimes called negentropy. In 1953, Brillouin derived a general equation [10] stating that the changing of an information bit value requires at least kT ln(2) energy. This is the same energy as the work Leo Szilard's engine produces in the idealistic case, which in turn equals the same quantity found by Landauer. In his book, [11] he further explored this problem concluding that any cause of a bit value change (measurement, decision about a yes/no question, erasure, display, etc.) will require the same amount, kT ln(2), of energy. Consequently, acquiring information about a system's microstates is associated with an entropy production, while erasure yields entropy production only when the bit value is changing. Setting up a bit of information in a sub-system originally in thermal equilibrium results in a local entropy reduction. However, there is no violation of the second law of thermodynamics, according to Brillouin, since a reduction in any local system's thermodynamic entropy results in an increase in thermodynamic entropy elsewhere. In this way, Brillouin clarified the meaning of negentropy which was considered as controversial because its earlier understanding can yield Carnot efficiency higher than one. Additionally, the relationship between energy and information formulated by Brillouin has been proposed as a connection between the amount of bits that the brain processes and the energy it consumes: Collell and Fauquet [12] argued that De Castro [13] analytically found the Landauer limit as the thermodynamic lower bound for brain computations. However, even though evolution is supposed to have "selected" the most energetically efficient processes, the physical lower bounds are not realistic quantities in the brain. Firstly, because the minimum processing unit considered in physics is the atom/molecule, which is distant from the actual way that brain operates; and, secondly, because neural networks incorporate important redundancy and noise factors that greatly reduce their efficiency. [14] Laughlin et al. [15] was the first to provide explicit quantities for the energetic cost of processing sensory information. Their findings in blowflies revealed that for visual sensory data, the cost of transmitting one bit of information is around 5 × 10 −14 Joules, or equivalently 10 4 ATP molecules. Thus, neural processing efficiency is still far from Landauer's limit of kT ln(2) J, but as a curious fact, it is still much more efficient than modern computers.
In 2009, Mahulikar & Herwig redefined thermodynamic negentropy as the specific entropy deficit of the dynamically ordered sub-system relative to its surroundings. [16] This definition enabled the formulation of the Negentropy Principle, which is mathematically shown to follow from the 2nd Law of Thermodynamics, during order existence.
Quantum theory
[ edit]
See also: Holographic principle § Energy, matter, and information equivalence; and Quantum relative entropy
Hirschman showed, [17] cf. Hirschman uncertainty, that Heisenberg's uncertainty principle can be expressed as a particular lower bound on the sum of the classical distribution entropies of the quantum observable probability distributions of a quantum mechanical state, the square of the wave-function, in coordinate, and also momentum space, when expressed in Planck units. The resulting inequalities provide a tighter bound on the uncertainty relations of Heisenberg.
It is meaningful to assign a " joint entropy", because positions and momenta are quantum conjugate variables and are therefore not jointly observable. Mathematically, they have to be treated as joint distribution. Note that this joint entropy is not equivalent to the Von Neumann entropy, −Tr ρlnρ ** = −⟨lnρ**⟩. Hirschman's entropy is said to account for the full information content of a mixture of quantum states. [18]
(Dissatisfaction with the Von Neumann entropy from quantum information points of view has been expressed by Stotland, Pomeransky, Bachmat and Cohen, who have introduced a yet different definition of entropy that reflects the inherent uncertainty of quantum mechanical states. This definition allows distinction between the minimum uncertainty entropy of pure states, and the excess statistical entropy of mixtures. [19])
See also
[ edit]
Thermodynamic entropy
Information entropy
Thermodynamics
Statistical mechanics
Information theory
Quantum entanglement
Quantum decoherence
Fluctuation theorem
Black hole entropy
Black hole information paradox
Entropy (information theory)
Entropy (statistical thermodynamics)
Entropy (order and disorder)
Orders of magnitude (entropy)
References
[ edit]
^ Schneider, T.D, Information theory primer with an appendix on logarithms, National Cancer Institute, 14 April 2007.
^ Gao, Xiang; Gallicchio, Emilio; Roitberg, Adrian (2019). "The generalized Boltzmann distribution is the only distribution in which the Gibbs-Shannon entropy equals the thermodynamic entropy". The Journal of Chemical Physics. 151 (3): 034113. arXiv: 1903.02121. Bibcode: 2019JChPh.151c4113G. doi: 10.1063/1.5111333. PMID 31325924. S2CID 118981017.
^ Gao, Xiang (March 2022). "The Mathematics of the Ensemble Theory". Results in Physics. 34 105230. arXiv: 2006.00485. Bibcode: 2022ResPh..3405230G. doi: 10.1016/j.rinp.2022.105230. S2CID 221978379.
^ Antoine Bérut; Artak Arakelyan; Artyom Petrosyan; Sergio Ciliberto; Raoul Dillenschneider; Eric Lutz (8 March 2012), "Experimental verification of Landauer's principle linking information and thermodynamics" (PDF), Nature, 483 (7388): 187– 190, Bibcode: 2012Natur.483..187B, doi: 10.1038/nature10872, PMID 22398556, S2CID 9415026
^ Szilard, Leo (1929). "Über die Entropieverminderung in einem thermodynamischen System bei Eingriffen intelligenter Wesen". Zeitschrift für Physik (in German). 53 ( 11– 12): 840– 856. Bibcode: 1929ZPhy...53..840S. doi: 10.1007/BF01341281. ISSN 0044-3328. S2CID 122038206. Available on-line in English at Aurellen.org.
^ Shoichi Toyabe; Takahiro Sagawa; Masahito Ueda; Eiro Muneyuki; Masaki Sano (2010-09-29). "Information heat engine: converting information to energy by feedback control". Nature Physics. 6 (12): 988– 992. arXiv: 1009.5287. Bibcode: 2010NatPh...6..988T. doi: 10.1038/nphys1821. S2CID 118444713. We demonstrated that free energy is obtained by a feedback control using the information about the system; information is converted to free energy, as the first realization of Szilard-type Maxwell's demon.
^ Karnani, M.; Pääkkönen, K.; Annila, A. (2009). "The physical character of information". Proc. R. Soc. A. 465 (2107): 2155– 75. Bibcode: 2009RSPSA.465.2155K. doi: 10.1098/rspa.2009.0063.
^ Sagawa, Takahiro; Ueda, Masahito (2008-02-26). "Second Law of Thermodynamics with Discrete Quantum Feedback Control". Physical Review Letters. 100 (8) 080403. arXiv: 0710.0956. Bibcode: 2008PhRvL.100h0403S. doi: 10.1103/PhysRevLett.100.080403. ISSN 0031-9007. PMID 18352605.
^ Cao, F. J.; Feito, M. (2009-04-10). "Thermodynamics of feedback controlled systems". Physical Review E. 79 (4) 041118. arXiv: 0805.4824. Bibcode: 2009PhRvE..79d1118C. doi: 10.1103/PhysRevE.79.041118. ISSN 1539-3755. PMID 19518184.
^ Brillouin, Leon (1953). "The negentropy principle of information". Journal of Applied Physics. 24 (9): 1152– 1163. Bibcode: 1953JAP....24.1152B. doi: 10.1063/1.1721463.
^ Leon Brillouin, Science and Information theory, Dover, 1956
^ Collell, G; Fauquet, J. (June 2015). "Brain activity and cognition: a connection from thermodynamics and information theory". Frontiers in Psychology. 6 (4): 818. doi: 10.3389/fpsyg.2015.00818. PMC 4468356. PMID 26136709.
^ De Castro, A. (November 2013). "The Thermodynamic Cost of Fast Thought". Minds and Machines. 23 (4): 473– 487. arXiv: 1201.5841. doi: 10.1007/s11023-013-9302-x. S2CID 11180644.
^ Narayanan, N. S. at al. (2005). "Redundancy and synergy of neuronal ensembles in motor cortex". J. Neurosci. 25 (17): 4207– 4216. doi: 10.1523/JNEUROSCI.4697-04.2005. PMC 6725112. PMID 15858046.
^ Laughlin, S. B at al. (November 2013). "The metabolic cost of neural information". Nat. Neurosci. 1 (1): 36– 41. doi: 10.1038/236. PMID 10195106. S2CID 204995437.
^ Mahulikar, S.P.; Herwig, H. (August 2009). "Exact thermodynamic principles for dynamic order existence and evolution in chaos". Chaos, Solitons & Fractals. 41 (4): 1939– 48. Bibcode: 2009CSF....41.1939M. doi: 10.1016/j.chaos.2008.07.051.
^ Hirschman, I.I. Jr. (January 1957). "A note on entropy". American Journal of Mathematics. 79 (1): 152– 6. doi: 10.2307/2372390. JSTOR 2372390.
^ Zachos, C. K. (2007). "A classical bound on quantum entropy". Journal of Physics A: Mathematical and Theoretical. 40 (21): F407– F412. arXiv: hep-th/0609148. Bibcode: 2007JPhA...40..407Z. doi: 10.1088/1751-8113/40/21/F02. S2CID 1619604.
^ Alexander Stotland; Pomeransky; Eitan Bachmat; Doron Cohen (2004). "The information entropy of quantum mechanical states". Europhysics Letters. 67 (5): 700– 6. arXiv: quant-ph/0401021. Bibcode: 2004EL.....67..700S. CiteSeerX 10.1.1.252.8715. doi: 10.1209/epl/i2004-10110-1. S2CID 51730529.
Further reading
[ edit]
Bennett, C.H. (1973). "Logical reversibility of computation". IBM J. Res. Dev. 17 (6): 525– 532. doi: 10.1147/rd.176.0525.
Brillouin, Léon (2004), Science And Information Theory (second ed.), Dover, ISBN 978-0-486-43918-1 . [Republication of 1962 original.]
Frank, Michael P. (May–June 2002). "Physical Limits of Computing". Computing in Science and Engineering. 4 (3): 16– 25. Bibcode: 2002CSE.....4c..16F. CiteSeerX 10.1.1.429.1618. doi: 10.1109/5992.998637. OSTI 1373456. S2CID 499628.
Greven, Andreas; Keller, Gerhard; Warnecke, Gerald, eds. (2003). Entropy. Princeton University Press. ISBN 978-0-691-11338-8 . (A highly technical collection of writings giving an overview of the concept of entropy as it appears in various disciplines.)
Kalinin, M.I.; Kononogov, S.A. (2005), "Boltzmann's constant, the energy meaning of temperature, and thermodynamic irreversibility", Measurement Techniques, 48 (7): 632– 636, Bibcode: 2005MeasT..48..632K, doi: 10.1007/s11018-005-0195-9, S2CID 118726162 .
Koutsoyiannis, D. (2011), "Hurst–Kolmogorov dynamics as a result of extremal entropy production", Physica A, 390 (8): 1424– 1432, Bibcode: 2011PhyA..390.1424K, doi: 10.1016/j.physa.2010.12.035 .
Landauer, R. (1993). "Information is Physical". Proc. Workshop on Physics and Computation PhysComp'92. Los Alamitos: IEEE Comp. Sci.Press. pp. 1– 4. doi: 10.1109/PHYCMP.1992.615478. ISBN 978-0-8186-3420-8 . S2CID 60640035.
Landauer, R. (1961). "Irreversibility and Heat Generation in the Computing Process". IBM J. Res. Dev. 5 (3): 183– 191. doi: 10.1147/rd.53.0183. Archived from the original on 2008-12-06. Retrieved 2006-03-11.
Leff, H.S.; Rex, A.F., eds. (1990). Maxwell's Demon: Entropy, Information, Computing. Princeton NJ: Princeton University Press. ISBN 978-0-691-08727-6 .
Middleton, D. (1960). An Introduction to Statistical Communication Theory. McGraw-Hill.
Shannon, Claude E. (July–October 1948). "A Mathematical Theory of Communication". Bell System Technical Journal. 27 (3): 379– 423. doi: 10.1002/j.1538-7305.1948.tb01338.x. hdl: 10338.dmlcz/101429. ( as PDF)
External links
[ edit]
Information Processing and Thermodynamic Entropy Stanford Encyclopedia of Philosophy.
An Intuitive Guide to the Concept of Entropy Arising in Various Sectors of Science — a wikibook on the interpretation of the concept of entropy. 
Retrieved from " https://en.wikipedia.org/w/index.php?title=Entropy_in_thermodynamics_and_information_theory&oldid=1342474834"
Categories:
Thermodynamic entropy
Entropy and information
Philosophy of thermal and statistical physics
Hidden categories:
CS1 German-language sources (de)
Articles with short description
Short description matches Wikidata
All articles with unsourced statements
Articles with unsourced statements from July 2017
This page was last edited on 9 March 2026, at 04:07 (UTC).
Text is available under the Creative Commons Attribution-ShareAlike 4.0 License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.
Privacy policy
About Wikipedia
Disclaimers
Contact Wikipedia
Legal & safety contacts
Code of Conduct
Developers
Statistics
Cookie statement
Mobile view
Search
Search [-]
Toggle the table of contents
Entropy in thermodynamics and information theory
1 language Add topic 