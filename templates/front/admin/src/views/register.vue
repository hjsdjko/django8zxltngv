<template>
	<div>
		<div class="container" :style='{"minHeight":"100vh","alignItems":"center","background":"url(http://codegen.caihongy.cn/20230908/322b929098b24499a774ded5b49b487b.jpg)","display":"flex","width":"100%","backgroundSize":"cover","backgroundPosition":"center center","backgroundRepeat":"no-repeat","justifyContent":"center","height":"auto"}'>
			<el-form v-if="pageFlag=='security1'" :style='{"border":"1px solid #ccc","padding":"30px 0px 20px 30px","boxShadow":"0 0px 0px rgba(0, 0, 0, .2)","margin":"100px auto","borderRadius":"4px","textAlign":"center","background":"rgba(255,255,255,.96)","width":"30vw","fontSize":"16px","position":"relative","height":"auto"}' class="rgs-form" :model="forgetForm">
				<div v-if="true" :style='{"padding":"0px","margin":"10px auto 0px","borderColor":"#eee","color":"#fff","display":"inline-block","top":"-80px","left":"-100%","background":"none","borderWidth":"0px","width":"300%","lineHeight":"40px","fontSize":"32px","position":"absolute","borderStyle":"solid","fontWeight":"600"}' class="title">基于python的学生考勤管理系统找回密码</div>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable">账号</div>
					<el-input v-model="forgetForm.username" autocomplete="off" placeholder="请您输入账号" />
				</el-form-item>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable">角色</div>
                    <el-select v-model="tableName" placeholder="请您选择角色">
                        <el-option label="教师" value="jiaoshi"></el-option>
                        <el-option label="学生" value="xuesheng"></el-option>
                    </el-select>
				</el-form-item>
				<button :style='{"border":"1px solid #fff","cursor":"pointer","padding":"0 0 0 20px","boxShadow":"0 0 0px rgba(64, 158, 255, .5)","margin":"20px auto 5px","color":"#fff","display":"block","letterSpacing":"10px","outline":"none","borderRadius":"50px","background":"#018fbf","width":"calc(100% - 150px)","fontSize":"20px","height":"44px"}' type="button" class="r-btn" @click="getSecurity()">下一步</button>
				<div :style='{"cursor":"pointer","padding":"0","margin":"10px 0","color":"rgba(159, 159, 159, 1)","textAlign":"right","display":"inline-block","width":"calc(100% - 150px)","lineHeight":"1","fontSize":"14px"}' class="r-login" @click="close()">已有账号，直接登录</div>
            </el-form>
			<el-form v-if="pageFlag=='security2'" :style='{"border":"1px solid #ccc","padding":"30px 0px 20px 30px","boxShadow":"0 0px 0px rgba(0, 0, 0, .2)","margin":"100px auto","borderRadius":"4px","textAlign":"center","background":"rgba(255,255,255,.96)","width":"30vw","fontSize":"16px","position":"relative","height":"auto"}' class="rgs-form" :model="ruleForm">
				<div v-if="true" :style='{"padding":"0px","margin":"10px auto 0px","borderColor":"#eee","color":"#fff","display":"inline-block","top":"-80px","left":"-100%","background":"none","borderWidth":"0px","width":"300%","lineHeight":"40px","fontSize":"32px","position":"absolute","borderStyle":"solid","fontWeight":"600"}' class="title">基于python的学生考勤管理系统密码重置</div>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable">密保问题</div>
					<el-input v-model="ruleForm.pquestion" readOnly autocomplete="off" placeholder="密保问题" />
				</el-form-item>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable">密保答案</div>
					<el-input v-model="ruleForm.myanswer" autocomplete="off" placeholder="请您输入密保答案" />
				</el-form-item>
				<button :style='{"border":"1px solid #fff","cursor":"pointer","padding":"0 0 0 20px","boxShadow":"0 0 0px rgba(64, 158, 255, .5)","margin":"20px auto 5px","color":"#fff","display":"block","letterSpacing":"10px","outline":"none","borderRadius":"50px","background":"#018fbf","width":"calc(100% - 150px)","fontSize":"20px","height":"44px"}' type="button" class="r-btn" @click="validateSecurity()">下一步</button>
				<div :style='{"cursor":"pointer","padding":"0","margin":"10px 0","color":"rgba(159, 159, 159, 1)","textAlign":"right","display":"inline-block","width":"calc(100% - 150px)","lineHeight":"1","fontSize":"14px"}' class="r-login" @click="close()">已有账号，直接登录</div>
            </el-form>
			<el-form v-if="pageFlag=='security3'" :style='{"border":"1px solid #ccc","padding":"30px 0px 20px 30px","boxShadow":"0 0px 0px rgba(0, 0, 0, .2)","margin":"100px auto","borderRadius":"4px","textAlign":"center","background":"rgba(255,255,255,.96)","width":"30vw","fontSize":"16px","position":"relative","height":"auto"}' class="rgs-form" :model="ruleForm">
				<div v-if="true" :style='{"padding":"0px","margin":"10px auto 0px","borderColor":"#eee","color":"#fff","display":"inline-block","top":"-80px","left":"-100%","background":"none","borderWidth":"0px","width":"300%","lineHeight":"40px","fontSize":"32px","position":"absolute","borderStyle":"solid","fontWeight":"600"}' class="title">基于python的学生考勤管理系统密码重置</div>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable">新密码</div>
					<el-input v-model="ruleForm.newpassword" autocomplete="off" type="password" placeholder="请您输入新密码" />
				</el-form-item>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable">确认密码</div>
					<el-input v-model="ruleForm.repassword" autocomplete="off" type="password" placeholder="请您确认新密码" />
				</el-form-item>
				<button :style='{"border":"1px solid #fff","cursor":"pointer","padding":"0 0 0 20px","boxShadow":"0 0 0px rgba(64, 158, 255, .5)","margin":"20px auto 5px","color":"#fff","display":"block","letterSpacing":"10px","outline":"none","borderRadius":"50px","background":"#018fbf","width":"calc(100% - 150px)","fontSize":"20px","height":"44px"}' type="button" class="r-btn" @click="updatePassword()">修改密码</button>
				<div :style='{"cursor":"pointer","padding":"0","margin":"10px 0","color":"rgba(159, 159, 159, 1)","textAlign":"right","display":"inline-block","width":"calc(100% - 150px)","lineHeight":"1","fontSize":"14px"}' class="r-login" @click="close()">已有账号，直接登录</div>
            </el-form>
			<el-form v-if="pageFlag=='register'" :style='{"border":"1px solid #ccc","padding":"30px 0px 20px 30px","boxShadow":"0 0px 0px rgba(0, 0, 0, .2)","margin":"100px auto","borderRadius":"4px","textAlign":"center","background":"rgba(255,255,255,.96)","width":"30vw","fontSize":"16px","position":"relative","height":"auto"}' ref="rgsForm" class="rgs-form" :model="rgsForm" :rules="rules">
				<div v-if="true" :style='{"padding":"0px","margin":"10px auto 0px","borderColor":"#eee","color":"#fff","display":"inline-block","top":"-80px","left":"-100%","background":"none","borderWidth":"0px","width":"300%","lineHeight":"40px","fontSize":"32px","position":"absolute","borderStyle":"solid","fontWeight":"600"}' class="title">基于python的学生考勤管理系统注册</div>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item" v-if="tableName=='jiaoshi'">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable" :class="changeRules('jiaoshigonghao')?'required':''">教师工号：</div>
					<el-input  v-model="ruleForm.jiaoshigonghao"  autocomplete="off" placeholder="教师工号"  type="text"  />
				</el-form-item>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item" v-if="tableName=='jiaoshi'">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable" :class="changeRules('mima')?'required':''">密码：</div>
					<el-input  v-model="ruleForm.mima"  autocomplete="off" placeholder="密码"  type="password"  />
				</el-form-item>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item" v-if="tableName=='jiaoshi'">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable" :class="changeRules('mima')?'required':''">确认密码：</div>
					<el-input  v-model="ruleForm.mima2" autocomplete="off" placeholder="确认密码" type="password" />
				</el-form-item>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item" v-if="tableName=='jiaoshi'">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable" :class="changeRules('jiaoshixingming')?'required':''">教师姓名：</div>
					<el-input  v-model="ruleForm.jiaoshixingming"  autocomplete="off" placeholder="教师姓名"  type="text"  />
				</el-form-item>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item" v-if="tableName=='jiaoshi'">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable" :class="changeRules('xingbie')?'required':''">性别：</div>
                    <el-select v-model="ruleForm.xingbie" placeholder="请选择性别" >
                        <el-option
                            v-for="(item,index) in jiaoshixingbieOptions"
                            v-bind:key="index"
                            :label="item"
                            :value="item">
                        </el-option>
                    </el-select>
				</el-form-item>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item" v-if="tableName=='jiaoshi'">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable" :class="changeRules('zhaopian')?'required':''">照片：</div>
                    <file-upload
                        tip="点击上传照片"
                        action="file/upload"
                        :limit="3"
                        :multiple="true"
                        :fileUrls="ruleForm.zhaopian?ruleForm.zhaopian:''"
                        @change="jiaoshizhaopianUploadChange"
                    ></file-upload>
				</el-form-item>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item" v-if="tableName=='jiaoshi'">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable" :class="changeRules('zhicheng')?'required':''">职称：</div>
					<el-input  v-model="ruleForm.zhicheng"  autocomplete="off" placeholder="职称"  type="text"  />
				</el-form-item>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item" v-if="tableName=='jiaoshi'">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable" :class="changeRules('lianxidianhua')?'required':''">联系电话：</div>
					<el-input  v-model="ruleForm.lianxidianhua"  autocomplete="off" placeholder="联系电话"  type="text"  />
				</el-form-item>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item" v-if="tableName=='jiaoshi'">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable" :class="changeRules('pquestion')?'required':''">密保问题：</div>
					<el-input  v-model="ruleForm.pquestion"  autocomplete="off" placeholder="密保问题"  type="text"  />
				</el-form-item>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item" v-if="tableName=='jiaoshi'">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable" :class="changeRules('panswer')?'required':''">密保答案：</div>
					<el-input  v-model="ruleForm.panswer"  autocomplete="off" placeholder="密保答案"  type="text"  />
				</el-form-item>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item" v-if="tableName=='xuesheng'">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable" :class="changeRules('xuehao')?'required':''">学号：</div>
					<el-input  v-model="ruleForm.xuehao"  autocomplete="off" placeholder="学号"  type="text"  />
				</el-form-item>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item" v-if="tableName=='xuesheng'">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable" :class="changeRules('mima')?'required':''">密码：</div>
					<el-input  v-model="ruleForm.mima"  autocomplete="off" placeholder="密码"  type="password"  />
				</el-form-item>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item" v-if="tableName=='xuesheng'">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable" :class="changeRules('mima')?'required':''">确认密码：</div>
					<el-input  v-model="ruleForm.mima2" autocomplete="off" placeholder="确认密码" type="password" />
				</el-form-item>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item" v-if="tableName=='xuesheng'">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable" :class="changeRules('xingming')?'required':''">姓名：</div>
					<el-input  v-model="ruleForm.xingming"  autocomplete="off" placeholder="姓名"  type="text"  />
				</el-form-item>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item" v-if="tableName=='xuesheng'">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable" :class="changeRules('xingbie')?'required':''">性别：</div>
                    <el-select v-model="ruleForm.xingbie" placeholder="请选择性别" >
                        <el-option
                            v-for="(item,index) in xueshengxingbieOptions"
                            v-bind:key="index"
                            :label="item"
                            :value="item">
                        </el-option>
                    </el-select>
				</el-form-item>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item" v-if="tableName=='xuesheng'">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable" :class="changeRules('touxiang')?'required':''">头像：</div>
                    <file-upload
                        tip="点击上传头像"
                        action="file/upload"
                        :limit="3"
                        :multiple="true"
                        :fileUrls="ruleForm.touxiang?ruleForm.touxiang:''"
                        @change="xueshengtouxiangUploadChange"
                    ></file-upload>
				</el-form-item>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item" v-if="tableName=='xuesheng'">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable" :class="changeRules('shouji')?'required':''">手机：</div>
					<el-input  v-model="ruleForm.shouji"  autocomplete="off" placeholder="手机"  type="text"  />
				</el-form-item>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item" v-if="tableName=='xuesheng'">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable" :class="changeRules('banji')?'required':''">班级：</div>
                    <el-select v-model="ruleForm.banji" placeholder="请选择班级" >
                        <el-option
                            v-for="(item,index) in xueshengbanjiOptions"
                            v-bind:key="index"
                            :label="item"
                            :value="item">
                        </el-option>
                    </el-select>
				</el-form-item>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item" v-if="tableName=='xuesheng'">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable" :class="changeRules('pquestion')?'required':''">密保问题：</div>
					<el-input  v-model="ruleForm.pquestion"  autocomplete="off" placeholder="密保问题"  type="text"  />
				</el-form-item>
				<el-form-item :style='{"padding":"0 0px","margin":"0 auto 10px","textAlign":"left","width":"calc(100% - 150px)","fontSize":"inherit","position":"relative","height":"auto"}' class="list-item" v-if="tableName=='xuesheng'">
					<div v-if="true" :style='{"padding":"0 8px 0 0","color":"#666","textAlign":"right","left":"-150px","width":"150px","lineHeight":"40px","fontSize":"14px","position":"absolute"}' class="lable" :class="changeRules('panswer')?'required':''">密保答案：</div>
					<el-input  v-model="ruleForm.panswer"  autocomplete="off" placeholder="密保答案"  type="text"  />
				</el-form-item>
				<button :style='{"border":"1px solid #fff","cursor":"pointer","padding":"0 0 0 20px","boxShadow":"0 0 0px rgba(64, 158, 255, .5)","margin":"20px auto 5px","color":"#fff","display":"block","letterSpacing":"10px","outline":"none","borderRadius":"50px","background":"#018fbf","width":"calc(100% - 150px)","fontSize":"20px","height":"44px"}' type="button" class="r-btn" @click="login()">注册</button>
				<div :style='{"cursor":"pointer","padding":"0","margin":"10px 0","color":"rgba(159, 159, 159, 1)","textAlign":"right","display":"inline-block","width":"calc(100% - 150px)","lineHeight":"1","fontSize":"14px"}' class="r-login" @click="close()">已有账号，直接登录</div>
			</el-form>
			
		</div>
	</div>
