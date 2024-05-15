from Crypto.Util.number import *

n = 14894221488742104297564620279942321819592244203466365036793164073415923227955362883846969512096120696095106667974354014475015056834048178708874909888933310502846634413362675161306315983430839323108364668056034605434869821876403929961362561782405464650231397217237165308952119879371715907095038912758119538725017237257529457808416061294210175343483957805139524151129612682582993289236350226397186367412303670591591442208798476812771097011988474970167358418978655435689705977320938284037700475756348484556475497499832666885909483983322624364542416880933723017903694567484678829046177497173423486651265700092794414972699
e = 65537
c = 12542122223463876497080816468940951542514552839312841191928922138670590594622041573160957859495907293498374037501237188549653012821405940180804139557425255762130222402008491010969713045778058280889927033966646355054620146164230694698046733379962625558477998675545674584364936345618592032471056990971318598515123929551207980028248619652764565497391341945831761336005768266416725572862773418900859916876475126285899339233051520862405329032674481001311697857778974884418852469700322052073729271343078257223356092813327186501836069830484813273988536285788021909621898621996437926054653667813366683079303258089797512391246
hint = 245064644271350707780799845874774560310440813845840572074209092087345119089436313990872774503126329006547570070326904835374922478817668549192211519593188430117065816361487731151252756475903721825922868188427498792479143605266219865286238646963241639116930719429841515772721726325986940247904619412391120871036

phi = n - hint + 1

d = pow(e, -1, phi)

m = pow(c, d, n)

print(long_to_bytes(m).decode())