> Source: https://www.physics.rutgers.edu/~morozov/677_f2017/Physics_677_2017_files/Berut_Lutz_Nature2012.pdf

LETTER 
doi:10.1038/nature10872 
Experimental verification of Landauer’s principle linking information and thermodynamics 
Antoine Bérut1, Artak Arakelyan1, Artyom Petrosyan1, Sergio Ciliberto1, Raoul Dillenschneider2 & Eric Lutz3{ 
In 1961, Rolf Landauer argued that the erasure of information is a dissipative process1. A minimal quantity of heat, proportional to the thermal energy and called the Landauer bound, is necessarily pro-duced when a classical bit of information is deleted. A direct con-sequence of this logically irreversible transformation is that the entropy of the environment increases by a finite amount. Despite its fundamental importance for information theory and computer science2–5, the erasure principle has not been verified experimentally so far, the main obstacle being the difficulty of doing single-particle experiments in the low-dissipation regime. Here we experimentally show the existence of the Landauer bound in a generic model of a one-bit memory. Using a system of a single colloidal particle trapped in a modulated double-well potential, we establish that the mean dissipated heat saturates at the Landauer bound in the limit of long erasure cycles. This result demonstrates the intimate link between information theory and thermodynamics. It further highlights the ultimate physical limit of irreversible computation. 
The idea of a connection between information and thermodynamics can be traced back to Maxwell’s ‘demon’6–8. The demon is an intelligent creature able to monitor individual molecules of a gas contained in two neighbouring chambers initially at the same temperature. Some of the molecules will be going faster than average and some will be going slower. By opening and closing a molecular-sized trap door in the partitioning wall, the demon collects the faster (hot) molecules in one of the chambers and the slower (cold) ones in the other. The temperature difference thus created can be used to run a heat engine, and produce useful work. By converting information (about the position and velocity of each particle) into energy, the demon is therefore able to decrease the entropy of the system without performing any work himself, in apparent violation of the second law of thermodynamics. A simplified, one-mole-cule engine introduced later9 has been recently realized experimentally using non-equilibrium feedback manipulation of a Brownian particle10. The paradox of the apparent violation of the second law can be resolved by noting that during a full thermodynamic cycle, the memory of the demon, which is used to record the coordinates of each molecule, has to be reset to its initial state11,12. Indeed, according to Landauer’s principle, any logically irreversible transformation of classical information is necessarily accompanied by the dissipation of at least kTln(2) of heat per lost bit (about 3 3 10221 J at room temperature (300 K)), where k is the Boltzmann constant and T is the temperature. 
A device is said to be logically irreversible if its input cannot be uniquely determined from its output13. Any Boolean function that maps several input states onto the same output state, such as AND, NAND, OR and XOR, is therefore logically irreversible. In particular, the erasure of information, the RESET TO ONE operation, is logically irreversible and leads to an entropy increase of kln(2) per erased bit14–16. This entropy cost required to reset the demon’s memory to a blank state is always larger than the initial entropy reduction, thus safeguarding the second law. Landauer’s principle hence seems to be a central result that not only exorcizes Maxwell’s demon, but also represents the 
fundamental physical limit of irreversible computation. However, its validity has been repeatedly questioned and its usefulness criticized17–22. From a technological perspective, energy dissipation per logic opera-tion in present-day silicon-based digital circuits is about a factor of 1,000 greater than the ultimate Landauer limit, but is predicted to quickly attain it within the next couple of decades23,24. Moreover, thermodynamic quantities on the scale of the thermal energy kT have been measured in mesoscopic systems such as colloidal particles in driven harmonic25 and non-harmonic optical traps26. 
To verify the erasure principle experimentally, we consider, following the original work of Landauer1, an overdamped colloidal particle in a double-well potential as a generic model of a one-bit memory. For this, we use a custom-built vertical optical tweezer that traps a silica bead (2mm in diameter) at the focus of a laser beam27,28. We create the double-well potential by focusing the laser alternately at two different positions with a high switching rate. The exact form of the potential is determined by the laser intensity and by the distance between the two focal points (Methods). As a result, the bead experiences an average potential U(x, t), whose measured form is plotted in Fig. 1 for different stages of the erasure cycle. When the barrier is high compared with the thermal energy, kT (Fig. 1a, f), the particle is trapped in one of the potential wells. By contrast, when the barrier is low (Fig. 1b), the particle can jump from one well to the other. The state of the memory is assigned the value 0 if the particle is in the left-hand well (x , 0) and 1 if the particle is in the right-hand well (x . 0). The memory is said to be erased when its state is reset to 1 (or alternatively 0) irrespective of its initial state. 
In our experiment, we follow a procedure which is quite similar to that discussed in detail in ref. 12. We start with the theoretical con-figuration in which the two wells are occupied with an equal probability of one-half. The initial entropy of the system is thus Si 5 kln(2). The memory is reset to 1 by first lowering the barrier height (Fig. 1b) and then applying a tilting force that brings the particle into the right-hand well (Fig. 1c–e). Finally, the barrier is increased to its initial value (Fig. 1f). At the end of this reset operation, the information initially contained in the memory has been erased and the final entropy is zero: Sf 5 0. Thus, the minimum entropy production of this erasure process is kln(2). The possibility of reaching this minimum depends on the timing of the procedure. The one used in our experiment is sketched in Fig. 2a. Specifically, we lower the barrier from a height larger than 8kT to 2.2kT over a time of 1 s by decreasing the power of the laser. This time is long compared with the relaxation time of the bead. We keep the barrier low for a time t, during which we apply a linearly increasing force of maximal amplitude Fmax, which corresponds to the tilt of the potential. We generate this force by displacing the cell containing the single bead with respect to the laser with the help of a piezoelectric motor. We close the erasure cycle by switching off the tilt and bringing the barrier back to its original height in again 1 s (Fig. 2a). A particle initially in memory state 0 will then be brought into state 1. The total duration of the erasure protocol is tcycle 5 t 1 2 s. Our two free parameters are the duration of the tilt, t, and its maximal amplitude, 
1Laboratoire de Physique, École Normale Supérieure, CNRS UMR5672 46 Allée d’Italie, 69364 Lyon, France. 2Physics Department and Research Center OPTIMAS, University of Kaiserslautern, 67663 Kaiserslautern, Germany. 3Department of Physics, University of Augsburg, 86135 Augsburg, Germany. {Present address: Dahlem Center for Complex Quantum Systems, Freie Universität Berlin, 14195 
 
Fmax (Methods). The second cycle in Fig. 2a corresponds to the reversed protocol, which brings the particle from state 1 to state 0 (Methods). 
We use a fast camera to record the successive positions of the bead during the erasure process. A typical measured trajectory of the particle for a transition 0 R 1 during a cycle is shown in Fig. 2c. A trajectory for the transition 1 R 1 is depicted in Fig. 2d. In this case there is an instantaneous jump to the other well induced by thermal noise, but the final state is 1. 
Thermodynamic quantities are stochastic variables at the micro-scopic level of our experiment, because thermal fluctuations cannot be neglected. The dissipated heat along a given trajectory, x(t), is given 
by the integral29 Q~{ 
ðtcycle 
0 dt _x(t)LU(x,t)=Lx. According to the laws 
of thermodynamics, the mean dissipated heat obtained by averaging over many trajectories is always larger than the entropy difference: 
ÆQæ $ 2TDS 5 kTln(2) 5 ÆQæLandauer. In practice, we average over situations in which the memory is either initially already in state 1 or is switched from state 0 to state 1. We typically average over more than 600 cycles. It is inconvenient to select randomly the initial con-figuration during two erasure cycles, so we treat the two cases indepen-dently. When the state of the memory is changed, we use a series of double cycles (Fig. 2a), which bring the bead from one well to the other, and back. In the opposite case, when the state of the memory is un-modified, we apply a series of double cycles containing a reinitialization phase (Fig. 2b). This series is useless in the erasure process itself, but is necessary to restart the measurement by keeping the bead in the initial well (Methods). We determine the dissipated heat during one erasure cycle as follows. We first note that the bead necessarily ends up in the initial state after completion of both double cycles. Because the modu-lation of the height of the barrier occurs on times much slower than the relaxation of the bead, it is quasi-reversible and does not contribute to the dissipated heat. We therefore only retain the contribution stemming from the external tilt, averaged over the cycles corresponding to the change of state and over the cycles in which the memory is unchanged. 
A key characteristic of the erasure process is its success rate, that is, the relative number of cycles bringing the bead in the expected well. Figure 3a shows the dependence of the erasure rate on the tilt amplitude, Fmax. For definiteness, we have kept the product Fmaxt constant. We observe that the erasure rate drops sharply at low amplitudes when the tilt force is too weak to push the bead over the barrier, as expected. For large values of Fmax, the erasure rate saturates at around 95%. This saturation reflects the finite size of the barrier and the possible occurrence of spontaneous thermal activation into the wrong well. An example of a distribution of the dissipated heat for the transition 0 R 1 is displayed in Fig. 3b. Owing to thermal fluctuations, the dissipated heat may be negative and maximum erasure below the Landauer limit may be achieved for individual realizations, but not on average16. 
Figure 3c shows the average dissipated heat, ÆQæ, over a large number of erasure protocols as a function of the duration of the cycle, for various success rates. For each cycle duration, t, we have set the amplitude, Fmax, of the tilt such that the erasure rate remains constant to a good approximation. For large durations, the mean dissipated heat does saturate at the Landauer limit. We observe, moreover, that incomplete erasure leads to less dissipated heat. For a success rate of r, the Landauer bound can be generalized to hQirLandauer~ kT½ln (2)zr ln (r)z(1{r) ln (1{r)". Thus, no heat needs to be pro-duced for r 5 0.5. In that case, the state of the memory is left unchanged by the protocol and the transformation is quasi-reversible. For ideal quasi-static erasure processes (t R ‘), the dissipated heat is equal to the Landauer value. For large but finite t, we can quantify the asymptotic approach to the Landauer limit by noting, following ref. 30, that ÆQæ 5 ÆQæLandauer 1 B/t, where B is a positive constant (Methods). For 
Waiting 
Reinitialization 
Cycle 1 
 
Cycle 2 Time 
0 
−0.5 
0.5 
10 20 Time (s) 
P os 
iti on 
 (μ m 
) 
−0.5 
0.5 
P os 
iti on 
 (μ m 
) 
0 10 20 Time (s) 
Time 
 
Time 
Power (mW) 
48 
15 
0 
External force 
Fmax 
−Fmax 
Lowering 
Power (mW) 
48 
15 
0 
External force 
Fmax 
−Fmax 
a c 
db 
τ 
τ 
Figure 2 | Erasure cycles and typical trajectories. a, Protocol used for the erasure cycles bringing the bead from the left-hand well (state 0) to the right-hand well (state 1), and vice versa. b, Protocol used to measure the heat for the cycles in which the bead does not change wells. The reinitialization is needed to restart the measurement, but is not a part of the erasure protocol (Methods). c, Example of a measured bead trajectory for the transition 0 R 1. d, Example of a measured bead trajectory for the transition 1 R 1. 
Position (μm) 
10 a b 
e f 
c d 
5 
0 
10 
5 
0 
10 
5 
0 
10 
5 
0 
0 0.5−0.5 
0 0.5−0.5 
0 0.5−0.5 
0 0.5−0.5 
0 0.5−0.5 
0 0.5−0.5 
10 
5 
0 
10 
5 
0 
 
 
 
 
Position (μm) 
Figure 1 | The erasure protocol used in the experiment. One bit of information stored in a bistable potential is erased by first lowering the central barrier and then applying a tilting force. In the figures, we represent the transition from the initial state, 0 (left-hand well), to the final state, 1 (right-hand well). We do not show the obvious 1 R 1 transition. Indeed the procedure is such that irrespective of the initial state, the final state of the particle is always 1. The potential curves shown are those measured in our experiment (Methods). 
 
 
shorter durations, we find excellent agreement with an exponential relaxation, ÆQæ 5 ÆQæLandauer 1 [Aexp(2t/tK) 1 1]B/t, with a relaxation time given by the Kramers time, tK, for the low barrier (Methods). Our experimental results indicate that the thermodynamic limit to informa-tion erasure, the Landauer bound, can be approached in the quasi-static regime but not exceeded. They hence demonstrate one of the fun-damental physical limitations of irreversible computation. Owing to the universality of thermodynamics, this limit is independent of the actual device, circuit or material used to implement the irreversible operation. 
METHODS SUMMARY We use a custom-built vertical optical tweezer made of an oil immersion objec-tive (363; numerical aperture, 1.4) that focuses a laser beam (wavelength, l 5 1,064 nm) to the diffraction limit for trapping glass beads27,28 (2mm in diameter). The beads are dispersed in bidistilled water at a very low concentration. The suspension is introduced in a disk-shaped cell (18 mm in diameter, 1 mm in depth), and a single bead is then trapped and moved away from the others. The position of the bead is tracked using a fast camera with a resolution of 108 nm per pixel, which after treatment gives the position with a precision greater than 10 nm. The trajectories of the bead are sampled at 502 Hz. The double-well potential is obtained by switching the laser at a rate of 10 kHz between two points separated by a distance df 5 1.45mm, which is kept fixed. The distance between the two minima of the double-well potential is 0.9mm. The height of the barrier is modulated by varying the power of the laser from IL 5 48 mW (barrier height, .8kT) to IL 5 15 mW (barrier height, 2.2kT). The external tilt is created by displacing the cell with respect to the laser with a piezoelectric motor, thus inducing a viscous flow. The viscous force is simply F 5 2cv, where c 5 1.89 3 10210 N s m21 is the 
amplitude of the viscous force is increased linearly during time t: F(t) 5 6Fmaxt/t. The heat dissipated by the tilt is 
Q~{ 
ðtcycle 
0 
dt F(t) _x(t)~+ ðt 
0 
dt Fmax(t=t) _x(t) 
The velocity is computed using the discretization _x(tzDt=2)<½x(tzDt){ x(t)"=Dt. 
Full Methods and any associated references are available in the online version of the paper at www.nature.com/nature. 
Received 11 October 2011; accepted 17 January 2012. 
1. Landauer, R. Irreversibility and heat generation in the computing process. IBM J. Res. Develop. 5, 183–191 (1961). 
2. Landauer, R.Dissipation and noise immunity incomputation and communication. Nature 335, 779–784 (1988). 
3. Lloyd, S. Ultimate physical limits to computation. Nature 406, 1047–1054 (2000). 4. Meindl, J. D. & Davis, J. A. The fundamental limit on binary switching energy for 
terascale integration. IEEE J. Solid-state Circuits 35, 1515–1516 (2000). 5. Plenio,M.B.& Vitelli, V. Thephysicsof forgetting: Landauer’s erasureprinciple and 
information theory. Contemp. Phys. 42, 25–60 (2001). 6. Brillouin, L. Science and Information Theory (Academic, 1956). 7. Leff, H. S. & Rex, A. F. Maxwell’s Demon 2: Entropy, Classical and Quantum 
Information, Computing (IOP, 2003). 8. Maruyama, K., Nori, F. & Vedral, V. The physics of Maxwell’s demon and 
information. Rev. Mod. Phys. 81, 1–23 (2009). 9. Szilard, L. On the decrease of entropy in a thermodynamic system by the 
intervention of intelligent beings. Z. Phys. 53, 840–856 (1929). 10. Toyabe, S., Sagawa, T., Ueda, M., Muneyuki, E. & Sano, M. Experimental 
demonstration of information-to-energy conversion and validation of the generalized Jarzynski equality. Nature Phys. 6, 988–992 (2010). 
11. Penrose,O. FoundationsofStatistical Mechanics:ADeductive Treatment (Pergamon, 1970). 
12. Bennett, C.H. The thermodynamicsof computation: a review. Int. J. Theor. Phys.21, 905–940 (1982). 
13. Bennett, C. H. Logical reversibility of computation. IBM J. Res. Develop. 17, 525–532 (1973). 
14. Shizume, K. Heat generation required by information erasure. Phys. Rev. E 52, 3495–3499 (1995). 
15. Piechocinska, P. Information erasure. Phys. Rev. A 61, 062314 (2000). 16. Dillenschneider, R. & Lutz, E. Memory erasure in small systems. Phys. Rev. Lett. 
102, 210601 (2009). 17. Earman, J. & Norton, J. D. EXORCIST XIV: The wrath of Maxwell’s demon. Part II. 
From Szilard to Landauer and beyond. Stud. Hist. Phil. Sci. B 30, 1–40 (1999). 18. Shenker, O. R. Logic and entropy. Preprint at Æhttp://philsci-archive.pitt.edu/115/æ 
(2000). 19. Maroney, O. J. E. The (absence of a) relationship between thermodynamic and 
logical reversibility. Studies Hist. Phil. Sci. B 36, 355–374 (2005). 20. Norton, J. D. Eaters of the lotus: Landauer’s principle and the return of Maxwell’s 
demon. Stud. Hist. Phil. Sci. B 36, 375–411 (2005). 21. Sagawa, T. & Ueda, M. Minimal energy cost for thermodynamic information 
processing: measurement and information erasure. Phys. Rev. Lett. 102, 250602 (2009). 
22. Norton, J. D. Waiting for Landauer. Stud. Hist. Phil. Sci. B 42, 184–198 (2011). 23. Frank, M. P. The physical limits of computing. Comput. Sci. Eng. 4, 16–26 (2002). 24. Pop, E. Energy dissipation and transport in nanoscale devices. Nano Res. 3, 
147–169 (2010). 25. Wang, G. M., Sevick, E. M., Mittag, E., Searles, D. J. & Evans, D. J. Experimental 
demonstration of violations of the second law of thermodynamics for small systems and short time scales. Phys. Rev. Lett. 89, 050601 (2002). 
26. Blickle, V., Speck, T., Helden, L., Seifert, U. & Bechinger, C. Thermodynamics of a colloidal particle in a time-dependent nonharmonic potential. Phys. Rev. Lett. 96, 070603 (2006). 
27. Jop, P., Petrosyan, A. & Ciliberto, S. Work and dissipation fluctuations near the stochastic resonance of a colloidal particle. Europhys. Lett. 81, 50005 (2008). 
28. Gomez-Solano, J. R., Petrosyan, A., Ciliberto, S., Chetrite, R. & Gawedzki, K. Experimental verificationof a modified fluctuation-dissipation relation for a micron-sized particle in a nonequilibrium steadystate. Phys. Rev. Lett. 103, 040601 (2009). 
29. Sekimoto, K. Stochastic Energetics (Springer, 2010). 30. Sekimoto, K. & Sasa, S. I. Complementarity relation for irreversible process derived 
from stochastic energetics. J. Phys. Soc. Jpn 6, 3326–3328 (1997). 
Acknowledgements This work was supported by the Emmy Noether Program of the DFG (contract no. LU1382/1-1), the Cluster of Excellence Nanosystems Initiative Munich (NIM), DAAD, and the Research Center Transregio 49 of the DFG. 
Author contributions All authors contributed substantially to this work. 
Author information Reprints and permissions information is available at www.nature.com/reprints. The authors declare no competing financial interests. Readers are welcome to comment on the online version of this article at www.nature.com/nature. Correspondence and requests for materials should be 
0 2 
80 
4 
3 
2 
1 
0 0 10 20 30 40 
0.15 
0.10 
0.05 
S uc 
ce ss 
 ra te 
 (% ) 
P (Q 
) 
90 
100 
4 6 Fmax (10−14 N) 
−2 0 2 4 Q (kT) 
〈Q 〉  ( kT 
) 
a 
b 
c 
τ (s) 
Figure 3 | Erasure rate and approach to the Landauer limit. a, Success rate of the erasure cycle as a function of the maximum tilt amplitude, Fmax, for constant Fmaxt. b, Heat distribution P(Q) for transition 0 R 1 with t 5 25 s and Fmax 5 1.89 3 10214 N. The solid vertical line indicates the mean dissipated heat, ÆQæ, and the dashed vertical line marks the Landauer limit, ÆQæLandauer. c, Mean dissipated heat for an erasure cycle as a function of protocol duration, t, measured for three different success rates, r: plus signs, r $ 0.90; crosses, r $ 0.85; circles, r $ 0.75. The horizontal dashed line is the Landauer limit. The continuous line is the fit with the function [Aexp(2t/tK) 1 1]B/t, where tK is the Kramers time for the low barrier (Methods). Error bars, 1 s.d. 
 
 
METHODS Experimental set-up. We use a custom-built vertical optical tweezer made of an oil immersion objective (363; numerical aperture, 1.4) that focuses a laser beam (wavelength, l 5 1,064 nm) to the diffraction limit for trapping glass beads27,28 
(2mm in diameter). The beads are dispersed in bidistilled water at a very low concentration. The suspension is introduced in a disk-shaped cell (18 mm in diameter, 1 mm in depth), and a single bead is then trapped and moved away from the others. This step is important to stop the trapped bead being perturbed by other Brownian particles during the measurement. The position of the bead is tracked using a fast camera with a resolution of 108 nm per pixel, which after treatment gives the position with a precision greater than 10 nm. The trajectories of the bead are sampled at 502 Hz. The double-well potential is obtained by switching the laser at a rate of 10 kHz between two points by a distance df 5 1.45 mm, which is kept fixed. The form of the potential, which is a function of df and the laser intensity, IL, can be determined in equilibrium by measuring the probability, P(x, IL) 5 Nexp[2U0(x, IL)/kT], of the bead being at position x, which implies that U0(x, IL) 5 2kTln[P(x, IL)/N] (Fig. 1a, b, f). The distribution P(x, IL) is estimated from about 106 samples. The measured U0(x, IL) are plotted in Fig. 1a, b, f and can be fitted by an eighth-order polynomial: U0(x,IL)~ 
P8 n~0 un(IL,df )xn. The dis-
tance between the two minima of the double-well potential is 0.9mm. The two wells are nearly symmetrical, with a maximum energy difference of 0.4kT. The height of the barrier, DU, is modulated by varying the power of the laser from IL 5 48 mW (barrier height, .8kT) to IL 5 15 mW (barrier height, 2.2kT). In equilibrium for a barrier of 8kT, the characteristic jumping time (Kramers time), tK 5 t0exp(DU/kT), between the two wells is about 3,000 s, which is much longer than any timescale in the experiment (t0 < 1 s in our experiment). 
The external tilt is created by displacing the cell with respect to the laser with a piezoelectric motor, thus inducing a viscous flow. The viscous force is simply F 5 2cv, where c 5 1.89 3 10210 N s m21 is the coefficient of friction and v is the velocity of the cell. In the erasure protocol, the amplitude of the viscous force is increased linearly during time t: F(t) 5 6Fmaxt/t. In Fig. 1c–e, we plot U(x, t) 5 U0(x, IL) 2 F(t)x for IL 5 15 mW and for three different values of t. The reinitialization procedure shown in Fig. 2b is necessary to displace the cell to its initial position, but it does not contribute to the erasure process. We note that, unlike the useful erasure cycles, this reinitialization is performed when the barrier is high. Thus, the bead remains always in the same well. Heat measurements. The heat dissipated by the tilt is 
Q~{ 
ðtcycle 
0 
dt F(t) _x(t)~+ ðt 
0 
dt Fmax(t=t) _x(t) 
The velocity is computed using the discretization _x(tzDt=2)<½x(tzDt){x(t)"=Dt. To characterize the asymptotic approach to the Landauer bound we use the fact that, in the quasi-static limit (t R ‘), the mean work, ÆWæ, can be expressed in terms of the free energy difference,DF, as hWi<DFzB=t (ref. 30). According to the first law of thermodynamics, ÆDUæ 5 ÆWæ 2 ÆQæ 5 0 for a cycle, and we therefore find that DF 5 2TDS and hQi~hWi<kT ln (2)zB=t. This asymptotic result is generic and does not depend on the details of the potential. For shorter times, we find an exponential relaxation of the form ÆQæ 5 kTln(2) 1 [Aexp(2t/tK) 1 1]B/t, where tK is the Kramers time for the low barrier. The presence of the characteristic Kramers time can be understood by noting that cycles that last more than a few multiples of tK are very efficient for erasure because the probability that a jump to the right-hand well occurs by thermal activation is greatly increased. 
 