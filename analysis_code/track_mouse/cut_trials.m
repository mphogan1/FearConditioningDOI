function[] = cut_trials(idx,idy,Ntrial)
fs = 30;
dy = diff(idy).^2;
dx = diff(idx).^2;
dist = [0 sqrt(dx+dy)];


 [peak,ind] = findpeaks(dist,'MinPeakHeight',100);

figure;hold on;
plot(dist);
plot(ind,peak,'.r');

'a'

% 
% 
% 
% 
% Ntot = numel(idx);
% Nexpt = 11700;
% if Ntot/Nexpt < 0.97
%     disp('too many frames lost')
%     dist2 = [];
%     return
% else
%     Nframes_trial = floor(Ntot/Ntrial);
%     for n = 1:Ntrial
%         dist2(n,:) = dist((n-1)*Nframes_trial+1:n*Nframes_trial);
%     end
% end
% 
% % 
% % 
% % 
% % Nframes_trial = floor(Ntot/Ntrial);
% % id_expt = [Nframes_trial:Nframes_trial:Ntot];
% % dN = 100;
% % TH = 80;
% % id_cut = zeros(1,Ntrial);
% % id_cut(end) = Ntot;
% % indpeak = find((dist>TH));
% % for n = 1:Ntrial-1
% %      indtemp = indpeak(find((indpeak>n*Nframes_trial-dN)&(indpeak<n*Nframes_trial+dN)));
% %      if numel(indtemp)==0
% %         id_cut(n) = round(n*Nframes_trial);
% %      else 
% %         id_cut(n) = indtemp(1);
% %      end
% % end
% % %fig
% % figure; hold on;
% % plot(dist);
% % plot(id_cut,dist(id_cut),'*r','MarkerSize',20);
% % 
% % %break down the trials
% % dist1 = cell(1,Ntrial);
% % dist1{1} = dist(1:id_cut(1));
% % L(1) = numel(dist1{1});
% % for n = 2:Ntrial
% %     dist1{n} = dist(id_cut(n-1)+1:id_cut(n));
% %     L(n) = numel(dist1{n});
% % end
% % minL = min(L);
% % for n = 1:Ntrial
% %     dist2(n,:) = dist1{n}(1:minL);
% % end
% 
% %fig
% t = ([1:Nframes_trial]/fs)-5;
% figure;
% plot(t,mean(dist2));
% xlim([-3 6]);