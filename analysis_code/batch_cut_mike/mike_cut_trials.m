function[mean_speed] = mike_cut_trials(idx,idy,TH,expected_frames,max_frame_error,make_graphs)
N = numel(idx);
dist = [0 sqrt((diff(idx).^2) + (diff(idy).^2))];
[peak, indpeak] = findpeaks(dist,'Threshold',TH);
Npeak = numel(peak);
duration = []; count = 0;
speed = []; speed_length = [];
for n = 1:Npeak
    if n == 1
       duration = indpeak(1);
       temp = dist(1:indpeak(1));
    elseif n == Npeak
       duration = [duration N-indpeak(end)];
       temp = dist(indpeak(n)+1:N);
    else
       duration = [duration indpeak(n)-indpeak(n-1)]; 
       temp = dist(indpeak(n-1)+1:indpeak(n));  
    end
    if abs(duration(n)-expected_frames)<max_frame_error
       count = count+1;
       speed{count} = temp;
       speed_length(count) = numel(temp);
    end
end
min_length = min(speed_length)-1;
if numel(speed)<10
   mean_speed = [];
   disp('too many frames lost, cannot continue');
   return;
end
for n = 1:numel(speed)
    speed{n} = speed{n}(1:min_length);
end
speed = vertcat(speed{:});
mean_speed = mean(speed,1);
%figures;
if make_graphs
    %
    figure; hold on;
    plot(dist); 
    plot(indpeak,peak,'.r','MarkerSize',12);
    ylabel('speed'); xlabel('time bin')
    %
    figure; hold on;
    bar(duration,'BarWidth',0.5);
    line([0 N/expected_frames],(expected_frames-max_frame_error)*[1 1],'Color','r');
    line([0 N/expected_frames],(expected_frames+max_frame_error)*[1 1],'Color','r');
    ylabel('trial duration'); xlabel('#trial');
    %
    figure; hold on;
    p = pcolor(speed); set(p,'LineStyle','none');
    title('speed'); ylabel('#trial'); xlabel('time bin');
    %
    figure; hold on;
    plot(mean(speed));
    ylabel('mean speed');
end