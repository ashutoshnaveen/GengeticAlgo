function a = funcrun(x,fun)

[ Vabs,Theta,V,Pcal,Qcal,it,Y ] = TCIMrun1(x);


%% cost of DGs
Cdg18;discharge118;
Fdg = sum(x(1:10).*Cdg);
[Pi,Qi,Pg,Qg,Pl,Ql,Lpij,Lqij] = loadflow1(x,38,Vabs,Theta,1);
Fcpg = 0.13*Pg(1);

Fev = sum(discharge(:,2).*0.07);
Cto = Fdg+Fcpg+Fev;
loss = sum(sum(Lpij));
VR = sum((Vabs-1).^2);
 disp([Pg(1),Fdg,Fcpg,Fev,loss, VR]);
a = 0.6*Cto^2+0.25*(loss)^2+0.15*VR;
end
 