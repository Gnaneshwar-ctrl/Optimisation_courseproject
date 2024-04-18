*Sets
*    Reservoirs / r1, r2, r3, r4, r5 /
*    TimePeriods / t1, t2, t3, ..., tn /;  ! Define the time periods here

*Parameters
*    a0(Reservoirs), a1(Reservoirs), a2(Reservoirs), a3(Reservoirs),  
*    b0(Reservoirs), b1(Reservoirs), b2(Reservoirs), b3(Reservoirs),  
*    drn(Reservoirs), evaporated(Reservoirs), PDEM(TimePeriods),         
*    RELS(Reservoirs, Reservoirs, TimePeriods), withdw(Reservoirs);

*Variables
*    PW(Reservoirs, TimePeriods),                                      
*    H(Reservoirs, TimePeriods),                                       
*    S(Reservoirs, TimePeriods),                                       
*    A(Reservoirs, TimePeriods),                                       
*    obj;                                                             

*Positive Variables PW, H, S, A;

*Equations
*    HeadVolume(Reservoirs, TimePeriods),                              
*    HeadArea(Reservoirs, TimePeriods),                                
*    WaterBalance(Reservoirs, TimePeriods),                           
*    ObjectiveFunction;                                            

*HeadVolume(Reservoirs, TimePeriods).. 
*    S(Reservoirs, TimePeriods) =e= a3(Reservoirs)*power(H(Reservoirs, TimePeriods),3) +
*                                  a2(Reservoirs)*power(H(Reservoirs, TimePeriods),2) +
*                                  a1(Reservoirs)*H(Reservoirs, TimePeriods) + a0(Reservoirs);

*HeadArea(Reservoirs, TimePeriods).. 
*   A(Reservoirs, TimePeriods) =e= b3(Reservoirs)*power(H(Reservoirs, TimePeriods),3) +
*                                  b2(Reservoirs)*power(H(Reservoirs, TimePeriods),2) +
*                                  b1(Reservoirs)*H(Reservoirs, TimePeriods) + b0(Reservoirs);

*WaterBalance(Reservoirs, TimePeriods-1).. 
*    S(Reservoirs, TimePeriods-1) + drn(Reservoirs) + sum((RELS(un, Reservoirs, TimePeriods))) = S(Reservoirs, TimePeriods) + sum((RELS(Reservoirs, ln, TimePeriods))) + withdw(Reservoirs) + evaporated(Reservoirs)*A(Reservoirs, TimePeriods);

*ObjectiveFunction.. 
*    obj =e= sum((sum(PW(Reservoirs, TimePeriods)))/PDEM(TimePeriods));

*Model OptimizationModel /all/;
    
*Option NLP = Ipopt;
*OptimizationModel.OptFile = 1;
*Solve OptimizationModel using NLP maximizing obj;

*Display PW.L, H.L, S.L, A.L, obj.L;

*** for single resirviour (part1)
* SETS      i / 1, 2, 3/;

* SCALAR    r RELEASE   /10.0/;

* PARAMETER
*    a(i) /1 6.0, 2 7.0, 3 8.0/
*    b(i) /1 -1.0, 2 -1.5, 3 -0.5/;

* VARIABLES obj OBJECTIVE;

* POSITIVE VARIABLES x(i) USE, s DOWNSTREAM FLOW; S.lo=2.0;

* EQUATIONS objective, cap;

* objective..obj =E= SUM(i,a(i)*x(i)+b(i)*x(i)**2); cap..sum(i,x(i))+s-r =E= 0.0;

* MODEL user /ALL/ ;

* SOLVE user USING NLP MAXIMIZE obj ;
* FILE res /WaterUser.txt/

* PUT res
* PUT 'Release         ', PUT r,
* PUT 'Downstream flow ', PUT s.l,
* PUT 'Objective       ', PUT obj.l, PUT //
* PUT 'i                  x(i) ' PUT /
* loop( (i), PUT i.TL,  PUT x.l(i), PUT /)
* PUT //, 'd(obj)/dr = ', PUT cap.m, PUT //

* *** for single resirviour (part2)
* SETS
* i /1*20/;
* SCALAR h0  Minimum Elevation  /758/;

* PARAMETER
* h(i) /
* 1 759
* 2 767
* 3 771
* 4 783
* 5 786
* 6 795
* 7 802
* 8 810
* 9 814
* 10 827
* 11 838
* 12 839
* 13 850
* 14 855
* 15 863
* 16        867
* 17        875
* 18        882
* 19        891
* 20        900
* /;

