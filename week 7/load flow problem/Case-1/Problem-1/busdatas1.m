% Returns Initial Bus datas of the system...

function busdt = busdatas1(num)

% Type....
% 1 - Slack Bus..
% 2 - PV Bus..
% 3 - PQ Bus..



%        |Bus|Type|  Vsp   | Theta  |  Pgi     |  Qgi   |     Pli  |   Qli   |    Qmin |    Qmax |

 busdat38  =[   1	1       1	0       0       0       0		0           0       0
                2	3       1	0       0       0	0.082401439	0.049440863	0       0
                3	3       1	0       0       0	0.073922919	0.032854631	0       0
                4	3       1	0       0       0	0.102514338	0.068342892	0       0
                5	3       1	0       0       0	0.049440863	0.024720432	0       0
                6	3       1	0       0       0	0.049281946	0.016427315	0       0
                7	3       1	0       0       0	0.170857229	0.085428615	0       0
                8	3       1	0       0       0	0.170857229	0.085428615	0       0
                9	3       1	0       0       0	0.049281946	0.016427315	0       0
                10	3       1	0       0       0	0.051257169	0.017085723	0       0
                11	3       1	0       0       0	0.038442877	0.025628584	0       0
                12	3       1	0       0       0	0.049440863	0.028840504	0       0
                13	3       1	0       0       0	0.051257169	0.029900015	0       0
                14	3       1	0       0       0	0.098881727	0.065921151	0       0
                15	3       1	0       0       0	0.049281946	0.016427315	0       0
                16	3       1	0       0       0	0.051257169	0.017085723	0       0
                17	3       1	0       0       0	0.051257169	0.017085723	0       0
                18	3       1	0       0       0	0.073922919	0.032854631	0       0
                19	3       1	0       0       0	0.074161295	0.032960576	0       0
                20	3       1	0       0       0	0.076885753	0.034171446	0       0
                21	3       1	0       0       0	0.073922919	0.032854631	0       0
                22	3       1	0       0       0	0.074161295	0.032960576	0       0
                23	3       1	0       0       0	0.076885753	0.042714307	0       0
                24	3       1	0       0       0	0.358800181	0.170857229	0       0
                25	3       1	0       0       0	0.358800181	0.170857229	0       0
                26	3       1	0       0       0	0.051257169	0.021357154	0       0
                27	3       1	0       0       0	0.049281946	0.020534144	0       0
                28	3       1	0       0       0	0.051257169	0.017085723	0       0
                29	3       1	0       0       0	0.102514338	0.05980003	0       0
                30	3       1	0       0       0	0.170857229	0.512571688	0       0
                31	3       1	0       0       0	0.123602159	0.057681007	0       0
                32	3       1	0       0       0	0.173043022	0.082401439	0       0
                33	3       1	0       0       0	0.051257169	0.034171446	0   	0
                34	3       1	0       0       0	0	        0	        0       0
                35	3       1	0       0       0	0	        0           0       0
                36	3       1	0       0       0	0           0           0       0
                37	3       1	0       0       0	0           0           0       0
                38	3       1	0       0       0	0           0           0       0];

switch num
   case 38
         busdt = busdat38;
    
        
end