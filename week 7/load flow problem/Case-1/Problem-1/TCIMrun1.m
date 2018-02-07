function [ Vabs,Theta,V,Pcal,Qcal,it,Y ] = TCIMrun1(x)
%  Here i m considering constant power condition 
%  for volatage dependancy on load just give input
%  to the Pl0,Pl1,Pl2,Ql0,Ql1,Ql2 at load constant section
%  Pl0 and Ql0 are for const power
%  Pl1 and Ql1 are for const current and
%  Pl2 and Ql2 are for const impedance constant for real and imag load
%  resp......
%  here we consider only constant power condition
%  convergence is checked for 25 bus radial system 
%  default file data is for 25 bus system for demo
% disp(x);
% pause;

% clc;
nn = length(x);
dg = x;
DGa;Pdg = zeros(38,1);
Pdg(DG)=x;
charge11;
nbus = 38;                  % IEEE-14, IEEE-30, IEEE-57..
Nbus = nbus;
Y =full( ybusppg(nbus));          % Calling ybusppg.m to get Y-Bus Matrix..
busd = busdatas1(nbus);      % Calling busdatas..
BMva = 1;                 % Base MVA..
bus = busd(:,1);            % Bus Number..
type = busd(:,2);           % Type of Bus 1-Slack, 2-PV, 3-PQ..
Vabs = busd(:,3);              % Specified Voltage..
Theta = busd(:,4);            % Voltage Angle..
V   = Vabs.*exp(Theta*1j);       % Volatge in complex form
Pg = busd(:,5)/BMva+Pdg ;        % PGi..
Qg = busd(:,6)/BMva;        % QGi..
Pl = busd(:,7)/BMva+charge(:,1);        % PLi..
Ql = busd(:,8)/BMva;        % QLi..
Qmin = busd(:,9)/BMva;      % Minimum Reactive Power Limit..
Qmax = busd(:,10)/BMva;     % Maximum Reactive Power Limit..
P = Pg- Pl;                % Pi = PGi - PLi..
Q = Qg - Ql;                % Qi = QGi - QLi..
Psp = P;                    % P Specified..
Qsp = Q;                    % Q Specified..
G = real(Y);                % Conductance matrix..
B = imag(Y);                % Susceptance matrix..

pv = find(type == 2 | type == 1);   % PV Buses..
pq = find(type == 3);               % PQ Buses..
npv = length(pv);                   % No. of PV buses..
npq = length(pq);                   % No. of PQ buses..
%% Current Injection in bus
I = Y*V;
Ir = real(I);
Im = imag(I);
%% Power Mismatch
Vr = real(V);
Vm = imag(V);
Vabs = abs(V);
% Theta = atan(Vm./Vr);
Theta = angle(V);
Pcal = Vr.*Ir+Vm.*Im;
Qcal = Vm.*Ir-Vr.*Im;
% Psp = Pg-(Pl0.*Pl+Pl1.*Vabs+Pl2.*Vabs.^2);
% Qsp = Qg-(Ql0.*Ql+Ql1.*Vabs+Ql2.*Vabs.^2);
delP = Psp-Pcal;
delQ = Qsp-Qcal;
%% non-updated Jacobian Matrix
J = zeros(2*(Nbus-1));
k=2;
r=2;
for n = 1:2:2*(Nbus-1)
    l =2;
    for m = 1:2:2*(Nbus-1)
        if type(r)==2
        if n==m
        else
            J(m,n+1)=0;
            J(m+1,n+1)=0;
        end
        else
        if n==m
        else
            J(m,n)=imag(Y(l,k));
            J(m+1,n)=real(Y(l,k));
            J(m,n+1)=real(Y(l,k));
            J(m+1,n+1)=-imag(Y(l,k));
        end
        end
        l = l+1;
    end
    k = k+1;
    r = r+1;
    
end
% disp(J)
%% load  constants   (Edit for use)
 Pl0 = ones(Nbus,1);
 Pl1 = zeros(Nbus,1);
 Pl2 = zeros(Nbus,1);
 Ql0 = ones(Nbus,1);
 Ql1 = zeros(Nbus,1);
 Ql2 = zeros(Nbus,1);
Tol = 1;  
Iter = 1;
% while (Tol > 1e-5)   % Iteration starting..
for it = 1:1000000
    %% a,b,c,d
