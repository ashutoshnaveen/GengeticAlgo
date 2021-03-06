% Returns Initial Bus datas of the system...

function busdt = busdatas13(num)

% Type....
% 1 - Slack Bus..
% 2 - PV Bus..
% 3 - PQ Bus..



%        |Bus|Type|  Vsp   | Theta  |  Pgi     |  Qgi   |     Pli  |   Qli   |    Qmin |    Qmax |

busdat38 =[1	1	1	0       0	0	0           0           0	0
            2	3	1	0       0	0	0.103559513	0.062135708	0	0
            3	3	1	0       0	0	0.103860742	0.04616033	0	0
            4	3	1	0       0	0	0.150107711	0.100071808	0	0
            5	3	1	0       0	0	0.062135708	0.031067854	0	0
            6	3	1	0       0	0	0.069240495	0.023080165	0	0
            7	3	1	0       0	0	0.250179519	0.125089759	0	0
            8	3	1	0       0	0	0.250179519	0.125089759	0	0
            9	3	1	0       0	0	0.069240495	0.023080165	0	0
            10	3	1	0       0	0	0.075053856	0.025017952	0	0
            11	3	1	0       0	0	0.056290392	0.037526928	0	0
            12	3	1	0       0	0	0.062135708	0.03624583	0	0
            13	3	1	0       0	0	0.075053856	0.043781416	0	0
            14	3	1	0       0	0	0.124271416	0.08284761	0	0
            15	3	1	0       0	0	0.069240495	0.023080165	0	0
            16	3	1	0       0	0	0.075053856	0.025017952	0	0
            17	3	1	0       0	0	0.075053856	0.025017952	0	0
            18	3	1	0       0	0	0.103860742	0.04616033	0	0
            19	3	1	0       0	0	0.093203562	0.041423805	0	0
            20	3	1	0       0	0	0.112580783	0.050035904	0	0
            21	3	1	0       0	0	0.103860742	0.04616033	0	0
            22	3	1	0       0	0	0.093203562	0.041423805	0	0
            23	3	1	0       0	0	0.112580783	0.06254488	0	0
            24	3	1	0       0	0	0.52537699	0.250179519	0	0
            25	3	1	0       0	0	0.52537699	0.250179519	0	0
            26	3	1	0       0	0	0.075053856	0.03127244	0	0
            27	3	1	0       0	0	0.069240495	0.028850206	0	0
            28	3	1	0       0	0	0.075053856	0.025017952	0	0
            29	3	1	0       0	0	0.150107711	0.087562832	0	0
            30	3	1	0       0	0	0.250179519	0.750538557	0	0
            31	3	1	0       0	0	0.155339269	0.072491659	0	0
            32	3	1	0       0	0	0.217474977	0.103559513	0	0
            33	3	1	0       0	0	0.075053856	0.050035904	0	0
            34	3	1	0       0	0	0           0           0	0
            35	3	1	0       0	0	0           0           0	0
            36	3	1	0       0	0	0           0           0	0
            37	3	1	0       0	0	0           0           0	0
            38	3	1	0       0	0	0           0           0	0

];

switch num
   case 38
         busdt = busdat38;%busdt(:,7:8)=busdt(:,7:8)*1.5;
%        busdt(:,7:8)=busdt(:,7:8)/1000;
    
        
end