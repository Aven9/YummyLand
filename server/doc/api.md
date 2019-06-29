# 后台接口API文档

## 说明

1. 协议为https
2. 域名homework.liuchaorun.cn
3. 所有请求默认携带前缀 /server
4. 返回数据均为json，数据格式如下，code为自定义状态码，data为返回数据，msg代表错误提示信息
    ```
    {
        code: INT,
        data: {},
        msg: STRING
    }
    ```
5. 状态码（code）说明

    |code|说明|
    |:---:|:---:|
    |0|成功|
    |1|未登录或登陆过期|
    |2|未注册账号|
    |3|账号或密码错误|
    |4|账号已被注册|
    |5|服务器错误|
    
## 用户模块

### 说明

1. 该某块所有接口默认带有前缀/user
2. return中表示的为返回数据中data的数据格式

### 获取注册验证码接口

***url:*** /verificationCode

***method:*** post

***params:***
```
email: string
```

***return:***
```
{
    status: 'success'
}
```

### 注册接口

***url:*** /register

***method:*** POST

***params:***
```
username: string,
email: string,
password: string, //最好转成sha256
```

***return:***
```
{
    status: 'success'
}
```

### 登陆接口

***url:*** /login

***method:*** POST

***params:***
```
email: string,
password: string
```

***return:***
```
{
    status: 'success'
}
```

### 获取个人信息

***url:*** /userInfo/get

***method:*** get

***params:***
```
null
```

***return:***
```
{
    username: string,
    email: string,
    imageUrl: string,
    birthday: data
}
```

### 修改个人信息

***url:*** /userInfo/modify

***method:*** post

***params:***
```
username: string,
email: string,
imageUrl: string,
birthday: data
```

***return:***
```
{
    status: 'success'
}
```

### 修改头像

***url:*** /userInfo/upload

***method:*** POST

***params:***
```
file: FILE
```

***return:***
```
{
    status: 'success'
}
```

### 获取收获地址

***url:*** /address/get

***method:*** GET

***params:***
```
null
```

***return:***
```
{
    address:[{
        id: int,
        name: string,
        phone: string,
        province: string,
        city: string,
        detail: string 
    }]
}
```

### 添加收获地址

***url:*** /address/add

***method:*** post

***params:***
```
name: string,
phone: string,
province: string,
city: string,
detail: string
```

***return:***
```
{
    status: 'success'
}
```

### 修改收货地址

***url:*** /address/modify

***method:*** post

***params:***
```
id: int
name: string,
phone: string,
province: string,
city: string,
detail: string
```

***return:***
```
{
    status: 'success'
}
```

### 删除收获地址

***url:*** /address/delete

***method:*** POST

***params:***
```
id: int
```

***return:***
```
{
    status: 'success'
}
```

## 用户商品模块

### 说明

1. 该某块所有接口默认带有前缀/food
2. return中表示的为返回数据中data的数据格式

### 根据分类获取商家

***url:*** /shop/getByType

***method:*** POST

***params:***
```
type: string
```

***return:***
```
{
    shops: [{
        id: int,
        name: string,
        imageUrl: string,
        introduction: string,
    }]
}
```

### 搜索商家

***url:*** /shop/getByName

***method:*** POST

***params:***
```
name: string
```

***return:***
```
{
    shops: [{
        id: int,
        name: string,
        imageUrl: string,
        introduction: string,
    }]
}
```

### 商家详情 

***url:*** /shop/get

***method:*** POST

***params:***
```
id: int
```

***return:***
```
{
    id: int,
    name: string,
    imageUrl: string,
    introduction: string,
    food: {
        'categoryName': [{
            id: int,
            name: string,
            price: int,
            imageUrl: string
        }]
    }
}
```

### 商家评论 

***url:*** /shop/common

***method:*** POST

***params:***
```
id: int
```

***return:***
```
{
    commons: [{
        usrname: string,
        text: string,
        imageUrl: string,
        rate: int,
        createdAt: timestamp
    }]
}
```

## 用户订单模块

### 说明

1. 该某块所有接口默认带有前缀/order
2. return中表示的为返回数据中data的数据格式
3. 订单转台码（status）说明

    |status|说明|
    |:---:|:---:|
    |0|订单创建|
    |1|商家接单|
    |2|商家派送|
    |3|订单完成|
    |4|用户取消|
    |5|商家取消|

### 创建订单

***url:*** /create

***method:*** post

***params:***
```
foods:[{
    id: int,
    number: int
}]
addressId: int,
remark: string, //备注
```

***return:***
```
{
    id: int// 订单id
}
```

### 取消订单

***url:*** /cancel

***method:*** post

***params:***
```
id: int
```

***return:***
```
{
    id: int, //订单id
}
```

### 确认订单

***url:*** /confirm

***method:*** post

***params:***
```
id: int
```

***return:***
```
{
    id: int//订单id
}
```

### 评论图片上传

***url:*** /common/upload

***method:*** post

***params:***
```
file: FILE
```

***return:***
```
{
    url: string
}
```

### 对完成订单评论

***url:*** /common

***method:*** post

***params:***
```
id: int,
text: string,
imageUrl: string,
rate: int
```

***return:***
```
{
    id: int, //评论id
}
```

## 商家用户模块

### 

***url:*** 

***method:*** 

***params:***
```

```

***return:***
```
```

## 商家订单系统

### 

***url:*** 

***method:*** 

***params:***
```

```

***return:***
```
```
