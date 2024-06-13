function[] = batch_mike_cut(do_normalise)
%initial parameters
TH = 80; expected_frames = 390; max_frame_error = 10;
%files
filepath{1} = 'C:\Mike_data\17_01_24 (cage 1 day 2)\mouse1';
filepath{2} = 'C:\Mike_data\17_01_24 (cage 1 day 2)\mouse3';
filepath{3} = 'C:\Mike_data\17_01_24 (cage 1 day 2)\mouse5';
filepath{4} = 'C:\Mike_data\18_01_24 (cage 2 day 2)\mouse9';
filepath{5} = 'C:\Mike_data\18_01_24 (cage 2 day 2)\mouse10';
filepath{6} = 'C:\Mike_data\18_01_24 (cage 3 day 2)\mouse11';
filepath{7} = 'C:\Mike_data\19_01_24 (cage 3 day 2)\mouse14';
filepath{8} = 'C:\Mike_data\19_01_24 (cage 3 day 2)\mouse15';
filepath{9} = 'C:\Mike_data\24_01_24 (cage 4 day 2)\mouse18';
filepath{10} = 'C:\Mike_data\24_01_24 (cage 4 day 2)\mouse20';













Nfolder = numel(filepath);
count_folder = 0;
for n = 1:Nfolder
    filename = dir(filepath{n});
    filename = filename(3:end);
    filename_track = []; count = 0;
    for m = 1:numel(filename)
        try
            if strcmp(filename(m).name(1:12),'tracked_data')
               count = count+1;
               filename_track{count} = filename(m).name;
            end
        end
    end
    speed = [];
    for m = 1:numel(filename_track)
        load([filepath{n} '\' filename_track{m}],'idx','idy')
        temp = mike_cut_trials(idx,idy,TH,expected_frames,max_frame_error, false);
        if numel(temp>0)
           temp = temp(1:expected_frames-max_frame_error-1);
           speed = [speed; temp];
        end
    end
    if size(speed)>0
       count_folder = count_folder+1; 
       if do_normalise
          mean_speed(count_folder,:) = (mean(speed,1)-mean(speed(:)))/std(speed(:));
       else
          mean_speed(count_folder,:) = mean(speed,1); 
       end
    else
       disp(sprintf('filepath %s not enough frames for estimating speed',filepath{n}));
    end
end
%create and name figure
hFig = figure;
    set(hFig, 'Name', 'Group 1, Day 2');
plot(mean(mean_speed));
xlabel('Frame Number');
ylabel('Mean Speed');
ymin = -2;
ymax = 2.5;
ylim([ymin,ymax]);

hold on

