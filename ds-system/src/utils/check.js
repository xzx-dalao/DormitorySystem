import CheckTools from './checkTools'


let checkMobile = (rule, value, callback) => {
  if (CheckTools.regMobile.test(value)) {
    return callback();
  }
  callback(new Error("请输入合法的手机号"));
};

let checkName = (rule, value, callback) => {
  if (CheckTools.regName.test(value)) {
    return callback();
  }
  callback(new Error("请输入合法的姓名"));
};

let checkAge = (rule, value, callback) => {
  if (CheckTools.regAge.test(value)) {
    return callback();
  }
  callback(new Error("请输入合法的年龄"));
};


export { checkMobile, checkName, checkAge }