* PARAMETER S_hat(i) /
* 1 0
* 2 78
* 3 118
* 4 321
* 5 405
* 6 779
* 7 1204
* 8 1885
* 9 2297
* 10 3921
* 11 5585
* 12 5750
* 13 7717
* 14 8690
* 15 10336
* 16 11198
* 17 13003
* 18 14676
* 19 16961
* 20 19458 /;

* POSITIVE VARIABLES
* a, b;
* b.up=100;
* a.up=100;
* VARIABLES
* e(i), obj;
* EQUATIONS residual(i), objective;
* residual(i).. e(i) =E= a*(h(i)-h0)**b - S_hat(i); objective.. obj=E=sum(i,power(e(i),2));
* MODEL hvs /ALL/;
* SOLVE hvs USING NLP MINIMIZING obj;
* FILE res /River1a.txt/;
* PUT res
* PUT "Coefficients(a and b) in formula S = a*(h-h0)**b"/ ; PUT"a=",a.L," b=",b.L//;
* PUT "No. Elevation Volume(real) Volume(calc)"/; LOOP(i,PUT i.TL, h(i), S_hat(i), ((a.L*(h(i)-h0)**b.L))/;);

*** for single resirviour (part3)
SCALAR K      /19500/;
SCALAR S_min  /5500/;
SCALAR beg_S  /15000/;
SETS
t   / t1*t24/;

PARAMETER
Q(t) inflow (million m3)
* normal
/
t1  426
t2  399
t3  523
t4  875
t5 2026
t6 3626
t7 2841
t8 1469
t9  821
t10 600
t11 458
t12 413
t13 426
t14 399
t15 523
t16 875
t17 2026
t18 3626
t19 2841
t20 1469
t21 821
t22 600
t23 458
t24 413
/;

Parameter
D(t) demand (million m3)
/
t1  1699.5
t2  1388.2
t3  1477.6
t4  1109.4
t5   594.6
t6   636.6
t7  1126.1
t8  1092.0
t9   510.8
t10  868.5
t11 1049.8
t12 1475.5
t13 1699.5
t14 1388.2
t15 1477.6
t16 1109.4
t17  594.6
t18  636.6
t19 1126.1
t20 1092.0
t21  510.8
t22  868.5
t23 1049.8
t24 1475.5
/;

Parameter
a(t) evaporation coefficient
/
t1  0.000046044
t2  0.00007674
t3  0.000180339
t4  0.000391374
t5  0.000602409
t6  0.000648453
t7  0.000656127
t8  0.000548691
t9  0.0003837
t10 0.000145806
t11 0.000103599
t12 0.000053718
t13 0.000046044
t14 0.00007674
t15 0.000180339
t16 0.000391374
t17 0.000602409
t18 0.000648453
t19 0.000656127
t20 0.000548691
t21 0.0003837
t22 0.000145806
t23 0.000103599
t24 0.000053718
/;
Parameter
b(t) evaporation coefficient
/
t1   1.92
t2   3.2
t3   7.52
t4  16.32
t5  25.12
t6  27.04
t7  27.36
t8  22.88
t9  16.00
t10  6.08
t11  4.32
t12  2.24
t13   1.92
t14  3.2
t15  7.52
t16 16.32
t17 25.12
t18 27.04
t19 27.36
t20 22.88
t21 16.00
t22  6.08
t23  4.32
t24  2.24
/;
POSITIVE VARIABLES
S(t), R(t);
S.UP(t)=K;
S.LO(t)=S_min;
VARIABLES
obj;
EQUATIONS  objective, balance(t);
objective.. obj =E= SUM(t,power((R(t)-D(t)),2));
balance(t).. (1+a(t))*S(t) =E= (1-a(t))*beg_S $(ord(t) EQ 1) + (1-a(t))*S(t-1)$(ord(t) GT 1) + Q(t) - R(t)- b(t);
MODEL Reservoir / ALL /;
SOLVE Reservoir USING NLP MINIMIZING obj;
FILE res /River1b.txt/;
PUT res
PUT "(mln.m3) (mln.m3)(mln.m3)(mln.m3)"/;
PUT " Storage Input Release Demand"/;
PUT "t0  ",beg_S/;
LOOP(t,PUT t.TL, S.L(t), Q(t), R.L(t), D(t) /;);