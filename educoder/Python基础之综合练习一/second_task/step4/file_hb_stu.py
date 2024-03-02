class Solution():
    def solve(self, file_1, file_2, file_3):
        '''
        :type file_1, file_2, file_3: str
        :rtype : None
        '''
        #请在此添加代码，实现将文件file_1和file_2中的数字按从小到大的顺序，写入文件file_3中
        #********** Begin *********#
        f1,f2,f3=open(file_1),open(file_2),open(file_3,'w')
        l=f1.readlines()
        l+=f2.readlines()
        l=list(map(int,l))
        l.sort()
        l=list(map(str,l))
        f3.write('\n'.join(l))
        ##********** End *********#