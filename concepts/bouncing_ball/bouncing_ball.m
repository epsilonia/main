

close all; clear
addpath('C:\Users\WALID\OneDrive\Documents\MATLAB\MyLib')
load_colors

% axislimits = [-16/9 16/9 -1 1];
% axislimits = 2*axislimits;
showxlabel = 1;
showylabel = 1;
showxticks = 1;
showyticks = 1;
xtickstep = 1;
ytickstep = 1;
equal = 1;
arrows = 1;

% axisw(gca,'center','k',1)

% parameters 
a = -5;
b = 12;
r = 0.5;
T = linspace(0,-b/a,100);
hmax = -b^2/(4*a);
axislimits = [-2*r,-b/a,-.5,hmax+2.2];
load_axis
axis off
for t=T
    hc = cercle(a*t^2+b*t,r);
    hf = plot(
    axis(axislimits);
    getframe();
    if t ~= T(end)
        delete(hc)
    end
end

function hc = cercle(x,r)
theta = linspace(0,2*pi,200);
hc = fill(r*cos(theta),r+x+r*sin(theta),'b','EdgeColor','None');
axis equal
end