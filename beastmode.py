
for tld in {com,net,org}
do
	# US postal abbreveations
	for x in {al,ak,az,ar,ca,co,ct,de,fl,ga,hi,id,il,in,ia,ks,ky,la,me,md,ma,mi,mn,ms,mo,mt,ne,nv,nh,nj,nm,ny,nc,nd,oh,ok,or,pa,ri,sc,sd,tn,tx,ut,vt,va,wa,wv,wi,wy,dc,as,gu,mp,pr,vi}
	do
		# main="${x}vaccinate"
		echo "${x}vaccinate.$tld" 
	done
done

