<template>
  <div>
    <div class="container" :style='{"minHeight":"100vh","alignItems":"center","background":"url(http://codegen.caihongy.cn/20230908/322b929098b24499a774ded5b49b487b.jpg)","display":"flex","width":"100%","backgroundSize":"cover","backgroundPosition":"center center","backgroundRepeat":"no-repeat","justifyContent":"center"}'>
      <el-form :style='{"border":"1px solid #ccc","padding":"100px 20px 20px","boxShadow":"0 0px 0px rgba(0, 0, 0, .2)","margin":"100px auto","borderRadius":"4px","textAlign":"center","background":"url(http://codegen.caihongy.cn/20230908/8e0e6c388b064f7abc46b7500ca1e3c6.png) no-repeat center 20px,rgba(255,255,255,.96)","width":"26vw","fontSize":"14px","position":"relative","height":"auto"}'>
        <div v-if="true" :style='{"padding":"0px","margin":"20px auto 30px","borderColor":"#ddd","color":"#fff","display":"inline-block","top":"-100px","left":"-100%","background":"none","borderWidth":"0px","width":"300%","lineHeight":"auto","fontSize":"32px","position":"absolute","borderStyle":"solid","fontWeight":"600"}' class="title-container">基于python的学生考勤管理系统登录</div>
        <div v-if="loginType==1" class="list-item" :style='{"width":"calc(100% - 150px)","margin":"0 auto 30px","position":"relative","alignItems":"center","flexWrap":"wrap","display":"flex"}'>
          <div v-if="true" class="lable" :style='{"color":"#666","left":"-150px","textAlign":"right","width":"150px","lineHeight":"44px","fontSize":"inherit","position":"absolute"}'>用户名：</div>
          <input :style='{"border":"0px solid rgba(167,142,68,.2)","padding":"0 10px","boxShadow":"0 0px 0px rgba(60, 60, 60, .1)","borderColor":"#ddd","color":"#666","outline":"0px solid #efefef","outlineOffset":"0px","borderRadius":"0px","background":"none","borderWidth":"0 0 1px","width":"100%","fontSize":"inherit","borderStyle":"solid","height":"36px"}' placeholder="请输入用户名" name="username" type="text" v-model="rulesForm.username">
        </div>
        <div v-if="loginType==1" class="list-item" :style='{"width":"calc(100% - 150px)","margin":"0 auto 30px","position":"relative","alignItems":"center","flexWrap":"wrap","display":"flex"}'>
          <div v-if="true" class="lable" :style='{"color":"#666","left":"-150px","textAlign":"right","width":"150px","lineHeight":"44px","fontSize":"inherit","position":"absolute"}'>密码：</div>
          <input :style='{"border":"0px solid rgba(167,142,68,.2)","padding":"0 10px","boxShadow":"0 0px 0px rgba(60, 60, 60, .1)","borderColor":"#ddd","color":"#666","outline":"0px solid #efefef","outlineOffset":"0px","borderRadius":"0px","background":"none","borderWidth":"0 0 1px","width":"100%","fontSize":"inherit","borderStyle":"solid","height":"36px"}' placeholder="请输入密码" name="password" type="password" v-model="rulesForm.password">
        </div>

		<div class="list-item select" :style='{"width":"calc(100% - 150px)","margin":"0 auto 30px","position":"relative","alignItems":"center","flexWrap":"wrap","display":"flex"}' v-if="roles.length>1">
			<div v-if="true" class="lable" :style='{"color":"#666","left":"-150px","textAlign":"right","width":"150px","lineHeight":"44px","fontSize":"inherit","position":"absolute"}'>角色：</div>
		  <el-select v-model="rulesForm.role" placeholder="请选择角色">
		    <el-option v-if="loginType==1||(loginType==2&&item.roleName!='管理员')" v-for="item in roles" :key="item.roleName" :label="item.roleName" :value="item.roleName" />
		  </el-select>
		</div>

		
        <div :style='{"margin":"20px auto 0","alignItems":"center","flexWrap":"wrap","display":"flex","width":"calc(100% - 150px)","fontSize":"16px","position":"relative","justifyContent":"flex-start"}'>
          <el-button v-if="loginType==1" :style='{"border":"0px solid #fff","cursor":"pointer","padding":"0 0 0 20px","margin":"0 0 20px","color":"#fff","textAlign":"center","letterSpacing":"10px","outline":"none","borderRadius":"50px","background":"#018fbf","width":"100%","fontSize":"20px","height":"44px"}' type="primary" @click="login()" class="loginInBt">登录</el-button>
          <el-button :style='{"border":"0px solid rgba(64, 158, 255, 1)","cursor":"pointer","padding":"0 6px 0 0","margin":"0 5px 10px","borderColor":"rgba(167,142,68,1)","color":"#333","outline":"none","borderRadius":"0px","background":"none","borderWidth":"0px","width":"auto","fontSize":"14px","borderStyle":"solid","fontWeight":"500","height":"40px"}' type="primary" @click="register('jiaoshi')" class="register">注册教师</el-button>
          <el-button :style='{"border":"0px solid rgba(64, 158, 255, 1)","cursor":"pointer","padding":"0 6px 0 0","margin":"0 5px 10px","borderColor":"rgba(167,142,68,1)","color":"#333","outline":"none","borderRadius":"0px","background":"none","borderWidth":"0px","width":"auto","fontSize":"14px","borderStyle":"solid","fontWeight":"500","height":"40px"}' type="primary" @click="register('xuesheng')" class="register">注册学生</el-button>
          <el-button :style='{"border":"0","cursor":"pointer","padding":"0 0px","margin":"0px 0 0","outline":"none","color":"rgba(159, 159, 159, 1)","borderRadius":"0","textAlign":"right","background":"none","width":"100%","fontSize":"14px","height":"40px"}' type="primary" @click="updatePassword()" class="register">忘记密码?</el-button>
        </div>
      </el-form>

    </div>
  </div>
