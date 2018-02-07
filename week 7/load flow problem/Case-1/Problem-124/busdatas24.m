% Returns Initial Bus datas of the system...

function busdt = busdatas24(num)

% Type....
% 1 - Slack Bus..
% 2 - PV Bus..
% 3 - PQ Bus..



%        |Bus|Type|  Vsp   | Theta  |  Pgi     |  Qgi   |     Pli  |   Qli   |    Qmin |    Qmax |

busdat38 =[1	1	1	0       0	0	0           0           0	0
            2	3	1	0       0	0	0.091333278	0.054799967	0	0
            3	3	1	0       0	0	0.075405786	0.033513683	0	0
            4	3	1	0       0	0	0.102045331	0.068030221	0	0
            5	3	1	0       0	0	0.054799967	0.027399983	0	0
            6	3	1	0       0	0	0.050270524	0.016756841	0	0
            7	3	1	0       0	0	0.170075552	0.085037776	0	0
            8	3	1	0       0	0	0.170075552	0.085037776	0	0
            9	3	1	0       0	0	0.050270524	0.016756841	0	0
            10	3	1	0       0	0	0.051022666	0.017007555	0	0
            11	3	1	0       0	0	0.038266999	0.025511333	0	0
            12	3	1	0       0	0	0.054799967	0.031966647	0	0
            13	3	1	0       0	0	0.051022666	0.029763222	0	0
            14	3	1	0       0	0	0.109599934	0.073066623	0	0
            15	3	1	0       0	0	0.050270524	0.016756841	0	0
            16	3	1	0       0	0	0.051022666	0.017007555	0	0
            17	3	1	0       0	0	0.051022666	0.017007555	0	0
            18	3	1	0       0	0	0.075405786	0.033513683	0	0
            19	3	1	0       0	0	0.08219995	0.036533311	0	0
            20	3	1	0       0	0	0.076533998	0.03401511	0	0
            21	3	1	0       0	0	0.075405786	0.033513683	0	0
            22	3	1	0       0	0	0.08219995	0.036533311	0	0
            23	3	1	0       0	0	0.076533998	0.042518888	0	0
            24	3	1	0       0	0	0.357158659	0.170075552	0	0
            25	3	1	0       0	0	0.357158659	0.170075552	0	0
            26	3	1	0       0	0	0.051022666	0.021259444	0	0
            27	3	1	0       0	0	0.050270524	0.020946052	0	0
            28	3	1	0       0	0	0.051022666	0.017007555	0	0
            29	3	1	0       0	0	0.102045331	0.059526443	0	0
            30	3	1	0       0	0	0.170075552	0.510226656	0	0
            31	3	1	0       0	0	0.136999917	0.063933295	0	0
            32	3	1	0       0	0	0.191799884	0.091333278	0	0
            33	3	1	0       0	0	0.051022666	0.03401511	0	0
            34	3	1	0       0	0	0           0           0	0
            35	3	1	0       0	0	0           0           0	0
            36	3	1	0       0	0	0           0           0	0
            37	3	1	0       0	0	0           0           0	0
            38	3	1	0       0	0	0           0           0	0

];

switch num
   case 38
         busdt = busdat38;
        
end