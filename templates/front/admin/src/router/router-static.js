import Vue from 'vue';
//配置路由
import VueRouter from 'vue-router'
Vue.use(VueRouter);
//1.创建组件
import Index from '@/views/index'
import Home from '@/views/home'
import Login from '@/views/login'
import NotFound from '@/views/404'
import UpdatePassword from '@/views/update-password'
import pay from '@/views/pay'
import register from '@/views/register'
import center from '@/views/center'
    import qiandaojilu from '@/views/modules/qiandaojilu/list'
    import kaoqintixing from '@/views/modules/kaoqintixing/list'
    import qingjiajilu from '@/views/modules/qingjiajilu/list'
    import xuesheng from '@/views/modules/xuesheng/list'
    import kemuxinxi from '@/views/modules/kemuxinxi/list'
    import jiaoshi from '@/views/modules/jiaoshi/list'
    import xueshengkaoqin from '@/views/modules/xueshengkaoqin/list'
    import syslog from '@/views/modules/syslog/list'
    import banji from '@/views/modules/banji/list'
    import systemnotice from '@/views/modules/systemnotice/list'
    import kechengxinxi from '@/views/modules/kechengxinxi/list'
    import kaoqintongji from '@/views/modules/kaoqintongji/list'


//2.配置路由   注意：名字
export const routes = [{
    path: '/',
    name: '系统首页',
    component: Index,
    children: [{
      // 这里不设置值，是把main作为默认页面
      path: '/',
      name: '系统首页',
      component: Home,
      meta: {icon:'', title:'center', affix: true}
    }, {
      path: '/updatePassword',
      name: '修改密码',
      component: UpdatePassword,
      meta: {icon:'', title:'updatePassword'}
    }, {
      path: '/pay',
      name: '支付',
      component: pay,
      meta: {icon:'', title:'pay'}
    }, {
      path: '/center',
      name: '个人信息',
      component: center,
      meta: {icon:'', title:'center'}
    }
      ,{
	path: '/qiandaojilu',
        name: '签到记录',
        component: qiandaojilu
      }
      ,{
	path: '/kaoqintixing',
        name: '考勤提醒',
        component: kaoqintixing
      }
      ,{
	path: '/qingjiajilu',
        name: '请假记录',
        component: qingjiajilu
      }
      ,{
	path: '/xuesheng',
        name: '学生',
        component: xuesheng
      }
      ,{
	path: '/kemuxinxi',
        name: '科目信息',
        component: kemuxinxi
      }
      ,{
	path: '/jiaoshi',
        name: '教师',
        component: jiaoshi
      }
      ,{
	path: '/xueshengkaoqin',
        name: '学生考勤',
        component: xueshengkaoqin
      }
      ,{
	path: '/syslog',
        name: '系统日志',
        component: syslog
      }
      ,{
	path: '/banji',
        name: '班级',
        component: banji
      }
      ,{
	path: '/systemnotice',
        name: '系统公告',
        component: systemnotice
      }
      ,{
	path: '/kechengxinxi',
        name: '课程信息',
        component: kechengxinxi
      }
      ,{
	path: '/kaoqintongji',
        name: '考勤统计',
        component: kaoqintongji
      }
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {icon:'', title:'login'}
  },
  {
    path: '/register',
    name: 'register',
    component: register,
    meta: {icon:'', title:'register'}
  },
  {
    path: '*',
    component: NotFound
  }
]
//3.实例化VueRouter  注意：名字
const router = new VueRouter({
  mode: 'hash',
  /*hash模式改为history*/
  routes // （缩写）相当于 routes: routes
})
const originalPush = VueRouter.prototype.push
//修改原型对象中的push方法
VueRouter.prototype.push = function push(location) {
   return originalPush.call(this, location).catch(err => err)
}
export default router;
