clc;
[ Vabs,Theta,V,Pcal,Qcal,it,VABASE, VBASE,Y ] = TCIMrun1(y(r,:) );
n = size(V);
N = n(1);
disp(it);
%% Real power injection
disp('----------------Real and Imag Power Injection in Line---------------');
disp('      Bus       Pa         Pb        Pc        Qa        Qb       Qc');
m=1;
for n = 1:3:N
    disp([m Pcal(n) Pcal(n+1) Pcal(n+2) Qcal(n) Qcal(n+1) Qcal(n+2)]);
    m = m+1;
end
%% Volatage magnitude at every bus
disp('----------------Voltage Magnitude and load Angle at every Bus----------------------');
disp('      Bus       Va         Vb        Vc      dela      delb     delc');
m=1;
for n = 1:3:N
    disp([m Vabs(n) Vabs(n+1) Vabs(n+2) Theta(n) Theta(n+1) Theta(n+2)]);
    m = m+1;
end
%% current magnitude at every bus
I = Y*V;
Iabs = abs(I);
Theta1 = angle(I);
disp('----------------Current Magnitude and load Angle at every Bus----------------------');
disp('      Bus       Ia         Ib        Ic      dela      delb     delc  ');
m=1;
for n = 1:3:N
    disp([m Iabs(n) Iabs(n+1) Iabs(n+2) Theta1(n) Theta1(n+1) Theta1(n+2)]);
    m = m+1;
end
 a = 1/3*(I(1)+exp(4/3*pi*j)*I(2)+exp(2/3*pi*j)*I(3));
 a = abs(a);
 disp(['- sequence current at root node = ' num2str(a)]);
 a = 1/3*(I(1)+I(2)+I(3));
 a = abs(a);
 disp(['0 sequence current at root node = ' num2str(a)])
 a = 1;
 for i = 1:1:6
    if y(i) == 1 & a==1
        a = a+1;
disp(['Distributed generator is connected to phase ' num2str(i) ' in bus 3']);
disp(['Power genrated by Distributed generator is ' num2str(y(7)+j*y(9))]);
    elseif y(i)==1& a ==2
 disp(['Distributed generator is connected to phase ' num2str(i-3) ' in bus 5']);
 disp(['Power genrated by Distributed generator is ' num2str(y(8)+j*y(10))]);
    end
end
