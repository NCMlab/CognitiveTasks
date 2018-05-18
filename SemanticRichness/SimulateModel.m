NLoads =  5; % Number of load levels
MaxTime = 60*5.5; % time in seconds
TrialOnTime = 1.75; % seconds
MinITI = 0.5; % seconds
TR = 1.;
HighResTs = 0.01;

% Two Conditions:
% Animate/Inanimate
% Low richness/High richness
%
% Animate/Low richness
% Inanimate/Low richness
% Animate/High richness
% Inanimate/Low richness
% Animate/High richness
%
% Contrasts
% Effect of Linear Load collapsing across conditions
% Effect of Quadratic Load collapsing across conditions
% Animate gt Inanimate collapsing across richness and Load
% Animate gt Inanimate collapsing across richness and Load

% The different cells of this experiment will be coded and the different
% load levels will be modeled using parametric modulators << Is that even
% possible?????
% If I collapse across animate/inanimate then I will have 10 trials per
% load. Then I will have two conditions: high and low richness
% Design matrix can have 10 columns:
% LowRich, Load 1
% LowRich, Load 2
% LowRich, Load 3
% LowRich, Load 4
% LowRich, Load 5
% HighRich, Load 1
% HighRich, Load 2
% HighRich, Load 3
% HighRich, Load 4
% HighRich, Load 5
%
% Contrasts;
Contrasts = struct;
Contrasts.High_gt_Low = [-1 -1 -1 -1 -1 1 1 1 1 1];
Contrasts.Low_gt_High = [1 1 1 1 1 -1 -1 -1 -1 -1];
Contrasts.Load1 = [1 0 0 0 0 1 0 0 0 0 ];
Contrasts.Load2 = [0 1 0 0 0 0 1 0 0 0 ];
Contrasts.Load3 = [0 0 1 0 0 0 0 1 0 0 ];
Contrasts.Load4 = [0 0 0 1 0 0 0 0 1 0 ];
Contrasts.Load5 = [0 0 0 0 1 0 0 0 0 1 ];
Contrasts.AllWords = [1 1 1 1 1 1 1 1 1 1];
LinLoad = [1 2 3 4 5 1 2 3 4 5];
Contrasts.LinLoad = LinLoad - mean(LinLoad);
Contrasts.HighRich = [1 1 1 1 1 0 0 0 0 0];
Contrasts.LowRich = [0 0 0 0 0 1 1 1 1 1];
ConNames = fieldnames(Contrasts);

% Contrasts = struct;
%  Contrasts.High_gt_Low = [-1 -1 -1 -1 -1 -1 1 1 1 1 1 1];
%  Contrasts.Low_gt_High = [1 1 1 1 1 1 -1 -1 -1 -1 -1 -1];
%  Contrasts.Load1 = [1 0 0 0 0 0 1 0 0 0 0 0];
%  Contrasts.Load2 = [0 1 0 0 0 0 0 1 0 0 0 0];
%  Contrasts.Load3 = [0 0 1 0 0 0 0 0 1 0 0 0];
%  Contrasts.Load4 = [0 0 0 1 0 0 0 0 0 1 0 0];
%  Contrasts.Load5 = [0 0 0 0 1 0 0 0 0 0 1 0];
% %Contrasts.All = [1 1 1 1 1 1 1 1 1 1 1 1];
% %Contrasts.All = 1;
%  LinLoad = [1 2 3 4 5 6 1 2 3 4 5 6];
%  Contrasts.LinLoad = LinLoad - mean(LinLoad);
ConNames = fieldnames(Contrasts);





%
% Interaction of Richness and Load: [-1 -2 -3 -4 -5 1 2 3 4 5]
% Before I set up the contrasts I need to make the SPM design and then work
% with SPM to see how it makes the contrasts for the different factors.


NCond = 4;
MinNumTrials = 5;
% Set this up as an array
% Rows: Load
% Columns: Conditions
% Depth: Number of Trials

NTrials = 3;
NTotalTrials = NLoads*NCond*NTrials;

TrialList = zeros(NTotalTrials,4);
TrialList(:,1) = 1:NTotalTrials;
% Column for trial number
% Create a column coding the load for each trial
% Create a column coding each of the two conditions

% Create a randomized list for trial order
% Randomize
% What are the limitations for this list?
% No more than three trials of the same condition and load.
% Check the matrix to make sure that there are not three in a row
% Create a column of ITI drawn from a series of random numbers draw from a
% Gamma distribution
%
% Pick a Gamma parameter
% for 1000
% 	Pick a set of ITI
% Is the sum of the ITIs within our max time?
% 		for 1000
%			Randomize the trials
% 			Calculate efficiencies
% Find the best ITI and trial order
% The following codes up the two factors of the design along with the
% number of loads.

