function temp = flow_result(x)
[ Vabs,Theta,V,Pcal,Qcal,it,VABASE, VBASE,Y ] = TCIMrun1(x );
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

 