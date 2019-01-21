# class Reception():
#     number=0
#     time=0
#     onoff=0
#     customer=[]

# class Repair():
#     number=0
#     time=0
#     onoff=0
#     customer=[]

# class Customer():
#     number=0
#     tk=0
#     rcin=0
#     rpdochak=0
#     rpin=0
#     rc=0
#     rp=0

# for T in range(int(input())):
#     n,m,k,a,b=list(map(int,input().split()))
#     al=list(map(int,input().split()))
#     bl=list(map(int,input().split()))
#     tl=list(map(int,input().split()))
#     rcl=[]
#     rpl=[]
#     csl=[]
#     for i in range(len(al)):
#         r=Reception()
#         r.time=al[i]
#         r.number=i+1
#         rcl.append(r)
#     for j in range(len(bl)):
#         p=Repair()
#         p.time=bl[j]
#         p.number=j+1
#         rpl.append(p)
#     for x in range(len(tl)):
#         t=Customer()
#         t.number=x+1
#         tk=tl[x]
#         csl.append(t)
#     t=0
#     answerl=[]
#     rcdaegi=[]
#     rpdaegi=[]
#     goodbye=[]
#     while 1:
#         if len(goodbye)==k:
#             break
#         dell=[]
#         for cu in range(len(csl)):
#             if csl[cu].tk==t:
#                 rcdaegi.append(csl[cu])
#                 dell.append(cu)
#         for outrc in rcl:
#             if outrc.onoff==1 and outrc.customer[0].rcin+outrc.time==t:
#                 rpdaegi.append(outrc.customer[0])
#                 del outrc.customer[0]
#                 outrc.onoff=0
#         for outrp in rpl:
#             if outrp.onoff==1 and outrp.customer[0].rpin+outrp.time==t:
#                 goodbye.append(outrp.customer[0])
#                 del outrp.customer[0]
#                 outrp.onoff=0
#         for rcd in range(len(rcdaegi)):
#             for rcnugu in rcl:
#                 if rcnugu.onoff==0:
#                     rcnugu.onoff=1
#                     minnum=1001
#                     index1=0
#                     for cn in range(len(rcdaegi)):
#                         if minnum>rcdaegi[cn].number:
#                             minnum=rcdaegi[cn].number
#                             index1=cn
#                     rcdaegi[index1].rc=rcnugu.number
#                     rcnugu.customer.append(rcdaegi[index1])
#                     del rcdaegi[index1]
#         for rpd in range(len(rpdaegi)):
#             for rpnugu in rpl:
#                 if rpnugu.onoff==0:
#                     rpnugu.onoff=1
#                     mintime=1001
#                     minnum=21
#                     reli=[]
#                     for cnn in range(len(rpdaegi)):
#                         if mintime>=rpdaegi[cnn].rpdochak:
#                             mintime=rpdaegi[cnn].rpdochak
#                     for cnn in range(len(rpdaegi)):
#                         if mintime==rpdaegi[cnn].rpdochak:
#                             reli.append(cnn)
#                     index2=0
#                     for last in reli:
#                         if minnum>rpdaegi[last].rc:
#                             index2=last
#                             minnum=rpdaegi[last].rc
#                     rpdaegi[index2].rp=rpnugu.number
#                     rpnugu.customer.append(rpdaegi[index2])
#                     del rpdaegi[index2]
#         t+=1
#         print(len(goodbye))
#     summary=0
#     for sibal in goodbye:
#         if sibal.rc==a and sibal.rp==b:
#             summary+=sibal.number
#     if summary==0:
#         summary=-1
#     print(f'#{T+1} {summary}')

# 실패!