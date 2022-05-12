import re

# a simple regex script to extract result from the log

file_pwd = "/content/pretrain_log.txt" # adjust the file path
f = open(file_pwd).read()

#loss_ce loss_tr prec
pat1 = re.compile(r'Epoch:\s*\[\d*\].*Loss_ce\s*\d*\.\d*\s*\((\d*\.\d*)\)\s*Loss_tr\s*\d*\.\d*\s*\((\d*\.\d*)\)\s*Prec.*\((\d*\.\d*)\%\)')  
result1 = pat1.findall(f)  
loss_ce = []
loss_tr = []
prec = []
for i in range(len(result1)):
    if (i+1) % 10 == 0:
        loss_ce.append(result1[i][0])
        loss_tr.append(result1[i][1])
        prec.append(result1[i][2])

print(loss_ce)
print(loss_tr)
print(prec)

pat2 = re.compile(r'Mean\sAP\:\s(\d*\.\d*)\%\s*CMC\sScores\:\s*top-1\s*(\d*\.\d*)\%\s*top-5\s*(\d*\.\d*)\%\s*top-10\s*(\d*\.\d*)\%')  
result2 = pat2.findall(f)  

mean_ap = []
top1 = []
top5 = []
top10 = []
for i in range(len(result2)):
    mean_ap.append(result2[i][0])
    top1.append(result2[i][1])
    top5.append(result2[i][2])
    top10.append(result2[i][3])

print(mean_ap,top1,top5,top10)


file_pwd = "/content/log.txt"
f = open(file_pwd).read()

pat1 = re.compile(r'Epoch:\s*\[\d*\].*Loss_ce\s*\d*\.\d*\s*\/\s*(\d*\.\d*)\s*Loss_tri\s*\d*\.\d*\s*\/\s*(\d*\.\d*)\s*Loss_ce_soft\s*(\d*\.\d*)\s*Loss_tri_soft\s*(\d*\.\d*)\s*Prec\s*\d*\.\d*\%\s*\/\s*(\d*\.\d*)\%')
result1 = pat1.findall(f)
loss_ce = []
loss_tr = []
loss_ce_soft = []
loss_tri_soft = []
prec = []
for i in range(len(result1)):
    if (i+1) % 400 == 0:
        loss_ce.append(result1[i][0])
        loss_tr.append(result1[i][1])
        loss_ce_soft.append(result1[i][2])
        loss_tri_soft.append(result1[i][3])
        prec.append(result1[i][4])


print(len(loss_ce))
print(loss_tr)
print(loss_ce_soft)
print(loss_tri_soft)
print(prec)

pat2 = re.compile(r'Mean\sAP\:\s(\d*\.\d*)\%\s*\*\s*Finished')
mean_ap = pat2.findall(f)

print(mean_ap)