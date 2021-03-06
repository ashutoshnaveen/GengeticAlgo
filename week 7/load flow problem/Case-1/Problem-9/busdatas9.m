% Returns Initial Bus datas of the system...

function busdt = busdatas9(num)

% Type....
% 1 - Slack Bus..
% 2 - PV Bus..
% 3 - PQ Bus..



%        |Bus|Type|  Vsp   | Theta  |  Pgi     |  Qgi   |     Pli  |   Qli   |    Qmin |    Qmax |

 busdat38 =[1	1   1	0       0	0	0           0           0	0
            2	3	1	0       0	0	0.100907946	0.060544768	0	0
            3	3	1	0       0	0	0.095483453	0.04243709	0	0
            4	3	1	0       0	0	0.12618166	0.084121107	0	0
            5	3	1	0       0	0	0.060544768	0.030272384	0	0
            6	3	1	0       0	0	0.063655635	0.021218545	0	0
            7	3	1	0       0	0	0.210302767	0.105151383	0	0
            8	3	1	0       0	0	0.210302767	0.105151383	0	0
            9	3	1	0       0	0	0.063655635	0.021218545	0	0
            10	3	1	0       0	0	0.06309083	0.021030277	0	0
            11	3	1	0       0	0	0.047318122	0.031545415	0	0
            12	3	1	0       0	0	0.060544768	0.035317781	0	0
            13	3	1	0       0	0	0.06309083	0.036802984	0	0
            14	3	1	0       0	0	0.121089535	0.080726357	0	0
            15	3	1	0       0	0	0.063655635	0.021218545	0	0
            16	3	1	0       0	0	0.06309083	0.021030277	0	0
            17	3	1	0       0	0	0.06309083	0.021030277	0	0
            18	3	1	0       0	0	0.095483453	0.04243709	0	0
            19	3	1	0       0	0	0.090817152	0.040363178	0	0
            20	3	1	0       0	0	0.094636245	0.042060553	0	0
            21	3	1	0       0	0	0.095483453	0.04243709	0	0
            22	3	1	0       0	0	0.090817152	0.040363178	0	0
            23	3	1	0       0	0	0.094636245	0.052575692	0	0
            24	3	1	0       0	0	0.44163581	0.210302767	0	0
            25	3	1	0       0	0	0.44163581	0.210302767	0	0
            26	3	1	0       0	0	0.06309083	0.026287846	0	0
            27	3	1	0       0	0	0.063655635	0.026523181	0	0
            28	3	1	0       0	0	0.06309083	0.021030277	0	0
            29	3	1	0       0	0	0.12618166	0.073605968	0	0
            30	3	1	0       0	0	0.210302767	0.6309083	0	0
            31	3	1	0       0	0	0.151361919	0.070635562	0	0
            32	3	1	0       0	0	0.211906687	0.100907946	0	0
            33	3	1	0       0	0	0.06309083	0.042060553	0	0
            34	3	1	0       0	0	0           0           0	0
            35	3	1	0       0	0	0           0           0	0
            36	3	1	0       0	0	0           0           0	0
            37	3	1	0       0	0	0           0       	0	0
            38	3	1	0       0	0	0           0           0	0

];

switch num
   case 38
         busdt = busdat38;
        
end