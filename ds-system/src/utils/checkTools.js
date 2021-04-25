let CheckTools = {
      
    //Email正则
    EmailRegExp: /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/,
    
    //手机号正则
    regMobile : /^(0|86|17951)?(13[0-9]|15[0123456789]|17[678]|18[0-9]|14[57])[0-9]{8}$/,

    //姓名正则
    regName : /^(([a-zA-Z+\.?\·?a-zA-Z+]{2,30}$)|([\u4e00-\u9fa5+\·?\u4e00-\u9fa5+]{2,30}$))/,

    //年龄正则
    regAge:/^(?:[1-9][0-9]?|1[01][0-9]|120)$/
}

export default CheckTools