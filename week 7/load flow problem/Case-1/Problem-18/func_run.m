function fit = func_run(x,fun)
[D,m] = size(x);
fit = zeros(1,m);
for i = 1:m
          fit(i) = funcrun(x(:,i)',fun);
end