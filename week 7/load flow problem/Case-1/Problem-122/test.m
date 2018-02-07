clear;
clc;
% global initial_flag

%     fileID=fopen('convergence.txt','w');
% Disp_Fun;
fun = input('Select a function:');
n = input('number of distributed generation+discharge bus: ');
D = 1*n;
N = 80; %No. of particles
FE_max = D*1e4; %Max. no. of function evaluations

Nr = 1; % No. of runs
normalize = 0; % 0 => no normalisation, else 1

[LB, UB, opt_f ] = get_Fun_info(fun,D);

FE = zeros(1,Nr);
new_f = zeros(1,Nr);
tot_time = zeros(1,Nr);

FE1 = zeros(1,Nr);
new_f1 = zeros(1,Nr);
tot_time1 = zeros(1,Nr);
F1 = zeros(Nr,5000);
F2 = F1;
F3 = F1;
F4 = F1;

SR = 0;
SR1 = 0;
tot_time = 0;

% % Warm up the RNG
for t=1:1:10000
    zz=aleab(0,1); %rand;
end

% fileID=fopen('function8.txt','w');
% fprintf(fileID,'%30s\r\n','S.N BO DE PSO ABC)');
y = zeros(Nr,D);po = zeros(Nr,n);
for r=1:1:Nr
po(r,:) = randperm(24,n)+1;
%     initial_flag = 0;
    
% disp(po(r,:))
 tic; %Reset the timer
    

[y(r,:) ,new_f1(r),F1] = DE(N,D,LB,UB,fun,FE_max);

tot_time1(r) = toc;
clc;
% powerflow;

end 

save('data2.txt','y','new_f1','-ascii');