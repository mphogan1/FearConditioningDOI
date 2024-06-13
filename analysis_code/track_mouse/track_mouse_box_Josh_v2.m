function[idx, idy] = track_mouse_box_Josh_v2(filename, filepath, graph, do_save)
%filename = 'fc2_save_camera1_mouse3_2022-11-05-160035-0000';
%filepath = 'C:\Mike_data\10_01_24 (cage 1 day 1)\mouse3';
%To look at videos graph = true, to save data do_save = true

block_size = 100; %num images per block
Nx = 1280; Ny = 1024; box_length = 200; %box size

%get images filenames
filesave_track = [filepath '\tracked_data_' filename(1:end-4) '.mat'];
filesave_movie = [filepath '\tracked_movie_' filename(1:end-4) '.avi'];

%load background
%filename_bg = [filepath '\camera' num2str(which_camera) '\bg.avi'];
obj_bg = VideoReader([filepath '\' filename]);

%load timestamps files
N = obj_bg.NumFrames;
Nblock = ceil(N/block_size); %num block of images


%define two filters respectively for colour and silouhette smoothing
Nmask = 15; Nmask_large = 30;
wind = gausswin(Nmask)*gausswin(Nmask)';
wind = wind/sum(wind(:));

%initialise video writing
if do_save
    v = VideoWriter(filesave_movie);
    set(v,'FrameRate',15); 
    open(v); 
end

%get background images
Nbg = obj_bg.NumFrames;
count_bg = 0;
for n = 1:100:Nbg
    try
    %LOAD IMAGE
    %x0 = obj_bg.readFrame;
    x0 = read(obj_bg, n);
    x = mean(double(x0),3);
    x = x/mean(x(:));
    [Ny, Nx] = size(x);
    
    %AVERAGE BGs
    if n == 1
       mx = x; 
    else
       mx = mx+x; 
    end
    count_bg = count_bg+1;
    disp(sprintf('bg %s',num2str(n)));
    catch
    end
end

mx = mx/count_bg; 
%SMOOTH BGs
mx = filter2(wind,double(mx)); 

%fig
if graph
   fig = figure;
   h = subplot(1,1,1);
end

%init indexes
idx = zeros(1,N); idy = zeros(1,N);
idx_box = zeros(1,N); idy_box = zeros(1,N);


n = 1; 
idx = zeros(1,N); idy = zeros(1,N);
xlow = zeros(1,N); xhigh = zeros(1,N);
ylow = zeros(1,N); yhigh = zeros(1,N);
for nb = 1:Nblock
    try
    %open the object
    obj = VideoReader([filepath '\' filename]);
    id_frame = [(nb-1)*block_size+1 nb*block_size];
    if nb*block_size > N
       id_frame(2) = N;
    end
    x0 = read(obj, id_frame); 
    
    %blockwise extraction
    for m = 1:block_size
        n = (nb-1)*block_size+m;
        if n > N
           break
        else
            %LOAD IM
            %load nth image
            x = mean(double(squeeze(x0(:,:,:,m))),3);
            x = x/mean(x(:));

            %GET SILOUHETTE
            %filter brightness
            x = filter2(wind,x); 
            %subtract brightness map
            x = x-mx; 

            %brightness threshold (look for dark object)
            th = quantile(x(:),0.01);
            xs = double(x<th);

            %get marker position & color ratio
            [idxtemp,idytemp] = find(xs==1);
            idx(n) = median(idxtemp); 
            idy(n) = median(idytemp);
            
            %set the box limit
            xlow(n) = idy(n)-box_length;
            xhigh(n) = idy(n)+box_length;
            ylow(n) = idx(n)-box_length;
            yhigh(n) = idx(n)+box_length;
            if xlow(n)<1
               xhigh(n) = xhigh(n)-xlow(n)+1;
               xlow(n) = 1;
            end
            if xhigh(n)>Nx
               xlow(n) = xlow(n)-(xhigh(n)-Nx);
               xhigh(n) = Nx;
            end
            if ylow(n)<1
               yhigh(n) = yhigh(n)-ylow(n)+1;
               ylow(n) = 1;
            end
            if yhigh(n)>Ny
               ylow(n) = ylow(n)-(yhigh(n)-Ny);
               yhigh(n) = Ny;
            end
            
            %extract patch
            if do_save
               writeVideo(v,x0([ylow(n):yhigh(n)],[xlow(n):xhigh(n)],:,m));  
            end
            
            %FIGURE
            if graph
                isbox = 1;            
                imshow(rgb2gray(squeeze(x0(:,:,:,m)))); 
                hold on;
                plot(idy(n),idx(n),['.g'],'MarkerSize',12);
                if isbox
                   xlim([xlow(n) xhigh(n)]);
                   ylim([ylow(n) yhigh(n)]);
                end
                title(sprintf('frame %s, sizeX: %s, sizeY: %s',num2str(n),num2str(xhigh(n) - xlow(n)),num2str(yhigh(n) - ylow(n))));
                drawnow; pause(0.01); 
            end
        end

        %DISPLAY
        disp(sprintf('frame %s',num2str(n)));
        
    end
    
    %clear
    if graph
       clf
    end
    clear obj;
    catch
    end
end
%SAVE
if do_save
   save(filesave_track,'idy','idx','xlow','xhigh','ylow','yhigh');
   close(v);
end
