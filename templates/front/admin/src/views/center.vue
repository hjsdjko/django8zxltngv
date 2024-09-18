<template>
  <div :style='{"minHeight":"calc(100vh - 200px)","padding":"0px 5%","margin":"0 auto","color":"#666","background":"none","width":"calc(100% - 0px)","fontSize":"14px","height":"100%"}'>
    <el-form
	  :style='{"padding":"30px 5%","borderColor":"#f6f6f6","alignItems":"flex-start","borderRadius":"4px","flexWrap":"wrap","background":"rgba(255,255,255,.9)","borderWidth":"2px","display":"flex","fontSize":"inherit","borderStyle":"solid"}'
      class="add-update-preview"
      ref="ruleForm"
      :model="ruleForm"
      label-width="200px"
    >  
     <el-row>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 20px","color":"inherit","borderRadius":"4px","background":"none","width":"100%","fontSize":"inherit"}'   v-if="flag=='jiaoshi'"  label="教师工号" prop="jiaoshigonghao">
          <el-input v-model="ruleForm.jiaoshigonghao" readonly              placeholder="教师工号" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 20px","color":"inherit","borderRadius":"4px","background":"none","width":"100%","fontSize":"inherit"}'   v-if="flag=='jiaoshi'"  label="教师姓名" prop="jiaoshixingming">
          <el-input v-model="ruleForm.jiaoshixingming"               placeholder="教师姓名" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 20px","color":"inherit","borderRadius":"4px","background":"none","width":"100%","fontSize":"inherit"}' v-if="flag=='jiaoshi'"  label="性别" prop="xingbie">
          <el-select v-model="ruleForm.xingbie"  placeholder="请选择性别">
            <el-option
                v-for="(item,index) in jiaoshixingbieOptions"
                v-bind:key="index"
                :label="item"
                :value="item">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 20px","color":"inherit","borderRadius":"4px","background":"none","width":"100%","fontSize":"inherit"}' v-if="flag=='jiaoshi'" label="照片" prop="zhaopian">
          <file-upload
          tip="点击上传照片"
          action="file/upload"
          :limit="3"
          :multiple="true"
          :fileUrls="ruleForm.zhaopian?ruleForm.zhaopian:''"
          @change="jiaoshizhaopianUploadChange"
          ></file-upload>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 20px","color":"inherit","borderRadius":"4px","background":"none","width":"100%","fontSize":"inherit"}'   v-if="flag=='jiaoshi'"  label="职称" prop="zhicheng">
          <el-input v-model="ruleForm.zhicheng"               placeholder="职称" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 20px","color":"inherit","borderRadius":"4px","background":"none","width":"100%","fontSize":"inherit"}'   v-if="flag=='jiaoshi'"  label="联系电话" prop="lianxidianhua">
          <el-input v-model="ruleForm.lianxidianhua"               placeholder="联系电话" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 20px","color":"inherit","borderRadius":"4px","background":"none","width":"100%","fontSize":"inherit"}'   v-if="flag=='jiaoshi'"  label="密保问题" prop="pquestion">
          <el-input v-model="ruleForm.pquestion"               placeholder="密保问题" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 20px","color":"inherit","borderRadius":"4px","background":"none","width":"100%","fontSize":"inherit"}'   v-if="flag=='jiaoshi'"  label="密保答案" prop="panswer">
          <el-input v-model="ruleForm.panswer"               placeholder="密保答案" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 20px","color":"inherit","borderRadius":"4px","background":"none","width":"100%","fontSize":"inherit"}'   v-if="flag=='xuesheng'"  label="学号" prop="xuehao">
          <el-input v-model="ruleForm.xuehao" readonly              placeholder="学号" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 20px","color":"inherit","borderRadius":"4px","background":"none","width":"100%","fontSize":"inherit"}'   v-if="flag=='xuesheng'"  label="姓名" prop="xingming">
          <el-input v-model="ruleForm.xingming"               placeholder="姓名" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 20px","color":"inherit","borderRadius":"4px","background":"none","width":"100%","fontSize":"inherit"}' v-if="flag=='xuesheng'"  label="性别" prop="xingbie">
          <el-select v-model="ruleForm.xingbie"  placeholder="请选择性别">
            <el-option
                v-for="(item,index) in xueshengxingbieOptions"
                v-bind:key="index"
                :label="item"
                :value="item">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 20px","color":"inherit","borderRadius":"4px","background":"none","width":"100%","fontSize":"inherit"}' v-if="flag=='xuesheng'" label="头像" prop="touxiang">
          <file-upload
          tip="点击上传头像"
          action="file/upload"
          :limit="3"
          :multiple="true"
          :fileUrls="ruleForm.touxiang?ruleForm.touxiang:''"
          @change="xueshengtouxiangUploadChange"
          ></file-upload>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 20px","color":"inherit","borderRadius":"4px","background":"none","width":"100%","fontSize":"inherit"}'   v-if="flag=='xuesheng'"  label="手机" prop="shouji">
          <el-input v-model="ruleForm.shouji"               placeholder="手机" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 20px","color":"inherit","borderRadius":"4px","background":"none","width":"100%","fontSize":"inherit"}' v-if="flag=='xuesheng'"  label="班级" prop="banji">
          <el-select v-model="ruleForm.banji"  placeholder="请选择班级">
            <el-option
                v-for="(item,index) in xueshengbanjiOptions"
                v-bind:key="index"
                :label="item"
                :value="item">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 20px","color":"inherit","borderRadius":"4px","background":"none","width":"100%","fontSize":"inherit"}'   v-if="flag=='xuesheng'"  label="密保问题" prop="pquestion">
          <el-input v-model="ruleForm.pquestion"               placeholder="密保问题" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"padding":"2px 0","margin":"0 auto 20px","color":"inherit","borderRadius":"4px","background":"none","width":"100%","fontSize":"inherit"}'   v-if="flag=='xuesheng'"  label="密保答案" prop="panswer">
          <el-input v-model="ruleForm.panswer"               placeholder="密保答案" clearable></el-input>
        </el-form-item>
		<el-form-item :style='{"padding":"2px 0","margin":"0 auto 20px","color":"inherit","borderRadius":"4px","background":"none","width":"100%","fontSize":"inherit"}' v-if="flag=='users'" label="用户名" prop="username">
			<el-input v-model="ruleForm.username" placeholder="用户名"></el-input>
		</el-form-item>
		<el-form-item :style='{"padding":"2px 0","margin":"0 auto 20px","color":"inherit","borderRadius":"4px","background":"none","width":"100%","fontSize":"inherit"}' v-if="flag=='users'" label="头像" prop="image">
		  <file-upload
		  tip="点击上传头像"
		  action="file/upload"
		  :limit="1"
		  :multiple="false"
		  :fileUrls="ruleForm.image?ruleForm.image:''"
		  @change="usersimageUploadChange"
		  ></file-upload>
		</el-form-item>
		<el-form-item :style='{"padding":"0","margin":"30px auto","alignItems":"center","textAlign":"center","background":"none","display":"flex","width":"60%","fontSize":"18px"}'>
			<el-button class="btn3" :style='{"border":"0px solid #3fcbca","cursor":"pointer","padding":"0 20px","margin":"0px 4px","color":"#fff","minWidth":"90px","outline":"none","borderRadius":"4px","background":"#4b88e4","width":"auto","fontSize":"14px","lineHeight":"40px","height":"40px"}' type="primary" @click="onUpdateHandler">
				<span class="icon iconfont icon-tijiao16" :style='{"margin":"0 2px","fontSize":"inherit","color":"inherit","display":"none"}'></span>
				确定
			</el-button>
		</el-form-item>
      </el-row>
    </el-form>
  </div>