Vr = real(V);
Vm = imag(V);
Vabs = abs(V);
a = ((Qg-Ql0.*Ql).*(Vr.^2-Vm.^2)-2.*Vr.*Vm.*(Pg-Pl0.*Pl))./Vabs.^4+(Vr.*Vm.*Pl1+Ql1.*Vm.^2)./Vabs.^3+Ql2;
b = ((Pg-Pl0.*Pl).*(Vr.^2-Vm.^2)+2.*Vr.*Vm.*(Qg-Ql0.*Ql))./Vabs.^4-(Vr.*Vm.*Ql1+Pl1.*Vm.^2)./Vabs.^3-Pl2;
d = ((Qg-Ql0.*Ql).*(Vr.^2-Vm.^2)-2.*Vr.*Vm.*(Pg-Pl0.*Pl))./Vabs.^4+(Vr.*Vm.*Pl1-Ql1.*Vm.^2)./Vabs.^3-Ql2;
c = ((Pg-Pl0.*Pl).*(Vm.^2-Vr.^2)-2.*Vr.*Vm.*(Qg-Ql0.*Ql))./Vabs.^4+(Vr.*Vm.*Ql1-Pl1.*Vm.^2)./Vabs.^3-Pl2;
% Theta = atan(Vm./Vr);
Theta = angle(V);
%% sub power
I = Y*V;
% disp([I V]);
Ssub = V.*(I);
Psub = real(Ssub);
Qsub = imag(Ssub);
% Jold=J;
%% updated Jacobian Matrix
k=2;
r=2;
% disp(type)
for n = 1:2:2*(Nbus-1)
    l=2;
    for m = 1:2:2*(Nbus-1)
        if type(r)==2
        if n==m
            J(m,n)=(real(Y(l,k))-b(k) )-....
                  (imag(Y(l,k))-a(k) ).*Vm(k)./Vr(k);
            J(m+1,n)=(-imag(Y(l,k))-d(k) )-...
                (real(Y(l,k))-c(k) ).*Vm(k)./Vr(k) ;
            J(m,n+1)=Vr(k)./Vabs(k).^2 ;
            J(m+1,n+1)=-Vm(k)./Vabs(k).^2 ;
        else
            J(m,n)=real(Y(l,k))-imag(Y(l,k)).*Vm(k)./Vr(k) ;
            J(m+1,n)=-imag(Y(l,k))-real(Y(l,k)).*Vm(k)./Vr(k) ;
        end
        else
        if n==m
              J(m,n)=imag(Y(l,k))-a(k) ;
              J(m+1,n)=real(Y(l,k))-c(k) ;
              J(m,n+1)=real(Y(l,k))-b(k);
              J(m+1,n+1)=-imag(Y(l,k))-d(k);
        end
        end
        l = l+1;
    end
    k = k+1;
    r = r+1;
end
%  disp(J);
 %% Current Mismatch Vector
r=1;
for n = 1:(Nbus)
    if type(r)==2
        delIr(n,1) = (Vr(n,1).*delP(n,1))./Vabs(n,1).^2;
        delIm(n,1) = (Vm(n,1).*delP(n,1))./Vabs(n,1).^2;
    else
        delIr(n,1) = (Vr(n,1).*delP(n,1)+Vm(n,1).*delQ(n,1))./Vabs(n,1).^2;
        delIm(n,1) = (Vm(n,1).*delP(n,1)-Vr(n,1).*delQ(n,1))./Vabs(n,1).^2;
    end
        r = r+1;
end
k=2;
for n = 1:2:2.*(Nbus-1)
    delI(n,1) = delIm(k,1);
    delI(n+1,1) = delIr(k,1);
    k = k+1;
end
%% Voltage correction Vector
delV = J^(-1)*delI;
k=2;
r=2;
for n = 1:2:2.*(Nbus-1)
    if type(r)==2
        delVm(k,1) = delV(n,1);
        delVr(k,1) =-Vm(k,1).*delVm(k,1)./Vr(k,1) ;
    else
        delVr(k,1) = delV(n,1);
        delVm(k,1) = delV(n+1,1);
    end
    k = k+1;
    r = r+1;
end
%% Voltage and Theta ubdation
delv = Vr.*delVr./Vabs+Vm.*delVm./Vabs;
deltheta = Vr.*delVm./Vabs.^2-Vm.*delVr./Vabs.^2;
Vabs = Vabs+delv;
Theta = Theta+deltheta;
V = Vabs.*exp(1j.*Theta);
% V = V+(delVr+delVm*1j);
%% Reactive power updation of pv bus
 I = Y*V;
 Ir = real(I);
 Im = imag(I);
 Qcal = Vm.*Ir-Vr.*Im;
 r = 1;
 Qg1 = Qcal+Ql;
 if it <7&&it>2
 for n = 1:Nbus
     if type(r)==2
        
             if Qg1(n,1)<Qmin(r,1)
                 Vabs(n,1) = Vabs(n,1)+0.01;
             elseif Qg1(n,1)>Qmax(r,1)
                 Vabs(n,1) = Vabs(n,1)-0.01;
             end
        
     end
     r = r+1;
 end
 end
 
 V = Vabs.*exp(1j.*Theta);
%% Current Injection in bus
I = Y*V;
Ir = real(I);
Im = imag(I);
%% Power Mismatch
Vr = real(V);
Vm = imag(V);
Vabs = abs(V);
% Theta = atan(Vm./Vr);
Theta = angle(V);
Pcal = Vr.*Ir+Vm.*Im;
Qcal = Vm.*Ir-Vr.*Im;
v = abs(V);
% Psp = Pg-(Pl0.*Pl+Pl1.*Vabs+Pl2.*Vabs.^2);
% Qsp = Qg-(Ql0.*Ql+Ql1.*Vabs+Ql2.*Vabs.^2);
Psp = Pg-Pl;
Qsp = Qg-Ql;
delP = Psp-Pcal;
delQ = Qsp-Qcal;
r = 1;
for n = 1:Nbus
    if type(r)==2
       
            delQ(n,1) = 0;
      
    end
    r = r+1;
end
del = max(max(abs([(delP(2:end,1)) (delQ(2:end,1))])).');
%  disp(delP);
%   disp(delQ);
%   disp(del)
if abs(del) < 10.^(-5)
%     disp(it);
    break;
end

%  pause;
end


