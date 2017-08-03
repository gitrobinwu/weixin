#-*- coding:utf-8 -*-
import hashlib 

# 微信公众号关联邮箱 
email = '2497161560@qq.com'
hash = hashlib.md5(email.encode('utf-8')).hexdigest()

if __name__ == '__main__':
	print hash 

