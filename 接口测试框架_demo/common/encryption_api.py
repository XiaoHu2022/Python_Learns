# -*- coding: utf-8 -*-
"""
@Time ： 2022-09-11 14:46
@Auth ： 小胡
@File ：encryption_api.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import base64
import time

import rsa

'''封装RSA类型的加密函数'''
SERVER_RSA_PUB_KEY = ''
def rsa_encrypt(msg:str,pub_key:str):
    '''
    公钥加密
    :param msg: 要加密的内容
    :param pub_key: pem格式的公钥字符串
    :return:
    '''
    #1、生成公钥对象，把公钥字符串转换为字节数据
    pub_key_bytes = pub_key.encode()
    pub = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key_bytes)
    #待加密的数据（msg）转换为字节数据
    content = msg.encode('utf-8')
    #2、加密
    crypt_msg = rsa.encrypt(content,pub)
    #3、转化成base64字符串返回
    return base64.b64encode(crypt_msg).decode()

'''生成签名----token前50位+时间戳'''
def generate_sign(token,pub_key):
    '''
    生成签名sign
    :param token: token字符串
    :param pub_key: pem格式的公钥
    :return:
    '''
    #1、获取token的前50位
    token_50 = token[:50]
    #获取时间戳：timestamp
    timestamp = int(time.time())
    #拼接token的前50位+时间戳
    msg = token_50 + str(timestamp)

    #进行RSA加密
    sign = rsa_encrypt(msg,pub_key)
    return sign,timestamp