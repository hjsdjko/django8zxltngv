#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class banji(BaseModel):
    __doc__ = u'''banji'''
    __tablename__ = 'banji'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    banji=models.CharField ( max_length=255,null=False,unique=True, verbose_name='班级' )
    renshu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='人数' )
    banzhuren=models.CharField ( max_length=255, null=True, unique=False, verbose_name='班主任' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    banjiweizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='班级位置' )
    '''
    banji=VARCHAR
    renshu=VARCHAR
    banzhuren=VARCHAR
    lianxidianhua=VARCHAR
    banjiweizhi=VARCHAR
    '''
    class Meta:
        db_table = 'banji'
        verbose_name = verbose_name_plural = '班级'
class jiaoshi(BaseModel):
    __doc__ = u'''jiaoshi'''
    __tablename__ = 'jiaoshi'

    __loginUser__='jiaoshigonghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='jiaoshigonghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='是'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    jiaoshigonghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='教师工号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    jiaoshixingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='教师姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    zhaopian=models.TextField   (  null=True, unique=False, verbose_name='照片' )
    zhicheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='职称' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    pquestion=models.CharField ( max_length=255, null=True, unique=False, verbose_name='密保问题' )
    panswer=models.CharField ( max_length=255, null=True, unique=False, verbose_name='密保答案' )
    '''
    jiaoshigonghao=VARCHAR
    mima=VARCHAR
    jiaoshixingming=VARCHAR
    xingbie=VARCHAR
    zhaopian=Text
    zhicheng=VARCHAR
    lianxidianhua=VARCHAR
    pquestion=VARCHAR
    panswer=VARCHAR
    '''
    class Meta:
        db_table = 'jiaoshi'
        verbose_name = verbose_name_plural = '教师'
class xuesheng(BaseModel):
    __doc__ = u'''xuesheng'''
    __tablename__ = 'xuesheng'

    __loginUser__='xuehao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='xuehao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    xuehao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='学号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    xingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    banji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='班级' )
    pquestion=models.CharField ( max_length=255, null=True, unique=False, verbose_name='密保问题' )
    panswer=models.CharField ( max_length=255, null=True, unique=False, verbose_name='密保答案' )
    '''
    xuehao=VARCHAR
    mima=VARCHAR
    xingming=VARCHAR
    xingbie=VARCHAR
    touxiang=Text
    shouji=VARCHAR
    banji=VARCHAR
    pquestion=VARCHAR
    panswer=VARCHAR
    '''
    class Meta:
        db_table = 'xuesheng'
        verbose_name = verbose_name_plural = '学生'
class kemuxinxi(BaseModel):
    __doc__ = u'''kemuxinxi'''
    __tablename__ = 'kemuxinxi'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    kemumingcheng=models.CharField ( max_length=255,null=False,unique=True, verbose_name='科目名称' )
    '''
    kemumingcheng=VARCHAR
    '''
    class Meta:
        db_table = 'kemuxinxi'
        verbose_name = verbose_name_plural = '科目信息'
class kechengxinxi(BaseModel):
    __doc__ = u'''kechengxinxi'''
    __tablename__ = 'kechengxinxi'



    __authTables__={'jiaoshigonghao':'jiaoshi',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    kechengmingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='课程名称' )
    kemumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='科目名称' )
    kechengtupian=models.TextField   (  null=True, unique=False, verbose_name='课程图片' )
    kechengfanwei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='课程范围' )
    kechengjieshao=models.TextField   (  null=True, unique=False, verbose_name='课程介绍' )
    jiaoshigonghao=models.CharField ( max_length=255,null=False, unique=False, verbose_name='教师工号' )
    jiaoshixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师姓名' )
    faburiqi=models.DateField   (  null=True, unique=False, verbose_name='发布日期' )
    '''
    kechengmingcheng=VARCHAR
    kemumingcheng=VARCHAR
    kechengtupian=Text
    kechengfanwei=VARCHAR
    kechengjieshao=Text
    jiaoshigonghao=VARCHAR
    jiaoshixingming=VARCHAR
    faburiqi=Date
    '''
    class Meta:
        db_table = 'kechengxinxi'
        verbose_name = verbose_name_plural = '课程信息'