Factors = repmat(fullfact([2,2, NLoads]),NTrials,1);
% How mch time do the trials take

%MaxTimeList = [6:0.5:9];
MaxTimeList = [10]%[6,8,10,12,14];
AllBestBE = zeros(3,length(ConNames),length(MaxTimeList));
AllBestGam = zeros(3,2,length(MaxTimeList));
for tt = 1:length(MaxTimeList)
    TotalNTrials = size(Factors,1);
    TrialTime = TotalNTrials*TrialOnTime;
    MaxITITime = MaxTimeList(tt)*60 - TrialTime;
    
    
%     NSim = 10;
%     GamASearch = [0.1:1:7];
%     %GamASearch = 6;
%     GamBSearch = [0.1:0.5:3];
%     %GamBSearch = 0.1;
%     TestGam = zeros(length(GamASearch),length(GamBSearch),NSim);
%     
%     for i = 1:NSim
%         fprintf(1,'Sim %d of %d\n',i,NSim);
%         for j = 1:length(GamASearch)
%             for k = 1:length(GamBSearch)
%                 SimITI = MinITI + [gamrnd(ones(TotalNTrials-1,1).*GamASearch(j),GamBSearch(k));0];
%                 TestGam(j,k,i) = sum(round(SimITI./HighResTs).*HighResTs);
%                 
%                 %SimITI = [0; gamrnd(ones(TotalNTrials - 1,1).*GamParam(1), GamParam(2))];
%                 %Round these to the nearest dt
%                 %tempITI = round(tempITI/HighResTs)*HighResTs + MinITI;
%                 
%             end
%         end
%     end
%     
%     
%     MaxGam = max(TestGam,[],3);
%     MaxGam(find(MaxGam > MaxITITime)) = 0;
%     %MaxGam(find(MaxGam < MaxITITime*0.85)) = 0;
%     % Cycle over the gamma values
%     
%     
%      %figure
%      %title('Values for Gamma Dist that use all Available Scan Time')
%      %surf(GamASearch, GamBSearch,MaxGam')
%      %xlabel('GamA')
%      %ylabel('GamB')
%      %colorbar
%     % Find the edge and extract the values
%     GamValues = zeros(length(GamASearch),2);
%     for i = 1:length(GamASearch)
%         if max(MaxGam(i,:)) > 0
%             GamValues(i,1) = GamASearch(i);
%         
%             GamValues(i,2) = GamBSearch(min(find(MaxGam(i,:) == max(MaxGam(i,:)))));
%         end
%     end
%     GamValues1 = GamValues(find(GamValues(:,1)>0),1);
%     GamValues2 = GamValues(find(GamValues(:,2)>0),2);
%     GamValues = [GamValues1 GamValues2];
    %GamValues% = GamValues(1:5,:);
    %GamValues = GamValues(14,:);
%     
%     
%     %GamParam = [4.6 0.35];
%     %GamParam = [3.1 1.85]
    GamParam = [5 1.5]
     GamValues = GamParam;
    %figure(134);hist(0.5+gamrnd(ones(1000,1).*GamParam(1), GamParam(2)),40)
    %
    % Create the high res HRF
    H = spm_hrf(TR*HighResTs);
    IntroOffTime = 10;
    EndOffTime = 10;
    onsets = cell(1,NLoads*2);
    durations = cell(1,NLoads*2);
    
    
   
    NSim = 100;
    NShuffle = 10;
    SimData = zeros(length(GamValues),length(ConNames), NSim, NShuffle);
    BestOrder = zeros(TotalNTrials,3);
    BestITI = zeros(TotalNTrials,3);
    BestBE = 10*ones(3,length(ConNames));
    WorstOrder = zeros(TotalNTrials,3);
    WorstITI = zeros(TotalNTrials,3);
    WorstBE = zeros(3,length(ConNames));
    BestGam = zeros(3,2);
    BestDesign = cell(3,2);
    for g = 1:size(GamValues,1)
        fprintf(1,'Working on parameter %d of %d ',g,length(GamValues));
        GamParam = GamValues(g,:);
        %     % Cycle over the values for gamma distribution
        for i = 1:NSim
            fprintf(1,'%s','.');
            % fprintf(1,'Working on sim %d of %d\n',i,NSim);
            % generate some random numbers from these values
            Flag = 1;
            while Flag == 1
                tempITI = MinITI + [gamrnd(ones(TotalNTrials - 1,1).*GamParam(1), GamParam(2)); 0];
                %Round these to the nearest dt
                tempITI = round(tempITI/HighResTs)*HighResTs;
                if (sum(tempITI) <= MaxITITime) & (sum(tempITI) > 0.85*MaxITITime)
                    Flag = 0;
                end
            end
            %sum(tempITI)
            % These are the start of the ITIs
            tempCumSum = IntroOffTime + cumsum(tempITI  + TrialOnTime);
            tempSumSumTrialStarts = tempCumSum - TrialOnTime - MinITI ;
            tempDesign = [tempITI tempSumSumTrialStarts Factors];
            % Randomize
            for rr = 1:NShuffle
                X =  zeros((EndOffTime + MaxTimeList(tt)*60)/HighResTs,NLoads*2); %%%<<<<<<<<<<<<<<<<<<
                hX = zeros((EndOffTime + MaxTimeList(tt)*60)/HighResTs,NLoads*2);
                
                r = randperm(TotalNTrials);
                for k = 1:TotalNTrials
                    CurCol = tempDesign(r(k),5) + (tempDesign(r(k),3) - 1)*NLoads;
                    % Create the cell arrays for use with SPM
                    %onsets{CurCol} = [onsets{CurCol} tempDesign((k),2)];
                    %durations{CurCol} = [durations{CurCol} TrialOnTime];
                    % Create high res version of the design with no CONV
                    X(int32(tempDesign((k),2)/HighResTs),CurCol) = 1;
                end
                % Note that the randomization is taking place for the trial conditions,
                % but the order of the ITI is not randomized.
                for k = 1:NLoads*2
                    temp = conv(X(:,k),H);
                    hX(:,k) = temp(1:length(X));
                end
                % Down sample
                % Subsample the design
                NTR = int32((EndOffTime + 60*MaxTimeList(tt)))/(TR);
                lX = zeros(NTR,NLoads*2 + 1);
                for p = 1:NLoads*2
                    temp = hX(1:TR/HighResTs:end,p);
                    lX(:,p) = temp;
                end
                lX(:,end) = 1;
                lX2 = [sum(lX(:,1:end-1),2) ones(size(lX,1),1)];
                % imagesc(lX(:,1:end-1))
                for cc = 1:length(ConNames)
                    [Eff, VRF, BoldEffect] = subfnCalDesignMetrics(lX,Contrasts.(ConNames{cc})');
                    SimData(g, cc, i, rr) = BoldEffect;
                   % fprintf(1,'%s\t%0.4f\n',ConNames{cc},BoldEffect)
                end
                OverAllBE = sum(SimData(g,:, i, rr));
                
                if OverAllBE < sum(BestBE(1,:))
                %if SimData(g,8, i, rr) < BestBE(1,8)
                    BestGam(2:3,:) = BestGam(1:2,:);
                    BestBE(2:3,:) = BestBE(1:2,:);
                    BestOrder(:,2:3) = BestOrder(:,1:2);
                    BestITI(:,2:3) = BestITI(:,1:2);
                    BestGam(1,:) = GamParam;
                    BestBE(1,:) = SimData(g,:, i, rr);
                    BestOrder(:,1) = r;
                    BestITI(:,1) = tempITI;
                    BestDesign{1,1} = lX;
                elseif OverAllBE < sum(BestBE(2,:))
                %elseif SimData(g,8, i, rr) < BestBE(2,8)
                    BestGam(3,:) = BestGam(2,:);
                    BestBE(3,:) = BestBE(2,:);
                    BestOrder(:,3) = BestOrder(:,2);
                    BestITI(:,3) = BestITI(:,2);
                    BestBE(2,:) = SimData(g,:, i, rr);
                    BestOrder(:,2) = r;
                    BestITI(:,2) = tempITI;
                end
                if SimData(g,8, i, rr) > sum(WorstBE(3,:))
                    WorstBE(1:2,:) = WorstBE(2:3,:);
                    WorstOrder(:,1:2) = WorstOrder(:,2:3);
                    WorstITI(:,1:2) = WorstITI(:,2:3);
                    WorstBE(3,:) = OverAllBE;
                    WorstOrder(:,3) = r;
                    WorstITI(:,3) = tempITI;
                    BestDesign{3,2} = lX;
                elseif SimData(g,8, i, rr) > sum(WorstBE(2,:))
                    WorstBE(1,:) = WorstBE(2,:);
                    WorstOrder(:,1) = WorstOrder(:,2);
                    WorstITI(:,1) = WorstITI(:,2);
                    WorstBE(2,:) = OverAllBE;
                    WorstOrder(:,2) = r;
                    WorstITI(:,2) = tempITI;
                end
                
            end
        end
        fprintf(1,'\n')
    end
    AllBestBE(:,:,tt) = BestBE;
    AllBestGam(:,:,tt) = BestGam;
end


WorstBE
BestBE
BestGam

GamParam = BestGam(1,:);

figure(134);hist(0.5+gamrnd(ones(1000,1).*GamParam(1), GamParam(2)),40)


%save SemanticSimulation

