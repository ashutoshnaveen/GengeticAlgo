% Returns Initial Bus datas of the system...

function busdt = busdatas10(num)

% Type....
% 1 - Slack Bus..
% 2 - PV Bus..
% 3 - PQ Bus..



%        |Bus|Type|  Vsp   | Theta  |  Pgi     |  Qgi   |     Pli  |   Qli   |    Qmin |    Qmax |

busdat38=[1	1	1	0       0	0	0           0           0	0
            2	3	1	0       0	0	0.102092004	0.061255203	0	0
            3	3	1	0       0	0	0.102212094	0.045427597	0	0
            4	3	1	0       0	0	0.142478019	0.094985346	0	0
            5	3	1	0       0	0	0.061255203	0.030627601	0	0
            6	3	1	0       0	0	0.068141396	0.022713799	0	0
            7	3	1	0       0	0	0.237463365	0.118731683	0	0
            8	3	1	0       0	0	0.237463365	0.118731683	0	0
            9	3	1	0       0	0	0.068141396	0.022713799	0	0
            10	3	1	0       0	0	0.07123901	0.023746337	0	0
            11	3	1	0       0	0	0.053429257	0.035619505	0	0
            12	3	1	0       0	0	0.061255203	0.035732202	0	0
            13	3	1	0       0	0	0.07123901	0.041556089	0	0
            14	3	1	0       0	0	0.122510405	0.081673604	0	0
            15	3	1	0       0	0	0.068141396	0.022713799	0	0
            16	3	1	0       0	0	0.07123901	0.023746337	0	0
            17	3	1	0       0	0	0.07123901	0.023746337	0	0
            18	3	1	0       0	0	0.102212094	0.045427597	0	0
            19	3	1	0       0	0	0.091882804	0.040836802	0	0
            20	3	1	0       0	0	0.106858514	0.047492673	0	0
            21	3	1	0       0	0	0.102212094	0.045427597	0	0
            22	3	1	0       0	0	0.091882804	0.040836802	0	0
            23	3	1	0       0	0	0.106858514	0.059365841	0	0
            24	3	1	0       0	0	0.498673067	0.237463365	0	0
            25	3	1	0       0	0	0.498673067	0.237463365	0	0
            26	3	1	0       0	0	0.07123901	0.029682921	0	0
            27	3	1	0       0	0	0.068141396	0.028392248	0	0
            28	3	1	0       0	0	0.07123901	0.023746337	0	0
            29	3	1	0       0	0	0.142478019	0.083112178	0	0
            30	3	1	0       0	0	0.237463365	0.712390096	0	0
            31	3	1	0       0	0	0.153138007	0.071464403	0	0
            32	3	1	0       0	0	0.214393209	0.102092004	0	0
            33	3	1	0       0	0	0.07123901	0.047492673	0	0
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