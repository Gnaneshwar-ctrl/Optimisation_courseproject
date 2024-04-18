SET n nodes
   / Supply_1, Supply_2,
     Simple_1*Simple_5,
     Divert_1, Divert_2,
     Res_1, Res_2,
     Outlet /;
     
ALIAS(n,n1);

SET
nn(n)     Simple nodes /Simple_1*Simple_5/
ns(n)     Supply nodes /Supply_1, Supply_2/
nr(n)     Water user nodes /Divert_1, Divert_2, Outlet/
nrr(n)    Irrigation nodes /Divert_1, Divert_2/
nl(n)     Reservoir nodes  /Res_1, Res_2/;


SET n_from_n(n,n1)  node n gets water from node n1 (any node)
/ Res_1.Supply_1,
  Res_2.Supply_2,
  Simple_1.Res_1,
  Simple_1.Res_2,
  Simple_2.Simple_1,
  Divert_1.Simple_2,
  Simple_3.Simple_2,
  Simple_3.Divert_1,
  Simple_4.Simple_3,
  Divert_2.Simple_4,
  Simple_5.Simple_4,
  Simple_5.Divert_2,
  Outlet.Simple_5 /;
  
SET n_to_nr(n,n1) node n diverts water to node n1 (user node)
/ Simple_2.Divert_1,
  Simple_4.Divert_2,
  Simple_5.Outlet /;
  
SET t months /Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec /;

PARAMETER beg_S(n) initial storage
/ Res_1  1000,
Res_2 300 /;

PARAMETER Ret(n) return flow coefficients
/ Divert_1  0.5,
  Divert_2  0.5,
Outlet 0.0 /;

TABLE Supply(n,t) water supplies (m3 per sec)
            Jan     Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
Supply_1    128     125 234 360 541 645 807 512 267 210 181 128
Supply_2    39      39  52  121 168 144 105 78  49  44  45  39;

TABLE Demand(n,t) water demands (m3 per sec)
            Jan Feb Mar Apr     May     Jun     Jul     Aug     Sep     Oct Nov Dec
Divert_1    0   0   0   64.5    109.8   184.4   243.7   200.9   99.5    0   0   0
Divert_2    0   0   0   13.5    15.0    22.1    26.0    24.9    13.0    0   0   0
Outlet      500 500 500 100     100     100     100     500     500     500 500 500;

POSITIVE VARIABLES
Divert(n,t)   Diversions
Q(n,t)        Inflows
R(n,t)        Releases
S(n,t)        Storages;

VARIABLE obj;

* Upper bound on diversions
Divert.up(n,t) = Demand(n,t);

* Upper bound of reservoirs
S.up('Res_1' ,t    )    = 1000;
S.up('Res_2' ,t    )    = 300;

* Final storage of reservoirs
S.lo('Res_1' ,'Dec' )    = 1000;
S.lo('Res_2' ,'Dec' )    = 300;

EQUATIONS
R_no(n,t) Simple node
R_ns(n,t) Source node
R_nr(n,t) Irrigation node
R_nl(n,t) Reservoir node
R_nn(n,t) Simple node
Objective;

* Simple node:  Release = Inflow
R_no(n,t)$(nn(n)).. R(n,t) =e= Q(n,t);
* Source node: Release = Supply
R_ns(n,t)$(ns(n)).. R(n,t) =e= Supply(n,t);
* Irrigation node: Release = Return Flow = Percent of Diversion
R_nr(n,t)$(nr(n)).. R(n,t) =e= ret(n)*Divert(n,t);
* Reservoir node: Release = Mass Balance
R_nl(n,t)$(nl(n)).. S(n,t) =e= beg_S(n)$(ord(t) EQ 1) + S(n,t-1)$(ord(t) GT 1) + Q(n,t)-R(n,t);
* Simple node: Inflow = Sum of Releases from Upstream - Sum of Diversions
R_nn(n,t).. Q(n,t) =e= sum(n1$(n_from_n(n,n1)),R(n1,t)) - sum(n1$(n_to_nr(n,n1)),Divert(n1,t));
*Sum over Irrigation Diversions/Demands + Downstream Flow/Demand
objective.. obj =e= sum(t,sum(n$nr(n), (Divert(n,t)/(Demand(n,t)+1e-9))));

MODEL Lakes /all/;
SOLVE Lakes USING LP MAXIMIZING obj;

file res /River2.txt/
put res;
put "Node Divert_1 Demand_1 Divert_2 Demand_2 Outlet Demand_O"/;
loop((t),put t.TL:6, Divert.L('Divert_1',t):9.2, Demand('Divert_1',t):9.2,Divert.L('Divert_2',t):9.2, Demand('Divert_2',t):9.2, Divert.L('Outlet',t) :9.2, Demand('Outlet',t) :9.2 /;);
put /"Reservoirs  "/;
put "Reservoir 1 Reservoir 2 "/;
put "Inflow Storage Release Inflow Storage Release "/; 
put "Q-1 S-1 R-1 Q-2 S-2 R-2 "/;
loop((t),put t.TL:8, Q.L('Res_1',t):8.1, S.L('Res_1',t):8.1, R.L('Res_1',t):8.1,Q.L('Res_2',t):8.1, S.L('Res_2',t):8.1, R.L('Res_2',t):8.1 /;);