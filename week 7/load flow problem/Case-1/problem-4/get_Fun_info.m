function [L,U,opt_f] = get_Fun_info(fun,D)

switch(fun) % fun from 1 to 25 are CEC'05 functions
    case {1}, % 25 bus
        LB = zeros(1,D);
        UB=LB;
        dg1;
        LB = dg(:,1)';
        UB = dg(:,2)';
        opt_f = 0;
    case {2}, % 13 bus
        LB = zeros(1,D);
        UB=LB;
        dg2;
        LB = dg(:,1)';
        UB = dg(:,2)';
        opt_f = 0;
    case {3}, % 34 bus
         LB = zeros(1,D);
        UB=LB;
        dg3;
        LB = dg(:,1)';
        UB = dg(:,2)';
        opt_f = 0;
   case {4}, % 123 bus
        LB = zeros(1,D);
        UB=LB;
        dg4;
        LB = dg(:,1)';
        UB = dg(:,2)';
        opt_f = 0;
end
sl = size(LB);

if (sl(1)*sl(2) == 1) % LB and UB are scalers
    L = LB*ones(1,D);
    U = UB*ones(1,D);
else
    L = LB;
    U = UB;
end
end