</template>

<script>
export default {
	data() {
		return {
			ruleForm: {
			},
			forgetForm: {},
            pageFlag : '',
			tableName:"",
			rules: {},
            jiaoshixingbieOptions: [],
            xueshengxingbieOptions: [],
            xueshengbanjiOptions: [],
		};
	},
	mounted(){
		this.pageFlag = this.$route.query.pageFlag
		if(this.$route.query.pageFlag=='register'){
			
			let table = this.$storage.get("loginTable");
			this.tableName = table;
			if(this.tableName=='jiaoshi'){
				this.ruleForm = {
					jiaoshigonghao: '',
					mima: '',
					jiaoshixingming: '',
					xingbie: '',
					zhaopian: '',
					zhicheng: '',
					lianxidianhua: '',
					pquestion: '',
					panswer: '',
				}
			}
			if(this.tableName=='xuesheng'){
				this.ruleForm = {
					xuehao: '',
					mima: '',
					xingming: '',
					xingbie: '',
					touxiang: '',
					shouji: '',
					banji: '',
					pquestion: '',
					panswer: '',
				}
			}
			if ('jiaoshi' == this.tableName) {
				this.rules.jiaoshigonghao = [{ required: true, message: '请输入教师工号', trigger: 'blur' }]
			}
			if ('jiaoshi' == this.tableName) {
				this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
			}
			if ('jiaoshi' == this.tableName) {
				this.rules.jiaoshixingming = [{ required: true, message: '请输入教师姓名', trigger: 'blur' }]
			}
			if ('xuesheng' == this.tableName) {
				this.rules.xuehao = [{ required: true, message: '请输入学号', trigger: 'blur' }]
			}
			if ('xuesheng' == this.tableName) {
				this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
			}
			if ('xuesheng' == this.tableName) {
				this.rules.xingming = [{ required: true, message: '请输入姓名', trigger: 'blur' }]
			}
			this.jiaoshixingbieOptions = "男,女".split(',')
			this.xueshengxingbieOptions = "男,女".split(',')
			this.$http({
				url: `option/banji/banji`,
				method: "get"
			}).then(({ data }) => {
				if (data && data.code === 0) {
					this.xueshengbanjiOptions = data.data;
				} else {
					this.$message.error(data.msg);
				}
			});
		}
	},
	created() {
	},
	destroyed() {
		  	},
	methods: {
		changeRules(name){
			if(this.rules[name]){
				return true
			}
			return false
		},
		// 获取uuid
		getUUID () {
			return new Date().getTime();
		},
		close(){
			this.$router.push({ path: "/login" });
		},
        jiaoshizhaopianUploadChange(fileUrls) {
            this.ruleForm.zhaopian = fileUrls;
        },
        xueshengtouxiangUploadChange(fileUrls) {
            this.ruleForm.touxiang = fileUrls;
        },

        // 多级联动参数


        //获取密保问题
        getSecurity(){
            if(!this.tableName) {
                this.$message.error("请选择角色");
                return false
            }
            if(!this.forgetForm.username){
                this.$message.error("请输入账号");
                return false
            }
            this.$http({
                url: this.tableName+`/security?username=` + this.forgetForm.username,
                method: "get",
            }).then(({
                data
            }) => {
                if (data.data && data.code === 0) {
                    this.ruleForm = data.data;
                    this.pageFlag="security2"
                } else {
                    if(!data.data) {
                        this.$message.error("用户不存在");
                    } else {
                        this.$message.error(data.msg);
                    }
                }
            });
        },
        //验证密保问题
        validateSecurity(){
            let that = this
            if(this.ruleForm.panswer!=this.ruleForm.myanswer){
                this.$message.error("答案输入不正确");
                return false
            }
            this.$message.success("答案正确");
            setTimeout(()=>{
                this.pageFlag="security3";
            },1000)
        },
        // 修改密码
        updatePassword() {
            if (this.ruleForm.newpassword != this.ruleForm.repassword) {
                this.$message.error("两次密码输入不一致");
                return;
            }
            this.ruleForm.mima = this.ruleForm.newpassword;
            this.ruleForm.password = this.ruleForm.newpassword;
            this.$http({
                url: this.tableName+`/update`,
                method: "post",
                data: this.ruleForm
            }).then(({
                data
            }) => {
                if (data && data.code === 0) {
                    this.$message({
                        message: "修改密码成功",
                        type: "success",
                        duration: 1500,
                        onClose: () => {}
                    });
                    this.close()
                } else {
                    this.$message.error(data.msg);
                }
            });
        },
		// 注册
		login() {
			var url=this.tableName+"/register";
					if((!this.ruleForm.jiaoshigonghao) && `jiaoshi` == this.tableName){
						this.$message.error(`教师工号不能为空`);
						return
					}
					if((!this.ruleForm.mima) && `jiaoshi` == this.tableName){
						this.$message.error(`密码不能为空`);
						return
					}
					if((this.ruleForm.mima!=this.ruleForm.mima2) && `jiaoshi` == this.tableName){
						this.$message.error(`两次密码输入不一致`);
						return
					}
					if((!this.ruleForm.jiaoshixingming) && `jiaoshi` == this.tableName){
						this.$message.error(`教师姓名不能为空`);
						return
					}
            if(this.ruleForm.zhaopian!=null) {
                this.ruleForm.zhaopian = this.ruleForm.zhaopian.replace(new RegExp(this.$base.url,"g"),"");
            }
					if(`jiaoshi` == this.tableName && this.ruleForm.lianxidianhua &&(!this.$validate.isMobile(this.ruleForm.lianxidianhua))){
						this.$message.error(`联系电话应输入手机格式`);
						return
					}
				if(`jiaoshi` == this.tableName && this.ruleForm.pquestion==''){
					this.$message.error(`密保问题不能为空`);
				    return
				}
				if(`jiaoshi` == this.tableName && this.ruleForm.panswer==''){
					this.$message.error(`密保答案不能为空`);
				    return
				}
					if((!this.ruleForm.xuehao) && `xuesheng` == this.tableName){
						this.$message.error(`学号不能为空`);
						return
					}
					if((!this.ruleForm.mima) && `xuesheng` == this.tableName){
						this.$message.error(`密码不能为空`);
						return
					}
					if((this.ruleForm.mima!=this.ruleForm.mima2) && `xuesheng` == this.tableName){
						this.$message.error(`两次密码输入不一致`);
						return
					}
					if((!this.ruleForm.xingming) && `xuesheng` == this.tableName){
						this.$message.error(`姓名不能为空`);
						return
					}
            if(this.ruleForm.touxiang!=null) {
                this.ruleForm.touxiang = this.ruleForm.touxiang.replace(new RegExp(this.$base.url,"g"),"");
            }
					if(`xuesheng` == this.tableName && this.ruleForm.shouji &&(!this.$validate.isMobile(this.ruleForm.shouji))){
						this.$message.error(`手机应输入手机格式`);
						return
					}
				if(`xuesheng` == this.tableName && this.ruleForm.pquestion==''){
					this.$message.error(`密保问题不能为空`);
				    return
				}
				if(`xuesheng` == this.tableName && this.ruleForm.panswer==''){
					this.$message.error(`密保答案不能为空`);
				    return
				}
			this.$http({
				url: url,
				method: "post",
				data:this.ruleForm
			}).then(({ data }) => {
				if (data && data.code === 0) {
					this.$message({
						message: "注册成功",
						type: "success",
						duration: 1500,
						onClose: () => {
							this.$router.replace({ path: "/login" });
						}
					});
				} else {
					this.$message.error(data.msg);
				}
			});
		}
	}
};
</script>

