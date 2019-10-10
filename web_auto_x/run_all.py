import unittest
from common import HTMLTestRunner_cn
#用例的路径
casePath="E:\web_auto\\case"
rule="test*.py"
discover=unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)

reportPath="E:\web_auto\\report\\"+"result.html"

fp=open(reportPath,"wb")

runner=HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title="报告的title",description="描述你的报告是干什么用",verbosity=2,retry=1)

runner.run(discover)
fp.close()
