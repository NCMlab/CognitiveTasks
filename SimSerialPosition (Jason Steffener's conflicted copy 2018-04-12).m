AccYoung = [1.000	0.87	0.89;
            1	1	1.000;
            1	1	1];
        

AccOld = [1.000	1.000	1.000;
            0.938	0.935	1.000;
            0.922	0.857	1.000];

        NSim = 10000;
        NPositions = 9;
        NRow = 3;
        NCol = 3;
        NRepeats = 100;
        
    
        Data = zeros(NRepeats,30,3);
        for k = 1:NRepeats
            for i = 1:30 % Number of trials
                NTrials = i;
                YngOverallAcc = zeros(NSim,1);
                
                
                R = floor(rand(NTrials,1)*NPositions+1);
                [x, y] = ind2sub([NRow,NCol],R(1));
                
                for j = 1:NSim
                    Sim = zeros(NTrials,1);
                    for i = 1:NTrials
                        % What positon is it?
                        R = floor(rand(NTrials,1)*NPositions+1);
                        
                        % What is the expected accuracy?
                        [x, y] = ind2sub([NRow,NCol],R(1));
                        
                        % Did they get this correct
                        if (rand() < AccYoung(y,x))
                            Sim(i) = 1;
                        end
                    end
                    
                    YngOverallAcc(j) = mean(Sim);
                end
                Data(k,i,:) = [min(YngOverallAcc), max(YngOverallAcc), mean(YngOverallAcc)];
            end
            
        end
        fprintf(1,"NTrials, MinAcc, MaxAcc, MeanAcc\n");
for i = 1:30
            fprintf(1,"%d, %0.2f, %0.2f, %0.2f\n", i, mean(squeeze(Data(:,i,1))),...
                mean(squeeze(Data(:,i,2))),mean(squeeze(Data(:,i,3))));
end
            

    
figure(1)
hist(YngOverallAcc,20)
min(YngOverallAcc)
max(YngOverallAcc)

% 
% OldOverallAcc = zeros(NSim,1);
% for j = 1:NSim
%     Sim = zeros(NTrials,1);
%     for i = 1:NTrials
%         % What positon is it?
%         R = floor(rand(NTrials,1)*NPositions+1);
% 
%         % What is the expected accuracy?
%  [x, y] = ind2sub([NRow,NCol],R(1));
%        
%         % Did they get this correct
%         if (rand() < AccOld(y,x))
%             Sim(i) = 1;
%         end
%     end
%     OldOverallAcc(j) = mean(Sim);
% end
% mean(OldOverallAcc)


% Use this accuracy to predict a random selection


OverallAcc = zeros(NSim,2);
for j = 1:NSim
    Sim = zeros(NTrials,2);
    for i = 1:NTrials
        % What positon is it?
                R = floor(rand(NTrials,1)*NPositions+1);

        % What is the expected accuracy?
        [x, y] = ind2sub([NRow,NCol],R(1));

        % Did they get this correct
        if (rand() < AccOld(y,x))
            Sim(i,2) = 1;
        end
        if (rand() < AccYoung(y,x))
            Sim(i,1) = 1;
        end
    end
    OverallAcc(j,1) = mean(Sim(:,1));
    OverallAcc(j,2) = mean(Sim(:,2));
end
figure(2)
hist(OverallAcc(:,1) - OverallAcc(:,2))
title('Same trials to both groups (Yng - Old)')

figure(1)
hist(YngOverallAcc-OldOverallAcc)
title('Different trials to each group (Yng - Old)')
figure(3)
subplot(1,2,1)
hist(YngOverallAcc)
[min(YngOverallAcc) max(YngOverallAcc)]
subplot(1,2,2)
hist(OldOverallAcc)

[min(OldOverallAcc) max(OldOverallAcc)]
min(OverallAcc)
max(OverallAcc)
min(OverallAcc(:,1) - OverallAcc(:,2))
max(OverallAcc(:,1) - OverallAcc(:,2))
min(YngOverallAcc-OldOverallAcc)
max(YngOverallAcc-OldOverallAcc)