</template>
<script>
// 数字，邮件，手机，url，身份证校验
import { isNumber,isIntNumer,isEmail,isMobile,isPhone,isURL,checkIdCard } from "@/utils/validate";

export default {
  data() {
    return {
      ruleForm: {},
      flag: '',
      usersFlag: false,
      jiaoshixingbieOptions: [],
      xueshengxingbieOptions: [],
      xueshengbanjiOptions: [],
    };
  },
  mounted() {
    var table = this.$storage.get("sessionTable");
    this.flag = table;
    this.$http({
      url: `${this.$storage.get("sessionTable")}/session`,
      method: "get"
    }).then(({ data }) => {
      if (data && data.code === 0) {
        this.ruleForm = data.data;
      } else {
        this.$message.error(data.msg);
      }
    });
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
  },
  methods: {
    jiaoshizhaopianUploadChange(fileUrls) {
        this.ruleForm.zhaopian = fileUrls;
    },
    xueshengtouxiangUploadChange(fileUrls) {
        this.ruleForm.touxiang = fileUrls;
    },
	usersimageUploadChange(fileUrls) {
		this.ruleForm.image = fileUrls;
	},
    onUpdateHandler() {
      if((!this.ruleForm.jiaoshigonghao)&& 'jiaoshi'==this.flag){
        this.$message.error('教师工号不能为空');
        return
      }


      if((!this.ruleForm.mima)&& 'jiaoshi'==this.flag){
        this.$message.error('密码不能为空');
        return
      }


      if((!this.ruleForm.jiaoshixingming)&& 'jiaoshi'==this.flag){
        this.$message.error('教师姓名不能为空');
        return
      }






        if(this.ruleForm.zhaopian!=null) {
                this.ruleForm.zhaopian = this.ruleForm.zhaopian.replace(new RegExp(this.$base.url,"g"),"");
        }




      if( 'jiaoshi' ==this.flag && this.ruleForm.lianxidianhua&&(!isMobile(this.ruleForm.lianxidianhua))){
        this.$message.error(`联系电话应输入手机格式`);
        return
      }




      if((!this.ruleForm.xuehao)&& 'xuesheng'==this.flag){
        this.$message.error('学号不能为空');
        return
      }


      if((!this.ruleForm.mima)&& 'xuesheng'==this.flag){
        this.$message.error('密码不能为空');
        return
      }


      if((!this.ruleForm.xingming)&& 'xuesheng'==this.flag){
        this.$message.error('姓名不能为空');
        return
      }






        if(this.ruleForm.touxiang!=null) {
                this.ruleForm.touxiang = this.ruleForm.touxiang.replace(new RegExp(this.$base.url,"g"),"");
        }


      if( 'xuesheng' ==this.flag && this.ruleForm.shouji&&(!isMobile(this.ruleForm.shouji))){
        this.$message.error(`手机应输入手机格式`);
        return
      }






      if('users'==this.flag && this.ruleForm.username.trim().length<1) {
	this.$message.error(`用户名不能为空`);
        return	
      }
	  if(this.flag=='users'){
	  	this.ruleForm.image = this.ruleForm.image.replace(new RegExp(this.$base.url,"g"),"")
	  }
      this.$http({
        url: `${this.$storage.get("sessionTable")}/update`,
        method: "post",
        data: this.ruleForm
      }).then(({ data }) => {
        if (data && data.code === 0) {
          this.$message({
            message: "修改信息成功",
            type: "success",
            duration: 1500,
            onClose: () => {
				if(this.flag=='users'){
					this.$storage.set('headportrait',this.ruleForm.image)
				}
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
	.el-date-editor.el-input {
		width: auto;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__label {
	  	  padding: 0 10px 0 0;
	  	  color: #00acc1;
	  	  background: none;
	  	  font-weight: 600;
	  	  display: inline-block;
	  	  width: 200px;
	  	  font-size: inherit;
	  	  line-height: 40px;
	  	  text-align: right;
	  	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__content {
	  margin-left: 200px;
	}
	
	.add-update-preview .el-input /deep/ .el-input__inner {
	  	  border-radius: 4px;
	  	  padding: 0 12px;
	  	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  	  outline: none;
	  	  color: inherit;
	  	  background: #fff;
	  	  width: 400px;
	  	  font-size: 14px;
	  	  border-color: #ced4da;
	  	  border-width: 1px;
	  	  border-style: solid;
	  	  height: 36px;
	  	}
	
	.add-update-preview .el-select /deep/ .el-input__inner {
	  	  padding: 0 10px;
	  	  color: inherit;
	  	  font-size: 14px;
	  	  border-color: #ced4da;
	  	  border-radius: 0px;
	  	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  	  outline: none;
	  	  background: #fff;
	  	  width: auto;
	  	  border-width: 1px;
	  	  border-style: solid;
	  	  min-width: 350px;
	  	  height: 36px;
	  	}
	
	.add-update-preview .el-date-editor /deep/ .el-input__inner {
	  	  padding: 0 10px 0 30px;
	  	  color: inherit;
	  	  font-size: 14px;
	  	  border-color: #ced4da;
	  	  border-radius: 0px;
	  	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  	  outline: none;
	  	  background: none;
	  	  width: auto;
	  	  border-width: 1px;
	  	  border-style: solid;
	  	  min-width: 250px;
	  	  height: 36px;
	  	}
	
	.add-update-preview /deep/ .el-upload--picture-card {
		background: transparent;
		border: 0;
		border-radius: 0;
		width: auto;
		height: auto;
		line-height: initial;
		vertical-align: middle;
	}
	
	.add-update-preview /deep/ .el-upload-list .el-upload-list__item {
	  	  border: 1px solid #ced4da;
	  	  cursor: pointer;
	  	  border-radius: 4px;
	  	  color: #aaa;
	  	  background: #fff;
	  	  object-fit: cover;
	  	  width: 180px;
	  	  font-size: 32px;
	  	  line-height: 80px;
	  	  text-align: center;
	  	  height: 80px;
	  	}
	
	.add-update-preview /deep/ .el-upload .el-icon-plus {
	  	  border: 1px solid #ced4da;
	  	  cursor: pointer;
	  	  border-radius: 4px;
	  	  color: #aaa;
	  	  background: #fff;
	  	  object-fit: cover;
	  	  width: 180px;
	  	  font-size: 32px;
	  	  line-height: 80px;
	  	  text-align: center;
	  	  height: 80px;
	  	}
	
	.add-update-preview .el-textarea /deep/ .el-textarea__inner {
	  	  border: 1px solid #ced4da;
	  	  border-radius: 4px;
	  	  padding: 12px;
	  	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  	  outline: none;
	  	  color: inherit;
	  	  background: #fff;
	  	  width: 500px;
	  	  font-size: 14px;
	  	  height: 140px;
	  	}
	
	.add-update-preview .btn3 {
				border: 0px solid #3fcbca;
				cursor: pointer;
				padding: 0 20px;
				margin: 0px 4px;
				color: #fff;
				font-size: 14px;
				line-height: 40px;
				border-radius: 4px;
				outline: none;
				background: #4b88e4;
				width: auto;
				min-width: 90px;
				height: 40px;
			}
	
	.add-update-preview .btn3:hover {
				opacity: 0.8;
			}
	
	.editor>.avatar-uploader {
		line-height: 0;
		height: 0;
	}
</style>
