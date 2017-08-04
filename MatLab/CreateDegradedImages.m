% Load up each image and its partner
% For each image do the following:
% Make black and white
% Make flipped version of it
% Make degraded versions of the image and its flipped version
% The result is:
% Original, 0 noise
% Flipped, 0 noise

BasePath = '/Users/jason/Dropbox/SteffenerColumbia/UOttawa/Students/Current/CourtneyGuy/FaceMatchExperiment/AllFaces';
OutFolder = 'Degraded';
cd(BasePath);
% Find the files
F = dir('*.jpg');
Nimage = length(F);
DegradeLevels = [0 12:12:72];

NdegradeLevels = length(DegradeLevels);

for i = 1:Nimage
    ImageFile = fullfile(BasePath,F(i).name);
    [~,InName,InExt] = fileparts(F(i).name)
    % Trim the orientation from the name
    funder = findstr(InName,'_');
    InNameShort = InName(funder+1:end);
    % read the image
    I = imread(ImageFile);
    [m,n,p] = size(I);
    Npix = m*n;
    
    % What is its luminosity?
    OrigLum = sum(sum(I(:,:,1).*0.299 + I(:,:,2).*0.587 + I(:,:,3).*0.114))./Npix;
    % convert to black and white
    Ibw = rgb2gray(I);
    BWlum = sum(sum(Ibw))/Npix;
    DegradedImages = uint8(zeros(m,n,NdegradeLevels,2)); %Left in 1 and right in 2
    
    % Determine if the face is left or right
    LeftFlag = 0;
    
    if ~isempty(strfind(InName,'left'))
        LeftFlag = 1;
    end
    for j = 1:NdegradeLevels
        % Find pixels to degrade
        % create list of random numbers
        PickPixelsToDegrade = randperm(Npix);
        
        % take a percentage of them based on the degrade levels
        NpixToDegrade = floor(Npix*DegradeLevels(j)./100);
        % create a list of random pixel values
        RandomNoise = rand(NpixToDegrade,1)*255;
        PixToDegrade = PickPixelsToDegrade(1:NpixToDegrade);
        
        temp = Ibw;
        temp(PixToDegrade) = RandomNoise;
        % Ensure the luminosity is preserved
        tempLum = sum(sum(temp))/Npix;
        % Correct the lum
        LumCorrection = BWlum/tempLum;
        % Also create flipped versions of the images        
        if LeftFlag
            DegradedImages(:,:,j,1) = temp.*LumCorrection;
            DegradedImages(:,:,j,2) = fliplr(temp.*LumCorrection);
        else
            DegradedImages(:,:,j,2) = temp.*LumCorrection;
            DegradedImages(:,:,j,1) = fliplr(temp.*LumCorrection);
        end
        % Write out the images
        % Write left
        OutName = fullfile(BasePath,OutFolder,sprintf('left_%s_Degrade_%03d.jpg',InNameShort,DegradeLevels(j)));
        imwrite(DegradedImages(:,:,j,1),OutName)
        % Write right
        OutName = fullfile(BasePath,OutFolder,sprintf('right_%s_Degrade_%03d.jpg',InNameShort,DegradeLevels(j)));
        imwrite(DegradedImages(:,:,j,2),OutName)
        
        
    end
end