<style lang="scss" scoped>
	.container {
	  position: relative;
	  background: url(http://codegen.caihongy.cn/20230908/322b929098b24499a774ded5b49b487b.jpg);

		.el-date-editor.el-input {
		  width: 100%;
		}
		
		.rgs-form .el-input /deep/ .el-input__inner {
						border-radius: 0px;
						padding: 0 10px;
						box-shadow: 0 0px 0px rgba(60, 60, 60, .1);
						outline: none;
						color: #666;
						background: none;
						width: calc(100% - 0px);
						font-size: 14px;
						border-color: #ddd;
						border-width: 0 0 1px;
						border-style: solid;
						height: 36px;
					}
		
		.rgs-form .el-select /deep/ .el-input__inner {
						border-radius: 0px;
						padding: 0 10px;
						box-shadow: 0 0px 0px rgba(60, 60, 60, .1);
						outline: none;
						color: #666;
						background: none;
						width: 100%;
						font-size: 14px;
						border-color: #ddd;
						border-width: 0 0 1px;
						border-style: solid;
						height: 36px;
					}
		
		.rgs-form .el-date-editor /deep/ .el-input__inner {
						border-radius: 0px;
						padding: 0 10px 0 30px;
						box-shadow: 0 0px 0px rgba(60, 60, 60, .1);
						outline: none;
						color: #666;
						background: none;
						width: 100%;
						font-size: 14px;
						border-color: #ddd;
						border-width: 0 0 1px;
						border-style: solid;
						height: 36px;
					}
		
		.rgs-form .el-date-editor /deep/ .el-input__inner {
						border-radius: 0px;
						padding: 0 10px 0 30px;
						box-shadow: 0 0px 0px rgba(60, 60, 60, .1);
						outline: none;
						color: #666;
						background: none;
						width: 100%;
						font-size: 14px;
						border-color: #ddd;
						border-width: 0 0 1px;
						border-style: solid;
						height: 36px;
					}
		
		.rgs-form /deep/ .el-upload--picture-card {
			background: transparent;
			border: 0;
			border-radius: 0;
			width: auto;
			height: auto;
			line-height: initial;
			vertical-align: middle;
		}
		
		.rgs-form /deep/ .upload .upload-img {
		  		  cursor: pointer;
		  		  color: #bbb;
		  		  font-size: 32px;
		  		  border-color: #ddd;
		  		  line-height: 80px;
		  		  border-radius: 4px;
		  		  box-shadow: 0 0px 0px rgba(60, 60, 60, .1);
		  		  background: none;
		  		  width: 160px;
		  		  border-width: 1px;
		  		  border-style: solid;
		  		  text-align: center;
		  		  height: 80px;
		  		}
		
		.rgs-form /deep/ .el-upload-list .el-upload-list__item {
		  		  cursor: pointer;
		  		  color: #bbb;
		  		  font-size: 32px;
		  		  border-color: #ddd;
		  		  line-height: 80px;
		  		  border-radius: 4px;
		  		  box-shadow: 0 0px 0px rgba(60, 60, 60, .1);
		  		  background: none;
		  		  width: 160px;
		  		  border-width: 1px;
		  		  border-style: solid;
		  		  text-align: center;
		  		  height: 80px;
		  		}
		
		.rgs-form /deep/ .el-upload .el-icon-plus {
		  		  cursor: pointer;
		  		  color: #bbb;
		  		  font-size: 32px;
		  		  border-color: #ddd;
		  		  line-height: 80px;
		  		  border-radius: 4px;
		  		  box-shadow: 0 0px 0px rgba(60, 60, 60, .1);
		  		  background: none;
		  		  width: 160px;
		  		  border-width: 1px;
		  		  border-style: solid;
		  		  text-align: center;
		  		  height: 80px;
		  		}
	}
	.required {
		position: relative;
	}
	.required::after{
				color: red;
				position: absolute;
				right: 5px;
				content: "*";
			}
	.editor>.avatar-uploader {
		line-height: 0;
		height: 0;
	}
</style>
