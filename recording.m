%% sample to analyze speech 
N = 400;
n = 0:N-1;
t = n/fs;

x = v(1660 + n)';

[x, fs] = audioread('input.wav');

figure(1)

%% Plot in center 

subplot(2, 1, 1)
plot(t, x)
xlabel('Time (sec)')
title('x(t)   [SIGNAL]')
% outline
