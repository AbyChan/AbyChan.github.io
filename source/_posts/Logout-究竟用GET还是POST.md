title: 'Logout: 究竟用GET还是POST?'
date: 2015-04-15 12:05:56
tags:
- logut
- restful
- get
- post
- http
---
ReSTful风格api设计中，遇到了一个问题
logout究竟用get还是post？
理论上来说logout安全（logout没有改变服务器状态，只是改变了session）且幂等，应该是get

但是用get在2010年前可能是正确答案，只不过现在的浏览器普遍具备pre load（预加载）功能，用get就悲剧了

so，post吧
