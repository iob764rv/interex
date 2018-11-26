%% sample to analyze speech 
N = 400;
n = 0:N-1;
t = n/fs;

x = v(1660 + n)';
xlabel('Time (seconds)')

figure(1)

%% Plot in center 

subplot(2, 1, 1)
plot(t, x)
xlabel('Time (sec)')
title('x(t)   [SIGNAL]')
% outline

[r11_max, k] = max(r11);

hold on
plot(lag_max, r11_max, 'ro')
grid on
xlim([-8 8])
