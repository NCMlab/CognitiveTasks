%BasePath = '/home/jsteffe/Dropbox/SteffenerColumbia/Projects/MyProjects/TaskDifficulty/Stimuli';
BasePath = '/home/jsteffe/Dropbox/SteffenerColumbia/Projects/MyProjects/NeuralCognitiveMapping/';
%BasePath = '/Users/jason/Dropbox/SteffenerColumbia/Projects/MyProjects/NeuralCognitiveMapping/';
%InFolder = fullfile('FRTPsychopyFiles','FRTFaces');
InFolder = '/media/jsteffe/Data001/NeuralCognitiveMapping/FRTPsychopyFiles/CroppedFRTFaces';
OutFolder = fullfile('FRTPsychopyFiles','AdjustedFRTFaces');
cd(BasePath);

%% Find the files
F = dir(fullfile(InFolder,'crop*.JPG'));
Nimage = length(F)
%DegradeLevels = [0:10:90];



% Create Noise versions of all images
newMin = 0;
newMax = 255;
for i = 1:Nimage
    ImageFile = fullfile(F(i).folder,F(i).name);
    [~,InName,InExt] = fileparts(F(i).name);
    
    
    % read the image
    Image = imread(ImageFile);
    % Intensity normalize all images to have the same range of values
    
    
    mmI = mean(mean(Image));
    ssI = std(std(single(Image)));
    
    % Check the size of the image
    [m,n] = size(Image);
    % Is the image the correct size?
    
    %
    fftImage = fft2(Image,m,n);
    magImage = real(fftImage);
    phaseImage = angle(fftImage);
    % Sometimes the surrogate images have wildly different intensities. 
    % I put the while loop in so that only surrogate images within a limit
    % are selected.
    DiffIntensity = 100;
    count = 0;
    while (DiffIntensity > 10) & count < 100
        ShufflePhase = randperm(m*n);
        ShufflePhase = reshape(ShufflePhase,m,n);
        SurrogateNoisePhase = reshape(phaseImage(ShufflePhase),m,n);
        SurrogateImage = real(ifft2(magImage.*exp(1i.*SurrogateNoisePhase)));
        DiffIntensity = abs(mean(mean(Image)) - mean(mean(SurrogateImage)));
        count = count + 1;
    end
    fprintf(1,'Noise for image %s created in %d attempts.\n',InName,count);
    if count >= 100
        warning(sprintf('Problem creating noise for %s\n',ImageFile));
    end
    if i == 1
        figure(i)
        subplot(2,2,1)
        image(Image)
        colormap('gray')
        subplot(2,2,3)
        imagesc(SurrogateImage)
        colormap('gray')
    end
    
        Noise1 = uint8(SurrogateImage);
        %Noise1 = ssI.*Noise1./(ssN);
        
%         ShufflePhase = randperm(m*n);
%         ShufflePhase = reshape(ShufflePhase,m,n);
%         SurrogateNoisePhase = reshape(phaseImage(ShufflePhase),m,n);
%         SurrogateImage = real(ifft2(magImage.*exp(1i.*SurrogateNoisePhase)));
        % Output name
       OutName = sprintf('noise%s%s',InName,'.JPG');
       imwrite(Noise1,fullfile(BasePath,OutFolder,OutName));
       % Make a copy of the original image also
       imwrite(Image,fullfile(BasePath,OutFolder,[InName '.JPG']));
    
end
%%
% First load up all of the images that are cropped AND degraded
% Find the files
F2 = dir(fullfile(BasePath,OutFolder,'*.JPG'));
N2image = length(F2)
% And calculate the mean and STD of all of them.
ImageData = zeros(N2image,2);
for i = 1:N2image
    ImageFile = fullfile(F2(i).folder,F2(i).name);
    % read the image
    Image = imread(ImageFile);
    ImageData(i,1) = mean(mean(Image));
    ImageData(i,2) = std(std(double(Image)));
end


mM = mean(ImageData)
% What are the names with the biggest mean differences from 100?
BigMeanDiff = find(abs(ImageData(:,1) - 100) > 0.5);
F2(BigMeanDiff).name

find(abs(ImageData(:,2) - 5) > 1)
%% Rescale images
MeanIntensity = 100; % I am setting a specific value that I want for each.
% These can be the grand mean values or something I set.
% This allows me to make adjustments without recrating the images each
% time.
StdIntensity = 5;
for i = 1:N2image
    ImageFile = fullfile(BasePath,OutFolder,F2(i).name);
    Image = imread(ImageFile);
%     figure(1)
%     subplot(2,2,1+(i-1)*2)
%     image(Image)
%     colormap('gray')
    CurrentMean = mean(mean(double(Image)));
    CurrentStd = std(std(double(Image)));
    
    scImage = (((double(Image) - CurrentMean)./CurrentStd).*StdIntensity + MeanIntensity);
    mean(mean(scImage))
    scImage2 = ((((Image) - uint8(CurrentMean))./uint8(CurrentStd)).*uint8(StdIntensity) + uint8(MeanIntensity));
    mean(mean(scImage2))
    
    
    CurrentMean = mean(mean(double(scImage)));
    CurrentStd = std(std(double(scImage)));
    scImage = ((double(Image) - CurrentMean)./CurrentStd).*StdIntensity + MeanIntensity;
    mean(mean(scImage))
    
    mean(mean(uint8(scImage)))
%     std(std(scImage))
%     subplot(2,2,2+(i-1)*2)
%     image(scImage)
    
    %scImage = scImage.*(mM(2)+5) + mM(1)+45;
    imwrite(uint8(scImage),ImageFile);

end

mean(mean(Image))
test = (double(Image) - mean(mean(Image)));
mean(mean(test))


%%
InName = 'cropAF03NEHL.JPG';
Image = imread(fullfile(InFolder, InName));  
InName2 = 'cropAF03NEHR.JPG';
Image2 = imread(fullfile(InFolder, InName2)); 

meanI = mean(mean(Image2))
stdI = std(std(double(Image2)))
minI = min(min(Image2))
maxI = max(max(Image2))
newMax = 15;
newMin = 0;
scImage2 = (Image2 - minI)*((newMax - newMin)/(maxI - minI)) + newMin;
    min(min(scImage2))
    max(max(scImage2))
    
meanI = mean(mean(scImage2))
stdI = std(std(double(scImage2)))


scImage3 = (((double(scImage2) - meanI)./stdI).*5 + 100);


mmI = mean(mean(Image))
ssI = std(std(single(Image)))
min(min(Image))
min(min(Image2))
max(max(Image))
max(max(Image2))

    imwrite(uint8(scImage3),'test1.jpg');

    
    figure(1)
    clf
    subplot(321)
    image(Image)
    colormap('gray')
    axis off
    subplot(323)
    image(Image2)
    colormap('gray')
    axis off
        subplot(325)
    image(scImage2)
    colormap('gray')
    axis off
        subplot(326)
    image(scImage3)
    colormap('gray')
    axis off
    