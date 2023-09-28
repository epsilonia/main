 t = linspace(-4,4,1000);
 M = 3;
 A = 5;
 P = 2;
 T = .5;
 y = M+A*cos(2*pi/P*(t-T));
 plot(t,y); 
 grid on