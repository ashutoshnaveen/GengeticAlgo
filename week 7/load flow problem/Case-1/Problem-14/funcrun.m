function a = funcrun(x,fun)

[ Vabs,Theta,V,Pcal,Qcal,it,Y ] = TCIMrun1(x);


%% cost of DGs
Cdg14;charge114;
Fdg = sum(x.*Cdg);
[Pi,Qi,Pg,Qg,Pl,Ql,Lpij,Lqij] = loadflow1(x,charge(:,1),38,Vabs,Theta,1);
Fcpg = 0.09*Pg(1);

Fev = sum(charge(:,1).*0.06);
Cto = Fdg+Fcpg+Fev;
loss = sum(sum(Lpij));
VR = sum((Vabs-1).^2);
 disp([Pg(1),Fdg,Fcpg,Fev,loss, VR]);
a = 0.6*Cto^2+0.25*(loss)^2+0.15*VR;
end
 