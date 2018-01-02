clear; clc;
%% Specify robot parameters
import URcontrol
import URmonitor
mdl_UR5;

ipAddress='169.254.188.7';
tcpPose=[0,0,0,0,0,0];
toolPayload=0.5;

%% Create Robot Objects
robotMonitor=URmonitor(ipAddress);
robotControl=URcontrol(ipAddress,tcpPose,toolPayload);

%% Program
pose_init = [149, -290, 100, -3.14, 0.001, 0.001]; %top left square - 1cm
pose = pose_init;
URcontrol.moveLinear(robotControl,'tool',pose_init); 
pause(3);
r = 1;
c = 1;
J=cell(28,19);
V=cell(28,19);
t = 0.5;
long_pause = false;

tic;
timerVal = tic;
for n=1:533
    
    if long_pause == true
        t = 1.5;
        long_pause = false;
    else
        t = 0.5;
    end
    
    %move above square & save joint values
    pose(1,2) = pose(1,2) - 10; 
    URcontrol.moveLinear(robotControl,'tool',pose);
    pause(t);
    v = URmonitor.getRobotInfo(robotMonitor,'jointState');
    V{r,c} = v;
    dlmwrite('via_points.csv',v,'-append','delimiter',',');
    
    %mark target square & save values
    pose(1,3) = 90;
    URcontrol.moveLinear(robotControl,'tool',pose); %mark
    pause(t);
    j = URmonitor.getRobotInfo(robotMonitor,'jointState');
    J{r,c} = j;
    dlmwrite('target_points.csv',j,'-append','delimiter',',');
    
    %come back to via point
    pose(1,3) = 100;
    URcontrol.moveLinear(robotControl,'tool',pose); %mark
    pause(t);

    c = c+1;

    if c == 20
       pose(1, 1) = pose(1, 1) - 10;
       pose(1, 2) = -290;
       r = r+1;
       c = 1;
       long_pause = true;
    end
end

elapsedTime = toc(timerVal);

%% Program for joint space
pose_target = csvread('target_points.csv');
pose_via = csvread('via_points.csv');

pose_init = pose_via(258,:);
URcontrol.moveLinear(robotControl,'joint',pose_init);
URmonitor.waitForExecution(robotMonitor);

cell_target=cell(28,19);
cell_via=cell(28,19);

r=1;
c=1;

for n = 1:532
    cell_target{r,c}=pose_target(n,:);
    cell_via{r,c}=pose_via(n,:);
    c=c+1;
        if c==20
            r = r+1;
            c = 1;
        end
end



for n = 1:5
    e_list(n,1) = n
    e_list(n,2) = randi([1 28])
    e_list(n,3) = randi([1 19])
end
%%
for n = 1:20
   % q0 = URmonitor.getRobotInfo(robotMonitor,'jointState')
    pose_via = cell_via{e_list(n,2), e_list(n,3)}
    pose_target = cell_target{e_list(n,2), e_list(n,3)}
    
    [pos,vel,acc] = mtraj(@lspb,q0,q1,50);

    URcontrol.moveLinear(robotControl,'joint',pose_via);
    URmonitor.waitForExecution(robotMonitor);
    URcontrol.moveLinear(robotControl,'joint',pose_target);
    URmonitor.waitForExecution(robotMonitor);
    URcontrol.moveLinear(robotControl,'joint',pose_via);
    URmonitor.waitForExecution(robotMonitor);
    URcontrol.moveLinear(robotControl,'joint',pose_init);
    URmonitor.waitForExecution(robotMonitor);
    
end

%% Via waypoint, too fast

for n = 1:5
    tic;
    startTime=tic;
    wayPoint = cell_via{e_list(n,2), e_list(n,3)};
    finalPoint = cell_target{e_list(n,2), e_list(n,3)};
    
    %URcontrol.moveLinear(robotControl,'joint',pose_init);
    %URmonitor.waitForExecution(robotMonitor);
    URcontrol.moveCircular(robotControl,wayPoint,finalPoint);
    URmonitor.waitForExecution(robotMonitor);
    URcontrol.moveCircular(robotControl,wayPoint,pose_init);
    URmonitor.waitForExecution(robotMonitor);
end
toc(startTime)
%% Calibrate corners
pose_tl = [150, -300, 100, -3.14, 0.001, 0.001]; %top left square
mark_tl = [150, -300, 90, -3.14, 0.001, 0.001]; %top left square

pose_tr = [150, -480, 100, -3.14, 0.001, 0.001]; %top right square
mark_tr = [150, -480, 90, -3.14, 0.001, 0.001]; %top right square

pose_br = [-120, -480, 100, -3.14, 0.001, 0.001]; %bottom right square
mark_br = [-120, -480, 90, -3.14, 0.001, 0.001]; %bottom right square

pose_bl = [-120, -300, 100, -3.14, 0.001, 0.001]; %top left square
mark_bl = [-120, -300, 90, -3.14, 0.001, 0.001]; %top left square


URcontrol.moveLinear(robotControl,'tool',pose_tl);
pause(2);
URcontrol.moveLinear(robotControl,'tool',mark_tl);
pause(1);
URcontrol.moveLinear(robotControl,'tool',pose_tl);
pause(1);

URcontrol.moveLinear(robotControl,'tool',pose_tr);
pause(1);
URcontrol.moveLinear(robotControl,'tool',mark_tr);
pause(1);
URcontrol.moveLinear(robotControl,'tool',pose_tr);
pause(1);

URcontrol.moveLinear(robotControl,'tool',pose_br);
pause(2);
URcontrol.moveLinear(robotControl,'tool',mark_br);
pause(1);
URcontrol.moveLinear(robotControl,'tool',pose_br);
pause(1);

URcontrol.moveLinear(robotControl,'tool',pose_bl);
pause(1);
URcontrol.moveLinear(robotControl,'tool',mark_bl);
pause(1);
URcontrol.moveLinear(robotControl,'tool',pose_bl);
pause(1);