class qiandaojilu(BaseModel):
    __doc__ = u'''qiandaojilu'''
    __tablename__ = 'qiandaojilu'



    __authTables__={'jiaoshigonghao':'jiaoshi','xuehao':'xuesheng',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='回复'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    kechengmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='课程名称' )
    qiandaomingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='签到名称' )
    qiandaotupian=models.TextField   ( null=False, unique=False, verbose_name='签到图片' )
    qiandaoshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='签到时间' )
    jiaoshigonghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师工号' )
    qiandaobeizhu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='签到备注' )
    xuehao=models.CharField ( max_length=255,null=False, unique=False, verbose_name='学号' )
    banji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='班级' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    '''
    kechengmingcheng=VARCHAR
    qiandaomingcheng=VARCHAR
    qiandaotupian=Text
    qiandaoshijian=DateTime
    jiaoshigonghao=VARCHAR
    qiandaobeizhu=VARCHAR
    xuehao=VARCHAR
    banji=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'qiandaojilu'
        verbose_name = verbose_name_plural = '签到记录'
class qingjiajilu(BaseModel):
    __doc__ = u'''qingjiajilu'''
    __tablename__ = 'qingjiajilu'



    __authTables__={'jiaoshigonghao':'jiaoshi','xuehao':'xuesheng',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    kechengmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='课程名称' )
    kechengtupian=models.TextField   (  null=True, unique=False, verbose_name='课程图片' )
    jiaoshigonghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师工号' )
    jiaoshixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师姓名' )
    qingjiashijian=models.DateField   (  null=True, unique=False, verbose_name='请假时间' )
    qingjiayuanyin=models.CharField ( max_length=255, null=True, unique=False, verbose_name='请假原因' )
    xuehao=models.CharField ( max_length=255,null=False, unique=False, verbose_name='学号' )
    banji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='班级' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    kechengmingcheng=VARCHAR
    kechengtupian=Text
    jiaoshigonghao=VARCHAR
    jiaoshixingming=VARCHAR
    qingjiashijian=Date
    qingjiayuanyin=VARCHAR
    xuehao=VARCHAR
    banji=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'qingjiajilu'
        verbose_name = verbose_name_plural = '请假记录'
class xueshengkaoqin(BaseModel):
    __doc__ = u'''xueshengkaoqin'''
    __tablename__ = 'xueshengkaoqin'



    __authTables__={'xuehao':'xuesheng','jiaoshigonghao':'jiaoshi',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    kechengmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='课程名称' )
    kaoqinqingkuang=models.CharField ( max_length=255,null=False, unique=False, verbose_name='考勤情况' )
    kaoqinshuoming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='考勤说明' )
    kaoqinriqi=models.DateField   (  null=True, unique=False, verbose_name='考勤日期' )
    xuehao=models.CharField ( max_length=255,null=False, unique=False, verbose_name='学号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    banji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='班级' )
    jiaoshigonghao=models.CharField ( max_length=255,null=False, unique=False, verbose_name='教师工号' )
    '''
    kechengmingcheng=VARCHAR
    kaoqinqingkuang=VARCHAR
    kaoqinshuoming=VARCHAR
    kaoqinriqi=Date
    xuehao=VARCHAR
    xingming=VARCHAR
    banji=VARCHAR
    jiaoshigonghao=VARCHAR
    '''
    class Meta:
        db_table = 'xueshengkaoqin'
        verbose_name = verbose_name_plural = '学生考勤'
class kaoqintongji(BaseModel):
    __doc__ = u'''kaoqintongji'''
    __tablename__ = 'kaoqintongji'



    __authTables__={'jiaoshigonghao':'jiaoshi',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    kaoqinriqi=models.DateField   (  null=True, unique=False, verbose_name='考勤日期' )
    kechengmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='课程名称' )
    zhengchangrenshu=models.IntegerField  (  null=True, unique=False, verbose_name='正常人数' )
    chidaorenshu=models.IntegerField  (  null=True, unique=False, verbose_name='迟到人数' )
    qingjiarenshu=models.IntegerField  (  null=True, unique=False, verbose_name='请假人数' )
    kuangkerenshu=models.IntegerField  (  null=True, unique=False, verbose_name='旷课人数' )
    zaotuirenshu=models.IntegerField  (  null=True, unique=False, verbose_name='早退人数' )
    jiaoshigonghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师工号' )
    jiaoshixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师姓名' )
    '''
    kaoqinriqi=Date
    kechengmingcheng=VARCHAR
    zhengchangrenshu=Integer
    chidaorenshu=Integer
    qingjiarenshu=Integer
    kuangkerenshu=Integer
    zaotuirenshu=Integer
    jiaoshigonghao=VARCHAR
    jiaoshixingming=VARCHAR
    '''
    class Meta:
        db_table = 'kaoqintongji'
        verbose_name = verbose_name_plural = '考勤统计'
class kaoqintixing(BaseModel):
    __doc__ = u'''kaoqintixing'''
    __tablename__ = 'kaoqintixing'



    __authTables__={'xuehao':'xuesheng',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    tongzhibiaoti=models.CharField ( max_length=255,null=False, unique=False, verbose_name='通知标题' )
    tongzhineirong=models.TextField   (  null=True, unique=False, verbose_name='通知内容' )
    tongzhiriqi=models.DateField   (  null=True, unique=False, verbose_name='通知日期' )
    xuehao=models.CharField ( max_length=255,null=False, unique=False, verbose_name='学号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    '''
    tongzhibiaoti=VARCHAR
    tongzhineirong=Text
    tongzhiriqi=Date
    xuehao=VARCHAR
    xingming=VARCHAR
    shouji=VARCHAR
    '''
    class Meta:
        db_table = 'kaoqintixing'
        verbose_name = verbose_name_plural = '考勤提醒'
class syslog(BaseModel):
    __doc__ = u'''syslog'''
    __tablename__ = 'syslog'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    username=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户名' )
    operation=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户操作' )
    method=models.CharField ( max_length=255, null=True, unique=False, verbose_name='请求方法' )
    params=models.TextField   (  null=True, unique=False, verbose_name='请求参数' )
    time=models.BigIntegerField  (  null=True, unique=False, verbose_name='请求时长(毫秒)' )
    ip=models.CharField ( max_length=255, null=True, unique=False, verbose_name='IP地址' )
    '''
    username=VARCHAR
    operation=VARCHAR
    method=VARCHAR
    params=Text
    time=BigInteger
    ip=VARCHAR
    '''
    class Meta:
        db_table = 'syslog'
        verbose_name = verbose_name_plural = '系统日志'
class systemnotice(BaseModel):
    __doc__ = u'''systemnotice'''
    __tablename__ = 'systemnotice'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    '''
    content=Text
    '''
    class Meta:
        db_table = 'systemnotice'
        verbose_name = verbose_name_plural = '系统公告'
