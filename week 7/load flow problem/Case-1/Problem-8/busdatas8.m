% Returns Initial Bus datas of the system...

function busdt = busdatas8(num)

% Type....
% 1 - Slack Bus..
% 2 - PV Bus..
% 3 - PQ Bus..



%        |Bus|Type|  Vsp   | Theta  |  Pgi     |  Qgi   |     Pli  |   Qli   |    Qmin |    Qmax |

busdat38=[    1	1	1	0       0	0	0           0           0	0
            2	3	1	0       0	0	0.09805033	0.058830198	0	0
            3	3	1	0       0	0	0.088542537	0.039352238	0	0
            4	3	1	0       0	0	0.108141728	0.072094485	0	0
            5	3	1	0       0	0	0.058830198	0.029415099	0	0
            6	3	1	0       0	0	0.059028358	0.019676119	0	0
            7	3	1	0       0	0	0.180236213	0.090118107	0	0
            8	3	1	0       0	0	0.180236213	0.090118107	0	0
            9	3	1	0       0	0	0.059028358	0.019676119	0	0
            10	3	1	0       0	0	0.054070864	0.018023621	0	0
            11	3	1	0       0	0	0.040553148	0.027035432	0	0
            12	3	1	0       0	0	0.058830198	0.034317616	0	0
            13	3	1	0       0	0	0.054070864	0.031541337	0	0
            14	3	1	0       0	0	0.117660396	0.078440264	0	0
            15	3	1	0       0	0	0.059028358	0.019676119	0	0
            16	3	1	0       0	0	0.054070864	0.018023621	0	0
            17	3	1	0       0	0	0.054070864	0.018023621	0	0
            18	3	1	0       0	0	0.088542537	0.039352238	0	0
            19	3	1	0       0	0	0.088245297	0.039220132	0	0
            20	3	1	0       0	0	0.081106296	0.036047243	0	0
            21	3	1	0       0	0	0.088542537	0.039352238	0	0
            22	3	1	0       0	0	0.088245297	0.039220132	0	0
            23	3	1	0       0	0	0.081106296	0.045059053	0	0
            24	3	1	0       0	0	0.378496048	0.180236213	0	0
            25	3	1	0       0	0	0.378496048	0.180236213	0	0
            26	3	1	0       0	0	0.054070864	0.022529527	0	0
            27	3	1	0       0	0	0.059028358	0.024595149	0	0
            28	3	1	0       0	0	0.054070864	0.018023621	0	0
            29	3	1	0       0	0	0.108141728	0.063082675	0	0
            30	3	1	0       0	0	0.180236213	0.54070864	0	0
            31	3	1	0       0	0	0.147075495	0.068635231	0	0
            32	3	1	0       0	0	0.205905693	0.09805033	0	0
            33	3	1	0       0	0	0.054070864	0.036047243	0	0
            34	3	1	0       0	0	0           0           0	0
            35	3	1	0       0	0	0           0           0	0
            36	3	1	0       0	0	0           0           0	0
            37	3	1	0       0	0	0           0           0	0
            38	3	1	0       0	0	0           0           0	0];
switch num

   case 38
         busdt = busdat38;
        
end