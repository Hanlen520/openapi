# openapi
第三方openapi单元测试，python+yaml，更新yaml文件即可

# 说明


URL参数

格式说明


| 应用编码 | 需要对接的功能模块，如部门信息为：organization 
|---------|----------|
|应用版本  |  对接应用的版本号，如：v1 
|接口编码    对接应用的接口，如新增部门：addOrganization 
|openid    |企业接入唯一授权标识，为19位随机字符串，由外勤365统一分配 
|appkey    |企业授权数据签名密钥，为18位随机字符串，由外勤365分配 
|timestamp|    请求消息时间，格式为：yyyyMMddHHmmSS如：20140701142836 
|digest  |  数据签名，使用32位小写字母，用于验证数据的真实性。数据校验码生成规则：md5(消息体|appkey|timestamp),
|msg_id |   消息ID，发送请求的唯一标识，一般使用uuid，服务器响应时会将原值返回。 

# 请求示例

##### 企业OPENID: 
5465103569540931532

##### 企业APPKEY: 
BFCO0PAgIUgd50c0l6

##### 示例数据：

{"org_id":"ORG001","org_name":"南京掌控网络","org_parent_id":"","org_sequence":001}

##### 获取时间戳为：20150806142836

##### 生成消息ID：ORG00001 (随机生成)

##### digest=Md5({"org_id":"ORG001","org_name":"南京掌控网络","org_parent_id":"","org_sequence":001}|BFCO0PAgIUgd50c0l6|20150806142836)

##### 生成数据签名(digest)为：74267bf0cae0998a719879ec9b3c7780

##### 生成请求URL：

https://openapi.waiqin365.com/api/organization/v1/addOrganization/5465103569540931532/20150806142836/74267bf0cae0998a719879ec9b3c7780/ORG00001

##### 消息体：

{"org_id":"ORG001","org_name":"南京掌控网络","org_parent_id":"","org_sequence":001}
