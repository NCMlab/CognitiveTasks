MaxLoad = 9;
NSim = 10000;
NRepeats = 100;
MaxTrials = 20;
OverallAcc = zeros(MaxLoad, NSim, NRepeats, NTrials);
% Cycle over the load
for s = 1:NSim
    fprintf(1,'Starting simulation %d of %d\n',s, NSim);
    for i = 1:MaxLoad
        for j = 1:NRepeats
            % cycle over the number of trials in the experiment
            for k = 1:MaxTrials
                NPositions = i;
                % What is the observed accuracy for
                % this load
                CurrAcc = AverageAcc(find(Load == NPositions));
                % Generate the serial positions for the number of trials
                R = floor(rand(k,1)*NPositions+1);
                % Estimate the accuracy of these trials and find the mean accuracy
                AccThisSim = mean(rand(k,1) < CurrAcc(R));
                OverallAcc(i, s, j, k) = AccThisSim;
            end
        end
    end
end
fid = fopen('SimSerialPositionAcc.csv','w');
fprintf(fid,'NTrials, Load 1, Load 2, Load 3, Load 4, Load 5, Load 6, Load 7, Load 8, Load 9 \n');

for j = 1:MaxTrials
    fprintf(fid,'%d,',j);
    for i = 1:MaxLoad
        temp = squeeze(OverallAcc(i,:,:,j));
        % What is the minimum accuracy across simulations?
        % What i sthe mean of the minimum across all repetitions of the
        % simulations?
        fprintf(fid,'%0.3f,',mean(min(temp)));
        %fprintf(1,'%d, %d, %0.2f\n',i,j,mean(min(temp)));
    end
    fprintf(fid,'\n');
end

%% 
% Can I run a sim at load 9 and 30 trials. Then find the location of probe
% lettters for the worst accuracy and for the best accuracy. 
NPositions = 9
AccRange = zeros(10000,1);


    % Pick locations andthen simyulate 
    R = floor(rand(k,1)*NPositions+1);
    R = [2 1 3 2 2]
    for i = 1:10000
        AccRange(i) = mean(rand(k,1) < CurrAcc(R));
    end
    AccThisSim = mean(rand(k,1) < CurrAcc(R));
    if AccThisSim > 0.95
            R
            AccThisSim
        break
    end
end