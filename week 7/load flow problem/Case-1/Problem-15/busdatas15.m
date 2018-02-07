% Returns Initial Bus datas of the system...

function busdt = busdatas15(num)

% Type....
% 1 - Slack Bus..
% 2 - PV Bus..
% 3 - PQ Bus..



%        |Bus|Type|  Vsp   | Theta  |  Pgi     |  Qgi   |     Pli  |   Qli   |    Qmin |    Qmax |
busdat38=[1	1	1	0       0	0	0           0           0	0
            2	3	1	0       0	0	0.101984595	0.061190757	0	0
            3	3	1	0       0	0	0.102383984	0.045503993	0	0
            4	3	1	0       0	0	0.145639729	0.097093153	0	0
            5	3	1	0       0	0	0.061190757	0.030595378	0	0
            6	3	1	0       0	0	0.068255989	0.022751996	0	0
            7	3	1	0       0	0	0.242732881	0.121366441	0	0
            8	3	1	0       0	0	0.242732881	0.121366441	0	0
            9	3	1	0       0	0	0.068255989	0.022751996	0	0
            10	3	1	0       0	0	0.072819864	0.024273288	0	0
            11	3	1	0       0	0	0.054614898	0.036409932	0	0
            12	3	1	0       0	0	0.061190757	0.035694608	0	0
            13	3	1	0       0	0	0.072819864	0.042478254	0	0
            14	3	1	0       0	0	0.122381513	0.081587676	0	0
            15	3	1	0       0	0	0.068255989	0.022751996	0	0
            16	3	1	0       0	0	0.072819864	0.024273288	0	0
            17	3	1	0       0	0	0.072819864	0.024273288	0	0
            18	3	1	0       0	0	0.102383984	0.045503993	0	0
            19	3	1	0       0	0	0.091786135	0.040793838	0	0
            20	3	1	0       0	0	0.109229797	0.048546576	0	0
            21	3	1	0       0	0	0.102383984	0.045503993	0	0
            22	3	1	0       0	0	0.091786135	0.040793838	0	0
            23	3	1	0       0	0	0.109229797	0.06068322	0	0
            24	3	1	0       0	0	0.509739051	0.242732881	0	0
            25	3	1	0       0	0	0.509739051	0.242732881	0	0
            26	3	1	0       0	0	0.072819864	0.03034161	0	0
            27	3	1	0       0	0	0.068255989	0.028439996	0	0
            28	3	1	0       0	0	0.072819864	0.024273288	0	0
            29	3	1	0       0	0	0.145639729	0.084956509	0	0
            30	3	1	0       0	0	0.242732881	0.728198644	0	0
            31	3	1	0       0	0	0.152976892	0.071389216	0	0
            32	3	1	0       0	0	0.214167648	0.101984595	0	0
            33	3	1	0       0	0	0.072819864	0.048546576	0	0
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