#函数
import fun1
import random
import numpy as np
# V=2
# C=4

#初始值
year = 10                   #进化次数
yilunpk = 4                 #随机pk多少次再进行整体去除繁殖进化
minp = 0                    #最小食物，小于即死亡

ying = 10                   #鹰种群数量
ge = 20                     #鸽子种群数量

families = ying+ge               #种群个体数
families_shuxing = 5       #个体属性数（个体编号，是否存活，个体分数,属性1为鹰0为鸽,选择逃跑or斗争0/1）
no_ = 0 #个体序号
families_ = families        #剩余种群个体数
yilundead = families/2               #一轮（pk yilunpk次）默认死亡数


#创建一个种群
par = np.ones((families,families_shuxing),dtype=np.int64)
no_ -= 1

for i in range(ying):
    no_ +=1
    i = no_
    par[i] = i,1,10,1,0
    pass
for i in range(ge):
    no_ +=1
    i = no_
    par[i] = i,1,10,0,0
    pass



print(par)

#主循环
for i in range(year):
    families_ = families
    print(families_,"families_")#剩余种群个体数
    list0 = list(range(families))
    deadn = 0
    for i in range(yilunpk):

        families_ = 0
        for i in range(families):             # 存活存货人数
            if par[i, 1] == 1:
                families_ += 1
            else:
                print("有人死亡",i)
            pass

        if families_ % 2 == 1:           # 存活人数求偶,如果是偶数那么会剩最后一个不被pk
            families_ -= 1
            pass
        print(families_)
        random.shuffle(list0)  #防止每次都是同一个落单
        list1 = list0[0:int(families_ / 2)]  # pk顺序
        list2 = list0[int(families_ / 2 ): int(families_)+1]
        print(len(list1),"list1")
        print(len(list2),"list2")
        random.shuffle(list1)
        random.shuffle(list2)
        for i in range(int(families_/2)):   #进行一轮所有存活的两两pk，并记录这一轮中分数最少的那一个个体的no_ 和最低分数
            a = list2[i]
            b = list1[i]
            x1,x2,x3,x4,x5 = par[a]
            y1,y2,y3,y4,y5 = par[b]
            x3,y3 = fun1.pk(x4,y4,x3,y3)
            par[a] = x1,x2,x3,x4,x5
            par[b] = y1,y2,y3,y4,y5
            if y3<=minp:
                minn = b
                par[minn, 1] = 0
                list0.remove(minn)
                deadn+=1
                pass
            elif x3<=minp:
                minn = a
                par[minn, 1] = 0
                list0.remove(minn)
                deadn+=1
            pass
        pass    #把一轮所有人员两两pk最低分数从family移除，并进行下一次的记录存活人数，当存活人数>存活人数/2+1又开始全部两两pk并把最低分数从family移除，直到family被削减到三分之一
    par_ =  par[np.lexsort(-par.T[:2,:])]##排序，将已经死亡的人堆在下面  （这个默认是升序排序，故-1会被排到0的上面）
    par_ = par_[:len(list0),:]##切割表格，将死亡的人排除
    sorted_indices = np.argsort(par_[:, 2])
    # 使用索引数组恢复原来的二维数组
    par_ = par_[sorted_indices]
    print("pk后并升序排序后的数组")
    print(par_)
    if deadn<yilundead:
        a=int(yilundead-deadn)
        par_ = par_[a:,:]
        b=par_[-a:,3:4]
        for i in range(a):
            m=b[i]
            m = m[0]
            print(m,"小于deadn")
            par_1 = np.ones((1, 5), dtype = np.int64)
            par_1[0] = no_ + 1, 1, 10, m, 0
            par_ = np.concatenate((par_, par_1))  # 把新的子代合并到父代的最下方
            no_+=1
            pass
    if deadn>=yilundead:
        # 需要一个如果deadn大于family-deadn的if
        b = par_[-deadn :, 3 :4]
        # print(deadn,"deadn")
        # print(b,"zuida")
        for i in range(deadn):
            m=b[i]
            m=m[0]
            par_1 = np.ones((1,5),dtype=np.int64)
            par_1[0] = no_ + 1, 1, 10, m, 0
            par_ = np.concatenate((par_, par_1))  # 把新的子代合并到父代的最下方
            no_+=1
            pass
        pass
    print("去除并繁殖后的数组")
    print(par_)
    for i in range(int(families-1)):
        par_[i, 2] = 10
        pass
    par = par_  ##传递表格
    print("最后的数组")
    print(par)
    np.savetxt("ans1.txt", par, fmt = "%d", delimiter = "------")  ##保存结果，写到文件里面

























