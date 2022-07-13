#导入需要使用的工具
from com.android.monkeyrunner import MonkeyRunner
from com.android.monkeyrunner import MonkeyDevice
from com.android.monkeyrunner import MonkeyImage
#连接模拟器
device=MonkeyRunner.waitForConnection(5,'127.0.0.1:62001')
print(device)
#进入APP页面
device.startActivity(component='com.dajia.view.wcy/com.dajia.view.login.ui.LoginActivity')
#定位元素并对元素进行点击
device.touch(130,712,'DOWN_AND_UP')
#输入字符
device.type('12312312')

device.drag((556,284),(600,284),0.1,10)
