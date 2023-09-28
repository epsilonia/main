

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
equal = 0;
arrows = 1;

% axisw(gca,'center','k',1)

% parameters 
a = -5;
b = 12;
r = 0.5;
T = linspace(0,-b/a,100);
T = sort([T 2]);
hmax = -b^2/(4*a);
axislimits = [-2*r,-b/a+.5,-.5,hmax+2.4];
load_axis
axis off
h = @(t)(a*t.^2+b*t);
hp = @(t)(2*a*t+b);
for t=T
    tf = linspace(0,t,200);
    hf = plot(tf,h(tf),'red','linewidth',3);
    hc = cercle(h(t),r);
    hl = plot([t,t,0],[0,h(t),h(t)],'color','k');
    ht1 = text(t,-0.3,'$t$','fontsize',20,'interpreter','latex');
    ht2 = text(t+0.1,h(t)/2,'$h(t)$','fontsize',20,'interpreter','latex');
    hv = quiver(0,h(t),0,hp(t)/4,0,'color','red','linewidth',2);
    axis(axislimits);
    getframe();
    if t==2
        pause(2);
    end
    if t ~= T(end)
        delete(hc);
        delete(hf);
        delete(hl);
        delete(ht1);
        delete(ht2);
        delete(hv);
    end
end

function hc = cercle(x,r)
theta = linspace(0,2*pi,200);
hc = fill(r/4.5*cos(theta),r+x+r*sin(theta),'b','EdgeColor','None');
% axis equal
end