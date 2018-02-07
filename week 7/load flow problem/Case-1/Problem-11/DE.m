function [best_x,best_f,F] = DE(N,D,LB,UB,fun,max_FEs)
N1 = floor(4*N/5);
 F1 = 0.7;
 CR = 0.9;
 x=zeros(N,D);
 for i=1:1:N
    for j=1:1:D
        x(i,j) = aleab(LB(j),UB(j));
    end
 end
f = zeros(1,N);
for i = 1:1:N
    f(i) = func_run(x(i,:)',fun);
end
p_x = x;
p_f = f;
it = 1;
[best_f, g] = min(p_f);
best_x = x(g,:);
F(it) = best_f;
FEs=N;
stop=0;
maxit = 6000;
b_i = max(round(0.1*N),2);
while stop<1
    x = x(randperm(N),:);
    [temp_fit, sorted_index] = sort(p_f, 'descend');
     ks = sorted_index(1:N1);
     i_i = zeros(1,N);
     i_i(ks) = 1;
    for i = 1:1:N
        r = zeros(1,3);
        best_i = floor(rand*b_i)+1;
        best_i = sorted_index(best_i);
        r(1)=floor(rand*N)+1;
        while r(1)==i
            r(1)=floor(rand*N)+1;
        end
        r(2)=floor(rand*N)+1;
        while r(2)==i||r(2)==r(1)
            r(2)=floor(rand*N)+1;
        end
        r(3)=floor(rand*N)+1;
        while r(3)==i||r(3)==r(2)||r(3)==r(1)
            r(3)=floor(rand*N)+1;
        end
        if i_i(i) == 1
%            v = p_x(i,:)+F1.*(p_x(r(1),:)-p_x(i,:))+F1.*(p_x(r(2),:)-p_x(r(3),:));
           v = p_x(r(1),:)+F1.*(p_x(r(2),:)-x(r(3),:));
        else
%            v = p_x(i,:)+F1.*(p_x(best_i,:)-p_x(i,:))+F1.*(p_x(r(2),:)-x(r(2),:));
           v = p_x(best_i,:)+F1.*(p_x(r(2),:)-x(r(2),:));
        end
        u = p_x(i,:);
        for j = 1:D
            if rand < CR
                u(j)=v(j);
            end
        end
        for j = 1:1:D
            if u(1,j)<LB(j)
                u(1,j)=LB(j);
            elseif u(1,j)>UB(j)
                u(1,j)=UB(j);
            end
        end
        
        f1 = func_run(u',fun);
        if f1 < p_f(1,i)
            p_f(1,i)=f1;
            x(i,:)=p_x(i,:);
            p_x(i,:)=u;
        end
        
        FEs = FEs+1;
    end
%     disp([f' p_f']);
%     pause;
    [best_f,g]=min(p_f);
    best_x = p_x(g,:);
    it = it+1;
    F(it)=best_f;
    disp(p_f);
    disp(best_f);disp(best_x)
    if FEs > max_FEs
        stop = 1;
        save('result1.txt','p_x','-ascii');
    end
end

end