</template>
<script>
import menu from "@/utils/menu";
export default {
  data() {
    return {
		verifyCheck2: false,
		flag: false,
      baseUrl:this.$base.url,
      loginType: 1,
      rulesForm: {
        username: "",
        password: "",
        role: "",
      },
      menus: [],
      roles: [],
      tableName: "",
    };
  },
  mounted() {
    let menus = menu.list();
    this.menus = menus;

    for (let i = 0; i < this.menus.length; i++) {
      if (this.menus[i].hasBackLogin=='是') {
        this.roles.push(this.menus[i])
      }
    }

  },
  created() {

  },
  destroyed() {
	    },
  components: {
  },
  methods: {

    //重置密码
    updatePassword(){
      this.$storage.set("loginTable", "");
      this.$router.push({path:'/register',query:{pageFlag:'security1'}})
    },
    //注册
    register(tableName){
		this.$storage.set("loginTable", tableName);
		this.$router.push({path:'/register',query:{pageFlag:'register'}})
    },
    // 登陆
    login() {

		if (!this.rulesForm.username) {
			this.$message.error("请输入用户名");
			return;
		}
		if (!this.rulesForm.password) {
			this.$message.error("请输入密码");
			return;
		}
		if(this.roles.length>1) {
			if (!this.rulesForm.role) {
				this.$message.error("请选择角色");
				return;
			}

			let menus = this.menus;
			for (let i = 0; i < menus.length; i++) {
				if (menus[i].roleName == this.rulesForm.role) {
					this.tableName = menus[i].tableName;
				}
			}
		} else {
			this.tableName = this.roles[0].tableName;
			this.rulesForm.role = this.roles[0].roleName;
		}
		
		this.loginPost()
    },
	loginPost() {
		this.$http({
			url: `${this.tableName}/login?username=${this.rulesForm.username}&password=${this.rulesForm.password}`,
			method: "post"
		}).then(({ data }) => {
			if (data && data.code === 0) {
				this.$storage.set("Token", data.token);
				this.$storage.set("role", this.rulesForm.role);
				this.$storage.set("sessionTable", this.tableName);
				this.$storage.set("adminName", this.rulesForm.username);
				this.$router.replace({ path: "/" });
			} else {
				this.$message.error(data.msg);
			}
		});
	},
  }
}
</script>

<style lang="scss" scoped>
.container {
  min-height: 100vh;
  position: relative;
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
      background: url(http://codegen.caihongy.cn/20230908/322b929098b24499a774ded5b49b487b.jpg);
        
  .list-item /deep/ .el-input .el-input__inner {
		border: 0px solid rgba(167,142,68,.2);
		padding: 0 10px;
		color: #666;
		font-size: inherit;
		border-color: #ddd;
		outline-offset: 0px;
		border-radius: 0px;
		box-shadow: 0 0px 0px rgba(60, 60, 60, .1);
		outline: 0px solid #efefef;
		background: none;
		width: 100%;
		border-width: 0 0 1px;
		border-style: solid;
		height: 36px;
	  }
  
  .list-item.select /deep/ .el-select .el-input__inner {
		border-radius: 0px;
		padding: 0 10px;
		margin: 20px 0 0;
		color: #666;
		background: none;
		width: 100%;
		font-size: 14px;
		border-color: #ddd;
		border-width: 0 0 1px;
		border-style: solid;
		height: 36px;
	  }
  
  .list-code /deep/ .el-input .el-input__inner {
  	  	border-radius: 0px;
  	  	padding: 0 10px;
  	  	box-shadow: 0 0px 0px rgba(60, 60, 60, .1);
  	  	outline: none;
  	  	color: #666;
  	  	background: none;
  	  	width: calc(100% - 90px);
  	  	font-size: inherit;
  	  	border-color: #ddd;
  	  	border-width: 0 0 1px;
  	  	border-style: solid;
  	  	height: 36px;
  	  }

  .list-type /deep/ .el-radio__input .el-radio__inner {
		background: rgba(53, 53, 53, 0);
		border-color: #666666;
	  }
  .list-type /deep/ .el-radio__input.is-checked .el-radio__inner {
        background: #bfbfbf;
        border-color: #bfbfbf;
      }
  .list-type /deep/ .el-radio__label {
		color: #666666;
		font-size: 16px;
	  }
  .list-type /deep/ .el-radio__input.is-checked+.el-radio__label {
        color: rgba(50,50,50,1);
        font-size: 16px;
      }
}

</style>
