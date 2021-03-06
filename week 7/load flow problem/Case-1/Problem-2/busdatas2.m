% Returns Initial Bus datas of the system...

function busdt = busdatas2(num)

% Type....
% 1 - Slack Bus..
% 2 - PV Bus..
% 3 - PQ Bus..



%        |Bus|Type|  Vsp   | Theta  |  Pgi     |  Qgi   |     Pli  |   Qli   |    Qmin |    Qmax |

 busdat38  =[1     1       1	0       0	0	0           0            0       0
              2     3       1	0       0	0	0.078141422	0.046884853	 0       0
              3     3       1	0       0	0	0.073458155	0.032648069	 0       0
              4     3       1	0       0	0	0.102737929	0.068491953	 0       0
              5     3       1	0       0	0	0.046884853	0.023442427	 0	     0
              6     3       1	0       0	0	0.048972104	0.016324035	 0       0
              7     3       1	0       0	0	0.171229881	0.085614941  0       0
            8       3       1	0       0	0	0.171229881	0.085614941	0       0
            9       3       1	0       0	0	0.048972104	0.016324035	0       0
            10      3       1	0       0	0	0.051368964	0.017122988	0       0
            11      3       1	0       0	0	0.038526723	0.025684482	0       0
            12      3       1	0       0	0	0.046884853	0.027349498	0       0
            13      3       1	0       0	0	0.051368964	0.029965229	0       0
            14      3       1	0       0	0	0.093769707	0.062513138	0       0
            15      3       1	0       0	0	0.048972104	0.016324035	0       0
            16      3       1	0       0	0	0.051368964	0.017122988	0       0
            17      3       1	0       0	0	0.051368964	0.017122988	0	0
            18      3       1	0       0	0	0.073458155	0.032648069	0	0
            19      3       1	0       0	0	0.07032728	0.031256569	0	0
            20      3       1	0       0	0	0.077053447	0.034245976	0	0
            21      3       1	0       0	0	0.073458155	0.032648069	0	0
            22      3       1	0       0	0	0.07032728	0.031256569	0	0
            23      3       1	0       0	0	0.077053447	0.04280747	0	0
            24      3       1	0       0	0	0.359582751	0.171229881	0	0
            25      3       1	0       0	0	0.359582751	0.171229881	0	0
            26      3       1	0   	0	0	0.051368964	0.021403735	0	0
            27      3       1	0       0	0	0.048972104	0.020405043	0	0
            28      3       1	0       0	0	0.051368964	0.017122988	0	0
            29  	3       1	0       0	0	0.102737929	0.059930458	0	0
            30      3       1	0       0	0	0.171229881	0.513689644	0	0
            31  	3   	1	0       0	0	0.117212134	0.054698996	0	0
            32      3       1	0       0	0	0.164096987	0.078141422	0	0
            33      3   	1	0   	0	0	0.051368964	0.034245976	0	0
            34  	3       1	0       0	0	0           0           0	0
            35      3       1	0       0	0	0       	0           0	0
            36      3       1	0       0	0	0           0           0	0
            37      3       1	0       0	0	0           0           0	0
            38      3       1	0       0	0	0           0           0	0
];

switch num
   case 38
         busdt = busdat38;
    
        
end