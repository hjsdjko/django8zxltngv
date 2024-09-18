<template>
	<div class="navbar">
		<div class="title" :style='{"display":"block","order":"1"}'>
			<el-image v-if="false" class="title-img" :style='{"width":"44px","objectFit":"cover","borderRadius":"100%","float":"left","height":"44px"}' src="http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg" fit="cover" />
			<span class="title-name" :style='{"padding":"0 0 0 12px","lineHeight":"auto","fontSize":"26px","color":"inherit","float":"left","fontWeight":"500"}'>{{this.$project.projectName}}</span>
		</div>
		<!-- 系统通知-1 -->
		<el-button class="notice" @click="dialogVisible = true" :style='{"border":"0px solid rgba(0, 0, 0, 0.2)","cursor":"pointer","padding":"10px 62px 0 24px","outline":"none","color":"#494f5d","borderRadius":"0px","background":"url(http://codegen.caihongy.cn/20230907/d3a6b26ac0a64d73896c06df84e28060.png) no-repeat  left center / 22px","width":"40px","fontSize":"inherit","lineHeight":"44px","height":"40px","order":"4"}' type="success">
		  <span class="icon iconfont icon-gonggao6" :style='{"margin":"0 2px","fontSize":"18px","color":"#fff","display":"none","height":"40px"}'></span>
		  
		</el-button>
		<el-dialog title="" :append-to-body="true" :visible.sync="dialogVisible" width="30%">
		  <div v-html="noticeDetail.content"></div>
		</el-dialog>
		<!--
		<div class="right" :style='{"position":"absolute","right":"20px","top":"8px","display":"flex"}'>
			<div :style='{"cursor":"pointer","margin":"0 5px","lineHeight":"44px","color":"#333"}' class="nickname">{{this.$storage.get('role')}} {{this.$storage.get('adminName')}}</div>
			<div :style='{"cursor":"pointer","margin":"0 5px","lineHeight":"44px","color":"#666"}' class="logout" @click="onLogout">退出登录</div>
		</div>
		-->
		
		<el-dropdown @command="handleCommand" trigger="click" :style='{"fontSize":"inherit","position":"absolute","right":"5%","color":"inherit","display":"inline-block"}'>
		  <div class="el-dropdown-link" :style='{"alignItems":"center","display":"flex"}'>
		    <el-image v-if="user" :style='{"width":"32px","margin":"0 10px","objectFit":"cover","borderRadius":"100%","display":"inline-block","height":"32px"}' :src="avatar?this.$base.url + avatar : require('@/assets/img/avator.png')" fit="cover"></el-image>
		    <span :style='{"color":"inherit","lineHeight":"32px","fontSize":"inherit"}'>{{this.$storage.get('adminName')}}</span>
		    <span class="icon iconfont icon-xiala" :style='{"color":"inherit","margin":"0 0 0 5px","fontSize":"12px"}'></span>
		  </div>
		  <el-dropdown-menu class="top-el-dropdown-menu" slot="dropdown">
		    <el-dropdown-item class="item1" :command="''">首页</el-dropdown-item>
		    <el-dropdown-item class="item2" :command="'center'">用户信息</el-dropdown-item>
		    <el-dropdown-item class="item4" :command="'logout'">退出登录</el-dropdown-item>
		  </el-dropdown-menu>
		</el-dropdown>
		
	</div>
</template>

<script>
	import axios from 'axios'
	export default {
		data() {
			return {
				dialogVisible: false,
				ruleForm: {},
				user: null,
				// 系统公告
				noticeDetail: {},
			};
		},
		created() {
			// 系统公告
			this.getNotice()
		},
		computed: {
			avatar(){
				return this.$storage.get('headportrait')?this.$storage.get('headportrait'):''
			}
		},
		mounted() {
			let sessionTable = this.$storage.get("sessionTable")
			this.$http({
				url: sessionTable + '/session',
				method: "get"
			}).then(({
				data
			}) => {
				if (data && data.code === 0) {
					if(sessionTable == 'jiaoshi') {
						this.$storage.set('headportrait',data.data.zhaopian)
					}
					if(sessionTable == 'xuesheng') {
						this.$storage.set('headportrait',data.data.touxiang)
					}
					if(sessionTable == 'users') {
						this.$storage.set('headportrait',data.data.image)
					}
					this.$storage.set('userForm',JSON.stringify(data.data))
					this.user = data.data;
					this.$storage.set('userid',data.data.id);
				} else {
					let message = this.$message
					message.error(data.msg);
				}
			});
		},
		methods: {
			// 获取系统公告
			getNotice() {
				this.$http({
				    url: '/systemnotice/detail/1',
				    method: "get"
				}).then(({data})=>{
                    if ( data && data.code==0 ) {
						this.noticeDetail = data.data
					}
				})
			},
			handleCommand(name) {
				if (name == 'front') {
					this.onIndexTap()
				} else if (name == 'logout') {
					this.onLogout()
				} else if (name == 'board'){
					this.toBoard()
				} else if (name == 'backUp'){
					this.backUp()
				} else {
					let router = this.$router
					name = '/'+name
					router.push(name)
				}
			},
			
			onLogout() {
				let storage = this.$storage
				let router = this.$router
				storage.clear()
				this.$store.dispatch('tagsView/delAllViews')
				router.replace({
					name: "login"
				});
			},
			onIndexTap(){
				window.location.href = `${this.$base.indexUrl}`
			},
		}
	};
</script>


<style lang="scss" scoped>
	.top-el-dropdown-menu {
				border: 1px solid #EBEEF5;
				border-radius: 4px;
				padding: 10px 0;
				box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);
				margin: 18px 0;
				background: #FFF;
			}
	
	.top-el-dropdown-menu li.el-dropdown-menu__item.item1 {
				cursor: pointer;
				padding: 0 20px;
				margin: 0;
				outline: 0;
				color: #606266;
				background: #fff;
				font-size: 14px;
				line-height: 36px;
				list-style: none;
			}
	
	.top-el-dropdown-menu li.el-dropdown-menu__item.item1:hover {
				background: #ecf5ff;
			}
	
	.top-el-dropdown-menu li.el-dropdown-menu__item.item2 {
				cursor: pointer;
				padding: 0 20px;
				margin: 0;
				outline: 0;
				color: #606266;
				background: #fff;
				font-size: 14px;
				line-height: 36px;
				list-style: none;
			}
	
	.top-el-dropdown-menu li.el-dropdown-menu__item.item2:hover {
				background: #ecf5ff;
			}
	
	.top-el-dropdown-menu li.el-dropdown-menu__item.item3 {
				cursor: pointer;
				padding: 0 20px;
				margin: 0;
				outline: 0;
				color: #606266;
				background: #fff;
				font-size: 14px;
				line-height: 36px;
				list-style: none;
			}
	
	.top-el-dropdown-menu li.el-dropdown-menu__item.item3:hover {
				background: #ecf5ff;
			}
	
	.top-el-dropdown-menu li.el-dropdown-menu__item.item4 {
				cursor: pointer;
				padding: 0 20px;
				margin: 0;
				outline: 0;
				color: #606266;
				background: #fff;
				font-size: 14px;
				line-height: 36px;
				list-style: none;
			}
	
	.top-el-dropdown-menu li.el-dropdown-menu__item.item4:hover {
				background: #ecf5ff;
			}
</style>
